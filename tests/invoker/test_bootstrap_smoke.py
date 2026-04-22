from pathlib import Path

from invoker.kb import KnowledgeBase
from invoker.kg.authored import load_hero_facts
from invoker.pipeline.orchestrator import run_bootstrap


def test_full_pipeline_on_one_hero(tmp_path: Path):
    authored = tmp_path / "authored"
    authored.mkdir()
    pangolier = authored / "pangolier.yaml"
    pangolier.write_text(
        """
hero_id: 120
hero_slug: pangolier
localized_name: Pangolier
capabilities:
  - type: magic_burst
    score: 0.8
    evidence: ["Rolling Thunder plus Swashbuckle create burst windows"]
  - type: mobility
    score: 0.9
    evidence: ["Swashbuckle and Shield Crash reposition quickly"]
targets:
  - type: punishes_immobile_backline
    score: 0.8
provenance:
  authored_by: human
  authored_at: 2026-04-22
  assist_model: null
""".strip()
    )

    profiles = load_hero_facts(pangolier, source_patch="7.41b")
    assert profiles.hero_id == 120

    run_bootstrap(tmp_path, "7.41b", "invoker@test")

    kb = KnowledgeBase(patch="7.41b", data_dir=tmp_path)
    assert kb.hero(120).localized_name == "Pangolier"
    assert "Pangolier" in kb.summary(120)
