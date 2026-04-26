import pytest

from invoker.kg.ability_context import AbilityContext, TalentContext
from invoker.kg.hero_context import (
    HeroContextPacket,
    HeroIdentityContext,
    HeroNotFoundError,
    _find_hero,
    build_hero_context,
)
from invoker.kg.hero_stats_context import HeroStatsContext

_HEROES_LIST = [
    {
        "id": 28,
        "name": "npc_dota_hero_slardar",
        "localized_name": "Slardar",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": ["Carry", "Durable", "Initiator"],
    }
]

_HERO_STATS_MAP = {
    "28": {
        "id": 28,
        "name": "npc_dota_hero_slardar",
        "base_str": 22,
        "base_agi": 16,
        "base_int": 15,
        "str_gain": 3.2,
        "agi_gain": 1.5,
        "int_gain": 1.7,
        "base_armor": 3,
        "attack_range": 150,
        "move_speed": 295,
        "primary_attr": "str",
        "attack_type": "Melee",
    }
}

_ABILITIES_MAP = {
    "slardar_crush": {
        "dname": "Slithereen Crush",
        "behavior": "No Target",
        "dmg_type": "Physical",
        "bkbpierce": "No",
        "dispellable": "Strong Dispels Only",
        "desc": "Slams the ground.",
        "attrib": [{"key": "damage", "header": "DAMAGE:", "value": ["75", "150", "225", "300"]}],
        "mc": "100",
        "cd": "7",
    },
    "special_bonus_hp_250": {"dname": "+250 Health"},
}

_HERO_ABILITIES_MAP = {
    "npc_dota_hero_slardar": {
        "abilities": ["slardar_crush"],
        "talents": [{"name": "special_bonus_hp_250", "level": 1}],
    }
}


@pytest.mark.parametrize(
    "token",
    ["slardar", "Slardar", "28", "npc_dota_hero_slardar"],
)
def test_find_hero_matches_multiple_tokens(token):
    result = _find_hero(_HEROES_LIST, token)
    assert result["id"] == 28


def test_find_hero_raises_for_unknown():
    with pytest.raises(HeroNotFoundError):
        _find_hero(_HEROES_LIST, "nonexistent_hero")


@pytest.mark.asyncio
async def test_build_hero_context_returns_packet(monkeypatch, tmp_path):
    import invoker.kg.hero_context as hc

    class FakeFetcher:
        async def heroes(self):
            return _HEROES_LIST

        async def hero_stats(self):
            return _HERO_STATS_MAP

        async def abilities(self):
            return _ABILITIES_MAP

        async def hero_abilities_map(self):
            return _HERO_ABILITIES_MAP

        async def close(self):
            pass

    monkeypatch.setattr(hc, "OpenDotaFetcher", lambda *a, **kw: FakeFetcher())

    packet = await build_hero_context(tmp_path, "slardar", patch="7.41b")

    assert isinstance(packet, HeroContextPacket)
    assert isinstance(packet.hero, HeroIdentityContext)
    assert isinstance(packet.stats, HeroStatsContext)
    assert packet.hero.hero_slug == "slardar"
    assert packet.hero.hero_id == 28
    assert packet.patch == "7.41b"
    assert packet.stats.base_str is not None
    assert packet.stats.primary_attr == "str"
    assert len(packet.abilities) == 1
    assert isinstance(packet.abilities[0], AbilityContext)
    assert packet.abilities[0].internal_name == "slardar_crush"
    assert len(packet.talents) == 1
    assert isinstance(packet.talents[0], TalentContext)
    assert packet.talents[0].name == "+250 Health"
