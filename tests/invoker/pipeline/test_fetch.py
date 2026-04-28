from pathlib import Path

import pytest

import invoker.pipeline.fetch as fetch_module
from invoker.config import Config
from invoker.pipeline.fetch import fetch_all


class FakeGameFilesSource:
    def __init__(self, root: Path, patch: str):
        assert root == Path("/game-data")
        assert patch == "7.41b"

    def heroes(self):
        return [
            {
                "id": 73,
                "name": "npc_dota_hero_alchemist",
                "localized_name": "Alchemist",
                "primary_attr": "str",
                "attack_type": "Melee",
                "roles": ["Carry"],
            },
            {
                "id": 120,
                "name": "npc_dota_hero_pangolier",
                "localized_name": "Pangolier",
                "primary_attr": "all",
                "attack_type": "Melee",
                "roles": ["Nuker"],
            },
        ]

    def abilities(self):
        return {"alchemist_acid_spray": {"dname": "Acid Spray"}}

    def hero_abilities_map(self):
        return {
            "npc_dota_hero_alchemist": {
                "abilities": ["alchemist_acid_spray"],
                "talents": [],
            }
        }


class FakeOpenDotaFetcher:
    def __init__(self, cache: Path, patch: str):
        self.cache = cache
        self.patch = patch

    async def pro_matches(self):
        return [{"match_id": 1}]

    async def matchups(self, hero_id: int):
        return [{"hero_id": 120, "games_played": 10, "wins": 6, "for": hero_id}]

    async def close(self):
        pass


class FakeStratzFetcher:
    available = False

    def __init__(self, cache: Path, patch: str, token: str | None):
        self.cache = cache
        self.patch = patch
        self.token = token

    async def close(self):
        pass


def _config(tmp_path: Path, *, game_data_dir: Path | None = Path("/game-data")) -> Config:
    return Config(
        stratz_token=None,
        data_dir=tmp_path,
        game_data_dir=game_data_dir,
        log_level="INFO",
        dev_heroes=None,
    )


@pytest.mark.asyncio
async def test_fetch_all_reads_constants_from_game_files(monkeypatch, tmp_path):
    monkeypatch.setattr(fetch_module, "GameFilesSource", FakeGameFilesSource)
    monkeypatch.setattr(fetch_module, "OpenDotaFetcher", FakeOpenDotaFetcher)
    monkeypatch.setattr(fetch_module, "StratzFetcher", FakeStratzFetcher)

    result = await fetch_all(_config(tmp_path), "7.41b", hero_filter={"Alchemist"})

    assert result["heroes"] == [FakeGameFilesSource(Path("/game-data"), "7.41b").heroes()[0]]
    assert result["hero_names"] == {73: "Alchemist", 120: "Pangolier"}
    assert result["abilities"] == {"alchemist_acid_spray": {"dname": "Acid Spray"}}
    assert result["hero_abilities"]["npc_dota_hero_alchemist"]["abilities"] == [
        "alchemist_acid_spray"
    ]
    assert result["pro_matches"] == [{"match_id": 1}]
    assert set(result["matchups"]) == {73}


@pytest.mark.asyncio
async def test_fetch_all_requires_game_data_dir(tmp_path):
    with pytest.raises(ValueError, match="INVOKER_GAME_DATA_DIR"):
        await fetch_all(_config(tmp_path, game_data_dir=None), "7.41b")
