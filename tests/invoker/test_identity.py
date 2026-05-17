import json
from pathlib import Path

from invoker.identity import (
    export_ability_localization,
    export_game_resource_bundle,
    export_identity_localization,
    export_item_identity_localization,
    export_localized_resources,
    hero_lookup_candidates,
)


def _write_snapshot(
    root: Path,
    *,
    alias_collision: bool = False,
    missing_schinese_alchemist: bool = False,
) -> Path:
    patch_dir = root / "7.41c"
    (patch_dir / "localization").mkdir(parents=True)
    (patch_dir / "snapshot.json").write_text(
        json.dumps(
            {
                "schema_version": 1,
                "patch": "7.41c",
                "source": "/local/extracted/dota2npc",
                "source_format": "pre-extracted-vpk-kv1",
                "generated_at": "2026-05-16T00:00:00Z",
                "locales": ["english", "schinese"],
                "source_files": {"heroes": "npc/npc_heroes.txt"},
            },
            indent=2,
        )
    )
    (patch_dir / "heroes.json").write_text(
        json.dumps(
            {
                "npc_dota_hero_pangolier": {
                    "Enabled": "1",
                    "HeroID": "120",
                    "AttributeBaseStrength": "19",
                    "AttributeBaseAgility": "18",
                    "AttributeBaseIntelligence": "16",
                    "AttributeStrengthGain": "2.5",
                    "AttributeAgilityGain": "3.2",
                    "AttributeIntelligenceGain": "1.9",
                    "AttributePrimary": "DOTA_ATTRIBUTE_AGILITY",
                    "AttackCapabilities": "DOTA_UNIT_CAP_MELEE_ATTACK",
                    "ArmorPhysical": "2",
                    "AttackRange": "150",
                    "MovementSpeed": "295",
                    "Role": "Carry,Escape",
                    "workshop_guide_name": "Pangolier",
                },
                "npc_dota_hero_alchemist": {
                    "Enabled": "1",
                    "HeroID": "73",
                    "AttributeBaseStrength": "23",
                    "AttributeBaseAgility": "22",
                    "AttributeBaseIntelligence": "25",
                    "AttributeStrengthGain": "2.7",
                    "AttributeAgilityGain": "1.5",
                    "AttributeIntelligenceGain": "1.8",
                    "AttributePrimary": "DOTA_ATTRIBUTE_STRENGTH",
                    "AttackCapabilities": "DOTA_UNIT_CAP_MELEE_ATTACK",
                    "ArmorPhysical": "1",
                    "AttackRange": "150",
                    "MovementSpeed": "305",
                    "Role": "Carry,Support",
                    "workshop_guide_name": "Alchemist",
                },
            },
            indent=2,
        )
    )
    (patch_dir / "items.json").write_text(
        json.dumps(
            {
                "item_blink": {
                    "ID": "1",
                    "AbilityBehavior": "DOTA_ABILITY_BEHAVIOR_POINT",
                    "AbilityCastRange": "1200",
                    "AbilityCooldown": "15.0",
                    "AbilityManaCost": "0",
                    "AbilityValues": {
                        "blink_damage_cooldown": "3.0",
                        "blink_range": "1200",
                    },
                    "ItemCost": "2250",
                },
                "item_occult_bracelet": {"ItemCost": "0"},
                "item_recipe_phylactery": {
                    "ItemCost": "200",
                    "ItemRecipe": "1",
                    "ItemRequirements": {"01": "item_pers;item_diadem"},
                    "ItemResult": "item_phylactery",
                },
            },
            indent=2,
        )
    )
    (patch_dir / "neutral_items.json").write_text(
        json.dumps({"neutral_tiers": {"1": {"items": {"item_occult_bracelet": "1"}}}})
    )
    (patch_dir / "abilities.json").write_text(
        json.dumps(
            {
                "alchemist_acid_spray": {
                    "AbilityBehavior": "DOTA_ABILITY_BEHAVIOR_POINT | DOTA_ABILITY_BEHAVIOR_AOE",
                    "AbilityCooldown": "21",
                    "AbilityManaCost": "120",
                    "AbilityUnitDamageType": "DAMAGE_TYPE_PHYSICAL",
                    "AbilityValues": {
                        "armor_reduction": {"value": "3 4 5 6"},
                        "radius": "350 400 450 500",
                    },
                    "SpellImmunityType": "SPELL_IMMUNITY_ENEMIES_NO",
                },
                "special_bonus_unique_alchemist": {
                    "AbilityType": "DOTA_ABILITY_TYPE_ATTRIBUTES",
                    "AbilityValues": {"value": "+1"},
                },
                "item_blink": {"ID": "1", "ItemCost": "2250"},
            },
            indent=2,
        )
    )
    (patch_dir / "hero_abilities.json").write_text(
        json.dumps(
            {
                "npc_dota_hero_alchemist": {
                    "abilities": ["alchemist_acid_spray", "item_blink"],
                    "talents": [{"name": "special_bonus_unique_alchemist", "level": 1}],
                }
            },
            indent=2,
        )
    )
    english_alias = "pangolier; ar"
    schinese_alias = "shilinjianshi; gungun; tangte"
    if alias_collision:
        english_alias = "shared"
    (patch_dir / "localization" / "english.json").write_text(
        json.dumps(
            {
                "DOTA_Tooltip_Hero_npc_dota_hero_pangolier": "Pangolier",
                "npc_dota_hero_pangolier__name_alias": english_alias,
                "DOTA_Tooltip_Hero_npc_dota_hero_alchemist": "Alchemist",
                "npc_dota_hero_alchemist__name_alias": ("shared" if alias_collision else "alch"),
                "DOTA_Tooltip_Ability_item_blink": "Blink Dagger",
                "DOTA_Tooltip_ability_item_blink_Description": ("Teleport a short distance."),
                "DOTA_SearchAlias_Ability_item_blink": "blink dagger",
                "DOTA_Tooltip_Ability_item_occult_bracelet:n": "Occult Bracelet",
                "DOTA_Tooltip_Ability_item_occult_bracelet_Description": (
                    "Gain power after damage."
                ),
                "DOTA_Tooltip_Ability_item_recipe_phylactery": "Phylactery Recipe",
                "DOTA_SearchAlias_Ability_item_occult_bracelet": "occult bracelet",
                "DOTA_Tooltip_ability_alchemist_acid_spray": "Acid Spray",
                "DOTA_Tooltip_ability_alchemist_acid_spray_Description": "Sprays acid.",
                "DOTA_Tooltip_ability_special_bonus_unique_alchemist": ("+1 Acid Spray Armor"),
            },
            indent=2,
        )
    )
    schinese = {
        "DOTA_Tooltip_Hero_npc_dota_hero_pangolier": "石鳞剑士",
        "npc_dota_hero_pangolier__name_alias": schinese_alias,
    }
    if not missing_schinese_alchemist:
        schinese["DOTA_Tooltip_Hero_npc_dota_hero_alchemist"] = "炼金术士"
    schinese["npc_dota_hero_alchemist__en:n"] = "Alchemist"
    schinese["DOTA_Tooltip_Ability_item_blink"] = "闪烁匕首"
    schinese["DOTA_Tooltip_ability_item_blink_Description"] = "传送一小段距离。"
    schinese["DOTA_SearchAlias_Ability_item_blink"] = "tiaodao;跳刀"
    schinese["DOTA_Tooltip_Ability_item_occult_bracelet:n"] = "玄奥手镯"
    schinese["DOTA_Tooltip_Ability_item_occult_bracelet_Description"] = "受伤后获得力量。"
    schinese["DOTA_Tooltip_Ability_item_recipe_phylactery"] = "魂匣卷轴"
    schinese["DOTA_Tooltip_ability_alchemist_acid_spray"] = "酸性喷雾"
    schinese["DOTA_Tooltip_ability_alchemist_acid_spray_Description"] = "喷洒酸液。"
    schinese["DOTA_Tooltip_ability_special_bonus_unique_alchemist"] = "+1 酸雾护甲"
    (patch_dir / "localization" / "schinese.json").write_text(
        json.dumps(schinese, ensure_ascii=False, indent=2)
    )
    return root


