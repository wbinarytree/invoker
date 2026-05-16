import json
from pathlib import Path

import pytest
import yaml

import invoker.pipeline.team_profile as team_profile_module
from invoker.paths import team_registry_file
from invoker.pipeline.team_profile import (
    CanonicalRoster,
    TeamProfileBuildResult,
    TeamProfileCurationResult,
    TeamProfileNotFoundError,
    TeamProfileScaffoldResult,
    aggregate_team_profile,
    build_team_profile,
    load_team_profile,
    resolve_team,
)


def _write_minimal_registry(data_dir: Path, team_id: int = 123) -> Path:
    registry = team_registry_file(data_dir)
    registry.parent.mkdir(parents=True, exist_ok=True)
    registry.write_text(
        "schema_version: 1\n"
        "teams:\n"
        f"  - team_id: {team_id}\n"
        "    name: Authored Team\n"
        "    players:\n"
        "      - account_id: 10\n"
        "        position: 1\n"
        "      - account_id: 11\n"
        "        position: 2\n"
        "      - account_id: 12\n"
        "        position: 3\n"
        "      - account_id: 13\n"
        "        position: 4\n"
        "      - account_id: 14\n"
        "        position: 5\n"
    )
    return registry


def test_aggregate_team_profile_counts_hero_pool_and_roster():
    profile = aggregate_team_profile(
        team_id=123,
        patch="7.41b",
        team={"team_id": 123, "name": None, "aliases": [], "name_source": None},
        match_rows=[
            {
                "match_id": 1,
                "radiant": True,
                "leagueid": 10,
                "league_name": "Example League",
                "version": 22,
            },
            {"match_id": 2, "radiant": False},
        ],
        match_details={
            1: {
                "radiant_team_id": 123,
                "dire_team_id": 456,
                "radiant_win": True,
                "patch": 60,
                "start_time": 1775606400,
                "radiant_team": {"team_id": 123, "name": "BetBoom Team", "tag": "BB"},
                "dire_team": {"team_id": 456, "name": "Opponent"},
                "players": [
                    {
                        "player_slot": 0,
                        "account_id": 10,
                        "hero_id": 1,
                        "personaname": "Yatoro",
                        "lane_role": 1,
                        "gold_per_min": 700,
                    },
                    {
                        "player_slot": 1,
                        "account_id": 11,
                        "hero_id": 2,
                        "personaname": "Larl",
                        "lane_role": 2,
                        "gold_per_min": 600,
                    },
                    {
                        "player_slot": 2,
                        "account_id": 12,
                        "hero_id": 3,
                        "lane_role": 3,
                        "gold_per_min": 500,
                    },
                    {
                        "player_slot": 3,
                        "account_id": 13,
                        "hero_id": 4,
                        "lane_role": 3,
                        "gold_per_min": 350,
                    },
                    {
                        "player_slot": 4,
                        "account_id": 14,
                        "hero_id": 5,
                        "lane_role": 1,
                        "gold_per_min": 300,
                    },
                    {"player_slot": 128, "account_id": 20, "hero_id": 6},
                ],
            },
            2: {
                "radiant_team_id": 999,
                "dire_team_id": 123,
                "radiant_win": True,
                "patch": 59,
                "start_time": 1774483200,
                "dire_name": "BetBoom",
                "players": [
                    {
                        "player_slot": 128,
                        "account_id": 10,
                        "hero_id": 2,
                        "name": "Yatoro [Pro]",
                        "lane_role": 1,
                        "gold_per_min": 800,
                    },
                    {
                        "player_slot": 129,
                        "account_id": 11,
                        "hero_id": 1,
                        "lane_role": 2,
                        "gold_per_min": 600,
                    },
                    {
                        "player_slot": 130,
                        "account_id": 12,
                        "hero_id": 3,
                        "lane_role": 3,
                        "gold_per_min": 500,
                    },
                    {
                        "player_slot": 131,
                        "account_id": 13,
                        "hero_id": 4,
                        "lane_role": 3,
                        "gold_per_min": 350,
                    },
                    {
                        "player_slot": 132,
                        "account_id": 14,
                        "hero_id": 5,
                        "lane_role": 1,
                        "gold_per_min": 250,
                    },
                ],
            },
        },
        hero_names={1: "Hero One", 2: "Hero Two", 3: "Hero Three", 4: "Hero Four"},
        fetched_at="2026-04-30T00:00:00Z",
    )

    assert profile["team"]["team_id"] == 123
    assert profile["team"]["name"] == "BetBoom Team"
    assert profile["team"]["name_source"] == "opendota_match_payload"
    assert profile["team"]["tag"] == "BB"
    assert profile["team"]["observed_names"] == [
        {"name": "BetBoom Team", "count": 1},
        {"name": "BetBoom", "count": 1},
    ]
    assert profile["scope"]["match_count"] == 2
    assert profile["scope"]["contributing_match_count"] == 2
    assert [p["account_id"] for p in profile["roster"]["players"]] == [10, 11, 12, 13, 14]
    assert profile["roster"]["players"][0] == {
        "account_id": 10,
        "personaname": "Yatoro [Pro]",
        "games": 2,
        "primary_position": None,
        "position_source": None,
    }
    assert profile["roster"]["roster_hash"] != "unknown"
    assert profile["observed_patches"] == [
        {"patch_id": 59, "patch_name": None, "match_count": 1},
        {"patch_id": 60, "patch_name": None, "match_count": 1},
    ]
    assert profile["observed_patch_windows"] == [
        {
            "patch": "7.41",
            "start_date": "2026-03-24",
            "end_date_exclusive": "2026-03-27",
            "match_count": 1,
        },
        {
            "patch": "7.41b",
            "start_date": "2026-04-07",
            "end_date_exclusive": "2026-05-06",
            "match_count": 1,
        },
    ]
    assert profile["tournaments"] == [
        {"leagueid": 10, "league_name": "Example League"},
        {"leagueid": None, "league_name": "unknown"},
    ]
    assert [h["hero_id"] for h in profile["hero_pool"]] == [1, 2, 3, 4, 5]
    hero_two = next(h for h in profile["hero_pool"] if h["hero_id"] == 2)
    assert hero_two["games"] == 2
    assert hero_two["wins"] == 1
    assert hero_two["win_match_ids"] == [1]
    assert hero_two["loss_match_ids"] == [2]
    assert hero_two["positions"] == []
    hero_two_players = sorted(hero_two["players"], key=lambda p: p["account_id"])
    assert hero_two_players == [
        {
            "account_id": 10,
            "personaname": "Yatoro [Pro]",
            "games": 1,
            "primary_position": None,
            "position_source": None,
        },
        {
            "account_id": 11,
            "personaname": "Larl",
            "games": 1,
            "primary_position": None,
            "position_source": None,
        },
    ]
    assert profile["hero_pool"][-1]["localized_name"] is None

    yatoro = next(p for p in profile["players"] if p["account_id"] == 10)
    assert yatoro["personaname"] == "Yatoro [Pro]"
    assert yatoro["games"] == 2
    assert yatoro["wins"] == 1
    assert [h["hero_id"] for h in yatoro["hero_pool"]] == [1, 2]
    yatoro_hero_one = next(h for h in yatoro["hero_pool"] if h["hero_id"] == 1)
    assert yatoro_hero_one["win_match_ids"] == [1]
    assert yatoro_hero_one["loss_match_ids"] == []
    yatoro_hero_two = next(h for h in yatoro["hero_pool"] if h["hero_id"] == 2)
    assert yatoro_hero_two["win_match_ids"] == []
    assert yatoro_hero_two["loss_match_ids"] == [2]


