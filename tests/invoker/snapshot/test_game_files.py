import json

import pytest

from invoker.snapshot.game_files import snapshot_game_files
from invoker.snapshot.kv import KVParseError, parse_kv1


def test_parse_kv1_nested_blocks_and_comments():
    parsed = parse_kv1(
        """
        "Root"
        {
          // comment
          "hero"
          {
            "Ability1" "alchemist_acid_spray" // trailing comment
            "AbilityValues"
            {
              "radius"
              {
                "value" "350 400"
              }
            }
          }
        }
        """,
    )

    assert parsed["Root"]["hero"]["Ability1"] == "alchemist_acid_spray"
    assert parsed["Root"]["hero"]["AbilityValues"]["radius"]["value"] == "350 400"


def test_parse_kv1_skips_utf8_bom():
    assert parse_kv1('\ufeff"lang" { "Tokens" { "key" "value" } }') == {
        "lang": {"Tokens": {"key": "value"}}
    }


def test_parse_kv1_allows_newline_in_quoted_localization_string():
    parsed = parse_kv1('"lang" { "Tokens" { "key" "line one\nline two" } }')
    assert parsed["lang"]["Tokens"]["key"] == "line one\nline two"


def test_parse_kv1_fails_on_preprocessor_directives():
    with pytest.raises(KVParseError):
        parse_kv1('"Root" { #base "other.txt" }')


def test_snapshot_game_files_writes_json_contract_with_auto_localization(tmp_path):
    npc = tmp_path / "npc"
    heroes_dir = npc / "heroes"
    localization_dir = tmp_path / "resource" / "localization"
    heroes_dir.mkdir(parents=True)
    localization_dir.mkdir(parents=True)
    (npc / "npc_heroes.txt").write_text(
        """
        "DOTAHeroes"
        {
          "Version" "1"
          "npc_dota_hero_alchemist"
          {
            "Enabled" "1"
            "HeroID" "73"
            "Role" "Carry,Support"
            "Ability1" "alchemist_acid_spray"
            "Ability10" "special_bonus_unique_alchemist"
            "AbilityTalentStart" "10"
          }
        }
        """
    )
    (npc / "npc_abilities.txt").write_text(
        """
        "DOTAAbilities"
        {
          "Version" "1"
          "alchemist_acid_spray" { "AbilityCooldown" "22 21 20 19" }
          "item_should_not_be_special" { "AbilityCooldown" "1" }
        }
        """
    )
    (heroes_dir / "npc_dota_hero_alchemist.txt").write_text(
        """
        "DOTAAbilities"
        {
          "alchemist_acid_spray"
          {
            "AbilityValues"
            {
              "armor_reduction"
              {
                "value" "3 4 5 6"
                "special_bonus_unique_alchemist" "+1"
              }
            }
          }
        }
        """
    )
    (npc / "items.txt").write_text('"DOTAAbilities" { "item_blink" { "ItemCost" "2250" } }')
    (npc / "neutral_items.txt").write_text(
        '"neutral_items" { "neutral_tiers" { "1" { "items" { "item_test" "1" } } } }'
    )
    (localization_dir / "abilities_english.txt").write_text(
        '\ufeff"lang" { "Tokens" { '
        '"DOTA_Tooltip_ability_alchemist_acid_spray" "Acid Spray" '
        '"DOTA_Tooltip_ability_alchemist_acid_spray_Description" "Sprays acid." '
        "} }"
    )
    (localization_dir / "dota_schinese.txt").write_text(
        '"lang" { "Tokens" { "DOTA_Tooltip_Hero_npc_dota_hero_alchemist" "炼金术士" } }'
    )

    result = snapshot_game_files(
        tmp_path,
        tmp_path / "snapshots",
        "7.41b",
        locales=["english", "schinese"],
    )

    assert result.hero_count == 1
    assert result.locales == ("english", "schinese")
    hero_abilities = json.loads((result.patch_dir / "hero_abilities.json").read_text())
    assert hero_abilities["npc_dota_hero_alchemist"] == {
        "abilities": ["alchemist_acid_spray"],
        "talents": [{"name": "special_bonus_unique_alchemist", "level": 1}],
    }
    abilities = json.loads((result.patch_dir / "abilities.json").read_text())
    acid_values = abilities["alchemist_acid_spray"]["AbilityValues"]
    assert acid_values["armor_reduction"]["value"] == "3 4 5 6"
    localization = json.loads((result.patch_dir / "localization" / "english.json").read_text())
    assert localization["DOTA_Tooltip_ability_alchemist_acid_spray_Description"] == "Sprays acid."
    schinese = json.loads((result.patch_dir / "localization" / "schinese.json").read_text())
    assert schinese["DOTA_Tooltip_Hero_npc_dota_hero_alchemist"] == "炼金术士"
    assert "炼金术士" in (result.patch_dir / "localization" / "schinese.json").read_text()
    snapshot = json.loads((result.patch_dir / "snapshot.json").read_text())
    assert snapshot["source"] == "dota2npc extraction"
    assert snapshot["locales"] == ["english", "schinese"]
    assert snapshot["files"]["localization"] == {
        "english": "localization/english.json",
        "schinese": "localization/schinese.json",
    }
    assert str(tmp_path) not in json.dumps(snapshot)
