from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from invoker.corpus.sections import CorpusSectionError, load_sections
from invoker.corpus.store import CorpusStore
from invoker.marks import Mark


@dataclass(frozen=True)
class MarkResolution:
    ok: bool
    reason: str | None = None


_GAMEFILE_CLASSES: dict[str, tuple[str, frozenset[str]]] = {
    # class → (snapshot file, fixed section vocabulary — extended by code
    # change when a generator slice adds sections; spec decision 3)
    "items": ("items.json", frozenset({"cost", "components", "attribs", "mechanics"})),
    "abilities": ("abilities.json", frozenset()),
}


class MarkResolver:
    """Resolves marks for traceability, not truth (marks-not-verdicts).

    `corpus:` keys must be section citation keys of the stored expanded
    revision — the same key space generation validated against.
    `changelog:` keys must be tokens in the snapshot changelog.
    `gamefile:` keys (`<class>/<record>[#<section>]`) must name a record in
    the patch snapshot with a section from that class's fixed vocabulary;
    `loc:` keys must be localization tokens (the `ability`/`Ability` token
    casing variants both count — Valve mixes them). `stats:`/`human:` gain
    resolvers with the slices that introduce them.
    """

    def __init__(
        self,
        *,
        corpus_store: CorpusStore | None = None,
        changelog: dict[str, Any] | None = None,
        game_data_dir: Path | None = None,
        patch: str | None = None,
    ) -> None:
        self._store = corpus_store
        self._section_keys: dict[tuple[str, str], set[str] | str] = {}
        self._changelog_tokens = _changelog_tokens(changelog) if changelog is not None else None
        self._game_data_dir = game_data_dir
        self._patch = patch
        self._gamefile_records: dict[str, set[str] | str] = {}
        self._loc_tokens: set[str] | str | None = None

    def resolve(self, mark: Mark) -> MarkResolution:
        if mark.kind == "corpus":
            return self._resolve_corpus(mark.key)
        if mark.kind == "changelog":
            return self._resolve_changelog(mark.key)
        if mark.kind == "gamefile":
            return self._resolve_gamefile(mark.key)
        if mark.kind == "loc":
            return self._resolve_loc(mark.key)
        return MarkResolution(
            ok=False,
            reason=(
                f"no resolver for mark kind {mark.kind!r} yet (arrives with its generator slice)"
            ),
        )

    def _resolve_gamefile(self, key: str) -> MarkResolution:
        if self._game_data_dir is None or self._patch is None:
            return MarkResolution(ok=False, reason="game-file snapshot not available this run")
        klass, slash, rest = key.partition("/")
        record, _, section = rest.partition("#")
        if not slash or not record or klass not in _GAMEFILE_CLASSES:
            known = ", ".join(sorted(_GAMEFILE_CLASSES))
            return MarkResolution(
                ok=False, reason=f"malformed gamefile key {key!r} (known classes: {known})"
            )
        filename, sections = _GAMEFILE_CLASSES[klass]
        records = self._load_gamefile_records(klass, filename)
        if isinstance(records, str):
            return MarkResolution(ok=False, reason=records)
        if record not in records:
            return MarkResolution(
                ok=False, reason=f"{record} is not in the {self._patch} {klass} snapshot"
            )
        if section and section not in sections:
            return MarkResolution(
                ok=False, reason=f"unknown section {section!r} for gamefile class {klass!r}"
            )
        return MarkResolution(ok=True)

    def _load_gamefile_records(self, klass: str, filename: str) -> set[str] | str:
        assert self._game_data_dir is not None and self._patch is not None
        cached = self._gamefile_records.get(klass)
        if cached is None:
            path = self._game_data_dir / self._patch / filename
            try:
                cached = set(json.loads(path.read_text()))
            except (OSError, json.JSONDecodeError) as exc:
                cached = f"cannot read {path}: {exc}"
            self._gamefile_records[klass] = cached
        return cached

    def _resolve_loc(self, token: str) -> MarkResolution:
        if self._game_data_dir is None or self._patch is None:
            return MarkResolution(ok=False, reason="game-file snapshot not available this run")
        tokens = self._load_loc_tokens()
        if isinstance(tokens, str):
            return MarkResolution(ok=False, reason=tokens)
        if token in tokens or _swap_ability_case(token) in tokens:
            return MarkResolution(ok=True)
        return MarkResolution(ok=False, reason=f"{token} is not in the {self._patch} localization")

    def _load_loc_tokens(self) -> set[str] | str:
        assert self._game_data_dir is not None and self._patch is not None
        if self._loc_tokens is None:
            path = self._game_data_dir / self._patch / "localization" / "english.json"
            try:
                self._loc_tokens = set(json.loads(path.read_text()))
            except (OSError, json.JSONDecodeError) as exc:
                self._loc_tokens = f"cannot read {path}: {exc}"
        return self._loc_tokens

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


def _swap_ability_case(token: str) -> str:
    if "DOTA_Tooltip_ability_" in token:
        return token.replace("DOTA_Tooltip_ability_", "DOTA_Tooltip_Ability_", 1)
    return token.replace("DOTA_Tooltip_Ability_", "DOTA_Tooltip_ability_", 1)


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