def test_aggregate_team_profile_hashes_canonical_roster_and_surfaces_standins():
    profile = aggregate_team_profile(
        team_id=123,
        patch="7.41b",
        team={"team_id": 123, "name": None, "aliases": [], "name_source": None},
        match_rows=[
            {"match_id": 1, "radiant": True},
            {"match_id": 2, "radiant": True},
        ],
        match_details={
            1: {
                "radiant_team_id": 123,
                "radiant_win": True,
                "players": [
                    {"player_slot": 0, "account_id": 10, "hero_id": 1},
                    {"player_slot": 1, "account_id": 11, "hero_id": 2},
                    {"player_slot": 2, "account_id": 12, "hero_id": 3},
                    {"player_slot": 3, "account_id": 13, "hero_id": 4},
                    {"player_slot": 4, "account_id": 14, "hero_id": 5},
                ],
            },
            2: {
                "radiant_team_id": 123,
                "radiant_win": False,
                "players": [
                    {"player_slot": 0, "account_id": 10, "hero_id": 1},
                    {"player_slot": 1, "account_id": 11, "hero_id": 2},
                    {"player_slot": 2, "account_id": 12, "hero_id": 3},
                    {"player_slot": 3, "account_id": 13, "hero_id": 4},
                    {
                        "player_slot": 4,
                        "account_id": 99,
                        "hero_id": 6,
                        "personaname": "Standin",
                    },
                ],
            },
        },
        hero_names={1: "Hero One", 2: "Hero Two", 3: "Hero Three", 4: "Hero Four"},
        fetched_at="2026-04-30T00:00:00Z",
        canonical_roster=CanonicalRoster({10, 11, 12, 13, 14}, "authored_registry"),
    )

    assert [p["account_id"] for p in profile["roster"]["players"]] == [10, 11, 12, 13, 14]
    assert profile["roster"]["stand_ins"] == [
        {
            "account_id": 99,
            "personaname": "Standin",
            "games": 1,
            "match_ids": [2],
        }
    ]
    assert profile["roster"]["canonical_source"] == "authored_registry"
    assert [p["account_id"] for p in profile["players"]] == [10, 11, 12, 13, 14]
    standin_hero = next(h for h in profile["hero_pool"] if h["hero_id"] == 6)
    assert standin_hero["games"] == 1
    assert standin_hero["players"] == []
    assert standin_hero["positions"] == []
    assert profile["source"]["match_roster_classifications"] == [
        {"match_id": 1, "roster_type": "canonical", "stand_in_account_ids": []},
        {"match_id": 2, "roster_type": "standin", "stand_in_account_ids": [99]},
    ]


