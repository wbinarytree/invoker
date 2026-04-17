import json

import pytest

from ...support import FIXTURES_DIR

FIXTURE_DIR = FIXTURES_DIR / "opendota"

HEROES = ["slardar", "puck", "invoker"]


def test_heroes_fixture_shape():
    data = json.loads((FIXTURE_DIR / "heroes.json").read_text())
    assert isinstance(data, list)
    assert len(data) >= 3
    for key in ("id", "localized_name", "name", "primary_attr", "roles"):
        assert key in data[0], f"missing {key}"


@pytest.mark.parametrize("hero", HEROES)
def test_hero_abilities_fixture_shape(hero: str):
    data = json.loads((FIXTURE_DIR / f"hero_abilities_{hero}.json").read_text())
    hkey = f"npc_dota_hero_{hero}"
    assert hkey in data
    entry = data[hkey]
    assert "abilities" in entry
    assert isinstance(entry["abilities"], list)
    assert len(entry["abilities"]) > 0


@pytest.mark.parametrize("hero", HEROES)
def test_abilities_fixture_shape(hero: str):
    data = json.loads((FIXTURE_DIR / f"abilities_{hero}.json").read_text())
    assert len(data) > 0
    for key, ability in data.items():
        if key == "generic_hidden":
            continue
        # "Invoked Spell" placeholder slots for Invoker have desc but no dname yet in
        # some OpenDota builds — accept either ordering.
        if ability.get("behavior") == "Hidden":
            continue
        assert "dname" in ability, f"{hero}:{key}: missing dname"
        assert "desc" in ability, f"{hero}:{key}: missing desc"


def test_abilities_slardar_core_spells_present():
    data = json.loads((FIXTURE_DIR / "abilities_slardar.json").read_text())
    haze = data.get("slardar_amplify_damage")
    assert haze is not None
    assert "armor" in haze["desc"].lower()

    crush = data.get("slardar_slithereen_crush")
    assert crush is not None
    assert "stun" in crush["desc"].lower()


def test_abilities_puck_core_spells_present():
    data = json.loads((FIXTURE_DIR / "abilities_puck.json").read_text())

    rift = data.get("puck_waning_rift")
    assert rift is not None
    assert "silence" in rift["desc"].lower()

    coil = data.get("puck_dream_coil")
    assert coil is not None
    assert "stun" in coil["desc"].lower()

    phase = data.get("puck_phase_shift")
    assert phase is not None
    assert "immune" in phase["desc"].lower()


def test_abilities_invoker_core_spells_present():
    """Invoker is the stress case: 3 reagents + 10 invoked spells must all carry
    usable mechanical text. A missing description here would poison any
    downstream tag extraction."""
    data = json.loads((FIXTURE_DIR / "abilities_invoker.json").read_text())

    # All 10 invoked spells must be present with descriptions.
    invoked = [
        "invoker_cold_snap",
        "invoker_ghost_walk",
        "invoker_tornado",
        "invoker_emp",
        "invoker_alacrity",
        "invoker_chaos_meteor",
        "invoker_sun_strike",
        "invoker_forge_spirit",
        "invoker_ice_wall",
        "invoker_deafening_blast",
    ]
    for key in invoked:
        spell = data.get(key)
        assert spell is not None, f"missing invoked spell {key}"
        assert spell.get("desc"), f"{key}: empty desc"

    # Spot checks: reagent-scaled mechanics must be mentioned in prose, not
    # only in attrib keys, since the LLM extractor sees only the prose.
    assert "exort" in data["invoker_sun_strike"]["desc"].lower()
    assert "quas" in data["invoker_cold_snap"]["desc"].lower()
    assert "silence" not in data["invoker_alacrity"]["desc"].lower()  # sanity
    assert "armor" in data["invoker_forge_spirit"]["desc"].lower()
