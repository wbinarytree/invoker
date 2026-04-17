import json

import pytest

from invoker.llm.client import LLMResponse
from invoker.pipeline.reason import (
    BatchReasonInput,
    EdgeReasonInput,
    ReasonNotGroundedError,
    generate_reasons_batch,
    validate_grounding,
)


class CannedClient:
    model_name = "canned"

    def __init__(self, payload: list[dict]) -> None:
        self._text = json.dumps(payload)

    def generate_json(
        self,
        prompt: str,
        *,
        prompt_version: int,
        schema: object | None = None,
        cache_tag: str | None = None,
    ) -> LLMResponse:
        return LLMResponse(text=self._text, model="canned", prompt_version=prompt_version)


def _make_batch(edges: list[tuple[int, str, str]]) -> BatchReasonInput:
    """edges: (hero_b_id, relation, hero_b_name)"""
    return BatchReasonInput(
        hero_a_name="Slardar",
        hero_a_tags=["armor_reduction", "single_target_disable"],
        edges=[
            EdgeReasonInput(
                hero_b_id=hid,
                hero_b_name=name,
                hero_b_tags=["physical_carry"],
                relation=rel,
                score=0.1,
                games=100,
            )
            for hid, rel, name in edges
        ],
    )


def test_batch_reason_generates():
    inp = _make_batch([(120, "synergy", "Pangolier")])
    payload = [{"hero_b_id": 120, "reason": "Armor reduction stacks with physical carry."}]
    out = generate_reasons_batch(inp, CannedClient(payload))
    assert len(out) == 1
    assert out[0].hero_b_id == 120
    assert "armor" in out[0].reason.lower()


def test_batch_reason_multiple_edges():
    inp = _make_batch([(120, "synergy", "Pangolier"), (1, "counter", "Anti-Mage")])
    payload = [
        {"hero_b_id": 120, "reason": "Armor reduction stacks with physical carry."},
        {"hero_b_id": 1, "reason": "Single target disable catches Anti-Mage."},
    ]
    out = generate_reasons_batch(inp, CannedClient(payload))
    assert len(out) == 2
    assert out[1].hero_b_id == 1


def test_batch_reason_length_mismatch_raises():
    inp = _make_batch([(120, "synergy", "Pangolier"), (1, "counter", "Anti-Mage")])
    payload = [{"hero_b_id": 120, "reason": "Only one item returned."}]
    with pytest.raises(ValueError, match="length"):
        generate_reasons_batch(inp, CannedClient(payload))


def test_batch_reason_wrong_ids_raises():
    inp = _make_batch([(120, "synergy", "Pangolier")])
    payload = [{"hero_b_id": 999, "reason": "Unknown hero."}]
    with pytest.raises(ValueError, match="Response hero_b_ids"):
        generate_reasons_batch(inp, CannedClient(payload))


def test_batch_reason_duplicate_id_raises():
    inp = _make_batch([(120, "synergy", "Pangolier"), (1, "counter", "Anti-Mage")])
    payload = [
        {"hero_b_id": 120, "reason": "First."},
        {"hero_b_id": 120, "reason": "Duplicate."},
    ]
    with pytest.raises(ValueError, match="Response hero_b_ids"):
        generate_reasons_batch(inp, CannedClient(payload))


def test_validate_grounding_accepts_tag_mention():
    validate_grounding("armor reduction stacks", ["armor_reduction"], [])


def test_validate_grounding_rejects_no_mention():
    with pytest.raises(ReasonNotGroundedError):
        validate_grounding(
            "they both win fights", ["armor_reduction"], ["physical_damage_amplifier"]
        )