def test_aggregate_team_profile_can_exclude_standin_matches():
    profile = aggregate_team_profile(
        team_id=123,
        patch="7.41b",
        team={"team_id": 123, "name": None, "aliases": [], "name_source": None},
        match_rows=[
            {"match_id": 1, "radiant": True},
            {"match_id": 2, "radiant": True},
        ],
        match_details={
            1: {
                "radiant_team_id": 123,
                "radiant_win": True,
                "players": [
                    {"player_slot": 0, "account_id": 10, "hero_id": 1},
                    {"player_slot": 1, "account_id": 11, "hero_id": 2},
                    {"player_slot": 2, "account_id": 12, "hero_id": 3},
                    {"player_slot": 3, "account_id": 13, "hero_id": 4},
                    {"player_slot": 4, "account_id": 14, "hero_id": 5},
                ],
            },
            2: {
                "radiant_team_id": 123,
                "radiant_win": False,
                "players": [
                    {"player_slot": 0, "account_id": 10, "hero_id": 6},
                    {"player_slot": 1, "account_id": 11, "hero_id": 2},
                    {"player_slot": 2, "account_id": 12, "hero_id": 3},
                    {"player_slot": 3, "account_id": 13, "hero_id": 4},
                    {"player_slot": 4, "account_id": 99, "hero_id": 7},
                ],
            },
        },
        hero_names={},
        fetched_at="2026-04-30T00:00:00Z",
        canonical_roster=CanonicalRoster({10, 11, 12, 13, 14}, "authored_registry"),
        include_standin_matches=False,
    )

    assert profile["scope"]["stand_in_policy"] == "exclude"
    assert profile["scope"]["contributing_match_count"] == 1
    assert [h["hero_id"] for h in profile["hero_pool"]] == [1, 2, 3, 4, 5]
    assert profile["roster"]["stand_ins"] == [
        {"account_id": 99, "personaname": None, "games": 1, "match_ids": [2]}
    ]
    player_ten = next(p for p in profile["players"] if p["account_id"] == 10)
    assert player_ten["games"] == 1
    assert [h["hero_id"] for h in player_ten["hero_pool"]] == [1]


