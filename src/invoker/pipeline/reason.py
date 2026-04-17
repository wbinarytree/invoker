from __future__ import annotations

from dataclasses import dataclass

from pydantic import BaseModel, TypeAdapter

from invoker.llm import LLMClient
from invoker.prompts import load


@dataclass
class EdgeReasonInput:
    hero_b_id: int
    hero_b_name: str
    hero_b_tags: list[str]
    relation: str  # "synergy" | "counter"
    score: float
    games: int


@dataclass
class BatchReasonInput:
    hero_a_name: str
    hero_a_tags: list[str]
    edges: list[EdgeReasonInput]


@dataclass
class EdgeReasonOutput:
    hero_b_id: int
    reason: str
    model: str
    prompt_version: int


class ReasonNotGroundedError(ValueError):
    pass


class _EdgeReasonItem(BaseModel):
    hero_b_id: int
    reason: str


_REASON_BATCH_ADAPTER: TypeAdapter[list[_EdgeReasonItem]] = TypeAdapter(list[_EdgeReasonItem])


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


def _format_edges(edges: list[EdgeReasonInput]) -> str:
    lines: list[str] = []
    for e in edges:
        tags = ", ".join(e.hero_b_tags) or "(no tags)"
        lines.append(
            f"- hero_b_id={e.hero_b_id} name={e.hero_b_name} tags=[{tags}]"
            f" relation={e.relation} score={e.score:+.3f} games={e.games}"
        )
    return "\n".join(lines)


def generate_reasons_batch(
    inp: BatchReasonInput, client: LLMClient
) -> list[EdgeReasonOutput]:
    """
    Generate reasons for all edges in a single LLM call.

    Returns one EdgeReasonOutput per input edge, in input order.
    Raises ValueError if the response is malformed or lengths mismatch.
    """
    prompt = load("edge_reasons_batch")
    rendered = prompt.render(
        HERO_A_NAME=inp.hero_a_name,
        HERO_A_TAGS=", ".join(inp.hero_a_tags) or "(no tags)",
        EDGES=_format_edges(inp.edges),
    )
    response = client.complete_json(rendered, prompt_version=prompt.version, schema=list[_EdgeReasonItem])
    parsed = _REASON_BATCH_ADAPTER.validate_json(response.text)

    if len(parsed) != len(inp.edges):
        raise ValueError(
            f"Response length {len(parsed)} != input length {len(inp.edges)}"
        )

    expected_ids = {e.hero_b_id for e in inp.edges}
    outputs: list[EdgeReasonOutput] = []
    for item in parsed:
        if item.hero_b_id not in expected_ids:
            raise ValueError(f"Unexpected hero_b_id {item.hero_b_id} in response")
        outputs.append(
            EdgeReasonOutput(
                hero_b_id=item.hero_b_id,
                reason=item.reason,
                model=response.model,
                prompt_version=response.prompt_version,
            )
        )
    return outputs
