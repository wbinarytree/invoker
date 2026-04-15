from pathlib import Path

from invoker.graph import build_graph, cache_graph
from invoker.kb import KnowledgeBase
from invoker.pipeline.manifest import build_manifest, write_manifest
from invoker.pipeline.summarize import write_summary
from invoker.pipeline.validators import ValidationContext, validate_hero
from invoker.pipeline.writer import write_hero
from tests.test_summarize import _hero


def test_full_pipeline_on_one_hero(tmp_path: Path):
    h = _hero()

    write_hero(tmp_path, "7.41b", h)

    ctx = ValidationContext(roster_hero_ids={28, 120, 96})
    validate_hero(h, ctx)

    summary_path = write_summary(tmp_path, h, "pro")
    assert summary_path.exists()

    m = build_manifest(tmp_path, "7.41b", [h.hero_id], ["pro"], complete=True)
    write_manifest(tmp_path, m)

    g = build_graph(tmp_path, "7.41b", [h.hero_id])
    cache_graph(tmp_path, "7.41b", g)

    kb = KnowledgeBase(patch="7.41b", bracket="pro", data_dir=tmp_path)
    assert kb.hero(28).localized_name == "Slardar"
    assert len(kb.synergies(28, min_confidence="med")) == 1
    assert "Slardar" in kb.summary(28)