class FakeGameFilesSource:
    def __init__(self, root: Path, patch: str):
        assert root == Path("/game")
        assert patch == "7.41b"

    def heroes(self):
        return [
            {"id": 1, "localized_name": "Hero One"},
            {"id": 2, "localized_name": "Hero Two"},
        ]


class FakeOpenDotaFetcher:
    def __init__(self, cache_dir: Path, patch: str):
        self.cache_dir = cache_dir
        self.patch = patch
        self.force_values: list[bool] = []

    async def team_matches(self, team_id: int, *, force: bool = False):
        self.force_values.append(force)
        assert team_id == 123
        return [
            {"match_id": 1, "radiant": True, "league_name": "Example League"},
            {"match_id": 2, "radiant": True},
        ]

    async def match_detail(self, match_id: int, *, force: bool = False):
        self.force_values.append(force)
        if match_id == 2:
            raise RuntimeError("not parsed")
        return {
            "radiant_team_id": 123,
            "radiant_win": False,
            "patch": 60,
            "start_time": 1775606400,
            "players": [
                {"player_slot": 0, "account_id": 10, "hero_id": 1, "personaname": "P1"},
                {"player_slot": 1, "account_id": 11, "hero_id": 2, "personaname": "P2"},
                {"player_slot": 2, "account_id": 12, "hero_id": 1, "personaname": "P3"},
                {"player_slot": 3, "account_id": 13, "hero_id": 2, "personaname": "P4"},
                {"player_slot": 4, "account_id": 14, "hero_id": 1, "personaname": "P5"},
            ],
        }

    async def close(self):
        pass


class FakeOpenDotaFetcherWithStandin:
    def __init__(self, cache_dir: Path, patch: str):
        self.cache_dir = cache_dir
        self.patch = patch

    async def team_matches(self, team_id: int, *, force: bool = False):
        assert team_id == 123
        return [{"match_id": 1, "radiant": True}, {"match_id": 2, "radiant": True}]

    async def match_detail(self, match_id: int, *, force: bool = False):
        if match_id == 1:
            accounts = [10, 11, 12, 13, 14]
            heroes = [1, 2, 3, 4, 5]
        else:
            accounts = [10, 11, 12, 13, 99]
            heroes = [6, 2, 3, 4, 7]
        return {
            "radiant_team_id": 123,
            "radiant_win": match_id == 1,
            "players": [
                {
                    "player_slot": index,
                    "account_id": account_id,
                    "hero_id": heroes[index],
                    "personaname": f"P{account_id}",
                }
                for index, account_id in enumerate(accounts)
            ],
        }

    async def close(self):
        pass


@pytest.mark.asyncio
async def test_build_team_profile_writes_profile_and_index(monkeypatch, tmp_path):
    monkeypatch.setattr(team_profile_module, "GameFilesSource", FakeGameFilesSource)
    monkeypatch.setattr(team_profile_module, "OpenDotaFetcher", FakeOpenDotaFetcher)
    _write_minimal_registry(tmp_path)

    result = await build_team_profile(
        data_dir=tmp_path,
        game_data_dir=Path("/game"),
        cache_dir=tmp_path / "cache",
        team_id=123,
        patch="7.41b",
        limit=50,
        force=True,
    )
    assert isinstance(result, TeamProfileBuildResult)

    assert result.profile_path.exists()
    assert result.index_path.exists()
    assert result.match_count == 2
    assert result.hero_count == 2
    assert result.missing_match_detail_count == 1
    assert result.profile_path.parent.name == result.roster_hash

    profile = json.loads(result.profile_path.read_text())
    assert profile["source"]["position_sources"] == ["authored"]
    hero_one = next(h for h in profile["hero_pool"] if h["hero_id"] == 1)
    hero_two = next(h for h in profile["hero_pool"] if h["hero_id"] == 2)
    assert hero_one["positions"] == [
        {"position": 1, "games": 1},
        {"position": 3, "games": 1},
        {"position": 5, "games": 1},
    ]
    assert hero_two["positions"] == [
        {"position": 2, "games": 1},
        {"position": 4, "games": 1},
    ]
    by_account = {
        p["account_id"]: (p["primary_position"], p["position_source"])
        for p in profile["roster"]["players"]
    }
    assert by_account == {
        10: (1, "authored"),
        11: (2, "authored"),
        12: (3, "authored"),
        13: (4, "authored"),
        14: (5, "authored"),
    }
    yatoro = next(p for p in profile["players"] if p["account_id"] == 10)
    assert yatoro["primary_position"] == 1
    assert yatoro["position_source"] == "authored"
    assert result.index_path.read_text().count('"team_id": 123') == 1


