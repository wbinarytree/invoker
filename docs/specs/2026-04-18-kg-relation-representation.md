# KG-Oriented Hero Relation Representation

**Date:** 2026-04-18
**Status:** draft — for review and discussion
**Scope:** architecture direction; no code implied
**Supersedes in spirit:** the narrow "stats-first explanation" interpretation of Phase 1.2

---

## Purpose

This note captures the current conclusion from reviewing Phase 1.2 against the actual project goal.

The goal of Invoker is not to produce lightly-explained STRATZ pair stats. The goal is to build a knowledge graph that can support a strong drafting agent operating with the mindset of a professional Dota team.

That changes what the system should optimize for.

The system should treat hero-to-hero relationships as first-class knowledge objects:

- inferred from hero mechanics
- optionally validated or calibrated by stats
- stored in structured form
- rendered into text only as a downstream presentation layer

Text reasons are useful, but they are not the primary artifact.

---

## Current Pipeline

Today the relation path is effectively:

1. Use an LLM to extract per-hero functional tags from ability text.
2. Use STRATZ / OpenDota to choose candidate hero pairs.
3. Use an LLM to explain the chosen pairs with hero A and hero B tags.

In short:

`stats choose the pair -> tags explain the pair`

This is a reasonable bootstrap architecture for "explained stats," but it is not yet a strong hero-relation engine.

---

## Core Problem

The weakness is not "we use an LLM twice."

The weakness is that the relation layer is too weakly represented.

Right now:

- relation existence mostly comes from observed pair stats
- relation explanation mostly comes from flat mechanical tags
- there is no explicit structured object describing the mechanism of the relationship

This makes the system vulnerable to two failure modes:

1. **Missed relationships**
   If a real synergy/counter is not strong enough in STRATZ or not present in the candidate set, the system never reasons about it.

2. **Plausible but shallow explanations**
   The LLM can write a mechanically plausible sentence about a statistically selected pair without proving that the sentence captures the actual mechanism that drives the pair.

This is acceptable for a reporting layer.
It is weak for a KG that should power draft reasoning.

---

## What The Current Architecture Can And Cannot Do

### What it can do

The current architecture can support a modest Phase 1 goal:

- build patch-aware hero artifacts
- produce mechanically grounded explanations for strong observed pairs
- support manual inspection
- provide a base for later redesign

### What it cannot do well

It is not enough for the real project goal if that goal is:

- discover relationships from mechanics first
- represent why a pair works in a reusable structured form
- support draft reasoning beyond pairwise observed stats
- separate "mechanically inferred" from "statistically observed"

That stronger goal requires a better relation representation.

---

## Product Reframe

There are at least three possible products:

1. **Explained stats**
   "These pairs look strong in data, and here is a mechanically grounded explanation."

2. **Mechanics-first relation engine**
   "These heroes are likely to synergize or counter because their capabilities fit in a structured way."

3. **Drafting engine**
   "This pick is good in this draft state, role assignment, tempo profile, and patch context."

Invoker's long-term goal is clearly not just (1).

The immediate target should be (2), because (2) is the knowledge layer that later enables (3).

This means:

- statistical sources should become evidence, not ontology
- relation objects should become structured artifacts, not just free-text explanations
- the LLM should help extract and render knowledge, not define relation existence by prompt alone

---

## Recommended Direction

The knowledge graph should be built around three layers:

1. **Hero capability representation**
   What a hero does, needs, punishes, and suffers from.

2. **Relation inference**
   Structured hero-to-hero relation edges inferred from those capabilities.

3. **Evidence attachment**
   Statistical signals used to support, calibrate, or contradict inferred relations.

That gives a more useful flow:

`hero mechanics -> structured capabilities -> inferred relations -> evidence -> optional natural-language rendering`

This is stronger than:

`stats -> candidate pairs -> explanation text`

---

## Representation Principles

The representation should satisfy these constraints:

- **Mechanically interpretable**
  A relation edge should say what capability interacts with what capability or liability.

- **Directionally explicit**
  `A enables B` is different from `B enables A`.

- **Usable without text**
  Draft logic should be able to consume the relation object directly.

- **Compatible with evidence**
  Stats should be attachable as evidence without defining the relation by themselves.

- **Composable**
  Pairwise edges should later be aggregatable into larger draft motifs.

- **Incremental**
  Phase 1.x should be able to implement a smaller useful slice without pretending to solve full draft reasoning.

---

## Proposed Hero Representation

Flat `functional_tags` are too weak as the long-term relation substrate.

The stronger representation should separate at least four buckets:

- `capabilities`: what the hero provides
- `requirements`: what the hero needs from allies or draft context
- `liabilities`: what the hero is weak against
- `targets`: what the hero punishes or exploits

Illustrative shape:

