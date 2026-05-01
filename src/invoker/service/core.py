from __future__ import annotations

import dataclasses
import json
import re
from functools import cached_property
from pathlib import Path
from typing import Any

import yaml

from invoker.kg.hero_context import (
    HeroNotFoundError,
    build_hero_context_from_source,
)
from invoker.paths import team_index_file, team_registry_file
from invoker.sources.game_files import GameFilesSource, GameFilesSourceError

SERVICE_SCHEMA_VERSION = 1
BUNDLE_SCHEMA_VERSION = 1


class KnowledgeServiceError(LookupError):
    def __init__(
        self,
        code: str,
        message: str,
        *,
        status_code: int = 400,
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.code = code
        self.message = message
        self.status_code = status_code
        self.details = details or {}


class KnowledgeService:
    """Read-only local knowledge service over one explicit resource bundle."""

    def __init__(self, bundle_root: Path) -> None:
        self.bundle_root = bundle_root
        if not self.bundle_root.exists():
            raise KnowledgeServiceError(
                "bundle_not_found",
                f"resource bundle does not exist: {self.bundle_root}",
                status_code=404,
            )

    @cached_property
    def metadata(self) -> dict[str, Any]:
        path = self.bundle_root / "bundle.json"
        if not path.exists():
            raise KnowledgeServiceError(
                "missing_bundle_metadata",
                f"resource bundle is missing metadata file: {path}",
                status_code=500,
            )
        raw = json.loads(path.read_text())
        if not isinstance(raw, dict):
            raise KnowledgeServiceError(
                "invalid_bundle_metadata",
                f"resource bundle metadata must be a JSON object: {path}",
                status_code=500,
            )
        if raw.get("schema_version") != BUNDLE_SCHEMA_VERSION:
            raise KnowledgeServiceError(
                "unsupported_bundle_schema",
                "resource bundle metadata has unsupported schema_version="
                f"{raw.get('schema_version')!r}; expected {BUNDLE_SCHEMA_VERSION}",
                status_code=500,
            )
        return raw

    @cached_property
    def patches(self) -> list[str]:
        raw = self.metadata.get("patches")
        if isinstance(raw, list):
            patches = sorted({str(p) for p in raw if isinstance(p, str) and p})
        else:
            patches = []
        if not patches:
            patches = sorted(
                p.name
                for p in (self.bundle_root / "derived").iterdir()
                if p.is_dir()
            ) if (self.bundle_root / "derived").exists() else []
        return patches

    @cached_property
    def default_patch(self) -> str | None:
        raw = self.metadata.get("default_patch")
        return raw if isinstance(raw, str) and raw else None

    def list_bundle_patches(self) -> dict[str, Any]:
        patch = self.default_patch if self.default_patch in self.patches else None
        return self._envelope(
            kind="bundle_patches",
            patch=patch,
            data={"patches": self.patches, "default_patch": patch},
            source={
                "artifact": "bundle_metadata",
                "schema_version": _int_or_none(self.metadata.get("schema_version")),
            },
        )

    def lookup_hero(self, query: str | int, patch: str | None = None) -> dict[str, Any]:
        resolved_patch = self._resolve_patch(patch)
        token = _normalize(str(query))
        candidates = [
            _hero_candidate(hero)
            for hero in self._game_source(resolved_patch).heroes()
            if token in _hero_tokens(hero)
        ]
        return self._envelope(
            kind="hero_lookup",
            patch=resolved_patch,
            data={"query": str(query), "candidates": candidates},
            source=self._game_source_metadata(resolved_patch),
        )

    def get_hero_constants(self, hero: str | int, patch: str | None = None) -> dict[str, Any]:
        resolved_patch = self._resolve_patch(patch)
        try:
            packet = build_hero_context_from_source(
                self._game_source(resolved_patch), str(hero), patch=resolved_patch
            )
        except (HeroNotFoundError, GameFilesSourceError) as exc:
            raise KnowledgeServiceError(
                "hero_constants_not_found",
                "resource bundle does not contain game constants for "
                f"hero={hero!r} patch={resolved_patch}: {exc}",
                status_code=404,
            ) from exc
        return self._envelope(
            kind="hero_constants",
            patch=resolved_patch,
            data=dataclasses.asdict(packet),
            source=self._game_source_metadata(resolved_patch),
        )

    def resolve_team(self, query: str | int, patch: str | None = None) -> dict[str, Any]:
        resolved_patch = self._resolve_patch(patch)
        token = _normalize(str(query))
        candidates = [
            candidate
            for candidate in self._team_candidates(resolved_patch)
            if token in _team_tokens(candidate)
        ]
        return self._envelope(
            kind="team_resolution",
            patch=resolved_patch,
            data={"query": str(query), "candidates": candidates},
            source=self._team_index_source(resolved_patch),
        )

    def resolve_player(
        self,
        query: str | int,
        team: str | int | None = None,
        patch: str | None = None,
    ) -> dict[str, Any]:
        resolved_patch = self._resolve_patch(patch)
        profiles = (
            [self._load_profile_for_team(team, resolved_patch)]
            if team is not None
            else [
                self._load_profile_entry(resolved_patch, entry)
                for entry in self._team_entries(resolved_patch)
            ]
        )
        token = _normalize(str(query))
        candidates: list[dict[str, Any]] = []
        seen: set[tuple[int, int | None]] = set()
        for profile in profiles:
            team_view = self._team_identity(profile)
            registry_entry = self._team_registry_entry(team_view.get("team_id"))
            for candidate in _player_candidates(profile, team_view):
                _merge_registry_player(candidate, registry_entry)
                key = (candidate["account_id"], candidate.get("team_id"))
                if key in seen or token not in _player_tokens(candidate):
                    continue
                seen.add(key)
                candidates.append(candidate)
        return self._envelope(
            kind="player_resolution",
            patch=resolved_patch,
            data={
                "query": str(query),
                "team": str(team) if team is not None else None,
                "candidates": candidates,
            },
            source=self._team_index_source(resolved_patch),
        )

    def get_team_profile(self, team: str | int, patch: str | None = None) -> dict[str, Any]:
        resolved_patch = self._resolve_patch(patch)
        profile = self._load_profile_for_team(team, resolved_patch)
        return self._envelope(
            kind="team_profile",
            patch=resolved_patch,
            data=self._public_profile(profile),
            source=self._team_profile_source(profile),
        )

    def get_team_roster(self, team: str | int, patch: str | None = None) -> dict[str, Any]:
        resolved_patch = self._resolve_patch(patch)
        profile = self._load_profile_for_team(team, resolved_patch)
        return self._envelope(
            kind="team_roster",
            patch=resolved_patch,
            data={
                "team": self._public_team(profile),
                "roster": self._public_roster(profile),
            },
            source=self._team_profile_source(profile),
        )

    def get_team_hero_pool(self, team: str | int, patch: str | None = None) -> dict[str, Any]:
        resolved_patch = self._resolve_patch(patch)
        profile = self._load_profile_for_team(team, resolved_patch)
        return self._envelope(
            kind="team_hero_pool",
            patch=resolved_patch,
            data={
                "team": self._public_team(profile),
                "hero_pool": self._public_hero_pool(profile),
            },
            source=self._team_profile_source(profile),
        )

    def get_team_player_hero_pool(
        self,
        team: str | int,
        player: str | int,
        patch: str | None = None,
    ) -> dict[str, Any]:
        resolved_patch = self._resolve_patch(patch)
        profile = self._load_profile_for_team(team, resolved_patch)
        player_entry = self._resolve_one_player(profile, player, resolved_patch)
        data = {
            "team": self._public_team(profile),
            "player": {
                key: value for key, value in player_entry.items() if key != "hero_pool"
            },
            "hero_pool": player_entry.get("hero_pool") or [],
        }
        return self._envelope(
            kind="team_player_hero_pool",
            patch=resolved_patch,
            data=data,
            source=self._team_profile_source(profile),
        )

    def _resolve_patch(self, patch: str | None) -> str:
        if patch is not None:
            if patch not in self.patches:
                raise KnowledgeServiceError(
                    "patch_not_found",
                    f"resource bundle does not contain patch={patch!r}",
                    status_code=404,
                    details={"available_patches": self.patches},
                )
            return patch
        if self.default_patch in self.patches:
            return str(self.default_patch)
        if len(self.patches) == 1:
            return self.patches[0]
        raise KnowledgeServiceError(
            "patch_ambiguous",
            "resource bundle contains multiple patches and no default patch",
            details={"available_patches": self.patches},
        )

    def _game_source(self, patch: str) -> GameFilesSource:
        cache_name = f"_game_source_{_safe_attr(patch)}"
        source = self.__dict__.get(cache_name)
        if source is None:
            try:
                source = GameFilesSource(self.bundle_root / "game_constants", patch)
            except GameFilesSourceError as exc:
                raise KnowledgeServiceError(
                    "missing_game_constants",
                    "resource bundle does not contain game constants for "
                    f"patch={patch}: {exc}",
                    status_code=404,
                ) from exc
            self.__dict__[cache_name] = source
        return source

    def _game_source_metadata(self, patch: str) -> dict[str, Any]:
        snapshot_path = self.bundle_root / "game_constants" / patch / "snapshot.json"
        snapshot = json.loads(snapshot_path.read_text()) if snapshot_path.exists() else {}
        return {
            "artifact": "game_constants",
            "schema_version": _int_or_none(snapshot.get("schema_version")),
            "generated_at": snapshot.get("generated_at"),
            "source": snapshot.get("source"),
            "locale": snapshot.get("locale"),
        }

    def _team_index_source(self, patch: str) -> dict[str, Any]:
        index = self._team_index(patch)
        return {
            "artifact": "team_profile_index",
            "schema_version": _int_or_none(index.get("schema_version")),
        }

    def _team_profile_source(self, profile: dict[str, Any]) -> dict[str, Any]:
        raw_source = profile.get("source")
        source: dict[str, Any] = raw_source if isinstance(raw_source, dict) else {}
        return {
            "artifact": "team_profile",
            "schema_version": _int_or_none(profile.get("schema_version")),
            "fetched_at": source.get("fetched_at"),
            "missing_match_detail_count": source.get("missing_match_detail_count"),
        }

    def _team_index(self, patch: str) -> dict[str, Any]:
        path = team_index_file(self.bundle_root, patch)
        if not path.exists():
            raise KnowledgeServiceError(
                "missing_team_index",
                "resource bundle does not contain team profiles for "
                f"patch={patch}; missing {path}",
                status_code=404,
            )
        raw = json.loads(path.read_text())
        if not isinstance(raw, dict):
            raise KnowledgeServiceError(
                "invalid_team_index",
                f"team profile index must be a JSON object: {path}",
                status_code=500,
            )
        return raw

    def _team_entries(self, patch: str) -> list[dict[str, Any]]:
        profiles = self._team_index(patch).get("profiles") or []
        return [entry for entry in profiles if isinstance(entry, dict)]

    def _team_candidates(self, patch: str) -> list[dict[str, Any]]:
        candidates: list[dict[str, Any]] = []
        for entry in self._team_entries(patch):
            profile = self._load_profile_entry(patch, entry)
            team = self._team_identity(profile)
            team["patch"] = patch
            candidates.append(team)
        return candidates

    def _load_profile_for_team(self, team: str | int, patch: str) -> dict[str, Any]:
        team_id = self._resolve_one_team_id(team, patch)
        entries = [entry for entry in self._team_entries(patch) if entry.get("team_id") == team_id]
        if not entries:
            raise KnowledgeServiceError(
                "team_profile_not_found",
                f"No team profile for team_id={team_id} patch={patch}. "
                f"Run: invoker build-team-profile --team-id {team_id} --patch {patch}",
                status_code=404,
            )
        if len(entries) > 1:
            raise KnowledgeServiceError(
                "team_profile_ambiguous",
                f"Multiple team profiles exist for team_id={team_id} patch={patch}. "
                "Rebuild the resource bundle with one public profile for this team.",
                details={"team_id": team_id, "patch": patch},
            )
        return self._load_profile_entry(patch, entries[0])

    def _load_profile_entry(self, patch: str, entry: dict[str, Any]) -> dict[str, Any]:
        path = self._profile_path(patch, entry)
        if not path.exists():
            team_id = entry.get("team_id")
            raise KnowledgeServiceError(
                "team_profile_not_found",
                f"Team profile index references missing file for team_id={team_id} "
                f"patch={patch}: {path}. Run: invoker build-team-profile "
                f"--team-id {team_id} --patch {patch}",
                status_code=404,
            )
        raw = json.loads(path.read_text())
        if not isinstance(raw, dict):
            raise KnowledgeServiceError(
                "invalid_team_profile",
                f"team profile must be a JSON object: {path}",
                status_code=500,
            )
        expected_team_id = entry.get("team_id")
        actual_team_id = _profile_team(raw).get("team_id")
        if isinstance(expected_team_id, int) and actual_team_id != expected_team_id:
            raise KnowledgeServiceError(
                "invalid_team_profile",
                "team profile team_id does not match index entry: "
                f"expected {expected_team_id}, found {actual_team_id!r}",
                status_code=500,
            )
        return raw

    def _profile_path(self, patch: str, entry: dict[str, Any]) -> Path:
        teams_root = team_index_file(self.bundle_root, patch).parent
        path_value = entry.get("path")
        if isinstance(path_value, str) and path_value:
            raw_path = Path(path_value)
            if raw_path.is_absolute():
                raise KnowledgeServiceError(
                    "invalid_team_index",
                    f"team profile index path must be relative: {path_value}",
                    status_code=500,
                )
            profile_path = (teams_root / raw_path).resolve(strict=False)
            teams_root_resolved = teams_root.resolve(strict=False)
            if not profile_path.is_relative_to(teams_root_resolved):
                raise KnowledgeServiceError(
                    "invalid_team_index",
                    "team profile index path escapes the resource bundle: "
                    f"{path_value}",
                    status_code=500,
                )
            return profile_path
        roster_hash = entry.get("roster_hash")
        team_id = entry.get("team_id")
        if isinstance(team_id, int) and isinstance(roster_hash, str):
            return (
                teams_root
                / str(team_id)
                / roster_hash
                / "profile.json"
            )
        raise KnowledgeServiceError(
            "invalid_team_index",
            f"team profile index entry is missing path fields for patch={patch}",
            status_code=500,
        )

    def _resolve_one_team_id(self, team: str | int, patch: str) -> int:
        if isinstance(team, int) or str(team).strip().isdigit():
            team_id = int(team)
            if any(entry.get("team_id") == team_id for entry in self._team_entries(patch)):
                return team_id
            raise KnowledgeServiceError(
                "team_profile_not_found",
                f"No team profile for team_id={team_id} patch={patch}. "
                f"Run: invoker build-team-profile --team-id {team_id} --patch {patch}",
                status_code=404,
            )
        resolution = self.resolve_team(str(team), patch=patch)
        candidates = resolution["data"]["candidates"]
        if not candidates:
            raise KnowledgeServiceError(
                "team_not_found",
                f"No team matched query={team!r} patch={patch}",
                status_code=404,
            )
        team_ids = sorted({candidate["team_id"] for candidate in candidates})
        if len(team_ids) > 1:
            raise KnowledgeServiceError(
                "team_ambiguous",
                f"Team query {team!r} is ambiguous for patch={patch}",
                details={"candidates": candidates},
            )
        return team_ids[0]

    def _resolve_one_player(
        self,
        profile: dict[str, Any],
        player: str | int,
        patch: str,
    ) -> dict[str, Any]:
        team_id = (profile.get("team") or {}).get("team_id")
        resolution = self.resolve_player(player, team=team_id, patch=patch)
        candidates = resolution["data"]["candidates"]
        if not candidates:
            raise KnowledgeServiceError(
                "player_not_found",
                f"No player matched query={player!r} team_id={team_id} patch={patch}",
                status_code=404,
            )
        account_ids = sorted({candidate["account_id"] for candidate in candidates})
        if len(account_ids) > 1:
            raise KnowledgeServiceError(
                "player_ambiguous",
                f"Player query {player!r} is ambiguous for team_id={team_id} patch={patch}",
                details={"candidates": candidates},
            )
        for entry in profile.get("players") or []:
            if isinstance(entry, dict) and entry.get("account_id") == account_ids[0]:
                enriched = dict(entry)
                raw_team = profile.get("team")
                team = raw_team if isinstance(raw_team, dict) else {}
                _merge_registry_player(
                    enriched, self._team_registry_entry(team.get("team_id"))
                )
                return enriched
        raise KnowledgeServiceError(
            "player_hero_pool_not_found",
            f"No player hero pool for account_id={account_ids[0]} team_id={team_id} patch={patch}",
            status_code=404,
        )

    @cached_property
    def _team_registry(self) -> dict[int, dict[str, Any]]:
        path = team_registry_file(self.bundle_root)
        if not path.exists():
            return {}
        raw = yaml.safe_load(path.read_text()) or {}
        if not isinstance(raw, dict):
            raise KnowledgeServiceError(
                "invalid_team_registry",
                f"team registry must be a YAML object: {path}",
                status_code=500,
            )
        teams = raw.get("teams") or []
        if not isinstance(teams, list):
            raise KnowledgeServiceError(
                "invalid_team_registry",
                f"team registry teams must be a list: {path}",
                status_code=500,
            )
        out: dict[int, dict[str, Any]] = {}
        for team in teams:
            if isinstance(team, dict) and isinstance(team.get("team_id"), int):
                out[team["team_id"]] = team
        return out

    def _team_registry_entry(self, team_id: Any) -> dict[str, Any] | None:
        return self._team_registry.get(team_id) if isinstance(team_id, int) else None

    def _team_identity(self, profile: dict[str, Any]) -> dict[str, Any]:
        team = _profile_team(profile)
        registry = self._team_registry_entry(team.get("team_id")) or {}
        observed = (
            team.get("observed_names")
            if isinstance(team.get("observed_names"), list)
            else []
        )
        aliases = _strings(team.get("aliases")) + _strings(registry.get("aliases"))
        registry_name = registry.get("name") if isinstance(registry.get("name"), str) else None
        return {
            "team_id": team.get("team_id"),
            "name": registry_name or team.get("name"),
            "tag": team.get("tag"),
            "aliases": sorted(set(aliases)),
            "observed_names": observed,
            "registry_name": registry_name,
        }

    def _public_team(self, profile: dict[str, Any]) -> dict[str, Any]:
        raw = _strip_internal_storage(profile.get("team") or {})
        if not isinstance(raw, dict):
            return {}
        identity = self._team_identity(profile)
        raw["name"] = identity.get("name")
        raw["aliases"] = identity.get("aliases") or []
        if identity.get("registry_name") is not None:
            raw["registry_name"] = identity["registry_name"]
        return raw

    def _public_roster(self, profile: dict[str, Any]) -> dict[str, Any]:
        raw = _strip_internal_storage(profile.get("roster") or {})
        if not isinstance(raw, dict):
            return {}
        team = _profile_team(profile)
        registry = self._team_registry_entry(team.get("team_id"))
        players = raw.get("players")
        if isinstance(players, list):
            raw["players"] = [
                _enrich_public_player(player, registry)
                if isinstance(player, dict)
                else player
                for player in players
            ]
        return raw

    def _public_profile(self, profile: dict[str, Any]) -> dict[str, Any]:
        raw = _strip_internal_storage(profile)
        if not isinstance(raw, dict):
            return {}
        raw["team"] = self._public_team(profile)
        raw["roster"] = self._public_roster(profile)
        raw["hero_pool"] = self._public_hero_pool(profile)
        raw["players"] = self._public_players(profile)
        return raw

    def _public_hero_pool(self, profile: dict[str, Any]) -> list[Any]:
        raw_pool = profile.get("hero_pool") or []
        if not isinstance(raw_pool, list):
            return []
        registry = self._team_registry_entry(_profile_team(profile).get("team_id"))
        return [
            _enrich_hero_pool_entry(entry, registry)
            if isinstance(entry, dict)
            else entry
            for entry in _strip_internal_storage(raw_pool)
        ]

    def _public_players(self, profile: dict[str, Any]) -> list[Any]:
        raw_players = profile.get("players") or []
        if not isinstance(raw_players, list):
            return []
        registry = self._team_registry_entry(_profile_team(profile).get("team_id"))
        return [
            _enrich_public_player(player, registry)
            if isinstance(player, dict)
            else player
            for player in _strip_internal_storage(raw_players)
        ]

    def _envelope(
        self,
        *,
        kind: str,
        patch: str | None,
        data: dict[str, Any],
        source: dict[str, Any],
    ) -> dict[str, Any]:
        return {
            "service_schema_version": SERVICE_SCHEMA_VERSION,
            "patch": patch,
            "kind": kind,
            "data": data,
            "source": source,
        }


def _hero_candidate(hero: dict[str, Any]) -> dict[str, Any]:
    internal_name = str(hero.get("name") or "")
    return {
        "hero_id": hero.get("id"),
        "hero_slug": internal_name.removeprefix("npc_dota_hero_"),
        "internal_name": internal_name,
        "localized_name": hero.get("localized_name"),
        "primary_attr": hero.get("primary_attr"),
        "attack_type": hero.get("attack_type"),
        "roles": hero.get("roles") or [],
    }


def _hero_tokens(hero: dict[str, Any]) -> set[str]:
    internal_name = str(hero.get("name") or "")
    return {
        _normalize(str(hero.get("id") or "")),
        _normalize(internal_name),
        _normalize(internal_name.removeprefix("npc_dota_hero_")),
        _normalize(str(hero.get("localized_name") or "")),
    }


def _profile_team(profile: dict[str, Any]) -> dict[str, Any]:
    raw_team = profile.get("team")
    return raw_team if isinstance(raw_team, dict) else {}


def _team_tokens(candidate: dict[str, Any]) -> set[str]:
    tokens = {_normalize(str(candidate.get("team_id") or ""))}
    for key in ("name", "tag"):
        value = candidate.get(key)
        if isinstance(value, str):
            tokens.add(_normalize(value))
    for alias in candidate.get("aliases") or []:
        if isinstance(alias, str):
            tokens.add(_normalize(alias))
    for observed in candidate.get("observed_names") or []:
        if isinstance(observed, dict) and isinstance(observed.get("name"), str):
            tokens.add(_normalize(observed["name"]))
    return tokens


def _player_candidates(profile: dict[str, Any], team: dict[str, Any]) -> list[dict[str, Any]]:
    candidates: dict[int, dict[str, Any]] = {}
    for collection, role in (
        ((profile.get("roster") or {}).get("players") or [], "roster"),
        (profile.get("players") or [], "player_pool"),
        ((profile.get("roster") or {}).get("stand_ins") or [], "stand_in"),
    ):
        for player in collection:
            if not isinstance(player, dict) or not isinstance(player.get("account_id"), int):
                continue
            account_id = player["account_id"]
            entry = candidates.setdefault(
                account_id,
                {
                    "account_id": account_id,
                    "personaname": player.get("personaname"),
                    "team_id": team.get("team_id"),
                    "team_name": team.get("name"),
                    "roles": [],
                },
            )
            if entry.get("personaname") is None and player.get("personaname") is not None:
                entry["personaname"] = player.get("personaname")
            if role not in entry["roles"]:
                entry["roles"].append(role)
    return list(candidates.values())


def _player_tokens(candidate: dict[str, Any]) -> set[str]:
    tokens = {_normalize(str(candidate.get("account_id") or ""))}
    for key in ("personaname", "registry_name"):
        name = candidate.get(key)
        if isinstance(name, str):
            tokens.add(_normalize(name))
    return tokens


def _registry_players_by_id(registry: dict[str, Any] | None) -> dict[int, dict[str, Any]]:
    if registry is None:
        return {}
    players = registry.get("players")
    if not isinstance(players, list):
        return {}
    out: dict[int, dict[str, Any]] = {}
    for player in players:
        if isinstance(player, dict) and isinstance(player.get("account_id"), int):
            out[player["account_id"]] = player
    return out


def _merge_registry_player(
    player: dict[str, Any],
    registry: dict[str, Any] | None,
) -> None:
    account_id = player.get("account_id")
    if not isinstance(account_id, int):
        return
    registry_player = _registry_players_by_id(registry).get(account_id)
    if registry_player is None:
        return
    name = registry_player.get("name")
    if isinstance(name, str):
        player["registry_name"] = name
        if player.get("personaname") is None:
            player["personaname"] = name
    position = registry_player.get("position")
    if isinstance(position, int):
        player["registry_position"] = position


def _enrich_public_player(
    player: dict[str, Any],
    registry: dict[str, Any] | None,
) -> dict[str, Any]:
    enriched = dict(player)
    _merge_registry_player(enriched, registry)
    return enriched


def _enrich_hero_pool_entry(
    entry: dict[str, Any],
    registry: dict[str, Any] | None,
) -> dict[str, Any]:
    enriched = dict(entry)
    players = enriched.get("players")
    if isinstance(players, list):
        enriched["players"] = [
            _enrich_public_player(player, registry)
            if isinstance(player, dict)
            else player
            for player in players
        ]
    return enriched


def _strings(value: Any) -> list[str]:
    return [item for item in value if isinstance(item, str)] if isinstance(value, list) else []


def _strip_internal_storage(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: _strip_internal_storage(child)
            for key, child in value.items()
            if key != "roster_hash"
        }
    if isinstance(value, list):
        return [_strip_internal_storage(child) for child in value]
    return value


def _normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def _int_or_none(value: Any) -> int | None:
    return value if isinstance(value, int) else None


def _safe_attr(value: str) -> str:
    return re.sub(r"\W+", "_", value)