@pytest.mark.asyncio
async def test_build_team_profile_stops_when_manual_positions_are_incomplete(monkeypatch, tmp_path):
    monkeypatch.setattr(team_profile_module, "GameFilesSource", FakeGameFilesSource)
    monkeypatch.setattr(team_profile_module, "OpenDotaFetcher", FakeOpenDotaFetcher)

    registry = team_registry_file(tmp_path)
    registry.parent.mkdir(parents=True, exist_ok=True)
    registry.write_text(
        "schema_version: 1\n"
        "teams:\n"
        "  - team_id: 123\n"
        "    name: Authored Team\n"
        "    players:\n"
        "      - account_id: 10\n"
        "        position: null\n"
        "      - account_id: 11\n"
        "        position: 5\n"
        "      - account_id: 12\n"
        "        position: null\n"
        "      - account_id: 13\n"
        "        position: null\n"
        "      - account_id: 14\n"
        "        position: null\n"
    )

    result = await build_team_profile(
        data_dir=tmp_path,
        game_data_dir=Path("/game"),
        cache_dir=tmp_path / "cache",
        team_id=123,
        patch="7.41b",
    )
    assert isinstance(result, TeamProfileCurationResult)


@pytest.mark.asyncio
async def test_build_team_profile_uses_authored_five_and_can_exclude_standins(
    monkeypatch, tmp_path
):
    monkeypatch.setattr(team_profile_module, "GameFilesSource", FakeGameFilesSource)
    monkeypatch.setattr(team_profile_module, "OpenDotaFetcher", FakeOpenDotaFetcherWithStandin)

    registry = team_registry_file(tmp_path)
    registry.parent.mkdir(parents=True, exist_ok=True)
    registry.write_text(
        "schema_version: 1\n"
        "teams:\n"
        "  - team_id: 123\n"
        "    name: Authored Team\n"
        "    players:\n"
        "      - account_id: 10\n"
        "        position: 1\n"
        "      - account_id: 11\n"
        "        position: 2\n"
        "      - account_id: 12\n"
        "        position: 3\n"
        "      - account_id: 13\n"
        "        position: 4\n"
        "      - account_id: 14\n"
        "        position: 5\n"
    )

    result = await build_team_profile(
        data_dir=tmp_path,
        game_data_dir=Path("/game"),
        cache_dir=tmp_path / "cache",
        team_id=123,
        patch="7.41b",
        include_standin_matches=False,
    )
    assert isinstance(result, TeamProfileBuildResult)

    profile = json.loads(result.profile_path.read_text())
    assert [p["account_id"] for p in profile["roster"]["players"]] == [10, 11, 12, 13, 14]
    assert profile["roster"]["canonical_source"] == "authored_registry"
    assert profile["roster"]["stand_ins"] == [
        {"account_id": 99, "personaname": "P99", "games": 1, "match_ids": [2]}
    ]
    assert profile["scope"]["stand_in_policy"] == "exclude"
    assert profile["scope"]["contributing_match_count"] == 1
    assert [h["hero_id"] for h in profile["hero_pool"]] == [1, 2, 3, 4, 5]
    hero_one = next(h for h in profile["hero_pool"] if h["hero_id"] == 1)
    assert hero_one["positions"] == [{"position": 1, "games": 1}]
    assert [p["account_id"] for p in profile["players"]] == [10, 11, 12, 13, 14]


