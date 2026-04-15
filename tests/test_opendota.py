import json
from pathlib import Path

FIXTURE = Path(__file__).parent / "fixtures" / "opendota" / "heroes.json"


def test_heroes_fixture_shape():
    data = json.loads(FIXTURE.read_text())
    assert isinstance(data, list)
    assert len(data) >= 3
    h = data[0]
    for key in ("id", "localized_name", "name", "primary_attr", "roles"):
        assert key in h, f"missing {key}"
