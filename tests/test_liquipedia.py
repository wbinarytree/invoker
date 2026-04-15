import json
from pathlib import Path

from invoker.sources.liquipedia import LiquipediaFetcher

FIXTURE = Path(__file__).parent / "fixtures" / "liquipedia" / "slardar.json"


def test_extract_roles():
    page = json.loads(FIXTURE.read_text())
    roles = LiquipediaFetcher.extract_roles(page)
    assert "Initiator" in roles or "Disabler" in roles, f"expected role labels, got {roles}"


def test_extract_abilities_non_empty():
    page = json.loads(FIXTURE.read_text())
    abilities = LiquipediaFetcher.extract_abilities(page)
    assert abilities, "expected at least one ability parsed"
    assert all("name" in a and "text" in a for a in abilities)
