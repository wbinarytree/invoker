from __future__ import annotations

import hashlib
import json
from collections import Counter
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml

from invoker.logging import get_logger
from invoker.paths import team_index_file, team_profile_file, team_registry_file
from invoker.sources.game_files import GameFilesSource
from invoker.sources.opendota import OpenDotaFetcher

SCHEMA_VERSION = 1
UNKNOWN = "unknown"
logger = get_logger(__name__)


@dataclass(frozen=True)
class TeamProfileBuildResult:
    team_id: int
    roster_hash: str
    profile_path: Path
    index_path: Path
    match_count: int
    hero_count: int
    missing_match_detail_count: int


def _utc_now() -> str:
    return datetime.now(UTC).isoformat().replace("+00:00", "Z")


def _hero_names(game_data_dir: Path, patch: str) -> dict[int, str]:
    source = GameFilesSource(game_data_dir, patch)
    names: dict[int, str] = {}
    for hero in source.heroes():
        hero_id = hero.get("id")
        localized_name = hero.get("localized_name")
        if isinstance(hero_id, int) and isinstance(localized_name, str):
            names[hero_id] = localized_name
    return names


def _team_registry_entry(data_dir: Path, team_id: int) -> dict[str, Any] | None:
    path = team_registry_file(data_dir)
    if not path.exists():
        return None
    raw = yaml.safe_load(path.read_text()) or {}
    if not isinstance(raw, dict):
        return None
    teams = raw.get("teams") or []
    if not isinstance(teams, list):
        return None
    for team in teams:
        if isinstance(team, dict) and team.get("team_id") == team_id:
            return team
    return None


def _team_metadata(data_dir: Path, team_id: int) -> dict[str, Any]:
    entry = _team_registry_entry(data_dir, team_id)
    if entry is None:
        return {"team_id": team_id, "name": None, "aliases": []}
    name = entry.get("name") if isinstance(entry.get("name"), str) else None
    aliases = entry.get("aliases")
    return {
        "team_id": team_id,
        "name": name,
        "aliases": [a for a in aliases if isinstance(a, str)] if isinstance(aliases, list) else [],
    }