```json
{
  "hero_id": 28,
  "localized_name": "Slardar",
  "capabilities": [
    {"type": "armor_reduction", "strength": 0.9, "source": "Corrosive Haze"},
    {"type": "vision_reveal", "strength": 1.0, "source": "Corrosive Haze"},
    {"type": "aoe_stun", "strength": 0.7, "source": "Slithereen Crush"},
    {"type": "jump_start", "strength": 0.7, "source": "Blink + Crush"}
  ],
  "requirements": [
    {"type": "damage_followup", "importance": 0.8},
    {"type": "jump_access", "importance": 0.6}
  ],
  "liabilities": [
    {"type": "kiting", "severity": 0.7},
    {"type": "disengage", "severity": 0.6}
  ],
  "targets": [
    {"type": "invisibility_dependence", "strength": 1.0},
    {"type": "low_armor_core", "strength": 0.8}
  ]
}
```

This is not final schema text. It is the shape of the semantics we want.

### Why this is stronger than flat tags

It distinguishes:

- what a hero brings
- what a hero needs
- what a hero punishes
- what a hero struggles into

That distinction is the minimum needed for reusable relation inference.

---

## Proposed Feature Families

The exact vocabulary can evolve, but the representation should move toward typed families rather than a single undifferentiated flat list.

Examples:

### Capabilities

- `initiation`
- `reliable_stun`
- `aoe_lockdown`
- `vision_reveal`
- `armor_reduction`
- `healing_reduction`
- `save`
- `sustain`
- `wave_clear`
- `tower_damage`
- `physical_burst`
- `magic_burst`
- `long_fight_scaling`

### Requirements

- `needs_frontline`
- `needs_lockdown`
- `needs_vision`
- `needs_damage_followup`
- `needs_save`
- `needs_lane_stability`

### Liabilities

- `weak_to_gap_close`
- `weak_to_silence`
- `weak_to_dispel`
- `weak_to_kiting`
- `weak_to_bkb_timing`
- `relies_on_invisibility`
- `relies_on_channeling`
- `relies_on_sustain`

### Targets

- `punishes_low_armor`
- `punishes_immobile_backline`
- `punishes_invisibility`
- `punishes_sustain`
- `punishes_summons`
- `punishes_long_cooldown_cores`

These families should remain intentionally small at first.

---

## Proposed Relation Representation

Hero-to-hero relations should be first-class structured objects.

Illustrative shape:

```json
{
  "relation_id": "28->120:synergy:enabler_payoff:armor_reduction",
  "from_hero_id": 28,
  "to_hero_id": 120,
  "relation_kind": "synergy",
  "pattern": "enabler_payoff",
  "from_feature": {
    "family": "capability",
    "type": "armor_reduction"
  },
  "to_feature": {
    "family": "capability",
    "type": "physical_burst"
  },
  "mechanical_rationale": "armor reduction amplifies repeated physical damage instances",
  "mechanical_confidence": 0.9,
  "evidence": {
    "statistical": {
      "source": "stratz",
      "score": 0.08,
      "games": 50
    }
  },
  "confidence": "high"
}
```

Counter example:

```json
{
  "relation_id": "28->32:counter:vision_exposure",
  "from_hero_id": 28,
  "to_hero_id": 32,
  "relation_kind": "counter",
  "pattern": "vision_exposure",
  "from_feature": {
    "family": "capability",
    "type": "vision_reveal"
  },
  "to_feature": {
    "family": "liability",
    "type": "relies_on_invisibility"
  },
  "mechanical_rationale": "persistent reveal disables stealth-based initiation and escape",
  "mechanical_confidence": 0.95,
  "evidence": {
    "statistical": null
  },
  "confidence": "med"
}
```

### Important properties

This gives us:

- direction
- relation type
- reusable pattern class
- explicit interacting features
- evidence attachment
- confidence separate from evidence source

That is much closer to a real KG edge than `score + reason`.

---

## Relation Pattern Layer

The system should not infer arbitrary pairwise prose. It should infer a small set of reusable relation patterns.

Good early pattern candidates:

- `enabler_payoff`
- `setup_followup`
- `save_protection`
- `vision_exposure`
- `mobility_punish`
- `sustain_break`
- `frontline_backline_access`

Examples:

- `armor_reduction` -> `physical_burst` => `enabler_payoff`
- `reliable_stun` -> `high_burst_followup` => `setup_followup`
- `save` -> `greedy_damage_core` => `save_protection`
- `vision_reveal` -> `relies_on_invisibility` => `vision_exposure`

These patterns are better than free-text relation categories because they are:

- interpretable
- reusable
- testable
- later composable into draft motifs

---

## Evidence Model

Stats should not define relation existence. They should attach as evidence.

Each relation can have:

- `mechanical_evidence`: from extracted hero semantics and rule-based inference
- `statistical_evidence`: STRATZ / OpenDota support when available
- `confidence`: a synthesized judgment using both

This allows the system to distinguish:

