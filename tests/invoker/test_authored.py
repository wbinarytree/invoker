from pathlib import Path

from invoker.kg import load_hero_facts


def test_load_hero_facts_coerces_string_evidence(tmp_path: Path):
    path = tmp_path / "pangolier.yaml"
    path.write_text(
        """
hero_id: 120
hero_slug: pangolier
localized_name: Pangolier
capabilities:
  - type: mobility
    score: 0.9
    evidence:
      - Swashbuckle dashes through terrain
requirements:
  - type: needs_damage_followup
    score: 0.7
liabilities:
  - type: weak_to_silence
    score: 0.6
targets:
  - type: punishes_immobile_backline
    score: 0.8
role_distribution:
  mid: 0.6
  offlane: 0.4
provenance:
  authored_by: human
  authored_at: 2026-04-22
  assist_model: null
""".strip()
    )

    profile = load_hero_facts(path, source_patch="7.41b")

    assert profile.hero_slug == "pangolier"
    assert profile.capabilities[0].evidence[0].text == "Swashbuckle dashes through terrain"
    assert profile.targets[0].type == "punishes_immobile_backline"
    assert profile.provenance.authored_by == "human"
