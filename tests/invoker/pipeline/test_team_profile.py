from pathlib import Path

import pytest

import invoker.pipeline.team_profile as team_profile_module
from invoker.paths import team_registry_file
from invoker.pipeline.team_profile import (
    TeamProfileNotFoundError,
    aggregate_team_profile,
    build_team_profile,
    load_team_profile,
    resolve_team,
)


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
                ],
            },
        },
        hero_names={1: "Hero One", 2: "Hero Two", 3: "Hero Three", 4: "Hero Four"},
        fetched_at="2026-04-30T00:00:00Z",
        patch_constants=[
            {"id": 59, "name": "7.40"},
            {"id": 60, "name": "7.41"},
        ],
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
        "primary_position": 1,
    }
    assert profile["roster"]["roster_hash"] != "unknown"
    assert profile["observed_patches"] == [
        {"patch_id": 59, "patch_name": "7.40", "match_count": 1},
        {"patch_id": 60, "patch_name": "7.41", "match_count": 1},
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
    assert hero_two["positions"] == {"1": 1, "2": 1}
    assert hero_two["primary_position"] == 1
    hero_two_players = sorted(hero_two["players"], key=lambda p: p["account_id"])
    assert hero_two_players == [
        {
            "account_id": 10,
            "personaname": "Yatoro [Pro]",
            "games": 1,
            "positions": {"1": 1},
            "primary_position": 1,
        },
        {
            "account_id": 11,
            "personaname": "Larl",
            "games": 1,
            "positions": {"2": 1},
            "primary_position": 2,
        },
    ]
    assert profile["hero_pool"][-1]["localized_name"] is None

    yatoro = next(p for p in profile["players"] if p["account_id"] == 10)
    assert yatoro["personaname"] == "Yatoro [Pro]"
    assert yatoro["games"] == 2
    assert yatoro["wins"] == 1
    assert yatoro["positions"] == {"1": 2}
    assert yatoro["primary_position"] == 1
    assert [h["hero_id"] for h in yatoro["hero_pool"]] == [1, 2]
    yatoro_hero_one = next(h for h in yatoro["hero_pool"] if h["hero_id"] == 1)
    assert yatoro_hero_one["win_match_ids"] == [1]
    assert yatoro_hero_one["loss_match_ids"] == []
    yatoro_hero_two = next(h for h in yatoro["hero_pool"] if h["hero_id"] == 2)
    assert yatoro_hero_two["win_match_ids"] == []
    assert yatoro_hero_two["loss_match_ids"] == [2]


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
            "players": [
                {"player_slot": 0, "account_id": 10, "hero_id": 1, "personaname": "P1"},
                {"player_slot": 1, "account_id": 11, "hero_id": 2, "personaname": "P2"},
            ],
        }

    async def constants_patch(self):
        return [{"id": 60, "name": "7.41"}]

    async def close(self):
        pass


@pytest.mark.asyncio
async def test_build_team_profile_writes_profile_and_index(monkeypatch, tmp_path):
    monkeypatch.setattr(team_profile_module, "GameFilesSource", FakeGameFilesSource)
    monkeypatch.setattr(team_profile_module, "OpenDotaFetcher", FakeOpenDotaFetcher)

    result = await build_team_profile(
        data_dir=tmp_path,
        game_data_dir=Path("/game"),
        cache_dir=tmp_path / "cache",
        team_id=123,
        patch="7.41b",
        limit=50,
        force=True,
    )

    assert result.profile_path.exists()
    assert result.index_path.exists()
    assert result.match_count == 2
    assert result.hero_count == 2
    assert result.missing_match_detail_count == 1
    assert result.profile_path.parent.name == result.roster_hash

    profile_text = result.profile_path.read_text()
    assert '"hero_id": 1' in profile_text
    assert '"missing_match_detail_count": 1' in profile_text
    assert result.index_path.read_text().count('"team_id": 123') == 1


@pytest.mark.asyncio
async def test_load_team_profile_round_trip(monkeypatch, tmp_path):
    monkeypatch.setattr(team_profile_module, "GameFilesSource", FakeGameFilesSource)
    monkeypatch.setattr(team_profile_module, "OpenDotaFetcher", FakeOpenDotaFetcher)

    result = await build_team_profile(
        data_dir=tmp_path,
        game_data_dir=Path("/game"),
        cache_dir=tmp_path / "cache",
        team_id=123,
        patch="7.41b",
    )

    profile = load_team_profile(tmp_path, "7.41b", 123)
    assert profile["team"]["team_id"] == 123
    assert [h["hero_id"] for h in profile["hero_pool"]] == [1, 2]

    by_hash = load_team_profile(tmp_path, "7.41b", 123, roster_hash=result.roster_hash)
    assert by_hash == profile


def test_load_team_profile_missing_raises(tmp_path):
    with pytest.raises(TeamProfileNotFoundError, match="build-team-profile"):
        load_team_profile(tmp_path, "7.41b", 999)


def test_resolve_team_by_id_name_and_alias(tmp_path):
    registry = team_registry_file(tmp_path)
    registry.parent.mkdir(parents=True, exist_ok=True)
    registry.write_text(
        "schema_version: 1\n"
        "teams:\n"
        "  - team_id: 123\n"
        "    name: Example Team\n"
        "    aliases: [Example, ExTeam]\n"
    )

    assert resolve_team(tmp_path, "123")["team_id"] == 123
    assert resolve_team(tmp_path, "example team")["team_id"] == 123
    assert resolve_team(tmp_path, "exteam")["team_id"] == 123
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
    assert profile["team"]["observed_names"] == [
        {"name": "Stale OpenDota Name", "count": 1}
    ]
