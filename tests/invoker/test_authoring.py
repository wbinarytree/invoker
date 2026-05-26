import json
from pathlib import Path

import pytest
import yaml

from invoker.kg.ability_context import AbilityContext, AttribEntry, TalentContext
from invoker.kg.authoring import (
    AuthoredFactsValidationError,
    DraftFactsResult,
    draft_facts,
    format_relations_for_hero,
    promote_authored_draft,
    render_draft_facts_prompt,
    resolve_authored_file,
    validate_authored_payload,
)
from invoker.kg.hero_context import HeroContextPacket, HeroIdentityContext
from invoker.kg.hero_stats_context import HeroStatsContext, StatEntry


def _pangolier_packet() -> HeroContextPacket:
    return HeroContextPacket(
        patch="authoring",
        hero=HeroIdentityContext(
            hero_id=120,
            hero_slug="pangolier",
            localized_name="Pangolier",
            primary_attr="agi",
            attack_type="Melee",
            roles=["Nuker", "Escape"],
        ),
        stats=HeroStatsContext(
            base_str=StatEntry(value=22.0, percentile=0.5, band="average"),
            base_agi=StatEntry(value=24.0, percentile=0.78, band="high"),
            base_int=StatEntry(value=18.0, percentile=0.4, band="low"),
            str_gain=StatEntry(value=2.6, percentile=0.5, band="average"),
            agi_gain=StatEntry(value=3.4, percentile=0.85, band="very_high"),
            int_gain=StatEntry(value=1.8, percentile=0.3, band="low"),
            base_armor=StatEntry(value=2.0, percentile=0.5, band="average"),
            base_attack_min=StatEntry(value=26.0, percentile=0.4, band="average"),
            base_attack_max=StatEntry(value=32.0, percentile=0.4, band="average"),
            base_attack_speed=StatEntry(value=100.0, percentile=0.5, band="average"),
            base_attack_time=StatEntry(value=1.7, percentile=0.5, band="average"),
            attack_animation_point=StatEntry(value=0.33, percentile=0.4, band="average"),
            attack_acquisition_range=StatEntry(value=600.0, percentile=0.5, band="average"),
            attack_range=StatEntry(value=150.0, percentile=0.2, band="low"),
            move_speed=StatEntry(value=305.0, percentile=0.7, band="high"),
            primary_attr="agi",
            attack_type="Melee",
        ),
        abilities=[
            AbilityContext(
                internal_name="pangolier_swashbuckle",
                name="Swashbuckle",
                source="base_ability",
                behavior=["Point Target"],
                damage_type="Physical",
                pierces_debuff_immunity=False,
                dispellable=None,
                description="Dash and strike enemies in line.",
                attribs=[AttribEntry(header="DAMAGE:", value=["80", "120", "160", "200"])],
                cast_range=["575", "650", "725", "800"],
                timing={"cast_point": "0.15"},
                mana_cost="50",
                cooldown="14",
            ),
        ],
        talents=[
            TalentContext(
                internal_name="special_bonus_unique_pangolier_5",
                name="Rolling Thunder Disarm",
                level=4,
            ),
        ],
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
    text, version = render_draft_facts_prompt(_pangolier_packet())
    assert version >= 6
    assert "Pangolier" in text
    assert "Swashbuckle" in text
    assert "Live vocabulary JSON" in text
    assert "Ability context JSON" in text
    assert "Hero stats JSON" in text
    assert "Dota mechanism primer" in text
    assert "Talent context JSON" in text
    assert '"description": "Dash and strike enemies in line."' in text
    assert '"source": "base_ability"' in text
    assert '"cast_range": [' in text
    assert '"575"' in text
    assert '"timing": {' in text
    assert '"cast_point": "0.15"' in text
    assert '"band": "very_high"' in text
    assert '"base_attack_min": {' in text
    assert '"base_attack_max": {' in text
    assert '"base_attack_speed": {' in text
    assert '"base_attack_time": {' in text
    assert '"attack_animation_point": {' in text
    assert '"attack_acquisition_range": {' in text
    assert '"percentile":' in text
    assert "Rolling Thunder Disarm" in text
    assert '"capabilities"' in text
    assert '"vocabulary_gaps"' in text
    assert '"role_distribution"' not in text
    assert "Return JSON only." in text
    assert "Use only the live vocabulary terms" in text
    assert "talents are conditional" in text
    assert "Scepter, Shard" in text
    # Examples in vocab are trimmed to hero_slug strings, not freeform evidence dicts.
    assert '"reviewed save discussion"' not in text


def test_validate_authored_payload_rejects_unknown_vocab():
    payload = _pangolier_payload()
    payload["capabilities"][0]["type"] = "not_real"
    with pytest.raises(AuthoredFactsValidationError, match="not in the live vocabulary"):
        validate_authored_payload(payload)


def test_validate_authored_payload_rejects_unknown_top_level_keys():
    payload = _pangolier_payload()
    payload["notes"] = "do not silently persist free-form notes"
    with pytest.raises(AuthoredFactsValidationError, match="unknown top-level keys"):
        validate_authored_payload(payload)


def test_draft_facts_writes_prompt_then_yaml(monkeypatch, tmp_path: Path):
    packet = _pangolier_packet()

    async def _fake_build_hero_context(game_data_dir, hero, *, patch="authoring"):
        return packet

    monkeypatch.setattr(
        "invoker.kg.authoring.build_hero_context",
        _fake_build_hero_context,
    )

    first = draft_facts(tmp_path, tmp_path / "game", "pangolier")
    assert isinstance(first, DraftFactsResult)
    assert first.pending is True
    assert first.prompt_path.exists()
    assert first.response_path.exists()
    assert first.response_path.read_text() == ""

    first.response_path.write_text(json.dumps(_pangolier_payload(), indent=2))

    second = draft_facts(tmp_path, tmp_path / "game", "pangolier")
    assert second.pending is False
    assert second.authored_path is not None
    assert second.authored_path.exists()
    payload = yaml.safe_load(second.authored_path.read_text())
    assert payload["hero_slug"] == "pangolier"
    assert "vocabulary_gaps" not in payload


def test_draft_facts_records_vocabulary_gaps_separately(monkeypatch, tmp_path: Path):
    packet = _pangolier_packet()

    async def _fake_build_hero_context(game_data_dir, hero, *, patch="authoring"):
        return packet

    monkeypatch.setattr(
        "invoker.kg.authoring.build_hero_context",
        _fake_build_hero_context,
    )

    pending = draft_facts(tmp_path, tmp_path / "game", "pangolier")
    payload = _pangolier_payload()
    payload["vocabulary_gaps"] = [
        {
            "bucket": "capabilities",
            "concept": "spell immunity piercing movement disruption",
            "why_needed": (
                "the current vocabulary has mobility and stun but not immunity-piercing disruption"
            ),
            "evidence": "Rolling Thunder can keep disrupting while rolling",
            "candidate_term": "piercing_disruption",
        }
    ]
    pending.response_path.write_text(json.dumps(payload, indent=2))

    written = draft_facts(tmp_path, tmp_path / "game", "pangolier")

    assert written.pending is False
    assert written.gaps_path is not None
    assert written.gap_count == 1
    gaps = yaml.safe_load(written.gaps_path.read_text())
    assert gaps["gaps"][0]["hero_slug"] == "pangolier"
    assert gaps["gaps"][0]["status"] == "proposed"
    assert written.authored_path is not None
    assert "vocabulary_gaps" not in yaml.safe_load(written.authored_path.read_text())


def test_draft_facts_accepts_json_inside_fences(monkeypatch, tmp_path: Path):
    packet = _pangolier_packet()

    async def _fake_build_hero_context(game_data_dir, hero, *, patch="authoring"):
        return packet

    monkeypatch.setattr(
        "invoker.kg.authoring.build_hero_context",
        _fake_build_hero_context,
    )

    pending = draft_facts(tmp_path, tmp_path / "game", "pangolier")
    pending.response_path.write_text(
        "Here is the draft:\n```json\n" + json.dumps(_pangolier_payload(), indent=2) + "```"
    )

    written = draft_facts(tmp_path, tmp_path / "game", "pangolier")
    assert written.pending is False
    assert written.authored_path is not None


def test_promote_authored_draft_validates_and_backs_up(tmp_path: Path):
    root = tmp_path / "authored"
    root.mkdir()
    current = _pangolier_payload()
    current["capabilities"][0]["score"] = 0.2
    draft = _pangolier_payload()
    draft["capabilities"][0]["score"] = 0.9
    root.joinpath("pangolier.yaml").write_text(yaml.safe_dump(current, sort_keys=False))
    root.joinpath("pangolier.draft.yaml").write_text(yaml.safe_dump(draft, sort_keys=False))

    result = promote_authored_draft(tmp_path, "pangolier")

    promoted = yaml.safe_load(root.joinpath("pangolier.yaml").read_text())
    assert promoted["capabilities"][0]["score"] == 0.9
    assert result.backup_path is not None
    assert result.backup_path.exists()
    backed_up = yaml.safe_load(result.backup_path.read_text())
    assert backed_up["capabilities"][0]["score"] == 0.2
    assert root.joinpath("pangolier.draft.yaml").exists()


def test_promote_authored_draft_can_delete_draft(tmp_path: Path):
    root = tmp_path / "authored"
    root.mkdir()
    root.joinpath("pangolier.yaml").write_text(
        yaml.safe_dump(_pangolier_payload(), sort_keys=False)
    )
    root.joinpath("pangolier.draft.yaml").write_text(
        yaml.safe_dump(_pangolier_payload(), sort_keys=False)
    )

    result = promote_authored_draft(tmp_path, "pangolier", delete_draft=True)

    assert result.draft_deleted is True
    assert not root.joinpath("pangolier.draft.yaml").exists()


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
            },
            {
                "type": "reliable_stun",
                "score": 0.8,
                "evidence": ["Slithereen Crush stuns nearby enemies"],
            },
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
    assert "Slardar (28) -> synergy" in text
    assert "setup_followup" in text
