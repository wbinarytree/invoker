from __future__ import annotations

import json
from dataclasses import dataclass

from invoker.llm import LLMClient
from invoker.prompts import load


@dataclass
class ReasonInput:
    hero_a_id: int
    hero_a_name: str
    hero_a_tags: list[str]
    hero_b_id: int
    hero_b_name: str
    hero_b_tags: list[str]
    score: float
    games: int


@dataclass
class ReasonOutput:
    reason: str
    model: str
    prompt_version: int


def _render_and_call(prompt_name: str, inp: ReasonInput, client: LLMClient) -> ReasonOutput:
    prompt = load(prompt_name)
    rendered = prompt.render(
        HERO_A_NAME=inp.hero_a_name,
        HERO_A_TAGS=", ".join(inp.hero_a_tags) or "(no tags)",
        HERO_B_NAME=inp.hero_b_name,
        HERO_B_TAGS=", ".join(inp.hero_b_tags) or "(no tags)",
        SCORE=f"{inp.score:+.2f}",
        GAMES=str(inp.games),
    )
    response = client.complete_json(rendered, prompt_version=prompt.version)
    parsed = json.loads(response.text)
    return ReasonOutput(
        reason=parsed["reason"], model=response.model, prompt_version=response.prompt_version
    )


def generate_synergy_reason(inp: ReasonInput, client: LLMClient) -> ReasonOutput:
    return _render_and_call("synergy_reason", inp, client)


def generate_counter_reason(inp: ReasonInput, client: LLMClient) -> ReasonOutput:
    return _render_and_call("counter_reason", inp, client)


class ReasonNotGroundedError(ValueError):
    pass


def validate_grounding(reason: str, a_tags: list[str], b_tags: list[str]) -> None:
    """Reject a reason that mentions no tag from either hero."""
    text = reason.lower().replace("_", " ")
    all_tags = set(a_tags) | set(b_tags)
    for tag in all_tags:
        if tag.replace("_", " ") in text or tag in reason.lower():
            return
    raise ReasonNotGroundedError(
        f"Reason cites no tag from either hero. Reason: {reason!r}. Tags: {sorted(all_tags)}"
    )