def test_export_identity_localization_preserves_aliases_and_sanitizes_metadata(tmp_path):
    game_data = _write_snapshot(tmp_path)

    artifact = export_identity_localization(game_data, "7.41c")

    assert artifact["schema_version"] == 1
    assert artifact["patch"] == "7.41c"
    assert artifact["locales"] == ["english", "schinese"]
    assert "/local/extracted" not in json.dumps(artifact)
    pango = next(hero for hero in artifact["heroes"] if hero["slug"] == "pangolier")
    assert pango["hero_id"] == 120
    assert pango["display_names"] == {
        "english": "Pangolier",
        "schinese": "石鳞剑士",
    }
    assert pango["aliases"]["schinese"] == ["shilinjianshi", "gungun", "tangte"]
    blink = next(item for item in artifact["items"] if item["internal_name"] == "item_blink")
    assert blink["item_id"] == 1
    assert blink["display_names"]["english"] == "Blink Dagger"
    assert blink["descriptions"]["english"] == "Teleport a short distance."
    assert blink["aliases"]["schinese"] == ["tiaodao", "跳刀"]
    neutral = next(
        item for item in artifact["items"] if item["internal_name"] == "item_occult_bracelet"
    )
    assert neutral["is_neutral"] is True
    assert neutral["display_names"] == {
        "english": "Occult Bracelet",
        "schinese": "玄奥手镯",
    }
    assert neutral["descriptions"]["schinese"] == "受伤后获得力量。"