@pytest.mark.asyncio
async def test_build_team_profile_stops_when_registry_has_more_than_five_players(
    monkeypatch, tmp_path
):
    monkeypatch.setattr(team_profile_module, "GameFilesSource", FakeGameFilesSource)
    monkeypatch.setattr(team_profile_module, "OpenDotaFetcher", FakeOpenDotaFetcherWithStandin)
    registry = team_registry_file(tmp_path)
    registry.parent.mkdir(parents=True, exist_ok=True)
    registry.write_text(
        "schema_version: 1\n"
        "teams:\n"
        "  - team_id: 123\n"
        "    name: Authored Team\n"
        "    players:\n"
        "      - account_id: 10\n"
        "        position: 1\n"
        "      - account_id: 11\n"
        "        position: 2\n"
        "      - account_id: 12\n"
        "        position: 3\n"
        "      - account_id: 13\n"
        "        position: 4\n"
        "      - account_id: 14\n"
        "        position: 5\n"
        "      - account_id: 99\n"
        "        position: 4\n"
    )

    result = await build_team_profile(
        data_dir=tmp_path,
        game_data_dir=Path("/game"),
        cache_dir=tmp_path / "cache",
        team_id=123,
        patch="7.41b",
    )

    assert isinstance(result, TeamProfileCurationResult)
    assert result.player_count == 6
    assert result.registry_path == registry
    profiles_root = tmp_path / "derived" / "7.41b" / "teams"
    assert not profiles_root.exists() or not any(profiles_root.rglob("profile.json"))


@pytest.mark.asyncio
async def test_build_team_profile_stops_when_registry_has_partial_roster(monkeypatch, tmp_path):
    monkeypatch.setattr(team_profile_module, "GameFilesSource", FakeGameFilesSource)
    monkeypatch.setattr(team_profile_module, "OpenDotaFetcher", FakeOpenDotaFetcherWithStandin)
    registry = team_registry_file(tmp_path)
    registry.parent.mkdir(parents=True, exist_ok=True)
    registry.write_text(
        "schema_version: 1\n"
        "teams:\n"
        "  - team_id: 123\n"
        "    name: Authored Team\n"
        "    players:\n"
        "      - account_id: 10\n"
        "        position: 1\n"
        "      - account_id: 11\n"
        "        position: 2\n"
        "      - account_id: 12\n"
        "        position: 3\n"
        "      - account_id: 13\n"
        "        position: 4\n"
    )

    result = await build_team_profile(
        data_dir=tmp_path,
        game_data_dir=Path("/game"),
        cache_dir=tmp_path / "cache",
        team_id=123,
        patch="7.41b",
    )

    assert isinstance(result, TeamProfileCurationResult)
    assert result.player_count == 4
    profiles_root = tmp_path / "derived" / "7.41b" / "teams"
    assert not profiles_root.exists() or not any(profiles_root.rglob("profile.json"))


@pytest.mark.asyncio
async def test_build_team_profile_scaffolds_when_no_registry_entry(monkeypatch, tmp_path):
    monkeypatch.setattr(team_profile_module, "GameFilesSource", FakeGameFilesSource)
    monkeypatch.setattr(team_profile_module, "OpenDotaFetcher", FakeOpenDotaFetcher)

    result = await build_team_profile(
        data_dir=tmp_path,
        game_data_dir=Path("/game"),
        cache_dir=tmp_path / "cache",
        team_id=123,
        patch="7.41b",
    )

    assert isinstance(result, TeamProfileScaffoldResult)
    assert result.team_id == 123
    assert result.registry_path == team_registry_file(tmp_path)
    assert [p["account_id"] for p in result.discovered_roster] == [10, 11, 12, 13, 14]

    raw = yaml.safe_load(result.registry_path.read_text())
    assert raw["schema_version"] == 1
    entries = raw["teams"]
    assert len(entries) == 1
    entry = entries[0]
    assert entry["team_id"] == 123
    assert entry["aliases"] == []
    assert [p["account_id"] for p in entry["players"]] == [10, 11, 12, 13, 14]
    assert all(p["position"] is None for p in entry["players"])
    assert {p["name"] for p in entry["players"]} == {"P1", "P2", "P3", "P4", "P5"}

    # No profile.json should have been written.
    profiles_root = tmp_path / "derived" / "7.41b" / "teams"
    assert not profiles_root.exists() or not any(profiles_root.rglob("profile.json"))


