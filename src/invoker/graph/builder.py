from __future__ import annotations

import pickle
from pathlib import Path

import networkx as nx

from invoker.paths import graph_file
from invoker.pipeline.writer import read_hero


def build_graph(data_dir: Path, patch: str, hero_ids: list[int]) -> nx.MultiDiGraph:
    g: nx.MultiDiGraph = nx.MultiDiGraph()
    for hid in hero_ids:
        h = read_hero(data_dir, patch, hid)
        g.add_node(("hero", h.hero_id), name=h.localized_name, patch=patch)
        for tag in h.functional_tags:
            g.add_node(("tag", tag), kind="tag")
            g.add_edge(("hero", h.hero_id), ("tag", tag), relation="has_tag")
        for bracket, edges in h.synergies.items():
            for e in edges:
                if e.score is None:
                    continue
                g.add_edge(
                    ("hero", h.hero_id),
                    ("hero", e.hero_id),
                    relation="synergy",
                    bracket=bracket,
                    score=e.score,
                    games=e.games,
                    confidence=e.confidence,
                )
        for bracket, edges in h.counters.items():
            for e in edges:
                if e.score is None:
                    continue
                g.add_edge(
                    ("hero", h.hero_id),
                    ("hero", e.hero_id),
                    relation="counter",
                    bracket=bracket,
                    score=e.score,
                    games=e.games,
                    confidence=e.confidence,
                )
    return g


def cache_graph(data_dir: Path, patch: str, g: nx.MultiDiGraph) -> Path:
    path = graph_file(data_dir, patch)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as f:
        pickle.dump(g, f)
    return path


def load_graph(data_dir: Path, patch: str) -> nx.MultiDiGraph:
    path = graph_file(data_dir, patch)
    with path.open("rb") as f:
        return pickle.load(f)
