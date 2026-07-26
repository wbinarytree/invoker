from pathlib import Path

from invoker.benchmark.marks import MarkResolver
from invoker.marks import Mark, count_words, parse_marks, strip_marks

# reuse the corpus store fixture helpers from the sections tests
from tests.invoker.corpus.test_sections import make_store

KEY = "testwiki/evasion@42#Uphill_Miss_Chance"

CHANGELOG = {
    "schema_version": 1,
    "locales": ["english"],
    "patches": [
        {
            "name": "7.41",
            "date": "2026-03-24",
            "generic": [
                {
                    "section": "global_changes",
                    "title": {"token": "TITLE_TOKEN", "text": {"english": "General"}},
                    "notes": [
                        {
                            "token": "DOTA_Patch_7_41_General_Global_Changes",
                            "text": {"english": "Facets removed from the game"},
                        }
                    ],
                }
            ],
            "items": {
                "item_mage_slayer": [
                    {
                        "token": "ITEM_NOTE",
                        "text": {"english": "Recipe cost reduced"},
                        "info": {"token": "ITEM_INFO", "text": {"english": "detail"}},
                    }
                ]
            },
            "neutral_items": {},
            "heroes": {
                "npc_dota_hero_slardar": {
                    "abilities": [
                        {"token": "HERO_NOTE", "text": {"english": "Corrosive Haze cooldown"}}
                    ]
                }
            },
            "neutral_creeps": {},
        }
    ],
}


def test_parse_marks_dedupes_in_first_use_order():
    text = f"A. [corpus:{KEY}] B. [changelog:TOKEN_1] C. [corpus:{KEY}]"
    assert parse_marks(text) == [Mark("corpus", KEY), Mark("changelog", "TOKEN_1")]


def test_parse_marks_ignores_markdown_links_and_unknown_kinds():
    assert parse_marks("[link](https://example.test) and [wiki:foo] and [corpus:]") == []


def test_count_words_excludes_mark_tokens():
    text = f"Attacks miss 25% uphill. [corpus:{KEY}] [changelog:TOKEN]"
    assert strip_marks(text).strip() == "Attacks miss 25% uphill."
    assert count_words(text) == 4


def test_corpus_mark_resolves_against_stored_section_keys(tmp_path):
    resolver = MarkResolver(corpus_store=make_store(tmp_path))
    assert resolver.resolve(Mark("corpus", KEY)).ok
    # the lead section (no anchor) is citable too
    assert resolver.resolve(Mark("corpus", "testwiki/evasion@42")).ok


def test_corpus_mark_wrong_revision_or_section_is_unresolvable(tmp_path):
    resolver = MarkResolver(corpus_store=make_store(tmp_path))
    stale = resolver.resolve(Mark("corpus", "testwiki/evasion@41#Definition"))
    assert not stale.ok
    assert "not a section key" in (stale.reason or "")
    invented = resolver.resolve(Mark("corpus", f"{KEY}_Invented"))
    assert not invented.ok


def test_corpus_mark_unknown_page_reports_the_load_failure(tmp_path):
    resolver = MarkResolver(corpus_store=make_store(tmp_path))
    missing = resolver.resolve(Mark("corpus", "testwiki/missing@1"))
    assert not missing.ok
    assert "index" in (missing.reason or "")


def test_corpus_mark_malformed_key(tmp_path):
    resolver = MarkResolver(corpus_store=make_store(tmp_path))
    assert not resolver.resolve(Mark("corpus", "no-slash")).ok


def test_changelog_marks_resolve_note_info_and_title_tokens():
    resolver = MarkResolver(changelog=CHANGELOG)
    for token in (
        "DOTA_Patch_7_41_General_Global_Changes",
        "TITLE_TOKEN",
        "ITEM_NOTE",
        "ITEM_INFO",
        "HERO_NOTE",
    ):
        assert resolver.resolve(Mark("changelog", token)).ok, token
    made_up = resolver.resolve(Mark("changelog", "MADE_UP_TOKEN"))
    assert not made_up.ok


def test_unavailable_stores_report_why():
    resolver = MarkResolver()
    corpus = resolver.resolve(Mark("corpus", KEY))
    assert not corpus.ok
    assert "not available" in (corpus.reason or "")
    changelog = resolver.resolve(Mark("changelog", "TOKEN"))
    assert not changelog.ok
    assert "not available" in (changelog.reason or "")


def test_kinds_without_resolvers_yet_are_unresolvable_with_reason():
    resolver = MarkResolver()
    for kind in ("stats", "human"):
        resolution = resolver.resolve(Mark(kind, "item_mage_slayer"))
        assert not resolution.ok
        assert "no resolver" in (resolution.reason or "")


GAME_FIXTURE = Path(__file__).resolve().parents[2] / "fixtures" / "game_snapshot"


def snapshot_resolver() -> MarkResolver:
    return MarkResolver(game_data_dir=GAME_FIXTURE, patch="7.41b")


def test_gamefile_marks_resolve_records_and_sections():
    resolver = snapshot_resolver()
    assert resolver.resolve(Mark("gamefile", "items/item_mage_slayer")).ok
    assert resolver.resolve(Mark("gamefile", "items/item_mage_slayer#attribs")).ok
    assert resolver.resolve(Mark("gamefile", "abilities/alchemist_acid_spray")).ok


def test_gamefile_marks_reject_unknown_record_section_and_class():
    resolver = snapshot_resolver()
    missing = resolver.resolve(Mark("gamefile", "items/item_invented"))
    assert not missing.ok
    assert "not in the 7.41b items snapshot" in (missing.reason or "")
    section = resolver.resolve(Mark("gamefile", "items/item_mage_slayer#invented"))
    assert not section.ok
    assert "unknown section" in (section.reason or "")
    klass = resolver.resolve(Mark("gamefile", "cosmetics/item_mage_slayer"))
    assert not klass.ok
    assert "known classes" in (klass.reason or "")


def test_loc_marks_resolve_with_ability_case_swap():
    resolver = snapshot_resolver()
    assert resolver.resolve(Mark("loc", "DOTA_Tooltip_ability_item_mage_slayer_Description")).ok
    # stored token uses capital-A Ability; the lowercase query still resolves
    assert resolver.resolve(Mark("loc", "DOTA_Tooltip_ability_item_blink")).ok
    made_up = resolver.resolve(Mark("loc", "DOTA_Tooltip_ability_item_invented"))
    assert not made_up.ok


def test_gamefile_and_loc_unavailable_without_snapshot():
    resolver = MarkResolver()
    for kind, key in (("gamefile", "items/item_mage_slayer"), ("loc", "TOKEN")):
        resolution = resolver.resolve(Mark(kind, key))
        assert not resolution.ok
        assert "not available" in (resolution.reason or "")