def test_split_item_export_recovers_name_suffixes_descriptions_and_aliases(tmp_path):
    game_data = _write_snapshot(tmp_path)

    artifact = export_item_identity_localization(game_data, "7.41c")

    assert artifact["resource_type"] == "items"
    occult = next(
        item for item in artifact["items"] if item["internal_name"] == "item_occult_bracelet"
    )
    assert occult["display_names"]["english"] == "Occult Bracelet"
    assert occult["descriptions"]["english"] == "Gain power after damage."
    assert occult["aliases"]["english"] == ["occult bracelet"]


def test_ability_export_uses_hero_ability_list_and_localized_text(tmp_path):
    game_data = _write_snapshot(tmp_path)

    artifact = export_ability_localization(game_data, "7.41c")

    assert artifact["resource_type"] == "abilities"
    acid = next(
        ability
        for ability in artifact["abilities"]
        if ability["internal_name"] == "alchemist_acid_spray"
    )
    assert acid["display_names"] == {
        "english": "Acid Spray",
        "schinese": "酸性喷雾",
    }
    assert acid["descriptions"]["english"] == "Sprays acid."
    assert acid["heroes"] == ["npc_dota_hero_alchemist"]
    assert all(ability["internal_name"] != "item_blink" for ability in artifact["abilities"])


def test_split_resource_export_returns_hero_item_and_ability_artifacts(tmp_path):
    game_data = _write_snapshot(tmp_path)

    artifacts = export_localized_resources(game_data, "7.41c")

    assert sorted(artifacts) == ["abilities", "heroes", "items"]
    assert artifacts["heroes"]["resource_type"] == "heroes"
    assert artifacts["items"]["resource_type"] == "items"
    assert artifacts["abilities"]["resource_type"] == "abilities"


