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
        return {
            "team_id": team_id,
            "name": None,
            "aliases": [],
            "name_source": None,
        }
    name = entry.get("name") if isinstance(entry.get("name"), str) else None
    aliases = entry.get("aliases")
    return {
        "team_id": team_id,
        "name": name,
        "aliases": [a for a in aliases if isinstance(a, str)] if isinstance(aliases, list) else [],
        "name_source": "registry" if name else None,
    }


def _observed_team_name(
    team_id: int, side: str | None, detail: dict[str, Any], match_row: dict[str, Any]
) -> tuple[str | None, str | None]:
    if side is None:
        return None, None
    side_team = detail.get(f"{side}_team")
    if isinstance(side_team, dict) and side_team.get("team_id") == team_id:
        name = side_team.get("name") if isinstance(side_team.get("name"), str) else None
        tag = side_team.get("tag") if isinstance(side_team.get("tag"), str) else None
        if name:
            return name, tag
    fallback = detail.get(f"{side}_name", match_row.get(f"{side}_name"))
    if isinstance(fallback, str) and fallback.strip():
        return fallback, None
    return None, None


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


def _observed_patch_id(detail: dict[str, Any]) -> int | None:
    value = detail.get("patch")
    return value if isinstance(value, int) else None


def _patch_id_to_name(patch_constants: list[dict[str, Any]] | None) -> dict[int, str]:
    if not patch_constants:
        return {}
    out: dict[int, str] = {}
    for index, entry in enumerate(patch_constants):
        if not isinstance(entry, dict):
            continue
        name = entry.get("name")
        if not isinstance(name, str):
            continue
        patch_id = entry.get("id")
        if isinstance(patch_id, int):
            out[patch_id] = name
        else:
            out[index] = name
    return out


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


def _player_label(player: dict[str, Any]) -> str | None:
    for key in ("name", "personaname"):
        value = player.get(key)
        if isinstance(value, str) and value.strip():
            return value
    return None


