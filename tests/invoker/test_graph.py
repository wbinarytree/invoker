from pathlib import Path

from invoker.graph import build_graph, cache_graph, load_graph
from invoker.pipeline.writer import write_hero

from ..support.factories import make_hero


def test_graph_build_roundtrip(tmp_path: Path):
    h = make_hero()
    write_hero(tmp_path, "7.41b", h)
    g = build_graph(tmp_path, "7.41b", [h.hero_id])
    cache_graph(tmp_path, "7.41b", g)
    loaded = load_graph(tmp_path, "7.41b")
    assert ("hero", 28) in loaded.nodes
    assert ("tag", "armor_reduction") in loaded.nodes
    edges = list(loaded.out_edges(("hero", 28), data=True))
    assert any(e[2].get("relation") == "synergy" for e in edges)