def test_game_resource_bundle_attaches_abilities_talents_items_and_indexes(tmp_path):
    game_data = _write_snapshot(tmp_path)

    artifacts = export_game_resource_bundle(game_data, "7.41c")

    assert sorted(artifacts) == ["bundle", "heroes", "index", "items"]
    bundle = artifacts["bundle"]
    assert bundle["files"] == {
        "heroes": "heroes.json",
        "items": "items.json",
        "index": "index.json",
    }
    assert "/local/extracted" not in json.dumps(artifacts)

    alchemist = next(hero for hero in artifacts["heroes"]["heroes"] if hero["slug"] == "alchemist")
    assert alchemist["display_names"] == {
        "english": "Alchemist",
        "schinese": "炼金术士",
    }
    assert alchemist["primary_attr"] == "str"
    assert alchemist["roles"] == ["Carry", "Support"]
    assert alchemist["stats"]["base_str"]["value"] == 23.0
    acid = next(
        ability
        for ability in alchemist["abilities"]
        if ability["internal_name"] == "alchemist_acid_spray"
    )
    assert acid["display_names"] == {
        "english": "Acid Spray",
        "schinese": "酸性喷雾",
    }
    assert acid["descriptions"]["english"] == "Sprays acid."
    assert acid["mana_cost"] == "120"
    assert acid["cooldown"] == "21"
    assert acid["attribs"] == [
        {"header": "ARMOR REDUCTION:", "key": "armor_reduction", "value": ["3", "4", "5", "6"]},
        {"header": "RADIUS:", "key": "radius", "value": ["350", "400", "450", "500"]},
    ]
    assert all(ability["internal_name"] != "item_blink" for ability in alchemist["abilities"])
    assert alchemist["talents"] == [
        {
            "display_names": {
                "english": "+1 Acid Spray Armor",
                "schinese": "+1 酸雾护甲",
            },
            "hero_level": 10,
            "internal_name": "special_bonus_unique_alchemist",
            "level": 1,
            "sources": ["hero_abilities", "abilities", "localization"],
            "value_sources": ["AbilityValues"],
        }
    ]

    blink = next(
        item for item in artifacts["items"]["items"] if item["internal_name"] == "item_blink"
    )
    assert blink["ability"]["behavior"] == ["DOTA_ABILITY_BEHAVIOR_POINT"]
    assert blink["ability"]["values"] == [
        {"header": "BLINK DAMAGE COOLDOWN:", "key": "blink_damage_cooldown", "value": "3.0"},
        {"header": "BLINK RANGE:", "key": "blink_range", "value": "1200"},
    ]
    recipe = next(
        item
        for item in artifacts["items"]["items"]
        if item["internal_name"] == "item_recipe_phylactery"
    )
    assert recipe["is_recipe"] is True
    assert recipe["recipe"] == {
        "result": "item_phylactery",
        "requirements": [{"slot": "01", "components": ["item_pers", "item_diadem"]}],
    }

    index = artifacts["index"]
    assert index["heroes"]["by_slug"]["alchemist"] == "npc_dota_hero_alchemist"
    assert index["heroes"]["by_alias"]["english"]["alch"] == ["npc_dota_hero_alchemist"]
    assert index["items"]["by_alias"]["schinese"]["跳刀"] == ["item_blink"]


def test_hero_lookup_matches_source_alias_with_field_evidence(tmp_path):
    game_data = _write_snapshot(tmp_path)

    candidates = hero_lookup_candidates(game_data, "7.41c", "gungun")

    assert [candidate["hero_slug"] for candidate in candidates] == ["pangolier"]
    assert candidates[0]["matches"] == [
        {
            "field": "alias",
            "locale": "schinese",
            "value": "gungun",
            "source": "localization",
        }
    ]


def test_hero_lookup_preserves_cjk_display_names(tmp_path):
    game_data = _write_snapshot(tmp_path)

    candidates = hero_lookup_candidates(game_data, "7.41c", "石鳞剑士")

    assert [candidate["hero_slug"] for candidate in candidates] == ["pangolier"]
    assert candidates[0]["matches"] == [
        {
            "field": "display_name",
            "locale": "schinese",
            "value": "石鳞剑士",
            "source": "localization",
        }
    ]


def test_hero_lookup_ignores_empty_normalized_query(tmp_path):
    game_data = _write_snapshot(tmp_path)

    assert hero_lookup_candidates(game_data, "7.41c", "!!!") == []


def test_missing_non_english_hero_name_is_reported_unknown(tmp_path):
    game_data = _write_snapshot(tmp_path, missing_schinese_alchemist=True)

    artifact = export_identity_localization(game_data, "7.41c")
    alchemist = next(hero for hero in artifact["heroes"] if hero["slug"] == "alchemist")

    assert alchemist["display_names"] == {"english": "Alchemist"}
    assert {
        "kind": "hero_display_name",
        "internal_name": "npc_dota_hero_alchemist",
        "missing_locales": ["schinese"],
    } in artifact["unknowns"]


def test_export_identity_localization_records_ambiguous_aliases(tmp_path):
    game_data = _write_snapshot(tmp_path, alias_collision=True)

    artifact = export_identity_localization(game_data, "7.41c")

    assert {
        "kind": "hero_alias_collision",
        "locale": "english",
        "normalized_alias": "shared",
        "internal_names": [
            "npc_dota_hero_alchemist",
            "npc_dota_hero_pangolier",
        ],
    } in artifact["unknowns"]


def test_hero_lookup_returns_multiple_candidates_for_ambiguous_alias(tmp_path):
    game_data = _write_snapshot(tmp_path, alias_collision=True)

    candidates = hero_lookup_candidates(game_data, "7.41c", "shared")

    assert [candidate["hero_slug"] for candidate in candidates] == [
        "alchemist",
        "pangolier",
    ]
