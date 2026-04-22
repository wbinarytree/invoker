from pathlib import Path

from invoker.graph import build_graph, cache_graph
from invoker.kb import KnowledgeBase
from invoker.kg.reader import write_relations
from invoker.paths import relations_file
from invoker.pipeline.manifest import build_manifest, write_manifest
from invoker.pipeline.summarize import write_summary
from invoker.pipeline.writer import write_hero

from ..support.factories import make_hero, make_relation


def _setup(tmp_path: Path):
    h = make_hero()
    write_hero(tmp_path, "7.41b", h)
    rel = make_relation()
    write_relations(
        relations_file(tmp_path, "7.41b"),
        [rel],
        source_patch="7.41b",
        generated_at="2026-04-22T00:00:00Z",
    )
    from invoker.kg.reader import RelationsReader

    write_summary(tmp_path, h, RelationsReader([rel]))
    m = build_manifest(tmp_path, "7.41b", [h.hero_id], complete=True)
    write_manifest(tmp_path, m)
    g = build_graph(tmp_path, "7.41b", [h.hero_id])
    cache_graph(tmp_path, "7.41b", g)
    return h


def test_kb_hero_lookup(tmp_path: Path):
    _setup(tmp_path)
    kb = KnowledgeBase(patch="7.41b", bracket="pro", data_dir=tmp_path)
    assert kb.hero(28).localized_name == "Slardar"
    assert kb.hero("Slardar").hero_id == 28


def test_kb_synergies_filtered_by_confidence(tmp_path: Path):
    _setup(tmp_path)
    kb = KnowledgeBase(patch="7.41b", data_dir=tmp_path)
    assert len(kb.synergies(28, min_confidence="med")) == 1
    assert len(kb.synergies(28, min_confidence="high")) == 0


def test_kb_summary(tmp_path: Path):
    _setup(tmp_path)
    kb = KnowledgeBase(patch="7.41b", data_dir=tmp_path)
    assert "Slardar" in kb.summary(28)
