import json
from pathlib import Path

from invoker.identity import export_identity_localization, hero_lookup_candidates


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
                    "workshop_guide_name": "Pangolier",
                },
                "npc_dota_hero_alchemist": {
                    "Enabled": "1",
                    "HeroID": "73",
                    "workshop_guide_name": "Alchemist",
                },
            },
            indent=2,
        )
    )
    (patch_dir / "items.json").write_text(
        json.dumps(
            {
                "item_blink": {"ID": "1", "ItemCost": "2250"},
                "item_occult_bracelet": {"ItemCost": "0"},
            },
            indent=2,
        )
    )
    (patch_dir / "neutral_items.json").write_text(
        json.dumps({"neutral_tiers": {"1": {"items": {"item_occult_bracelet": "1"}}}})
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
                "npc_dota_hero_alchemist__name_alias": "shared" if alias_collision else "alch",
                "DOTA_Tooltip_Ability_item_blink": "Blink Dagger",
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
    neutral = next(
        item for item in artifact["items"] if item["internal_name"] == "item_occult_bracelet"
    )
    assert neutral["is_neutral"] is True


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