def _limit_matches(matches: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    return [m for m in matches if isinstance(m, dict)][: max(1, min(limit, 50))]


def _match_id(match_row: dict[str, Any]) -> int | None:
    match_id = match_row.get("match_id")
    return match_id if isinstance(match_id, int) else None


def _team_side(team_id: int, match_row: dict[str, Any], detail: dict[str, Any]) -> str | None:
    if detail.get("radiant_team_id") == team_id:
        return "radiant"
    if detail.get("dire_team_id") == team_id:
        return "dire"
    if isinstance(match_row.get("radiant"), bool):
        return "radiant" if match_row["radiant"] else "dire"
    return None


def _team_win(side: str | None, match_row: dict[str, Any], detail: dict[str, Any]) -> bool | None:
    radiant_win = detail.get("radiant_win", match_row.get("radiant_win"))
    if not isinstance(radiant_win, bool) or side is None:
        return None
    return radiant_win if side == "radiant" else not radiant_win


def _player_side(player: dict[str, Any]) -> str | None:
    slot = player.get("player_slot")
    if not isinstance(slot, int):
        return None
    return "radiant" if slot < 128 else "dire"


def _observed_patch(detail: dict[str, Any], match_row: dict[str, Any]) -> str:
    value = detail.get("patch", detail.get("version", match_row.get("version")))
    return str(value) if value is not None else UNKNOWN


def _tournament(match_row: dict[str, Any], detail: dict[str, Any]) -> dict[str, Any]:
    league_id = detail.get("leagueid", match_row.get("leagueid"))
    league_name = detail.get("league_name", match_row.get("league_name"))
    return {
        "leagueid": league_id if isinstance(league_id, int) else None,
        "league_name": league_name if isinstance(league_name, str) else UNKNOWN,
    }


def _roster_hash(account_ids: set[int]) -> str:
    if not account_ids:
        return UNKNOWN
    raw = ",".join(str(account_id) for account_id in sorted(account_ids))
    return hashlib.sha256(raw.encode()).hexdigest()[:12]


def _sorted_counters(counter: Counter[int]) -> list[dict[str, Any]]:
    return [
        {"account_id": account_id, "games": games}
        for account_id, games in sorted(counter.items(), key=lambda item: (-item[1], item[0]))
    ]


def aggregate_team_profile(
    *,
    team_id: int,
    patch: str,
    team: dict[str, Any],
    match_rows: list[dict[str, Any]],
    match_details: dict[int, dict[str, Any]],
    hero_names: dict[int, str],
    fetched_at: str,
) -> dict[str, Any]:
    hero_pool: dict[int, dict[str, Any]] = {}
    account_ids: set[int] = set()
    observed_patches: Counter[str] = Counter()
    tournaments: dict[str, dict[str, Any]] = {}
    missing_match_ids: list[int] = []

    for match_row in match_rows:
        match_id = _match_id(match_row)
        if match_id is None:
            continue
        detail = match_details.get(match_id)
        if not detail:
            missing_match_ids.append(match_id)
            continue

        side = _team_side(team_id, match_row, detail)
        win = _team_win(side, match_row, detail)
        observed_patches[_observed_patch(detail, match_row)] += 1
        tournament = _tournament(match_row, detail)
        tournament_key = str(tournament["leagueid"] or tournament["league_name"] or UNKNOWN)
        tournaments.setdefault(tournament_key, tournament)

        players = detail.get("players") or []
        if not isinstance(players, list):
            continue
        seen_heroes: set[int] = set()
        for player in players:
            if not isinstance(player, dict) or _player_side(player) != side:
                continue
            hero_id = player.get("hero_id")
            if not isinstance(hero_id, int):
                continue
            account_id = player.get("account_id")
            if isinstance(account_id, int):
                account_ids.add(account_id)
            entry = hero_pool.setdefault(
                hero_id,
                {
                    "hero_id": hero_id,
                    "localized_name": hero_names.get(hero_id),
                    "games": 0,
                    "wins": 0,
                    "_players": Counter(),
                    "match_ids": [],
                },
            )
            if hero_id not in seen_heroes:
                entry["games"] += 1
                if win is True:
                    entry["wins"] += 1
                entry["match_ids"].append(match_id)
                seen_heroes.add(hero_id)
            if isinstance(account_id, int):
                entry["_players"][account_id] += 1

    roster_hash = _roster_hash(account_ids)
    heroes = []
    for entry in hero_pool.values():
        players = _sorted_counters(entry.pop("_players"))
        entry["players"] = players
        heroes.append(entry)
    heroes.sort(key=lambda h: (-h["games"], h["hero_id"]))

    return {
        "schema_version": SCHEMA_VERSION,
        "team": team,
        "patch": patch,
        "scope": {
            "requested_patch": patch,
            "match_window": "recent_limit",
            "match_count": len(match_rows),
            "default_limit": 50,
        },
        "roster": {
            "roster_hash": roster_hash,
            "player_account_ids": sorted(account_ids),
            "confidence": "observed_from_matches" if account_ids else "unknown",
        },
        "observed_patches": [
            {"patch": observed_patch, "match_count": count}
            for observed_patch, count in sorted(observed_patches.items())
        ],
        "tournaments": sorted(
            tournaments.values(),
            key=lambda t: (t["league_name"] or UNKNOWN, t["leagueid"] or 0),
        ),
        "hero_pool": heroes,
        "source": {
            "primary": "opendota",
            "fetched_at": fetched_at,
            "match_ids": [_match_id(row) for row in match_rows if _match_id(row) is not None],
            "missing_match_detail_count": len(missing_match_ids),
            "missing_match_ids": missing_match_ids,
        },
    }


def _load_team_index(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"schema_version": SCHEMA_VERSION, "profiles": []}
    return json.loads(path.read_text())


class TeamProfileNotFoundError(LookupError):
    pass


def _profile_index_entries(
    data_dir: Path, patch: str, team_id: int
) -> list[dict[str, Any]]:
    index_path = team_index_file(data_dir, patch)
    if not index_path.exists():
        return []
    index = _load_team_index(index_path)
    profiles = index.get("profiles") or []
    return [
        p
        for p in profiles
        if isinstance(p, dict) and p.get("team_id") == team_id
    ]


def load_team_profile(
    data_dir: Path,
    patch: str,
    team_id: int,
    *,
    roster_hash: str | None = None,
) -> dict[str, Any]:
    candidates = _profile_index_entries(data_dir, patch, team_id)
    if not candidates:
        raise TeamProfileNotFoundError(
            f"No team profile for team_id={team_id} patch={patch}. "
            f"Run: invoker build-team-profile --team-id {team_id} --patch {patch}"
        )
    if roster_hash is not None:
        candidates = [p for p in candidates if p.get("roster_hash") == roster_hash]
        if not candidates:
            raise TeamProfileNotFoundError(
                f"No team profile for team_id={team_id} patch={patch} "
                f"roster_hash={roster_hash}."
            )
    if len(candidates) > 1:
        hashes = sorted(str(p.get("roster_hash")) for p in candidates)
        raise TeamProfileNotFoundError(
            f"Multiple team profiles for team_id={team_id} patch={patch}: "
            f"roster_hash in {hashes}. Pass roster_hash explicitly."
        )
    profile_path = team_profile_file(
        data_dir, patch, team_id, str(candidates[0]["roster_hash"])
    )
    if not profile_path.exists():
        raise TeamProfileNotFoundError(
            f"Team profile index references missing file: {profile_path}"
        )
    return json.loads(profile_path.read_text())


def resolve_team(data_dir: Path, query: str) -> dict[str, Any] | None:
    path = team_registry_file(data_dir)
    if not path.exists():
        return None
    raw = yaml.safe_load(path.read_text()) or {}
    if not isinstance(raw, dict):
        return None
    teams = raw.get("teams") or []
    if not isinstance(teams, list):
        return None
    needle = query.strip()
    if not needle:
        return None
    if needle.isdigit():
        team_id = int(needle)
        for team in teams:
            if isinstance(team, dict) and team.get("team_id") == team_id:
                return team
        return None
    lowered = needle.casefold()
    for team in teams:
        if not isinstance(team, dict):
            continue
        name = team.get("name")
        if isinstance(name, str) and name.casefold() == lowered:
            return team
        aliases = team.get("aliases") or []
        if isinstance(aliases, list) and any(
            isinstance(a, str) and a.casefold() == lowered for a in aliases
        ):
            return team
    return None


def _write_team_profile(data_dir: Path, patch: str, profile: dict[str, Any]) -> tuple[Path, Path]:
    team_id = profile["team"]["team_id"]
    roster_hash = profile["roster"]["roster_hash"]
    profile_path = team_profile_file(data_dir, patch, team_id, roster_hash)
    profile_path.parent.mkdir(parents=True, exist_ok=True)
    profile_path.write_text(json.dumps(profile, indent=2, ensure_ascii=False))

    index_path = team_index_file(data_dir, patch)
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index = _load_team_index(index_path)
    profiles = [
        p
        for p in index.get("profiles", [])
        if not (p.get("team_id") == team_id and p.get("roster_hash") == roster_hash)
    ]
    profiles.append(
        {
            "team_id": team_id,
            "team_name": profile["team"].get("name"),
            "roster_hash": roster_hash,
            "patch": patch,
            "match_count": profile["scope"]["match_count"],
            "hero_count": len(profile["hero_pool"]),
            "path": str(profile_path.relative_to(index_path.parent)),
        }
    )
    profiles.sort(key=lambda p: (p["team_id"], p["roster_hash"]))
    index["schema_version"] = SCHEMA_VERSION
    index["profiles"] = profiles
    index_path.write_text(json.dumps(index, indent=2, ensure_ascii=False))
    return profile_path, index_path


async def build_team_profile(
    *,
    data_dir: Path,
    game_data_dir: Path,
    cache_dir: Path,
    team_id: int,
    patch: str,
    limit: int = 50,
    force: bool = False,
) -> TeamProfileBuildResult:
    od = OpenDotaFetcher(cache_dir, patch)
    fetched_at = _utc_now()
    try:
        raw_matches = await od.team_matches(team_id, force=force)
        if not isinstance(raw_matches, list):
            raise ValueError("OpenDota team matches response must be a list")
        match_rows = _limit_matches(raw_matches, limit)
        details: dict[int, dict[str, Any]] = {}
        for match_row in match_rows:
            match_id = _match_id(match_row)
            if match_id is None:
                continue
            try:
                detail = await od.match_detail(match_id, force=force)
            except Exception as exc:
                logger.warning("Skipping match detail match_id=%s error=%s", match_id, exc)
                continue
            if isinstance(detail, dict):
                details[match_id] = detail
            else:
                logger.warning("Skipping non-object match detail match_id=%s", match_id)
                continue
    finally:
        await od.close()

    profile = aggregate_team_profile(
        team_id=team_id,
        patch=patch,
        team=_team_metadata(data_dir, team_id),
        match_rows=match_rows,
        match_details=details,
        hero_names=_hero_names(game_data_dir, patch),
        fetched_at=fetched_at,
    )
    profile_path, index_path = _write_team_profile(data_dir, patch, profile)
    return TeamProfileBuildResult(
        team_id=team_id,
        roster_hash=profile["roster"]["roster_hash"],
        profile_path=profile_path,
        index_path=index_path,
        match_count=profile["scope"]["match_count"],
        hero_count=len(profile["hero_pool"]),
        missing_match_detail_count=profile["source"]["missing_match_detail_count"],
    )
