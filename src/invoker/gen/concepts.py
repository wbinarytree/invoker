from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Protocol, TypeVar

from pydantic import BaseModel

from invoker.corpus.sections import CorpusSection, load_sections
from invoker.corpus.store import CorpusStore
from invoker.gen.artifacts import ConceptArtifact, ConceptCard
from invoker.gen.client import GenerationError, GenerationResult, StructuredResult

T = TypeVar("T", bound=BaseModel)

CONCEPT_PROMPT_VERSION = "1"

ARTICLE_SYSTEM_PROMPT = """You write reference articles for a grounded Dota 2 encyclopedia.

Rules:
- Use ONLY facts stated in the source sections the user provides. No outside \
knowledge, even when you are confident.
- Every factual sentence ends with one or more citation marks of the form \
[corpus:KEY], where KEY is one of the provided section keys, copied exactly.
- Numbers must match the cited section exactly.
- If the sources do not cover something, leave it out. Never fill a gap with a \
plausible value.
- Write concise reference prose in markdown with a few short sections. No \
preamble, no meta-commentary about sources or citations."""

CARD_SYSTEM_PROMPT = """You compress a grounded encyclopedia article into a card.

Rules:
- The card is at most 12 sentences and around 300 tokens total.
- Each sentence keeps the citation marks of the article sentences it \
compresses, as strings of the form corpus:KEY copied exactly from the article.
- Keep the load-bearing facts and exact numbers; drop narrative padding.
- Use ONLY the article text. No outside knowledge."""

_MARK_PATTERN = re.compile(r"\[corpus:([^\]\s]+)\]")


class GenerationBackend(Protocol):
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


def generate_concept(
    store: CorpusStore,
    backend: GenerationBackend,
    *,
    host_key: str,
    slug: str,
    patch: str,
    kb_dir: Path,
    effort: str | None = None,
) -> tuple[ConceptArtifact, Path]:
    """Generate one concept article + card from the stored corpus and write
    the artifact under <kb_dir>/concepts/<slug>.json."""
    index_page = store.load_index(host_key).pages.get(slug)
    if index_page is None:
        raise GenerationError(f"{slug}: not in the {host_key} corpus index; run fetch-corpus")
    sections = load_sections(store, host_key, slug)
    packet, valid_keys, packet_sha256 = build_packet(sections)

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

    card = backend.generate_structured(
        ConceptCard,
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

    artifact = ConceptArtifact(
        slug=slug,
        title=index_page.resolved_title,
        patch=patch,
        article_markdown=article.text,
        card=card.output,
        citations=[f"corpus:{key}" for key in citations],
        packet_sha256=packet_sha256,
        article_provenance=article.provenance,
        card_provenance=card.provenance,
    )
    path = kb_dir / "concepts" / f"{slug}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(artifact.model_dump_json(indent=2))
    return artifact, path
