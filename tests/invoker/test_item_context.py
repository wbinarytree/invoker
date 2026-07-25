from pathlib import Path

import pytest

from invoker.kg.item_context import (
    ItemNotFoundError,
    build_item_context,
    build_item_context_from_source,
)
from invoker.sources.game_files import GameFilesSource

FIXTURE_ROOT = Path(__file__).resolve().parents[1] / "fixtures" / "game_snapshot"


def mage_slayer_context():
    return build_item_context(FIXTURE_ROOT, "mage slayer", patch="7.41b")


def test_item_context_localization_and_template_join():
    context = mage_slayer_context()
    assert context.internal_name == "item_mage_slayer"
    assert context.name == "Mage Slayer"
    assert context.cost == 3100
    assert context.quality == "rare"
    assert context.dispellable == "Yes"
    assert context.damage_type == "Physical"
    assert context.lore == "Forged to fell the False King."
    # %field% templates resolved from AbilityValues, HTML stripped to lines
    assert context.description == (
        "Passive: Mage Slayer\n"
        "Places a debuff when you attack enemies, dealing 35 physical damage "
        "per second and causing them to do 40% less spell damage for 3 seconds."
    )
    values = {a.key: a.value for a in context.attribs}
    assert values["dps"] == "35"
    assert values["bonus_magical_armor"] == "18"


def test_item_context_components_from_recipe():
    context = mage_slayer_context()
    assert context.components == ["item_pers", "item_cloak"]
    assert context.component_names == ["Perseverance", "Cloak"]
    assert context.recipe_cost is None  # zero-cost recipe not reported


def test_item_context_costed_recipe_and_optional_component_marker():
    context = build_item_context(FIXTURE_ROOT, "item_costed_recipe_thing", patch="7.41b")
    assert context.recipe_cost == 250
    assert context.components == ["item_cloak"]  # trailing * stripped


def test_item_context_resolves_by_internal_name_and_prefixless():
    for token in ("item_blink", "blink", "Blink Dagger"):
        context = build_item_context(FIXTURE_ROOT, token, patch="7.41b")
        assert context.internal_name == "item_blink"
    assert context.cast_range == "1200"
    assert context.components is None


def test_recipes_are_not_items():
    source = GameFilesSource(FIXTURE_ROOT, "7.41b")
    records = source.item_records()
    assert "item_recipe_mage_slayer" not in records
    with pytest.raises(ItemNotFoundError):
        build_item_context_from_source(source, "item_recipe_mage_slayer", patch="7.41b")


def test_unknown_item_fails_loudly():
    with pytest.raises(ItemNotFoundError, match="not found in game-file snapshot"):
        build_item_context(FIXTURE_ROOT, "definitely_not_an_item", patch="7.41b")
