import asyncio
import json
from pathlib import Path

from invoker.sources.stratz import StratzFetcher, flatten_edges

from ...support import FIXTURES_DIR

FIXTURE = FIXTURES_DIR / "stratz" / "pangolier_matchup.json"


def test_missing_token_returns_none(tmp_path: Path):
    fetcher = StratzFetcher(cache_root=tmp_path, patch="test", token=None)
    result = asyncio.run(fetcher.synergies(28))
    assert result is None
    asyncio.run(fetcher.close())


def test_flatten_edges_from_fixture():
    raw = json.loads(FIXTURE.read_text())
    edges = flatten_edges(raw, hero_id=120)

    assert len(edges) > 0, "expected edges from fixture"

    # All edges must have required fields
    for e in edges:
        assert "heroId1" in e
        assert "heroId2" in e
        assert "synergy" in e
        assert "matchCount" in e

    # with-edges have positive synergy; vs-edges have negative
    with_syns = [e["synergy"] for e in edges if e["synergy"] > 0]
    vs_syns = [e["synergy"] for e in edges if e["synergy"] < 0]
    assert with_syns, "expected at least one positive (with) edge"
    assert vs_syns, "expected at least one negative (vs/counter) edge"

    # heroId1 is always Pangolier (120) since we queried for hero_id=120
    assert all(e["heroId1"] == 120 for e in edges)


def test_flatten_edges_wrong_hero_returns_empty():
    raw = json.loads(FIXTURE.read_text())
    edges = flatten_edges(raw, hero_id=999)
    assert edges == []
