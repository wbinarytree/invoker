"""Benchmark roster: heroes and pairs sampled from real professional matches.

The vertical slice (spec `docs/specs/2026-09-01-dota-knowledge-artifact-v1.md`,
slice 1) samples its hero roster from a real final: picks give the roster,
co-occurrence gives the pair set. Match ids and picks come from OpenDota
match-detail payloads, never from memory; hero ids resolve against the KB
patch's game-file snapshot; match dates are checked against the manual
patch windows. Anything that does not line up fails loudly.
"""

from __future__ import annotations

import hashlib
import json
from datetime import UTC, datetime
from itertools import combinations
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict

from invoker.patches import PatchWindow, load_patch_windows, patch_window_for_timestamp

SCHEMA_VERSION = 1
GENERATOR_VERSION = "1"
PICKS_PER_SIDE = 5
RADIANT, DIRE = 0, 1


class RosterError(ValueError):
    pass


class RosterHero(BaseModel):
    model_config = ConfigDict(extra="forbid")

    hero_id: int
    internal_name: str
    slug: str
    display_name: str
    picks: int
    games: list[int]


class RosterPair(BaseModel):
    model_config = ConfigDict(extra="forbid")

    a: str
    b: str
    a_hero_id: int
    b_hero_id: int
    ally_games: list[int]
    enemy_games: list[int]


class RosterMatch(BaseModel):
    model_config = ConfigDict(extra="forbid")

    match_id: int
    start_time: int
    start_date: str
    radiant_team: str | None
    dire_team: str | None
    radiant_picks: list[str]
    dire_picks: list[str]
    opendota_patch_id: int | None
    patch_window: str | None


class SamplingFrame(BaseModel):
    model_config = ConfigDict(extra="forbid")

    league_id: int | None
    league_name: str | None
    series_id: int | None
    series_type: int | None
    teams: list[str]


class PatchCheck(BaseModel):
    model_config = ConfigDict(extra="forbid")

    kb_patch: str
    windows_source: str
    match_windows: dict[str, str | None]
    all_in_kb_patch: bool
    kb_window_open_ended: bool
    note: str


class RosterProvenance(BaseModel):
    """Derived-file header per GUIDELINES: schema/generator version, source patch, timestamp.

    `generated_at` is wall-clock; `RosterArtifact.fingerprint` (sha256 over everything
    except provenance) is the field to compare when checking that a rebuild changed
    nothing.
    """

    model_config = ConfigDict(extra="forbid")

    source: str
    generator_version: str
    source_patch: str
    hero_identity_source: str
    generated_at: str


