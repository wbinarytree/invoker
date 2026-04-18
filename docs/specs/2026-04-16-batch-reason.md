# Batch Reason Generation

> Superseded on 2026-04-18 by the KG-first direction. Keep only as implementation history for the old stat-selected pair reasoning path. Active docs now start at [docs/CURRENT_DIRECTION.md](/Users/yaoda/Projects/invoker/docs/CURRENT_DIRECTION.md:1).

**Date:** 2026-04-16  
**Status:** approved  
**Scope:** small; new prompts, updated `reason.py` and `orchestrator.py`

---

## Problem

`run_for_hero` makes one LLM call per synergy/counter edge. With ~126 high-confidence
edges per hero (matchup data covers the full player pool), a two-hero dev run costs ~252
calls — over 12× the 20/day free-tier limit before a single cache entry lands.

---

## Solution

Replace the per-edge calls with **one batch call per hero** that covers all edges of both
relations in a single prompt. Token cost grows; call count collapses to:

```
2 heroes × 1 extract  =  2 calls
2 heroes × 1 batch    =  2 calls
─────────────────────────────────
Total                 =  4 calls
```

A `max_edges` cap (top N by `|score|`, applied separately to synergies and counters before
batching) keeps the prompt token-compact and focuses the KG on the highest-signal edges.
Default: **20 per relation**. Full bootstrap changes only this number, not the call structure.

---

## Prompt: `edge_reasons_batch` (new, replaces `synergy_reason` + `counter_reason`)

Single prompt handles both relations. Hero A name and tags appear once in the header.
Each item in the input list carries hero B info, the relation type, score, and game count.

Output: a JSON array parallel to the input list — same order, same length.

```
[{"hero_b_id": <int>, "reason": "<string>"}]
```

Bump version to 1 on creation. Retire `synergy_reason.md` and `counter_reason.md`.

---

## `reason.py` changes

Remove `generate_synergy_reason`, `generate_counter_reason`, `_render_and_call`, `ReasonInput`.

Add:

```python
@dataclass
class EdgeReasonInput:
    hero_b_id: int
    hero_b_name: str
    hero_b_tags: list[str]
    relation: str          # "synergy" | "counter"
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

def generate_reasons_batch(inp: BatchReasonInput, client: LLMClient) -> list[EdgeReasonOutput]:
    ...
```

Response validation: returned list must be same length as input; each item must have
`hero_b_id` and `reason`; `hero_b_id` values must match the input set.

`validate_grounding` is unchanged — called per output item against hero A tags + the
corresponding hero B tags (looked up from the input).

---

## `orchestrator.py` changes

Replace the per-edge loop with:

1. Cap synergies and counters to top `max_edges` by `|score|` (lists are already sorted).
2. Build one `BatchReasonInput` combining both relations.
3. Call `generate_reasons_batch` once.
4. Fan results back into `reasons_by_edge` dict keyed by `(relation, hero_b_id)`.
5. `run_for_hero` gains `max_edges: int = 20` parameter.

---

## What does NOT change

- `validate_grounding` logic
- Cache layer — batch call is cached by the same key scheme (model + prompt_version + rendered prompt)
- `extract_mechanical` — unaffected
- Output schema (`HeroDerived`) — reasons land in the same `StatEdge.reason` field
