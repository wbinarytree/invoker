import dataclasses
import json
from pathlib import Path

import pytest

from invoker.gen.artifacts import CardSentence, EntityCard
from invoker.gen.client import GenerationError
from invoker.gen.items import build_item_packet, generate_item
from invoker.kg.ability_context import AttribEntry
from invoker.kg.item_context import ItemContext, build_item_context

# reuse the queued-output fake from the concept tests
from tests.invoker.gen.test_concepts import FakeBackend

FIXTURE_ROOT = Path(__file__).resolve().parents[2] / "fixtures" / "game_snapshot"

COST = "gamefile:items/item_mage_slayer#cost"
COMPONENTS = "gamefile:items/item_mage_slayer#components"
ATTRIBS = "gamefile:items/item_mage_slayer#attribs"
MECHANICS = "gamefile:items/item_mage_slayer#mechanics"
DESC = "loc:DOTA_Tooltip_ability_item_mage_slayer_Description"
LORE = "loc:DOTA_Tooltip_ability_item_mage_slayer_Lore"


def context():
    return build_item_context(FIXTURE_ROOT, "mage_slayer", patch="7.41b")


def good_article() -> str:
    return (
        "# Mage Slayer\n\n"
        f"A rare item costing 3100 gold, built from Perseverance and Cloak. "
        f"[{COST}] [{COMPONENTS}]\n\n"
        "| Magic Resistance | 18% |\n|---|---|\n| DPS | 35 |\n\n"
        f"[{ATTRIBS}]\n\n"
        f"Attacks apply a 3-second debuff dealing 35 physical damage per second "
        f"and reducing spell damage output by 40%. [{DESC}] "
        f"The debuff is dispellable and its damage is physical. [{MECHANICS}] "
        f"Forged to end the reign of mages. [{LORE}]"
    )


def good_card() -> EntityCard:
    return EntityCard(
        entity="mage_slayer",
        sentences=[
            CardSentence(text="Rare item, 3100 gold.", marks=[COST]),
            CardSentence(text="Grants 18% magic resistance.", marks=[ATTRIBS]),
        ],
    )


def run_generate(tmp_path, backend, rejected_dir=None):
    return generate_item(
        FIXTURE_ROOT,
        backend,
        item="mage_slayer",
        patch="7.41b",
        kb_dir=tmp_path / "kb" / "7.41b",
        rejected_dir=rejected_dir,
    )


def test_packet_sections_and_marks():
    packet, text_by_mark, digest = build_item_packet(context())
    assert set(text_by_mark) == {COST, COMPONENTS, ATTRIBS, MECHANICS, DESC, LORE}
    # resolved percent-flagged header, not the KV key name — and the key
    # itself never leaks into the packet
    assert "MAGIC RESISTANCE: 18%" in text_by_mark[ATTRIBS]
    assert "bonus_magical_armor" not in text_by_mark[ATTRIBS]
    assert "Cost: 3100 gold" in text_by_mark[COST]
    # the build formula carries component prices; a zero-cost recipe and an
    # empty builds-into stay silent (null over placeholder)
    assert "- Perseverance (item_pers) — 1300 gold" in text_by_mark[COMPONENTS]
    assert "- Cloak (item_cloak) — 500 gold" in text_by_mark[COMPONENTS]
    assert "Recipe" not in text_by_mark[COMPONENTS]
    assert "Builds into" not in text_by_mark[COMPONENTS]
    assert "Dispellable: Yes" in text_by_mark[MECHANICS]
    assert f"## [{ATTRIBS}]" in packet
    _, _, digest2 = build_item_packet(context())
    assert digest == digest2


def test_packet_recipe_graph_both_directions():
    cloak = build_item_context(FIXTURE_ROOT, "item_cloak", patch="7.41b")
    _, text_by_mark, _ = build_item_packet(cloak)
    section = text_by_mark["gamefile:items/item_cloak#components"]
    assert "Components:" not in section  # basic item — nothing built from
    assert "Builds into:" in section
    assert "- Mage Slayer (item_mage_slayer) — 3100 gold" in section
    costed = build_item_context(FIXTURE_ROOT, "item_costed_recipe_thing", patch="7.41b")
    _, text_by_mark, _ = build_item_packet(costed)
    section = text_by_mark["gamefile:items/item_costed_recipe_thing#components"]
    assert "- Recipe — 250 gold" in section


