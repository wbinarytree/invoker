from __future__ import annotations

import hashlib
import re
from datetime import UTC, datetime
from pathlib import Path
from typing import Protocol, TypeVar

from pydantic import BaseModel

from invoker.corpus.sections import CorpusSection, load_sections
from invoker.corpus.store import CorpusStore
from invoker.gen.artifacts import (
    EntityArtifact,
    EntityCard,
    article_file_text,
    write_entity_artifact,
)
from invoker.gen.checks import (
    check_article_numbers,
    check_coverage,
    check_marks,
    check_numbers,
    extract_marks,
)
from invoker.gen.client import GenerationError, GenerationResult, StructuredResult

T = TypeVar("T", bound=BaseModel)

CONCEPT_PROMPT_VERSION = "9"

ARTICLE_SYSTEM_PROMPT = """You write reference articles for a grounded Dota 2 encyclopedia.

Rules:
- Use ONLY facts stated in the source sections the user provides. No outside \
knowledge, even when you are confident.
- The article is a lossless compression of the sources: every load-bearing \
fact in every provided section appears in it — exact values, enumerations, \
interaction rules, conditions and exceptions. Cover every section — a \
one-line or footnote section is still a section and must be cited at least \
once; omit only prose style, wiki housekeeping, and reference boilerplate.
- Carry enumerations in full: lists of sources, items, abilities, or talents \
with their values, and tables of constants, are reproduced as markdown \
tables with every row — never summarized by examples or "such as" \
selections.
- Every factual statement is covered by a citation mark of the form \
[corpus:KEY], where KEY is one of the provided section keys, copied exactly. \
The source headers display the bare key in brackets; your marks must always \
add the corpus: prefix — [corpus:KEY], never [KEY]. Place a mark wherever \
the source section changes; consecutive sentences drawn from the same \
section share a single mark at the end of the run.
- Cite the single narrowest section that states the fact. Never attach a \
citation the text does not strictly need; a broad section key is wrong \
when a more specific one states the fact. The one exception is a table or \
sentence that consolidates values from several sections: its trailing marks \
must cover every section whose values appear in it.
- Numbers must match the cited section exactly: reproduce values as the \
source states them. Never derive, sum, convert, count, or round numbers — \
a value the source does not literally contain must not appear. Reproduce \
ranges and series exactly as written; never expand a range into the \
individual values it covers.
- The patch named in the request is context, not source material: never \
state the patch or its version anywhere in the article, including the title.
- If the sources do not cover something, leave it out. Never fill a gap with a \
plausible value.
- Concise wording, complete content: brevity comes from tight sentences and \
tables, never from dropping facts. Markdown, sections mirroring the source \
topics. No preamble, no meta-commentary about sources or citations."""

CARD_SYSTEM_PROMPT = """You compress a grounded encyclopedia article into a card.

Rules:
- The card is at most 12 sentences and around 300 tokens total.
- The first sentence is the identity line: it is shown alone as the \
entity's summary in an index, so it must state concretely what the entity \
is and does, with its defining numbers. A reader who sees only this \
sentence must be able to tell what the entity is. It is the one exception \
to one-fact-per-sentence and carries the marks of every section it draws on.
- Every other sentence states one core fact, so each fact maps to its own \
source marks. Prefer dropping a minor fact over packing two facts into one \
sentence.
- State facts plainly with exact values. No flavor language: verbs like \
"burns" or "cripples" and summaries like "combines X with Y" say nothing \
checkable — write the stat names and numbers instead.
- Each sentence keeps the citation marks of the article text it \
compresses, as strings of the form corpus:KEY copied exactly from the \
article. A mark vouches only for facts its own section states — never \
attach a mark to a sentence whose facts come from elsewhere. Cite the \
narrowest key that states the fact; never pad with broader keys.
- Keep the load-bearing facts and exact numbers; drop narrative padding.
- Every number must appear literally in the article text a sentence's marks \
cover: never count list entries or table rows yourself, and never derive, \
sum, convert, or round a value.
- Use ONLY the article text. No outside knowledge."""


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


WIKI_ERROR_TEXT = "Error no text specified!"
MAIN_ARTICLE_LINE = re.compile(r"^Main Article:.*$", re.MULTILINE)


def is_degenerate_section(text: str) -> bool:
    """True for sections that carry no citable facts: MediaWiki template
    error strings leaked through extraction, and bare "Main Article: X"
    cross-reference stubs. Forcing coverage of these invites fabrication
    (batch KB generation spec, amendment 2)."""
    residue = MAIN_ARTICLE_LINE.sub("", text.replace(WIKI_ERROR_TEXT, ""))
    return not residue.strip()