@pytest.mark.asyncio
async def test_build_team_profile_does_not_override_existing_registry_entry(monkeypatch, tmp_path):
    monkeypatch.setattr(team_profile_module, "GameFilesSource", FakeGameFilesSource)
    monkeypatch.setattr(team_profile_module, "OpenDotaFetcher", FakeOpenDotaFetcher)

    registry = team_registry_file(tmp_path)
    registry.parent.mkdir(parents=True, exist_ok=True)
    original_yaml = (
        "schema_version: 1\n"
        "teams:\n"
        "  - team_id: 123\n"
        "    name: Pre-existing Name\n"
        "    aliases: [Pre]\n"
        "    players:\n"
        "      - account_id: 10\n"
        "        name: OldPersona\n"
        "        position: 1\n"
    )
    registry.write_text(original_yaml)

    result = await build_team_profile(
        data_dir=tmp_path,
        game_data_dir=Path("/game"),
        cache_dir=tmp_path / "cache",
        team_id=123,
        patch="7.41b",
    )

    # Existing entry is never overwritten; partial entries stop for curation.
    assert isinstance(result, TeamProfileCurationResult)
    assert registry.read_text() == original_yaml


@pytest.mark.asyncio
async def test_load_team_profile_round_trip(monkeypatch, tmp_path):
    monkeypatch.setattr(team_profile_module, "GameFilesSource", FakeGameFilesSource)
    monkeypatch.setattr(team_profile_module, "OpenDotaFetcher", FakeOpenDotaFetcher)
    _write_minimal_registry(tmp_path)

    result = await build_team_profile(
        data_dir=tmp_path,
        game_data_dir=Path("/game"),
        cache_dir=tmp_path / "cache",
        team_id=123,
        patch="7.41b",
    )
    assert isinstance(result, TeamProfileBuildResult)

    profile = load_team_profile(tmp_path, "7.41b", 123)
    assert profile["team"]["team_id"] == 123
    assert [h["hero_id"] for h in profile["hero_pool"]] == [1, 2]

    by_hash = load_team_profile(tmp_path, "7.41b", 123, roster_hash=result.roster_hash)
    assert by_hash == profile


def test_load_team_profile_missing_raises(tmp_path):
    with pytest.raises(TeamProfileNotFoundError, match="build-team-profile"):
        load_team_profile(tmp_path, "7.41b", 999)


def test_resolve_team_by_id_only(tmp_path):
    registry = team_registry_file(tmp_path)
    registry.parent.mkdir(parents=True, exist_ok=True)
    registry.write_text(
        "schema_version: 1\n"
        "teams:\n"
        "  - team_id: 123\n"
        "    name: Example Team\n"
        "    aliases: [Example, ExTeam]\n"
    )

    by_id = resolve_team(tmp_path, "123")
    by_name = resolve_team(tmp_path, "example team")
    by_alias = resolve_team(tmp_path, "exteam")
    assert by_id is not None and by_id["team_id"] == 123
    assert by_name is None
    assert by_alias is None
    assert resolve_team(tmp_path, "unknown") is None


def test_resolve_team_without_registry_returns_none(tmp_path):
    assert resolve_team(tmp_path, "123") is None


def test_aggregate_team_profile_registry_name_takes_precedence_over_observed():
    profile = aggregate_team_profile(
        team_id=123,
        patch="7.41b",
        team={
            "team_id": 123,
            "name": "Authored Name",
            "aliases": ["Auth"],
            "name_source": "registry",
        },
        match_rows=[{"match_id": 1, "radiant": True}],
        match_details={
            1: {
                "radiant_team_id": 123,
                "radiant_win": True,
                "radiant_team": {"team_id": 123, "name": "Stale OpenDota Name"},
                "players": [{"player_slot": 0, "account_id": 10, "hero_id": 1}],
            }
        },
        hero_names={1: "Hero One"},
        fetched_at="2026-04-30T00:00:00Z",
    )
    assert profile["team"]["name"] == "Authored Name"
    assert profile["team"]["name_source"] == "registry"
    assert profile["team"]["observed_names"] == [{"name": "Stale OpenDota Name", "count": 1}]
