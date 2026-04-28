from pathlib import Path

import pytest

from invoker.kg.ability_context import build_ability_contexts
from invoker.sources.game_files import GameFilesSource, GameFilesSourceError

FIXTURE_ROOT = Path(__file__).resolve().parents[2] / "fixtures" / "game_snapshot"


def test_game_files_source_heroes_and_stats():
    source = GameFilesSource(FIXTURE_ROOT, "7.41b")

    heroes = source.heroes()
    alchemist = next(hero for hero in heroes if hero["name"] == "npc_dota_hero_alchemist")
    test_ranged = next(hero for hero in heroes if hero["name"] == "npc_dota_hero_test_ranged")
    assert alchemist == {
        "id": 73,
        "name": "npc_dota_hero_alchemist",
        "localized_name": "Alchemist",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": ["Carry", "Support", "Durable"],
    }
    assert test_ranged["localized_name"] == "Test Ranged"

    stats = source.hero_stats()["73"]
    assert stats["base_str"] == 23.0
    assert stats["str_gain"] == 2.7
    assert stats["attack_range"] == 150.0
    assert stats["move_speed"] == 295.0


def test_game_files_source_abilities_match_context_input_shape():
    source = GameFilesSource(FIXTURE_ROOT, "7.41b")

    abilities, talents = build_ability_contexts(
        "npc_dota_hero_alchemist",
        source.abilities(),
        source.hero_abilities_map(),
    )

    acid = next(ability for ability in abilities if ability.internal_name == "alchemist_acid_spray")
    assert acid.name == "Acid Spray"
    assert acid.behavior == ["Point Target", "AOE"]
    assert acid.damage_type == "Physical"
    assert acid.pierces_debuff_immunity is False
    assert acid.mana_cost == "120"
    assert acid.cooldown == ["22", "21", "20", "19"]
    assert acid.attribs[0].header == "ARMOR REDUCTION:"
    assert acid.attribs[0].value == ["3", "4", "5", "6"]

    innate = next(
        ability for ability in abilities if ability.internal_name == "alchemist_goblins_greed"
    )
    assert innate.source == "innate"

    shard = source.abilities()["alchemist_berserk_potion"]
    assert shard["is_granted_by_shard"] is True
    assert shard["has_shard_upgrade"] is True
    assert shard["dispellable"] == "Yes"

    talent_names = [talent.name for talent in talents]
    assert "+1 Acid Spray Armor Reduction" in talent_names
    assert "+250 Health" in talent_names
    assert "+100 Missing Talent Record" in talent_names
    assert all("{s:" not in name and "?" not in name for name in talent_names)


def test_game_files_source_exposes_items():
    source = GameFilesSource(FIXTURE_ROOT, "7.41b")
    assert source.items()["item_blink"]["ItemCost"] == "2250"
    assert "neutral_tiers" in source.neutral_items()


def test_game_files_source_fails_loudly_when_patch_missing():
    with pytest.raises(GameFilesSourceError):
        GameFilesSource(FIXTURE_ROOT, "missing")
