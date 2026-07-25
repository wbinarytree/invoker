from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from invoker.benchmark.marks import Mark, parse_marks
from invoker.gen.client import GenerationError, GenerationProvenance
from invoker.gen.concepts import GenerationBackend, load_entity_article
from invoker.snapshot.changelog import search_changelog

ANSWERER_PROMPT_VERSION = "2"
MAX_SELECTED_ARTIFACTS = 4
MAX_CHANGELOG_QUERIES = 3
_CHANGELOG_HITS_PER_QUERY = 12

SELECT_SYSTEM_PROMPT = """You route questions to a grounded Dota 2 knowledge base.

The user message carries the question and the knowledge surfaces available \
this run. Choose which surfaces to open:
- artifacts: ids copied exactly from the artifact list, at most 4, whose \
articles plausibly answer the question.
- changelog_queries: at most 3 short keyword phrases for the in-game \
patch-note changelog, only when the question concerns when something was \
added, changed, or removed — and only if the changelog is listed as available.

Open only surfaces that plausibly bear on the question. If nothing listed \
does, return empty lists — never guess or stretch a loose match."""

COMPOSE_SYSTEM_PROMPT = """You answer a question from a grounded Dota 2 knowledge base.

Rules:
- Use ONLY facts stated in the provided material. No outside knowledge, \
even when you are confident.
- Every factual statement is covered by an inline source mark of the form \
[kind:KEY] copied exactly from the material: articles carry [corpus:...] \
marks inline, and changelog evidence lines begin with their \
[changelog:...] mark. A mark covers the sentences before it drawn from \
that source.
- Numbers must match the material exactly.
- Answer only what is asked, in the fewest words that answer it \
completely: one or two sentences for a when/what-changed question, a short \
reference entry (rarely over 120 words) for a what-is question. Do not add \
related context the question did not ask for. No preamble, no \
meta-commentary about sources.
- If the material does not cover part of the question, omit that part \
rather than filling the gap; if it covers none of it, say the knowledge \
base does not cover the question."""


class AnswerSelection(BaseModel):
    """The select call's output: which knowledge surfaces to open. Empty
    everywhere means nothing in the KB plausibly answers the question."""

    model_config = ConfigDict(extra="forbid")

    artifacts: list[str] = Field(default_factory=list)
    changelog_queries: list[str] = Field(default_factory=list)


@dataclass(frozen=True)
class KbEntry:
    id: str  # "<kind>/<slug>", e.g. "concept/evasion"
    title: str
    summary: str  # first card sentence (its marks live in the card structure)
    article: str  # full article markdown, citation marks inline


@dataclass(frozen=True)
class BenchmarkAnswer:
    """`text` is None when the select call found nothing to open — the
    resolution-miss outcome; no compose call is made."""

    text: str | None
    marks: list[Mark]
    selected_artifacts: list[str]
    changelog_queries: list[str]
    provenance: list[GenerationProvenance]


_CLASS_KINDS = {"concepts": "concept", "items": "item"}


def load_kb_entries(kb_dir: Path) -> list[KbEntry]:
    """Scan the KB archive into the answerer's index. Loading verifies each
    artifact's article binding, so a drifted article fails the run. An
    entity-class directory without an index loader fails loudly rather than
    silently vanishing from the index."""
    if not kb_dir.is_dir():
        return []
    entries: list[KbEntry] = []
    for class_dir in sorted(path for path in kb_dir.iterdir() if path.is_dir()):
        kind = _CLASS_KINDS.get(class_dir.name)
        if kind is None:
            raise GenerationError(
                f"KB entity class {class_dir.name!r} has no index loader yet; "
                "extend load_kb_entries with its artifact shape"
            )
        for entity_dir in sorted(path for path in class_dir.iterdir() if path.is_dir()):
            artifact, article = load_entity_article(entity_dir / "artifact.json")
            if artifact.kind != kind:
                raise GenerationError(
                    f"{entity_dir}: artifact kind {artifact.kind!r} does not match "
                    f"its class directory {class_dir.name!r}"
                )
            entries.append(
                KbEntry(
                    id=f"{kind}/{artifact.slug}",
                    title=artifact.title,
                    summary=artifact.card.sentences[0].text,
                    article=article,
                )
            )
    return entries