- mechanically inferred, statistically supported
- mechanically inferred, statistically weak
- mechanically inferred, statistically absent
- mechanically inferred, statistically contradicted

That distinction is useful for draft reasoning and review.

---

## Natural-Language Reasons Become Downstream

Under this direction, a free-text reason becomes a rendering of a structured relation edge, not the primary artifact.

That means:

- the system should be valid even without the text reason
- a text reason should summarize the structured mechanism already stored
- the drafting agent should depend on the structured edge, not on the sentence

This is a major conceptual shift from the current design.

---

## Draft-Facing Extension

Pair edges are useful, but the drafting system will eventually need higher-order motifs.

Illustrative motif:

```json
{
  "motif": "catch_into_physical_burst",
  "participants": [
    {"hero_id": 28, "role": "initiator"},
    {"hero_id": 120, "role": "damage_converter"}
  ],
  "requirements": [
    "target_lockdown",
    "physical_followup"
  ],
  "benefits": [
    "pickoff_conversion",
    "fast_single_target_kill"
  ]
}
```

This should not be Phase 1.2 work, but the relation representation should not block this future.

---

## What This Means For Phase 1.2

The narrow version of Phase 1.2 was:

- do extraction first
- use STRATZ/OpenDota to choose pairs
- explain those pairs better

That is not worth much if the real goal is the KG.

### Conclusion

Phase 1.2 should not be justified as "slightly better explanation of stat-selected pairs."

The only part that still clearly matters is the pipeline separation:

- pass 1: materialize hero extraction outputs first
- pass 2: run relation logic only after hero semantics are available

That two-pass boundary is still foundational even in a KG-first design.

### Minimal useful interpretation of Phase 1.2

If we keep Phase 1.2, it should be narrowly framed as:

- establish two-pass processing
- handle empty hero B tag coverage safely (`tagged == 0` skip)
- avoid schema churn that will be thrown away

This makes Phase 1.2 an infrastructure fix, not the final relation solution.

---

## Recommended Near-Term Options

### Option A — Minimal infrastructure fix

Do only:

- two-pass orchestrator
- empty-tag skip guard

Do not expand the relation artifact yet.

This is the safest option if we want to stop wasting effort on a weak relation layer.

### Option B — KG-oriented relation slice

Use the two-pass split, then implement a very small mechanics-first relation inference layer:

- define a small typed feature vocabulary
- infer a small set of structured relation patterns
- attach stats only as evidence

This best matches the long-term goal, but it requires explicit schema design.

### Option C — Pause and redesign representation first

If flat tags are too weak even for a first mechanics-first slice, pause implementation and define the capability and relation schema before building more pipeline logic.

This is valid if we believe the current tag vocabulary is not a usable substrate.

### Current recommendation

The current recommendation is:

- do **Option A** immediately if we need a small concrete step now
- prepare **Option B** as the real next architectural move

Do **not** spend much time polishing the current "stats first, explanation second" relation model.

---

## Suggested Schema Building Blocks

Not final, but likely useful entities:

### `HeroFeature`

- `family`
- `type`
- `strength`
- `source_ability`
- `evidence`

### `HeroCapabilityProfile`

- `capabilities`
- `requirements`
- `liabilities`
- `targets`

### `HeroRelation`

- `relation_id`
- `from_hero_id`
- `to_hero_id`
- `relation_kind`
- `pattern`
- `from_feature`
- `to_feature`
- `mechanical_rationale`
- `mechanical_confidence`
- `evidence`
- `confidence`
- `provenance`

### `RelationEvidence`

- `mechanical`
- `statistical`
- `notes`

The exact names can change. The key point is the semantics, not the field spelling.

---

## Key Decisions Captured Here

1. The project goal is a KG for high-quality drafting, not a report of explained STRATZ pair stats.
2. Hero-to-hero relations should be first-class structured objects.
3. Stats should become evidence, not the primary source of relation existence.
4. Free-text reasons should be derived from structured relations, not treated as the main artifact.
5. The two-pass split still matters because relation logic should run only after hero semantics are materialized.
6. A narrow Phase 1.2 is acceptable only as infrastructure, not as the intended final relation design.

---

## Open Questions

These still need explicit design decisions:

- Is the current flat tag vocabulary strong enough to seed a first capability profile?
- Should capability extraction remain a single LLM pass, or should it be split into typed families?
- How much rule-based inference should live in code versus be proposed by an LLM and validated?
- What is the minimum useful relation pattern set for the first KG slice?
- Should the first relation artifact be stored per hero file, or as a separate relation index?
- How should contradictory mechanical and statistical evidence be represented?

---

## Summary

The central lesson is simple:

If the KG is the real product, then the primary artifact cannot be "stat-selected pair plus explanatory sentence."

The primary artifact should be a structured relation fact:

- who affects whom
- in what direction
- through what mechanism
- with what evidence

That is the layer a drafting agent can reason over.
That is also the layer from which text explanations should later be rendered.
