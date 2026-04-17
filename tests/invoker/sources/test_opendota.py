import json

from ...support import FIXTURES_DIR

FIXTURE_DIR = FIXTURES_DIR / "opendota"


def test_heroes_fixture_shape():
    data = json.loads((FIXTURE_DIR / "heroes.json").read_text())
    assert isinstance(data, list)
    assert len(data) >= 3
    for key in ("id", "localized_name", "name", "primary_attr", "roles"):
        assert key in data[0], f"missing {key}"


def test_hero_abilities_fixture_shape():
    data = json.loads((FIXTURE_DIR / "hero_abilities_slardar.json").read_text())
    assert "npc_dota_hero_slardar" in data
    entry = data["npc_dota_hero_slardar"]
    assert "abilities" in entry
    assert isinstance(entry["abilities"], list)
    assert len(entry["abilities"]) > 0


def test_abilities_fixture_shape():
    data = json.loads((FIXTURE_DIR / "abilities_slardar.json").read_text())
    assert len(data) > 0
    for key, ability in data.items():
        if key == "generic_hidden":
            continue
        assert "dname" in ability, f"{key}: missing dname"
        assert "desc" in ability, f"{key}: missing desc"


def test_abilities_slardar_core_spells_present():
    data = json.loads((FIXTURE_DIR / "abilities_slardar.json").read_text())
    # Corrosive Haze is the key mechanical ability for extraction
    haze = data.get("slardar_amplify_damage")
    assert haze is not None
    assert "armor" in haze["desc"].lower()

    crush = data.get("slardar_slithereen_crush")
    assert crush is not None
    assert "stun" in crush["desc"].lower()
