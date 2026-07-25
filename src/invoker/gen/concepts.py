from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Protocol, TypeVar

from pydantic import BaseModel

from invoker.corpus.sections import CorpusSection, load_sections
from invoker.corpus.store import CorpusStore
from invoker.gen.artifacts import EntityArtifact, EntityCard
from invoker.gen.client import GenerationError, GenerationResult, StructuredResult

T = TypeVar("T", bound=BaseModel)

CONCEPT_PROMPT_VERSION = "3"

ARTICLE_SYSTEM_PROMPT = """You write reference articles for a grounded Dota 2 encyclopedia.

Rules:
- Use ONLY facts stated in the source sections the user provides. No outside \
knowledge, even when you are confident.
- Every factual statement is covered by a citation mark of the form \
[corpus:KEY], where KEY is one of the provided section keys, copied exactly. \
Place a mark wherever the source section changes; consecutive sentences drawn \
from the same section share a single mark at the end of the run.
- Cite the single narrowest section that states the fact. Never attach a \
citation the text does not strictly need; a broad section key is wrong \
when a more specific one states the fact.
- Numbers must match the cited section exactly.
- If the sources do not cover something, leave it out. Never fill a gap with a \
plausible value.
- Write concise reference prose in markdown with a few short sections. No \
preamble, no meta-commentary about sources or citations."""

CARD_SYSTEM_PROMPT = """You compress a grounded encyclopedia article into a card.

Rules:
- The card is at most 12 sentences and around 300 tokens total.
- One core fact per sentence, so each fact maps to its own source marks. \
Prefer dropping a minor fact over packing two facts into one sentence.
- Each sentence keeps the citation marks of the article sentence it \
compresses, as strings of the form corpus:KEY copied exactly from the article. \
Cite the narrowest key that states the fact; never pad with broader keys.
- Keep the load-bearing facts and exact numbers; drop narrative padding.
- Use ONLY the article text. No outside knowledge."""

_MARK_PATTERN = re.compile(r"\[corpus:([^\]\s]+)\]")


class GenerationBackend(Protocol):
    model: str
    """Requested model id — consumers record it in run-level provenance,
    so the protocol enforces it rather than callers falling back to
    getattr defaults that silently degrade the record."""

    def generate(
        self,
        *,
        prompt_name: str,
        prompt_version: str,
        system: str,
        user_content: str,
        effort: str | None = None,
    ) -> GenerationResult: ...

    def generate_structured(
        self,
        output_type: type[T],
        *,
        prompt_name: str,
        prompt_version: str,
        system: str,
        user_content: str,
        effort: str | None = None,
    ) -> StructuredResult[T]: ...


def build_packet(sections: list[CorpusSection]) -> tuple[str, set[str], str]:
    """Render sections into the generation context packet.

    Returns (packet_text, valid citation keys, packet sha256). The hash goes
    into artifact provenance so a regenerated packet is detectable.
    """
    parts: list[str] = []
    keys: set[str] = set()
    for section in sections:
        if not section.text:
            continue
        keys.add(section.citation_key)
        crumb = " > ".join(section.breadcrumbs) or "(lead)"
        parts.append(f"## [{section.citation_key}] {crumb}\n{section.text}")
    packet = "\n\n".join(parts)
    return packet, keys, hashlib.sha256(packet.encode()).hexdigest()


def extract_citations(markdown: str) -> list[str]:
    """Distinct citation keys marked in the article, in first-use order."""
    seen: dict[str, None] = {}
    for match in _MARK_PATTERN.finditer(markdown):
        seen.setdefault(match.group(1))
    return list(seen)


def _check_keys(used: list[str], valid: set[str], what: str, slug: str) -> None:
    unknown = [key for key in used if key not in valid]
    if unknown:
        raise GenerationError(
            f"{slug}: {what} cites keys not in the context packet: {', '.join(sorted(unknown))}"
        )
    if not used:
        raise GenerationError(f"{slug}: {what} contains no citation marks")


_NUMBER_PATTERN = re.compile(r"\d+(?:\.\d+)?")


def _article_segments(article_text: str) -> list[tuple[str, list[str]]]:
    """Split the article at citation marks: the text preceding a run of
    consecutive marks is attributed to those marks' sections. An uncited
    tail (if any) carries an empty key list."""
    segments: list[tuple[str, list[str]]] = []
    matches = list(_MARK_PATTERN.finditer(article_text))
    position = 0
    index = 0
    while index < len(matches):
        match = matches[index]
        keys = [match.group(1)]
        end = match.end()
        follower = index + 1
        while follower < len(matches) and not article_text[end : matches[follower].start()].strip():
            keys.append(matches[follower].group(1))
            end = matches[follower].end()
            follower += 1
        segments.append((article_text[position : match.start()], keys))
        position = end
        index = follower
    tail = article_text[position:]
    if tail.strip():
        segments.append((tail, []))
    return segments


