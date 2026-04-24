import json
from pathlib import Path

import pytest
import yaml

from invoker.kg.authoring import (
    AuthoredFactsValidationError,
    DraftFactsResult,
    HeroPromptContext,
    draft_facts,
    format_relations_for_hero,
    render_draft_facts_prompt,
    resolve_authored_file,
    validate_authored_payload,
)


def _pangolier_payload() -> dict:
    return {
        "hero_id": 120,
        "hero_slug": "pangolier",
        "localized_name": "Pangolier",
        "capabilities": [
            {
                "type": "mobility",
                "score": 0.9,
                "evidence": ["Swashbuckle and Shield Crash reposition quickly"],
            },
            {
                "type": "magic_burst",
                "score": 0.8,
                "evidence": ["Rolling Thunder creates burst windows"],
            },
        ],
        "requirements": [{"type": "needs_damage_followup", "score": 0.7}],
        "liabilities": [
            {
                "type": "weak_to_kiting",
                "score": 0.4,
                "evidence": ["If he cannot stay on top of targets, his impact drops"],
            }
        ],
        "targets": [
            {
                "type": "punishes_immobile_backline",
                "score": 0.8,
                "evidence": ["Rolling Thunder punishes backliners that cannot reposition"],
            }
        ],
        "role_distribution": {"mid": 0.6, "offlane": 0.4},
        "provenance": {
            "authored_by": "human",
            "authored_at": "2026-04-22",
            "assist_model": None,
        },
    }


def test_render_draft_facts_prompt_includes_hero_context():
    text, version = render_draft_facts_prompt(
        HeroPromptContext(
            hero_id=120,
            hero_slug="pangolier",
            localized_name="Pangolier",
            internal_name="npc_dota_hero_pangolier",
            roles=["Nuker", "Escape"],
            abilities=[{"name": "Swashbuckle", "text": "Dash and strike enemies in line."}],
        )
    )
    assert version >= 1
    assert "Pangolier" in text
    assert "Swashbuckle" in text
    assert '"capabilities"' in text
    assert "Return JSON only." in text


def test_validate_authored_payload_rejects_unknown_vocab():
    payload = _pangolier_payload()
    payload["capabilities"][0]["type"] = "not_real"
    with pytest.raises(AuthoredFactsValidationError, match="not in the live vocabulary"):
        validate_authored_payload(payload)


def test_draft_facts_writes_prompt_then_yaml(monkeypatch, tmp_path: Path):
    context = HeroPromptContext(
        hero_id=120,
        hero_slug="pangolier",
        localized_name="Pangolier",
        internal_name="npc_dota_hero_pangolier",
        roles=["Nuker", "Escape"],
        abilities=[{"name": "Swashbuckle", "text": "Dash and strike enemies in line."}],
    )

    async def _fake_fetch_prompt_context(data_dir, hero, patch="authoring"):
        return context

    monkeypatch.setattr(
        "invoker.kg.authoring.fetch_prompt_context",
        _fake_fetch_prompt_context,
    )

    first = draft_facts(tmp_path, "pangolier")
    assert isinstance(first, DraftFactsResult)
    assert first.pending is True
    assert first.prompt_path.exists()
    assert first.response_path.exists()
    assert first.response_path.read_text() == ""

    first.response_path.write_text(yaml.safe_dump(_pangolier_payload(), sort_keys=False))

    second = draft_facts(tmp_path, "pangolier")
    assert second.pending is False
    assert second.authored_path is not None
    assert second.authored_path.exists()
    payload = yaml.safe_load(second.authored_path.read_text())
    assert payload["hero_slug"] == "pangolier"


def test_draft_facts_accepts_json_inside_fences(monkeypatch, tmp_path: Path):
    context = HeroPromptContext(
        hero_id=120,
        hero_slug="pangolier",
        localized_name="Pangolier",
        internal_name="npc_dota_hero_pangolier",
        roles=["Nuker", "Escape"],
        abilities=[{"name": "Swashbuckle", "text": "Dash and strike enemies in line."}],
    )

    async def _fake_fetch_prompt_context(data_dir, hero, patch="authoring"):
        return context

    monkeypatch.setattr(
        "invoker.kg.authoring.fetch_prompt_context",
        _fake_fetch_prompt_context,
    )

    pending = draft_facts(tmp_path, "pangolier")
    pending.response_path.write_text(
        "Here is the draft:\n```json\n"
        + json.dumps(_pangolier_payload(), indent=2)
        + "```"
    )

    written = draft_facts(tmp_path, "pangolier")
    assert written.pending is False
    assert written.authored_path is not None


def test_resolve_authored_file_matches_name_and_id(tmp_path: Path):
    root = tmp_path / "authored"
    root.mkdir()
    path = root / "pangolier.yaml"
    path.write_text(yaml.safe_dump(_pangolier_payload(), sort_keys=False))
    assert resolve_authored_file(tmp_path, "pangolier") == path
    assert resolve_authored_file(tmp_path, "120") == path
    assert resolve_authored_file(tmp_path, "Pangolier") == path


def test_show_relations_formats_inferred_pairs(tmp_path: Path):
    root = tmp_path / "authored"
    root.mkdir()

    pangolier = _pangolier_payload()
    root.joinpath("pangolier.yaml").write_text(yaml.safe_dump(pangolier, sort_keys=False))

    slardar = {
        "hero_id": 28,
        "hero_slug": "slardar",
        "localized_name": "Slardar",
        "capabilities": [
            {
                "type": "armor_reduction",
                "score": 0.9,
                "evidence": ["Corrosive Haze reduces armor heavily"],
            }
        ],
        "requirements": [],
        "liabilities": [],
        "targets": [],
        "role_distribution": {"offlane": 1.0},
        "provenance": {
            "authored_by": "human",
            "authored_at": "2026-04-22",
            "assist_model": None,
        },
    }
    root.joinpath("slardar.yaml").write_text(yaml.safe_dump(slardar, sort_keys=False))

    text = format_relations_for_hero(tmp_path, "pangolier")
    assert "Relations for Pangolier" in text
    assert "Inbound" in text
    assert "enabler_payoff" in text