def make_context(**overrides) -> ItemContext:
    base = ItemContext(
        patch="7.41b",
        internal_name="item_stick",
        name="Stick",
        cost=1350,
        recipe_cost=None,
        quality="component",
        behavior=["Passive"],
        damage_type=None,
        dispellable=None,
        description=None,
        description_token=None,
        lore=None,
        lore_token=None,
        attribs=[AttribEntry(header="DAMAGE:", value="20", key="bonus_damage")],
        components=None,
        builds_into=[],
    )
    return dataclasses.replace(base, **overrides)


def test_boilerplate_passive_emits_no_mechanics_section():
    # bare Passive on a stat-stick (no description = no ability) is engine
    # boilerplate; the section vanishes rather than forcing a vacuous
    # "has Passive behavior" sentence into every article
    _, text_by_mark, _ = build_item_packet(make_context())
    assert "gamefile:items/item_stick#mechanics" not in text_by_mark


def test_passive_kept_when_item_has_an_ability():
    _, text_by_mark, _ = build_item_packet(
        make_context(
            description="Passive: Combo Breaker",
            description_token="DOTA_Tooltip_ability_item_stick_Description",
        )
    )
    assert "Behavior: Passive" in text_by_mark["gamefile:items/item_stick#mechanics"]


def test_mechanics_value_duplicating_attrib_row_is_dropped():
    # the KV stores aeon_disk's cooldown twice (AbilityCooldown and an
    # AbilityValues key); only the attribs row survives
    _, text_by_mark, _ = build_item_packet(
        make_context(
            description="Passive: Combo Breaker",
            description_token="DOTA_Tooltip_ability_item_stick_Description",
            attribs=[
                AttribEntry(
                    header="COOLDOWN DURATION:",
                    value=["105.0", "125.0", "145.0", "165.0"],
                    key="cooldown_duration",
                )
            ],
            cooldown=["105.0", "125.0", "145.0", "165.0"],
            mana_cost="150",
        )
    )
    mechanics = text_by_mark["gamefile:items/item_stick#mechanics"]
    assert "Cooldown" not in mechanics
    assert "Mana cost: 150" in mechanics


def test_packet_sections_match_resolver_vocabulary():
    # cross-module contract: every gamefile section the packet can emit
    # must be in the resolver's fixed vocabulary, and vice versa — a
    # section added on one side only silently breaks mark resolution
    from invoker.benchmark.marks import _GAMEFILE_CLASSES

    _, vocabulary = _GAMEFILE_CLASSES["items"]
    _, text_by_mark, _ = build_item_packet(context())
    emitted = {mark.partition("#")[2] for mark in text_by_mark if mark.startswith("gamefile:")}
    assert emitted == vocabulary


def test_generate_item_writes_artifact(tmp_path):
    backend = FakeBackend(good_article(), good_card())
    artifact, path = run_generate(tmp_path, backend)
    assert path.parent.name == "mage_slayer"
    saved = json.loads(path.read_text())
    assert saved["kind"] == "item"
    assert saved["slug"] == "mage_slayer"
    assert saved["title"] == "Mage Slayer"
    assert set(saved["citations"]) == {COST, COMPONENTS, ATTRIBS, DESC, MECHANICS, LORE}
    assert saved["article_provenance"]["prompt_name"] == "item-article"
    assert "card" not in saved  # the card's one home is the frontmatter
    file_text = (path.parent / "article.md").read_text()
    assert file_text.startswith("---\n")
    assert "Rare item, 3100 gold." in file_text  # card in frontmatter
    assert file_text.endswith(good_article())
    # the packet reached the model with keyed sections inline
    article_call = backend.calls[0]
    assert f"## [{ATTRIBS}]" in article_call["user_content"]


def test_unknown_mark_fails_loudly(tmp_path):
    article = "Made-up fact. [gamefile:items/item_mage_slayer#invented]"
    backend = FakeBackend(article, good_card())
    with pytest.raises(GenerationError, match="invented"):
        run_generate(tmp_path, backend)


def test_article_without_marks_fails_loudly(tmp_path):
    backend = FakeBackend("# Mage Slayer\n\nProse without citations.", good_card())
    with pytest.raises(GenerationError, match="no citation marks"):
        run_generate(tmp_path, backend)


def test_number_not_in_cited_section_fails(tmp_path):
    # 3100 is in #cost, not in #attribs — a resolvable mark cannot vouch
    # for a number its own section does not contain
    article = good_article() + f"\n\nCosts 3100 gold. [{ATTRIBS}]"
    backend = FakeBackend(article, good_card())
    with pytest.raises(GenerationError, match="3100"):
        run_generate(tmp_path, backend)


