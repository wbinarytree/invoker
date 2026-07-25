from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from invoker.corpus.sections import CorpusSectionError, load_sections
from invoker.corpus.store import CorpusStore
from invoker.marks import MARK_KINDS, Mark, count_words, parse_marks, strip_marks

__all__ = [
    "MARK_KINDS",
    "Mark",
    "MarkResolution",
    "MarkResolver",
    "count_words",
    "parse_marks",
    "strip_marks",
]


@dataclass(frozen=True)
class MarkResolution:
    ok: bool
    reason: str | None = None


class MarkResolver:
    """Resolves marks for traceability, not truth (marks-not-verdicts).

    `corpus:` keys must be section citation keys of the stored expanded
    revision — the same key space generation validated against. `changelog:`
    keys must be tokens in the snapshot changelog. The remaining kinds gain
    resolvers with the generator slices that introduce them (item/hero:
    `gamefile`/`loc`); until then they report as unresolvable with a reason
    saying so.
    """

    def __init__(
        self,
        *,
        corpus_store: CorpusStore | None = None,
        changelog: dict[str, Any] | None = None,
    ) -> None:
        self._store = corpus_store
        self._section_keys: dict[tuple[str, str], set[str] | str] = {}
        self._changelog_tokens = _changelog_tokens(changelog) if changelog is not None else None

    def resolve(self, mark: Mark) -> MarkResolution:
        if mark.kind == "corpus":
            return self._resolve_corpus(mark.key)
        if mark.kind == "changelog":
            return self._resolve_changelog(mark.key)
        return MarkResolution(
            ok=False,
            reason=(
                f"no resolver for mark kind {mark.kind!r} yet (arrives with its generator slice)"
            ),
        )

    def _resolve_corpus(self, key: str) -> MarkResolution:
        if self._store is None:
            return MarkResolution(ok=False, reason="corpus store not available this run")
        host_key, slash, rest = key.partition("/")
        slug = rest.partition("@")[0]
        if not slash or not slug:
            return MarkResolution(ok=False, reason=f"malformed corpus key {key!r}")
        keys = self._load_section_keys(host_key, slug)
        if isinstance(keys, str):
            return MarkResolution(ok=False, reason=keys)
        if key not in keys:
            return MarkResolution(
                ok=False,
                reason=f"{key} is not a section key of the stored {host_key}/{slug} revision",
            )
        return MarkResolution(ok=True)

    def _load_section_keys(self, host_key: str, slug: str) -> set[str] | str:
        """Section citation keys for a page, cached; a load failure caches
        its message so each broken page is reported once, not re-read."""
        assert self._store is not None
        cache_key = (host_key, slug)
        cached = self._section_keys.get(cache_key)
        if cached is None:
            try:
                sections = load_sections(self._store, host_key, slug)
            except (CorpusSectionError, OSError) as exc:
                cached = str(exc)
            else:
                cached = {section.citation_key for section in sections}
            self._section_keys[cache_key] = cached
        return cached

    def _resolve_changelog(self, key: str) -> MarkResolution:
        if self._changelog_tokens is None:
            return MarkResolution(ok=False, reason="changelog not available this run")
        if key not in self._changelog_tokens:
            return MarkResolution(
                ok=False, reason=f"{key} is not a token in the snapshot changelog"
            )
        return MarkResolution(ok=True)


def _changelog_tokens(changelog: dict[str, Any]) -> set[str]:
    """Every citable token in the changelog: note, info, and section-title
    tokens (the shapes search_changelog and the snapshot builder emit)."""
    tokens: set[str] = set()

    def collect(notes: list[dict[str, Any]]) -> None:
        for note in notes:
            tokens.add(note["token"])
            info = note.get("info")
            if info:
                tokens.add(info["token"])

    for patch in changelog.get("patches", []):
        for section in patch.get("generic", []):
            title = section.get("title")
            if title:
                tokens.add(title["token"])
            collect(section.get("notes", []))
        for scope in ("items", "neutral_items", "neutral_creeps"):
            for notes in patch.get(scope, {}).values():
                collect(notes)
        for per_hero in patch.get("heroes", {}).values():
            for notes in per_hero.values():
                collect(notes)
    return tokens
