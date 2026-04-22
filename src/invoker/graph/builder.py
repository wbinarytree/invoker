from __future__ import annotations

import pickle
from pathlib import Path

import networkx as nx

from invoker.kg.reader import RelationsReader
from invoker.paths import graph_file, relations_file
from invoker.pipeline.writer import read_hero


def build_graph(data_dir: Path, patch: str, hero_ids: list[int]) -> nx.MultiDiGraph:
    g: nx.MultiDiGraph = nx.MultiDiGraph()
    hero_id_set = set(hero_ids)

    for hid in hero_ids:
        hero = read_hero(data_dir, patch, hid)
        g.add_node(("hero", hero.hero_id), name=hero.localized_name, patch=patch)
        for bucket_name in ("capabilities", "requirements", "liabilities", "targets"):
            for feature in getattr(hero, bucket_name):
                g.add_node(("feature", feature.type), kind="feature")
                g.add_edge(
                    ("hero", hero.hero_id),
                    ("feature", feature.type),
                    relation="has_feature",
                    bucket=bucket_name,
                    score=feature.score,
                )

    rel_path = relations_file(data_dir, patch)
    if rel_path.exists():
        reader = RelationsReader.load(rel_path)
        for rel in reader.all():
            if rel.from_hero_id not in hero_id_set and rel.to_hero_id not in hero_id_set:
                continue
            g.add_node(("hero", rel.from_hero_id), patch=patch)
            g.add_node(("hero", rel.to_hero_id), patch=patch)
            g.add_edge(
                ("hero", rel.from_hero_id),
                ("hero", rel.to_hero_id),
                relation=rel.relation_kind,
                relation_id=rel.relation_id,
                pattern=rel.pattern,
                cohort=rel.cohort,
                source_feature=rel.source_feature,
                target_feature=rel.target_feature,
                confidence=rel.confidence,
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
