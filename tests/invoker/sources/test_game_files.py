from pathlib import Path

import pytest

from invoker.kg.ability_context import build_ability_contexts
from invoker.sources.game_files import (
    GameFilesSource,
    GameFilesSourceError,
    resolve_percent_template,
)

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
    assert stats["base_attack_min"] == 26.0
    assert stats["base_attack_max"] == 32.0
    assert stats["base_attack_speed"] == 100.0
    assert stats["base_attack_time"] == 1.7
    assert stats["attack_animation_point"] == 0.35
    assert stats["attack_acquisition_range"] == 600.0
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
    assert (
        acid.description == "Sprays acid in a 350/400/450/500 radius and reduces armor by 3/4/5/6%."
    )
    assert acid.cast_range == ["450", "500", "550", "600"]
    assert acid.timing == {"cast_point": "0.3"}
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
    assert "-18% Acid Spray Mana Cost" in talent_names
    assert all("{s:" not in name and "?" not in name for name in talent_names)
    assert all("%%" not in name for name in talent_names)


def test_game_files_source_exposes_items():
    source = GameFilesSource(FIXTURE_ROOT, "7.41b")
    assert source.items()["item_blink"]["ItemCost"] == "2250"
    assert "neutral_tiers" in source.neutral_items()


def test_game_files_source_fails_loudly_when_patch_missing():
    with pytest.raises(GameFilesSourceError):
        GameFilesSource(FIXTURE_ROOT, "missing")


def test_resolve_percent_template_collapses_escape_after_value():
    assert resolve_percent_template("Deals %damage%%% damage", {"damage": "40"}) == (
        "Deals 40% damage"
    )
    assert resolve_percent_template("%bonus%%%", {"bonus": "+5"}) == "+5%"
    assert resolve_percent_template("%rate%%%", {"rate": "2.5"}) == "2.5%"
    assert resolve_percent_template("%steps%%%", {"steps": "10/20/30"}) == "10/20/30%"


def test_resolve_percent_template_preserves_unreplaced_tokens():
    # An unresolved %key% must survive verbatim, including its trailing "%%"
    # escape — collapsing would corrupt the token boundary.
    assert resolve_percent_template("%missing%%% extra", {}) == "%missing%%% extra"
    assert resolve_percent_template("gain %a%%b%", {"b": "5"}) == "gain %a%5"


def test_resolve_percent_template_leaves_escape_after_non_numeric_text():
    assert resolve_percent_template("abc%%def", {}) == "abc%%def"
    assert resolve_percent_template("%%40", {}) == "%%40"