def test_article_dropping_a_packet_section_fails_loudly(tmp_path):
    # the lore loc section is uncited — coverage names the dropped key;
    # loc keys have no anchor, so the References exemption never applies
    article = good_article().replace(f" Forged to end the reign of mages. [{LORE}]", "")
    backend = FakeBackend(article, good_card())
    with pytest.raises(GenerationError, match=rf"does not cite packet sections.*{LORE}"):
        run_generate(tmp_path, backend)


def test_card_number_check_scoped_to_cited_section(tmp_path):
    bad = EntityCard(
        entity="mage_slayer",
        sentences=[CardSentence(text="Deals 99 damage per second.", marks=[ATTRIBS])],
    )
    backend = FakeBackend(good_article(), bad)
    with pytest.raises(GenerationError, match=r"card sentence 1.*99"):
        run_generate(tmp_path, backend)


def test_check_failure_persists_rejected_item_article(tmp_path):
    # parity with the concept side: a coverage failure after a paid
    # article call lands article + error under rejected/items/<slug>/
    article = good_article().replace(f"[{MECHANICS}] ", "")
    rejected = tmp_path / "rejected"
    with pytest.raises(GenerationError, match="does not cite"):
        run_generate(tmp_path, FakeBackend(article, good_card()), rejected_dir=rejected)
    (attempt,) = list((rejected / "items" / "mage_slayer").iterdir())
    assert (attempt / "article.md").read_text() == article
    assert "does not cite" in (attempt / "error.txt").read_text()
    assert not (attempt / "card.json").exists()


def test_item_card_failure_persists_article_and_card(tmp_path):
    bad = EntityCard(
        entity="mage_slayer",
        sentences=[CardSentence(text="Rare item.", marks=["gamefile:items/item_mage_slayer#nope"])],
    )
    rejected = tmp_path / "rejected"
    with pytest.raises(GenerationError, match="nope"):
        run_generate(tmp_path, FakeBackend(good_article(), bad), rejected_dir=rejected)
    (attempt,) = list((rejected / "items" / "mage_slayer").iterdir())
    assert (attempt / "article.md").read_text() == good_article()
    assert "nope" in (attempt / "card.json").read_text()


def test_no_rejected_dir_means_no_persistence(tmp_path):
    article = good_article().replace(f"[{MECHANICS}] ", "")
    with pytest.raises(GenerationError, match="does not cite"):
        run_generate(tmp_path, FakeBackend(article, good_card()))
    assert not list(tmp_path.glob("**/rejected"))


def test_regenerate_card_swaps_card_and_keeps_article(tmp_path):
    from invoker.gen.artifacts import load_entity_article
    from invoker.gen.items import regenerate_item_card

    _, path = run_generate(tmp_path, FakeBackend(good_article(), good_card()))
    lore_card = EntityCard(
        entity="mage_slayer",
        sentences=[
            CardSentence(text="Rare item, 3100 gold.", marks=[COST]),
            CardSentence(text="Forged to end the reign of mages.", marks=[LORE]),
        ],
    )
    backend = FakeBackend("unused", lore_card)
    updated, path2 = regenerate_item_card(backend, artifact_path=path)
    assert path2 == path
    assert updated.card.sentences[-1].marks == [LORE]
    # sha rebinds and the article body is byte-identical
    reloaded, body = load_entity_article(path)
    assert reloaded.card == lore_card
    assert body == good_article()
    # only the card call went to the backend — the article was not regenerated
    assert [call["prompt_name"] for call in backend.calls] == ["item-card"]


def test_regenerate_card_rejects_marks_outside_the_article(tmp_path):
    from invoker.gen.items import regenerate_item_card

    _, path = run_generate(tmp_path, FakeBackend(good_article(), good_card()))
    before = path.read_text()
    bad_card = EntityCard(
        entity="mage_slayer",
        sentences=[CardSentence(text="Rare item.", marks=["gamefile:items/item_mage_slayer#nope"])],
    )
    with pytest.raises(GenerationError, match="card"):
        regenerate_item_card(FakeBackend("unused", bad_card), artifact_path=path)
    assert path.read_text() == before  # nothing written on failure


def test_article_without_title_heading_fails_loudly(tmp_path):
    headless = good_article().removeprefix("# Mage Slayer\n\n")
    with pytest.raises(GenerationError, match="does not open with"):
        run_generate(tmp_path, FakeBackend(headless, good_card()))


def test_unknown_item_fails_loudly(tmp_path):
    backend = FakeBackend(good_article(), good_card())
    with pytest.raises(GenerationError, match="not_an_item"):
        generate_item(
            FIXTURE_ROOT,
            backend,
            item="not_an_item",
            patch="7.41b",
            kb_dir=tmp_path / "kb",
        )
