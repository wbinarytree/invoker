import json
from pathlib import Path

import pytest

from invoker.gen.artifacts import CardSentence, EntityCard
from invoker.gen.client import GenerationError
from invoker.gen.items import build_item_packet, generate_item
from invoker.kg.item_context import build_item_context

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
        f"The debuff is dispellable and its damage is physical. [{MECHANICS}]"
    )


def good_card() -> EntityCard:
    return EntityCard(
        entity="mage_slayer",
        sentences=[
            CardSentence(text="Rare item, 3100 gold.", marks=[COST]),
            CardSentence(text="Grants 18% magic resistance.", marks=[ATTRIBS]),
        ],
    )


def run_generate(tmp_path, backend):
    return generate_item(
        FIXTURE_ROOT,
        backend,
        item="mage_slayer",
        patch="7.41b",
        kb_dir=tmp_path / "kb" / "7.41b",
    )


def test_packet_sections_and_marks():
    packet, text_by_mark, digest = build_item_packet(context())
    assert set(text_by_mark) == {COST, COMPONENTS, ATTRIBS, MECHANICS, DESC, LORE}
    # resolved percent-flagged header, not the KV key name — and the key
    # itself never leaks into the packet
    assert "MAGIC RESISTANCE: 18%" in text_by_mark[ATTRIBS]
    assert "bonus_magical_armor" not in text_by_mark[ATTRIBS]
    assert "Cost: 3100 gold" in text_by_mark[COST]
    assert "Perseverance (item_pers)" in text_by_mark[COMPONENTS]
    assert "Dispellable: Yes" in text_by_mark[MECHANICS]
    assert f"## [{ATTRIBS}]" in packet
    _, _, digest2 = build_item_packet(context())
    assert digest == digest2


def test_packet_sections_match_resolver_vocabulary():
    # cross-module contract: every gamefile section the packet can emit
    # must be in the resolver's fixed vocabulary, and vice versa — a
    # section added on one side only silently breaks mark resolution
    from invoker.benchmark.marks import _GAMEFILE_CLASSES

    _, vocabulary = _GAMEFILE_CLASSES["items"]
    _, text_by_mark, _ = build_item_packet(context())
    emitted = {
        mark.partition("#")[2] for mark in text_by_mark if mark.startswith("gamefile:")
    }
    assert emitted == vocabulary


def test_generate_item_writes_artifact(tmp_path):
    backend = FakeBackend(good_article(), good_card())
    artifact, path = run_generate(tmp_path, backend)
    assert path.parent.name == "mage_slayer"
    saved = json.loads(path.read_text())
    assert saved["kind"] == "item"
    assert saved["slug"] == "mage_slayer"
    assert saved["title"] == "Mage Slayer"
    assert set(saved["citations"]) == {COST, COMPONENTS, ATTRIBS, DESC, MECHANICS}
    assert saved["article_provenance"]["prompt_name"] == "item-article"
    assert (path.parent / "article.md").read_text() == good_article()
    # the packet reached the model with keyed sections inline
    article_call = backend.calls[0]
    assert f"## [{ATTRIBS}]" in article_call["user_content"]


def test_unknown_mark_fails_loudly(tmp_path):
    article = "Made-up fact. [gamefile:items/item_mage_slayer#invented]"
    backend = FakeBackend(article, good_card())
    with pytest.raises(GenerationError, match="invented"):
        run_generate(tmp_path, backend)


def test_article_without_marks_fails_loudly(tmp_path):
    backend = FakeBackend("Prose without citations.", good_card())
    with pytest.raises(GenerationError, match="no citation marks"):
        run_generate(tmp_path, backend)


def test_number_not_in_cited_section_fails(tmp_path):
    # 3100 is in #cost, not in #attribs — a resolvable mark cannot vouch
    # for a number its own section does not contain
    article = f"Costs 3100 gold. [{ATTRIBS}]"
    backend = FakeBackend(article, good_card())
    with pytest.raises(GenerationError, match="3100"):
        run_generate(tmp_path, backend)


def test_card_number_check_scoped_to_cited_section(tmp_path):
    bad = EntityCard(
        entity="mage_slayer",
        sentences=[CardSentence(text="Deals 99 damage per second.", marks=[ATTRIBS])],
    )
    backend = FakeBackend(good_article(), bad)
    with pytest.raises(GenerationError, match=r"card sentence 1.*99"):
        run_generate(tmp_path, backend)


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