class Answerer:
    """Two-call ask-path stand-in for the eventual agent-with-tools form:
    select (which surfaces to open) then compose (answer with marks carried
    through). Sees only KB knowledge surfaces — never raw substrate and
    never a case's gold fields. A selection that violates the contract
    (unknown ids, over the fan-out cap, changelog when unavailable) raises
    instead of being silently repaired (no-silent-retries hard line)."""

    def __init__(
        self,
        backend: GenerationBackend,
        entries: list[KbEntry],
        changelog: dict[str, Any] | None,
    ) -> None:
        self._backend = backend
        self._entries = {entry.id: entry for entry in entries}
        self._changelog = changelog

    def answer(self, question: str) -> BenchmarkAnswer:
        selection, select_provenance = self._select(question)
        if not selection.artifacts and not selection.changelog_queries:
            return BenchmarkAnswer(
                text=None,
                marks=[],
                selected_artifacts=[],
                changelog_queries=[],
                provenance=[select_provenance],
            )
        composed = self._backend.generate(
            prompt_name="qa-compose",
            prompt_version=ANSWERER_PROMPT_VERSION,
            system=COMPOSE_SYSTEM_PROMPT,
            user_content=self._compose_content(question, selection),
        )
        return BenchmarkAnswer(
            text=composed.text,
            marks=parse_marks(composed.text),
            selected_artifacts=list(selection.artifacts),
            changelog_queries=list(selection.changelog_queries),
            provenance=[select_provenance, composed.provenance],
        )

    def _select(self, question: str) -> tuple[AnswerSelection, GenerationProvenance]:
        result = self._backend.generate_structured(
            AnswerSelection,
            prompt_name="qa-select",
            prompt_version=ANSWERER_PROMPT_VERSION,
            system=SELECT_SYSTEM_PROMPT,
            user_content=self._index_content(question),
        )
        selection = result.output
        unknown = [aid for aid in selection.artifacts if aid not in self._entries]
        if unknown:
            raise GenerationError(f"qa-select chose unknown artifact ids: {', '.join(unknown)}")
        if len(selection.artifacts) > MAX_SELECTED_ARTIFACTS:
            raise GenerationError(
                f"qa-select chose {len(selection.artifacts)} artifacts "
                f"(limit {MAX_SELECTED_ARTIFACTS})"
            )
        if selection.changelog_queries and self._changelog is None:
            raise GenerationError("qa-select queried the changelog but it is unavailable this run")
        if len(selection.changelog_queries) > MAX_CHANGELOG_QUERIES:
            raise GenerationError(
                f"qa-select made {len(selection.changelog_queries)} changelog queries "
                f"(limit {MAX_CHANGELOG_QUERIES})"
            )
        return selection, result.provenance

    def _index_content(self, question: str) -> str:
        lines = [f"Question: {question}", "", "Knowledge base artifacts:"]
        if self._entries:
            lines += [
                f"- {entry.id}: {entry.title} — {entry.summary}" for entry in self._entries.values()
            ]
        else:
            lines.append("(none generated yet)")
        lines.append("")
        if self._changelog is not None:
            lines.append("Changelog: available — in-game patch notes, keyword-searchable.")
        else:
            lines.append("Changelog: not available this run.")
        return "\n".join(lines)

    def _compose_content(self, question: str, selection: AnswerSelection) -> str:
        parts = [f"Question: {question}", "", "Material:"]
        for artifact_id in selection.artifacts:
            entry = self._entries[artifact_id]
            parts.append(f"\n## {entry.id} — {entry.title}\n\n{entry.article}")
        for query in selection.changelog_queries:
            parts.append(f"\n## changelog search: {query!r}\n\n{self._changelog_hits(query)}")
        return "\n".join(parts)

    def _changelog_hits(self, query: str) -> str:
        """Newest matches first, by patch date. A broad query like "facets"
        can match dozens of introduction-era notes, and taking the head of
        the oldest-first search buried the 7.41 removal note the question
        was actually about (first live battery). Recency is the right
        relevance prior for a changelog, so the cap keeps the newest
        patches' hits (intra-patch note order preserved) and says how many
        older ones it dropped. Sorting on the hit's own date rather than
        manifest position keeps this true if a manifest ever ships
        newest-first."""
        changelog = self._changelog
        if changelog is None:  # guarded in _select; defensive here
            raise GenerationError("changelog queried but unavailable")
        hits = search_changelog(changelog, grep=query)
        if not hits:
            return "(no matches)"
        by_patch: dict[str, list[dict[str, Any]]] = {}
        for hit in hits:
            by_patch.setdefault(hit["patch"], []).append(hit)
        newest_first = [
            hit
            for patch_hits in sorted(
                by_patch.values(), key=lambda group: group[0].get("date") or "", reverse=True
            )
            for hit in patch_hits
        ]
        lines = []
        for hit in newest_first[:_CHANGELOG_HITS_PER_QUERY]:
            date = f" ({hit['date']})" if hit.get("date") else ""
            lines.append(
                f"[changelog:{hit['token']}] patch {hit['patch']}{date} "
                f"{hit['scope']}/{hit['entity']}: {hit['text']}"
            )
        if len(hits) > _CHANGELOG_HITS_PER_QUERY:
            lines.append(f"({len(hits) - _CHANGELOG_HITS_PER_QUERY} older matches omitted)")
        return "\n".join(lines)