class RosterArtifact(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: int
    label: str
    kb_patch: str
    fingerprint: str
    sampling_frame: SamplingFrame
    matches: list[RosterMatch]
    heroes: list[RosterHero]
    pairs: list[RosterPair]
    patch_check: PatchCheck
    provenance: RosterProvenance


def _fingerprint(payload: dict[str, Any]) -> str:
    body = {k: v for k, v in payload.items() if k not in ("fingerprint", "provenance")}
    return hashlib.sha256(json.dumps(body, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def _int_or_none(value: Any) -> int | None:
    return int(value) if isinstance(value, int | float) and not isinstance(value, bool) else None


def _team_name(match: dict[str, Any], side: str) -> str | None:
    team = match.get(f"{side}_team")
    if isinstance(team, dict) and isinstance(team.get("name"), str):
        return team["name"]
    name = match.get(f"{side}_name")
    return name if isinstance(name, str) else None


def _picks_by_side(
    match: dict[str, Any], hero_index: dict[int, dict[str, Any]]
) -> dict[int, list[int]]:
    match_id = match.get("match_id")
    picks_bans = match.get("picks_bans")
    if not isinstance(picks_bans, list) or not picks_bans:
        raise RosterError(f"match {match_id} has no picks_bans; OpenDota may not have parsed it")
    ordered = sorted(picks_bans, key=lambda entry: entry.get("order", 0))
    sides: dict[int, list[int]] = {RADIANT: [], DIRE: []}
    for entry in ordered:
        if not entry.get("is_pick"):
            continue
        team = entry.get("team")
        hero_id = entry.get("hero_id")
        if team not in sides or not isinstance(hero_id, int):
            raise RosterError(f"match {match_id} has a malformed pick entry: {entry!r}")
        if hero_id not in hero_index:
            raise RosterError(
                f"match {match_id} picks hero id {hero_id}, which is not in the game snapshot"
            )
        sides[team].append(hero_id)
    for team, picks in sides.items():
        if len(picks) != PICKS_PER_SIDE:
            raise RosterError(
                f"match {match_id} side {team} has {len(picks)} picks, expected {PICKS_PER_SIDE}"
            )
        if len(set(picks)) != PICKS_PER_SIDE:
            raise RosterError(f"match {match_id} side {team} picks a hero twice: {picks}")
    if set(sides[RADIANT]) & set(sides[DIRE]):
        raise RosterError(f"match {match_id} has a hero on both sides")
    return sides


def _same_or_fail(values: list[Any], *, field: str) -> Any:
    distinct = {json.dumps(value, sort_keys=True) for value in values}
    if len(distinct) != 1:
        raise RosterError(f"matches disagree on {field}: {sorted(distinct)}")
    return values[0]


def build_roster(
    matches: list[dict[str, Any]],
    hero_records: list[dict[str, Any]],
    *,
    kb_patch: str,
    label: str,
    hero_identity_source: str,
    windows: list[PatchWindow] | None = None,
    windows_source: str = "src/invoker/patches.json",
) -> RosterArtifact:
    """Derive roster, co-occurrence pairs, and the patch check from match payloads.

    `hero_records` is `GameFilesSource.heroes()` output (id, name, localized_name).
    `windows` defaults to the packaged patch windows.
    """
    if not matches:
        raise RosterError("no matches given")
    match_ids: list[int] = []
    for match in matches:
        match_id = match.get("match_id")
        if not isinstance(match_id, int):
            raise RosterError(f"match payload missing match_id: {str(match)[:120]}")
        match_ids.append(match_id)
    if len(set(match_ids)) != len(match_ids):
        raise RosterError(f"duplicate match ids given: {sorted(match_ids)}")
    hero_index = {int(record["id"]): record for record in hero_records}

    league_id = _same_or_fail([_int_or_none(m.get("leagueid")) for m in matches], field="leagueid")
    series_id = _same_or_fail(
        [_int_or_none(m.get("series_id")) for m in matches], field="series_id"
    )
    series_type = _same_or_fail(
        [_int_or_none(m.get("series_type")) for m in matches], field="series_type"
    )
    league_name = _same_or_fail(
        [
            (m.get("league") or {}).get("name") if isinstance(m.get("league"), dict) else None
            for m in matches
        ],
        field="league name",
    )

    roster_matches: list[RosterMatch] = []
    hero_games: dict[int, list[int]] = {}
    pair_games: dict[tuple[int, int], dict[str, list[int]]] = {}
    teams: set[str] = set()

    def slug_of(hero_id: int) -> str:
        return str(hero_index[hero_id]["name"]).removeprefix("npc_dota_hero_")

    for match in sorted(matches, key=lambda m: (m.get("start_time") or 0, m.get("match_id") or 0)):
        match_id = match.get("match_id")
        start_time = match.get("start_time")
        if not isinstance(match_id, int) or not isinstance(start_time, int):
            raise RosterError(f"match payload missing match_id/start_time: {match!r:.120}")
        sides = _picks_by_side(match, hero_index)
        window = patch_window_for_timestamp(start_time, windows)
        for side_name in ("radiant", "dire"):
            name = _team_name(match, side_name)
            if name:
                teams.add(name)
        roster_matches.append(
            RosterMatch(
                match_id=match_id,
                start_time=start_time,
                start_date=datetime.fromtimestamp(start_time, UTC).date().isoformat(),
                radiant_team=_team_name(match, "radiant"),
                dire_team=_team_name(match, "dire"),
                radiant_picks=[slug_of(h) for h in sides[RADIANT]],
                dire_picks=[slug_of(h) for h in sides[DIRE]],
                opendota_patch_id=_int_or_none(match.get("patch")),
                patch_window=window.patch if window else None,
            )
        )
        for hero_id in sides[RADIANT] + sides[DIRE]:
            hero_games.setdefault(hero_id, []).append(match_id)
        for side in sides.values():
            for a, b in combinations(sorted(side), 2):
                pair_games.setdefault((a, b), {"ally": [], "enemy": []})["ally"].append(match_id)
        for a in sides[RADIANT]:
            for b in sides[DIRE]:
                key = (min(a, b), max(a, b))
                pair_games.setdefault(key, {"ally": [], "enemy": []})["enemy"].append(match_id)

    heroes = sorted(
        (
            RosterHero(
                hero_id=hero_id,
                internal_name=str(hero_index[hero_id]["name"]),
                slug=slug_of(hero_id),
                display_name=str(hero_index[hero_id]["localized_name"]),
                picks=len(games),
                games=sorted(games),
            )
            for hero_id, games in hero_games.items()
        ),
        key=lambda hero: hero.slug,
    )
    pairs = sorted(
        (
            RosterPair(
                a=slug_of(a),
                b=slug_of(b),
                a_hero_id=a,
                b_hero_id=b,
                ally_games=sorted(games["ally"]),
                enemy_games=sorted(games["enemy"]),
            )
            for (a, b), games in pair_games.items()
        ),
        key=lambda pair: (pair.a, pair.b),
    )
    # Pair slugs are ordered lexically so the pair id is stable regardless of hero id order.
    pairs = [
        pair
        if pair.a <= pair.b
        else RosterPair(
            a=pair.b,
            b=pair.a,
            a_hero_id=pair.b_hero_id,
            b_hero_id=pair.a_hero_id,
            ally_games=pair.ally_games,
            enemy_games=pair.enemy_games,
        )
        for pair in pairs
    ]
    pairs.sort(key=lambda pair: (pair.a, pair.b))

    match_windows = {str(m.match_id): m.patch_window for m in roster_matches}
    all_in = all(window == kb_patch for window in match_windows.values())
    kb_window = next((w for w in (windows or load_patch_windows()) if w.patch == kb_patch), None)
    if kb_window is None:
        raise RosterError(f"kb patch {kb_patch} has no window in {windows_source}")
    open_ended = kb_window.end_date_exclusive is None
    note = (
        "Match dates are resolved against the manual patch windows. all_in_kb_patch is only as "
        "strong as the windows: when kb_window_open_ended is true, a later patch may exist that "
        "the windows do not record yet. OpenDota's numeric patch id is recorded as reported and "
        "not mapped."
    )
    artifact = RosterArtifact(
        schema_version=SCHEMA_VERSION,
        label=label,
        kb_patch=kb_patch,
        fingerprint="",
        sampling_frame=SamplingFrame(
            league_id=league_id,
            league_name=league_name,
            series_id=series_id,
            series_type=series_type,
            teams=sorted(teams),
        ),
        matches=roster_matches,
        heroes=heroes,
        pairs=pairs,
        patch_check=PatchCheck(
            kb_patch=kb_patch,
            windows_source=windows_source,
            match_windows=match_windows,
            all_in_kb_patch=all_in,
            kb_window_open_ended=open_ended,
            note=note,
        ),
        provenance=RosterProvenance(
            source="opendota:/matches/{match_id}",
            generator_version=GENERATOR_VERSION,
            source_patch=kb_patch,
            hero_identity_source=hero_identity_source,
            generated_at=datetime.now(UTC).isoformat().replace("+00:00", "Z"),
        ),
    )
    artifact.fingerprint = _fingerprint(artifact.model_dump())
    return artifact


async def fetch_match_details(
    cache_root: Path, match_ids: list[int], *, patch: str, force: bool = False
) -> list[dict[str, Any]]:
    """Match-detail payloads through the shared OpenDota cache (cache-first; `force` refetches)."""
    from invoker.sources.opendota import OpenDotaFetcher

    fetcher = OpenDotaFetcher(cache_root, patch)
    try:
        return [await fetcher.match_detail(match_id, force=force) for match_id in match_ids]
    finally:
        await fetcher.close()


def write_roster(artifact: RosterArtifact, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(artifact.model_dump(), indent=2, ensure_ascii=False) + "\n")
    return path


def load_roster(path: Path) -> RosterArtifact:
    try:
        raw = json.loads(path.read_text())
    except FileNotFoundError as exc:
        raise RosterError(f"roster not found: {path}") from exc
    if raw.get("schema_version") != SCHEMA_VERSION:
        raise RosterError(
            f"roster schema {raw.get('schema_version')} at {path}; expected {SCHEMA_VERSION}"
        )
    artifact = RosterArtifact.model_validate(raw)
    expected = _fingerprint(artifact.model_dump())
    if artifact.fingerprint != expected:
        raise RosterError(f"roster fingerprint mismatch at {path}: file was edited or is stale")
    return artifact