def _check_article_numbers(article_text: str, text_by_key: dict[str, str], slug: str) -> None:
    """Article counterpart of the per-sentence card check: numbers in each
    cited segment must appear in that segment's own cited sections."""
    all_sections = "\n".join(text_by_key.values())
    for segment_text, keys in _article_segments(article_text):
        if keys:
            source = "\n".join(text_by_key.get(key, "") for key in keys)
            what = f"article segment citing {', '.join(keys)}"
        else:
            source = all_sections
            what = "uncited article text"
        _check_numbers(segment_text, source, what, slug)


def _check_numbers(text: str, source_text: str, what: str, slug: str) -> None:
    """Every number in generated text must literally appear in the cited
    source (spec: quoted numbers match what the cited source actually says).
    Citation marks are stripped first — keys carry revision numbers."""
    stripped = _MARK_PATTERN.sub("", text)
    missing = sorted(
        number for number in set(_NUMBER_PATTERN.findall(stripped)) if number not in source_text
    )
    if missing:
        raise GenerationError(
            f"{slug}: {what} contains numbers not found in the cited source: {', '.join(missing)}"
        )


def load_entity_article(artifact_path: Path) -> tuple[EntityArtifact, str]:
    """Load an artifact and its article, verifying the sha binding.

    A hand-edited or drifted article file fails loudly — artifacts are
    regenerated, never patched in place."""
    artifact = EntityArtifact.model_validate_json(artifact_path.read_text())
    article = (artifact_path.parent / artifact.article_file).read_text()
    digest = hashlib.sha256(article.encode()).hexdigest()
    if digest != artifact.article_sha256:
        raise GenerationError(
            f"{artifact.slug}: article file drifted from its artifact (sha mismatch); regenerate"
        )
    return artifact, article


def generate_concept(
    store: CorpusStore,
    backend: GenerationBackend,
    *,
    host_key: str,
    slug: str,
    patch: str,
    kb_dir: Path,
    effort: str | None = None,
) -> tuple[EntityArtifact, Path]:
    """Generate one concept article + card from the stored corpus and write
    the artifact under <kb_dir>/concepts/<slug>.json."""
    index_page = store.load_index(host_key).pages.get(slug)
    if index_page is None:
        raise GenerationError(f"{slug}: not in the {host_key} corpus index; run fetch-corpus")
    sections = load_sections(store, host_key, slug)
    packet, valid_keys, packet_sha256 = build_packet(sections)
    text_by_key = {section.citation_key: section.text for section in sections}

    article = backend.generate(
        prompt_name="concept-article",
        prompt_version=CONCEPT_PROMPT_VERSION,
        system=ARTICLE_SYSTEM_PROMPT,
        user_content=(
            f"Concept: {index_page.resolved_title} (patch context {patch})\n\n"
            f"Source sections:\n\n{packet}"
        ),
        effort=effort,
    )
    citations = extract_citations(article.text)
    _check_keys(citations, valid_keys, "article", slug)
    # scoped per citation, over section texts only — packet headers carry
    # key/revision digits that must never vouch for a number in prose
    _check_article_numbers(article.text, text_by_key, slug)

    card = backend.generate_structured(
        EntityCard,
        prompt_name="concept-card",
        prompt_version=CONCEPT_PROMPT_VERSION,
        system=CARD_SYSTEM_PROMPT,
        user_content=f"Entity: {slug}\n\nArticle:\n\n{article.text}",
        effort=effort,
    )
    card_keys = [
        mark.removeprefix("corpus:")
        for sentence in card.output.sentences
        for mark in sentence.marks
    ]
    _check_keys(card_keys, valid_keys, "card", slug)
    for position, sentence in enumerate(card.output.sentences, start=1):
        cited_text = "\n".join(
            text_by_key.get(mark.removeprefix("corpus:"), "") for mark in sentence.marks
        )
        _check_numbers(sentence.text, cited_text, f"card sentence {position}", slug)

    artifact = EntityArtifact(
        kind="concept",
        slug=slug,
        title=index_page.resolved_title,
        patch=patch,
        article_file="article.md",
        article_sha256=hashlib.sha256(article.text.encode()).hexdigest(),
        card=card.output,
        citations=[f"corpus:{key}" for key in citations],
        packet_sha256=packet_sha256,
        article_provenance=article.provenance,
        card_provenance=card.provenance,
    )
    concept_dir = kb_dir / "concepts" / slug
    concept_dir.mkdir(parents=True, exist_ok=True)
    (concept_dir / artifact.article_file).write_text(article.text)
    path = concept_dir / "artifact.json"
    path.write_text(artifact.model_dump_json(indent=2))
    return artifact, path