def build_packet(sections: list[CorpusSection]) -> tuple[str, dict[str, str], str]:
    """Render sections into the generation context packet.

    Returns (packet_text, section text by mark string, packet sha256) —
    the dict doubles as the valid-mark set and the number-check source,
    same contract as build_item_packet. The hash goes into artifact
    provenance so a regenerated packet is detectable. Degenerate sections
    (error strings, contentless cross-reference stubs) are dropped.
    """
    parts: list[str] = []
    text_by_mark: dict[str, str] = {}
    for section in sections:
        if not section.text or is_degenerate_section(section.text):
            continue
        text_by_mark[f"corpus:{section.citation_key}"] = section.text
        crumb = " > ".join(section.breadcrumbs) or "(lead)"
        parts.append(f"## [{section.citation_key}] {crumb}\n{section.text}")
    packet = "\n\n".join(parts)
    return packet, text_by_mark, hashlib.sha256(packet.encode()).hexdigest()


def persist_rejected(
    rejected_dir: Path | None,
    *,
    kind: str,
    slug: str,
    article_text: str,
    card: EntityCard | None,
    error: Exception,
) -> Path | None:
    """Persist paid-for output that will not become an artifact — the
    article (and card, when one exists) plus the error text — so an abort
    never discards what the tokens bought. Returns the directory written,
    or None when persistence is off (no rejected_dir)."""
    if rejected_dir is None:
        return None
    stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%S.%f")
    target = rejected_dir / kind / slug / stamp
    target.mkdir(parents=True, exist_ok=True)
    (target / "article.md").write_text(article_text)
    if card is not None:
        (target / "card.json").write_text(card.model_dump_json(indent=2))
    (target / "error.txt").write_text(f"{type(error).__name__}: {error}\n")
    return target


def generate_concept(
    store: CorpusStore,
    backend: GenerationBackend,
    *,
    host_key: str,
    slug: str,
    patch: str,
    kb_dir: Path,
    effort: str | None = None,
    rejected_dir: Path | None = None,
) -> tuple[EntityArtifact, Path]:
    """Generate one concept article + card from the stored corpus and write
    the artifact under <kb_dir>/concepts/<slug>.json."""
    index_page = store.load_index(host_key).pages.get(slug)
    if index_page is None:
        raise GenerationError(f"{slug}: not in the {host_key} corpus index; run fetch-corpus")
    sections = load_sections(store, host_key, slug)
    packet, text_by_mark, packet_sha256 = build_packet(sections)
    valid_marks = set(text_by_mark)

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
    card = None
    try:
        citations = extract_marks(article.text)
        check_marks(citations, valid_marks, "article", slug)
        check_coverage(citations, valid_marks, "article", slug)
        # scoped per citation, over section texts only — packet headers carry
        # key/revision digits that must never vouch for a number in prose
        check_article_numbers(article.text, text_by_mark, slug)

        card = backend.generate_structured(
            EntityCard,
            prompt_name="concept-card",
            prompt_version=CONCEPT_PROMPT_VERSION,
            system=CARD_SYSTEM_PROMPT,
            user_content=f"Entity: {slug}\n\nArticle:\n\n{article.text}",
            effort=effort,
        )
        card_marks = [mark for sentence in card.output.sentences for mark in sentence.marks]
        check_marks(card_marks, valid_marks, "card", slug)
        for position, sentence in enumerate(card.output.sentences, start=1):
            cited_text = "\n".join(text_by_mark.get(mark, "") for mark in sentence.marks)
            check_numbers(sentence.text, cited_text, f"card sentence {position}", slug)

        file_text = article_file_text(
            title=index_page.resolved_title,
            kind="concept",
            patch=patch,
            card=card.output,
            body=article.text,
        )
        artifact = EntityArtifact(
            kind="concept",
            slug=slug,
            title=index_page.resolved_title,
            patch=patch,
            article_file="article.md",
            article_sha256=hashlib.sha256(file_text.encode()).hexdigest(),
            card=card.output,
            citations=citations,
            packet_sha256=packet_sha256,
            article_provenance=article.provenance,
            card_provenance=card.provenance,
        )
        path = write_entity_artifact(kb_dir / "concepts" / slug, artifact, file_text)
    except Exception as exc:
        persist_rejected(
            rejected_dir,
            kind="concepts",
            slug=slug,
            article_text=article.text,
            card=card.output if card is not None else None,
            error=exc,
        )
        raise
    return artifact, path
