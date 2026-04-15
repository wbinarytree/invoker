import json

import pytest

from invoker.llm.client import LLMResponse
from invoker.pipeline.reason import (
    ReasonInput,
    ReasonNotGroundedError,
    generate_synergy_reason,
    validate_grounding,
)


class CannedClient:
    def __init__(self, reason: str) -> None:
        self.reason = reason
        self.model_name = "canned"

    def complete_json(self, prompt: str, *, prompt_version: int) -> LLMResponse:
        return LLMResponse(
            text=json.dumps({"reason": self.reason}),
            model="canned",
            prompt_version=prompt_version,
        )


def test_synergy_reason_generates():
    inp = ReasonInput(
        hero_a_id=28,
        hero_a_name="Slardar",
        hero_a_tags=["armor_reduction"],
        hero_b_id=120,
        hero_b_name="Pangolier",
        hero_b_tags=["physical_damage_amplifier"],
        score=0.08,
        games=50,
    )
    out = generate_synergy_reason(
        inp, CannedClient("Armor reduction stacks with physical damage amplifier.")
    )
    assert "armor" in out.reason.lower()


def test_validate_grounding_accepts_tag_mention():
    validate_grounding("armor reduction stacks", ["armor_reduction"], [])


def test_validate_grounding_rejects_no_mention():
    with pytest.raises(ReasonNotGroundedError):
        validate_grounding(
            "they both win fights", ["armor_reduction"], ["physical_damage_amplifier"]
        )