def aggregate_team_profile(
    *,
    team_id: int,
    patch: str,
    team: dict[str, Any],
    match_rows: list[dict[str, Any]],
    match_details: dict[int, dict[str, Any]],
    hero_names: dict[int, str],
    fetched_at: str,
    patch_constants: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    hero_pool: dict[int, dict[str, Any]] = {}
    player_pool: dict[int, dict[str, Any]] = {}
    roster_personas: dict[int, str] = {}
    roster_games: Counter[int] = Counter()
    observed_patches: Counter[int | None] = Counter()
    tournaments: dict[str, dict[str, Any]] = {}
    missing_match_ids: list[int] = []
    contributing_match_count = 0
    patch_id_to_name = _patch_id_to_name(patch_constants)
    observed_names: Counter[str] = Counter()
    observed_tags: Counter[str] = Counter()

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
        name, tag = _observed_team_name(team_id, side, detail, match_row)
        if name:
            observed_names[name] += 1
        if tag:
            observed_tags[tag] += 1
        observed_patches[_observed_patch_id(detail)] += 1
        tournament = _tournament(match_row, detail)
        league_id = tournament["leagueid"]
        league_name = tournament["league_name"]
        if league_id is not None:
            tournament_key = f"id:{league_id}"
        elif isinstance(league_name, str) and league_name != UNKNOWN:
            tournament_key = f"name:{league_name}"
        else:
            tournament_key = "unknown"
        tournaments.setdefault(tournament_key, tournament)

        players = detail.get("players") or []
        if not isinstance(players, list):
            continue
        contributing_match_count += 1
        seen_heroes: set[int] = set()
        seen_players: set[int] = set()
        for player in players:
            if not isinstance(player, dict) or _player_side(player) != side:
                continue
            hero_id = player.get("hero_id")
            if not isinstance(hero_id, int):
                continue
            account_id = player.get("account_id")
            persona = _player_label(player)
            if isinstance(account_id, int) and persona is not None:
                roster_personas[account_id] = persona

            entry = hero_pool.setdefault(
                hero_id,
                {
                    "hero_id": hero_id,
                    "localized_name": hero_names.get(hero_id),
                    "games": 0,
                    "wins": 0,
                    "match_ids": [],
                },
            )
            if hero_id not in seen_heroes:
                entry["games"] += 1
                if win is True:
                    entry["wins"] += 1
                entry["match_ids"].append(match_id)
                seen_heroes.add(hero_id)

            if not isinstance(account_id, int):
                continue
            if account_id not in seen_players:
                roster_games[account_id] += 1
                seen_players.add(account_id)
            player_entry = player_pool.setdefault(
                account_id,
                {
                    "account_id": account_id,
                    "personaname": None,
                    "games": 0,
                    "wins": 0,
                    "_heroes": {},
                },
            )
            if persona is not None:
                player_entry["personaname"] = persona
            player_entry["games"] += 1
            if win is True:
                player_entry["wins"] += 1
            hero_entry = player_entry["_heroes"].setdefault(
                hero_id,
                {
                    "hero_id": hero_id,
                    "localized_name": hero_names.get(hero_id),
                    "games": 0,
                    "wins": 0,
                    "match_ids": [],
                },
            )
            hero_entry["games"] += 1
            if win is True:
                hero_entry["wins"] += 1
            hero_entry["match_ids"].append(match_id)

    account_ids = set(roster_games)
    roster_hash = _roster_hash(account_ids)

    team_view = dict(team)
    if not team_view.get("name") and observed_names:
        team_view["name"] = observed_names.most_common(1)[0][0]
        team_view["name_source"] = "opendota_match_payload"
    if observed_tags:
        team_view["tag"] = observed_tags.most_common(1)[0][0]
    team_view["observed_names"] = [
        {"name": n, "count": c}
        for n, c in observed_names.most_common()
    ]
    heroes = sorted(hero_pool.values(), key=lambda h: (-h["games"], h["hero_id"]))

    roster_players = [
        {
            "account_id": account_id,
            "personaname": roster_personas.get(account_id),
            "games": games,
        }
        for account_id, games in sorted(
            roster_games.items(), key=lambda item: (-item[1], item[0])
        )
    ]

    players_view = []
    for entry in player_pool.values():
        per_hero = sorted(
            entry.pop("_heroes").values(),
            key=lambda h: (-h["games"], h["hero_id"]),
        )
        entry["hero_pool"] = per_hero
        players_view.append(entry)
    players_view.sort(key=lambda p: (-p["games"], p["account_id"]))

    return {
        "schema_version": SCHEMA_VERSION,
        "team": team_view,
        "patch": patch,
        "scope": {
            "requested_patch": patch,
            "match_window": "recent_limit",
            "match_count": len(match_rows),
            "contributing_match_count": contributing_match_count,
            "default_limit": 50,
        },
        "roster": {
            "roster_hash": roster_hash,
            "players": roster_players,
            "confidence": "observed_from_matches" if account_ids else "unknown",
        },
        "observed_patches": [
            {
                "patch_id": patch_id,
                "patch_name": patch_id_to_name.get(patch_id) if patch_id is not None else None,
                "match_count": count,
            }
            for patch_id, count in sorted(
                observed_patches.items(),
                key=lambda item: (item[0] is None, item[0] or 0),
            )
        ],
        "tournaments": sorted(
            tournaments.values(),
            key=lambda t: (t["league_name"] or UNKNOWN, t["leagueid"] or 0),
        ),
        "hero_pool": heroes,
        "players": players_view,
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
    patch_constants: list[dict[str, Any]] | None = None
    try:
        raw_matches = await od.team_matches(team_id, force=force)
        if not isinstance(raw_matches, list):
            raise ValueError("OpenDota team matches response must be a list")
        match_rows = _limit_matches(raw_matches, limit)
        try:
            raw_constants = await od.constants_patch()
            if isinstance(raw_constants, list):
                patch_constants = raw_constants
        except Exception as exc:
            logger.warning("Skipping OpenDota patch constants error=%s", exc)
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
        patch_constants=patch_constants,
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
