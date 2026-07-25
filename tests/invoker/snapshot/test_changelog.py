import pytest

from invoker.snapshot.changelog import ChangelogError, build_changelog, search_changelog
from invoker.snapshot.kv import parse_kv1

MANIFEST = """
"patch_manifest"
{
    ""
    {
        "generic"
        {
            "General_Global Changes"
            {
                "title" "#DOTA_Patch_7_41_General_Global_Changes_Title"
                "note"
                {
                    "note" "#DOTA_Patch_7_41_General_Global_Changes"
                    "show_in_tooltips" "1"
                }
                "note"
                {
                    "note" "#DOTA_Patch_7_41_General_Global_Changes_2"
                    "indent" "2"
                    "info" "#DOTA_Patch_7_41_General_Global_Changes_2_info"
                }
            }
        }
        "items"
        {
            "item_dagon"
            {
                "note"
                {
                    "note" "#DOTA_Patch_7_41_item_dagon"
                }
                "postfix_lines" "1"
            }
        }
        "items_neutral"
        {
        }
        "heroes"
        {
            "npc_dota_hero_slardar"
            {
                "slardar_amplify_damage"
                {
                    "note"
                    {
                        "note" "#DOTA_Patch_7_41_slardar_slardar_amplify_damage"
                    }
                }
                "default"
                {
                    "note"
                    {
                        "note" "#DOTA_Patch_7_41_slardar"
                    }
                }
                "postfix_lines" "1"
            }
        }
        "patch_name" "patch 7.41"
        "patch_date" "2026-02-20"
    }
    ""
    {
        "generic"
        {
        }
        "heroes"
        {
            "npc_dota_hero_slardar"
            {
                "default"
                {
                    "note"
                    {
                        "note" "#DOTA_Patch_7_41d_slardar"
                    }
                }
            }
        }
        "patch_name" "patch 7.41d"
        "patch_date" "2026-06-04"
    }
}
"""

TOKENS = {
    "english": {
        "DOTA_Patch_7_41_General_Global_Changes_Title": "Global Changes",
        "DOTA_Patch_7_41_General_Global_Changes": "Facets removed from the game",
        "DOTA_Patch_7_41_General_Global_Changes_2": "Second global note",
        "DOTA_Patch_7_41_General_Global_Changes_2_info": "extra info",
        "DOTA_Patch_7_41_item_dagon": "Dagon damage increased",
        "DOTA_Patch_7_41_slardar_slardar_amplify_damage": "Armor reduction increased",
        "DOTA_Patch_7_41_slardar": "Base armor reduced by 1",
        "DOTA_Patch_7_41d_slardar": "Base damage reduced by 2",
    },
    "schinese": {
        "DOTA_Patch_7_41_General_Global_Changes": "命石已从游戏中移除",
    },
}


def write_manifest(tmp_path):
    path = tmp_path / "patchnotes.vdpn"
    path.write_text(MANIFEST)
    return path


def test_kv_duplicate_keys_collect_into_lists():
    text = '"root" { "k" "1" "k" "2" "k" "3" "other" "x" }'
    collapsed = parse_kv1(text)
    assert collapsed["root"]["k"] == "3"
    collected = parse_kv1(text, collect_duplicates=True)
    assert collected["root"]["k"] == ["1", "2", "3"]
    assert collected["root"]["other"] == "x"


def test_build_changelog_structures_patches(tmp_path):
    changelog = build_changelog(write_manifest(tmp_path), TOKENS)

    assert changelog["schema_version"] == 1
    assert changelog["locales"] == ["english", "schinese"]
    assert [p["name"] for p in changelog["patches"]] == ["7.41", "7.41d"]

    patch = changelog["patches"][0]
    assert patch["date"] == "2026-02-20"
    section = patch["generic"][0]
    assert section["section"] == "General_Global Changes"
    assert section["title"]["text"]["english"] == "Global Changes"
    first, second = section["notes"]
    assert first["text"]["english"] == "Facets removed from the game"
    assert first["text"]["schinese"] == "命石已从游戏中移除"
    assert second["indent"] == "2"
    assert second["info"]["text"]["english"] == "extra info"

    assert patch["items"]["item_dagon"][0]["text"]["english"] == "Dagon damage increased"
    slardar = patch["heroes"]["npc_dota_hero_slardar"]
    assert set(slardar) == {"slardar_amplify_damage", "default"}


def test_build_changelog_requires_manifest_root(tmp_path):
    path = tmp_path / "bad.vdpn"
    path.write_text('"something_else" { }')
    with pytest.raises(ChangelogError, match="patch_manifest"):
        build_changelog(path, {})


def test_snapshot_game_files_ingests_changelog_when_present(tmp_path):
    import json

    from invoker.snapshot.game_files import snapshot_game_files

    npc = tmp_path / "npc"
    npc.mkdir(parents=True)
    (npc / "npc_heroes.txt").write_text(
        '"DOTAHeroes" { "npc_dota_hero_slardar" { "HeroID" "28" } }'
    )
    (npc / "npc_abilities.txt").write_text(
        '"DOTAAbilities" { "slardar_amplify_damage" { "AbilityCooldown" "5" } }'
    )
    (tmp_path / "patchnotes").mkdir()
    (tmp_path / "patchnotes" / "patchnotes.vdpn").write_text(MANIFEST)
    patchnotes_loc = tmp_path / "resource" / "localization" / "patchnotes"
    patchnotes_loc.mkdir(parents=True)
    tokens = " ".join(f'"{k}" "{v}"' for k, v in TOKENS["english"].items())
    (patchnotes_loc / "patchnotes_english.txt").write_text(
        f'"patchnotes" {{ "Tokens" {{ {tokens} }} }}'
    )

    result = snapshot_game_files(tmp_path, tmp_path / "snapshots", "7.41d")

    assert result.changelog_patch_count == 2
    assert result.changelog_note_count == 6
    changelog = json.loads((result.patch_dir / "changelog.json").read_text())
    assert [p["name"] for p in changelog["patches"]] == ["7.41", "7.41d"]
    hits = search_changelog(changelog, grep="facets removed")
    assert hits and hits[0]["patch"] == "7.41"
    snapshot = json.loads((result.patch_dir / "snapshot.json").read_text())
    assert snapshot["files"]["changelog"] == "changelog.json"
    assert snapshot["source_files"]["changelog_manifest"] == "patchnotes/patchnotes.vdpn"
    assert (
        snapshot["source_files"]["changelog_localization"]["english"]
        == "resource/localization/patchnotes/patchnotes_english.txt"
    )


def test_search_changelog_filters(tmp_path):
    changelog = build_changelog(write_manifest(tmp_path), TOKENS)

    facet_hits = search_changelog(changelog, grep="facets removed")
    assert len(facet_hits) == 1
    assert facet_hits[0]["patch"] == "7.41"
    assert facet_hits[0]["scope"] == "generic"

    slardar_hits = search_changelog(changelog, entity="slardar")
    assert {hit["patch"] for hit in slardar_hits} == {"7.41", "7.41d"}
    assert len(slardar_hits) == 3

    scoped = search_changelog(changelog, entity="slardar", note_patch="7.41d")
    assert len(scoped) == 1
    assert scoped[0]["text"] == "Base damage reduced by 2"

    localized = search_changelog(changelog, grep="移除", locale="schinese")
    assert len(localized) == 1
    assert localized[0]["token"] == "DOTA_Patch_7_41_General_Global_Changes"
