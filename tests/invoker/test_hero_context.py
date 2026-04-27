import pytest

from invoker.kg.ability_context import AbilityContext, TalentContext, build_ability_contexts
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


def test_build_ability_contexts_drops_hidden_subcommands_keeps_innate():
    abilities_map = {
        "hero_main": {"dname": "Main", "behavior": "No Target"},
        "hero_subcommand": {"dname": "Stop Rolling", "behavior": ["No Target", "Hidden"]},
        "hero_innate": {
            "dname": "Innate Thing",
            "behavior": ["Passive", "Hidden"],
            "is_innate": True,
        },
    }
    hero_abilities_map = {
        "npc_dota_hero_x": {
            "abilities": ["hero_main", "hero_subcommand", "hero_innate"],
            "talents": [],
        }
    }
    abilities, _ = build_ability_contexts("npc_dota_hero_x", abilities_map, hero_abilities_map)
    names = [a.name for a in abilities]
    assert "Main" in names
    assert "Innate Thing" in names
    assert "Stop Rolling" not in names


def test_build_ability_contexts_filters_tooltip_and_scepter_attribs():
    abilities_map = {
        "hero_main": {
            "dname": "Main",
            "behavior": "No Target",
            "attrib": [
                {"key": "damage", "header": "DAMAGE:", "value": "100"},
                {"key": "cast_point", "header": "CAST POINT:", "value": "0"},
                {"key": "tooltip", "header": "DAMAGE TOOLTIP:", "value": "100"},
                {"key": "scepter_radius", "header": "SCEPTER RADIUS:", "value": "300"},
                {"key": "shard_bonus", "header": "SHARD BONUS DAMAGE:", "value": "50"},
            ],
        },
    }
    hero_abilities_map = {"npc_dota_hero_x": {"abilities": ["hero_main"], "talents": []}}
    abilities, _ = build_ability_contexts("npc_dota_hero_x", abilities_map, hero_abilities_map)
    headers = [a.header for a in abilities[0].attribs]
    assert "DAMAGE:" in headers
    assert "CAST POINT:" in headers  # zero values kept — instant cast is real mechanic
    assert "DAMAGE TOOLTIP:" not in headers
    assert "SCEPTER RADIUS:" not in headers
    assert "SHARD BONUS DAMAGE:" not in headers


def test_build_ability_contexts_strips_talent_template_tokens():
    abilities_map = {
        "special_bonus_unique_x": {
            "dname": "+{s:bonus_AbilityCooldown}s Foo Cooldown",
        },
    }
    hero_abilities_map = {
        "npc_dota_hero_x": {
            "abilities": [],
            "talents": [{"name": "special_bonus_unique_x", "level": 4}],
        }
    }
    _, talents = build_ability_contexts("npc_dota_hero_x", abilities_map, hero_abilities_map)
    assert talents[0].name == "+?s Foo Cooldown"
