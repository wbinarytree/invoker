# KG Execution Plan

**Date:** 2026-04-18
**Status:** draft — for review and sequencing
**Scope:** concrete execution plan for moving Invoker from hero-KB-first toward KG-first drafting support
**Governed by:** `docs/specs/2026-04-18-kg-design-guidelines.md`

---

## Purpose

This plan turns the current alignment into execution.

We are aligned on the diagnosis:

- the existing system is useful as a hero knowledge base
- it is not yet shaped correctly as a drafting knowledge graph
- polishing the current "stats-selected pairs + prose reasons" design is not the highest-value path

This plan therefore separates:

- **infrastructure work we still need**
- **representation work we must design next**
- **KG work we should implement in sequence**

---

## Overall Strategy

Proceed in three layers:

1. **Stabilize the build boundary**
   Finish the minimal pipeline separation we need regardless of final relation design.

2. **Define the canonical semantics**
   Lock the first useful hero fact and relation schemas before expanding more pipeline logic.

3. **Implement a small but real KG slice**
   Build mechanics-first relation inference with evidence attachment and planner-usable outputs.

Do not spend much more effort improving the current prose-first relation path beyond what is needed to keep the codebase coherent during the transition.

---

## Roadmap Summary

### Stage 0 — Decision lock

Objective:
Make the architectural direction explicit so later work does not drift.

Deliverables:

- KG design guidelines
- KG representation note
- expert review alignment
- this execution plan

Exit criteria:

- team agrees that the target is a KG-first drafting substrate, not an explained-stat hero KB
- team agrees that stats become evidence, not the primary relation ontology

Status:
This stage is effectively underway now.

---

## Stage 1 — Minimal Infrastructure Fix

### Objective

Keep only the pipeline work that remains valuable under the new architecture.

### Why this still matters

Even in a mechanics-first KG design, relation logic should not run before hero semantics are materialized.

The two-pass boundary is still correct.

### Scope

- split the per-hero sequential flow into two passes
- pass 1 materializes hero extraction outputs
- pass 2 runs relation/reason logic only after pass 1 artifacts exist
- skip relation/reason generation when hero B semantic coverage is empty

### What this stage should NOT do

- no new hero schema expansion unless required for minimal compatibility
- no `no_data_matchups`
- no heavy investment in better prose explanations for stat-selected pairs
- no inferred-edge persistence yet

### Exit criteria

1. All requested heroes can be extracted before any relation stage executes.
2. Relation/reason calls see materialized hero B semantics when available.
3. When hero B semantic coverage is empty, the call is skipped cleanly.
4. Existing bootstrap and validation workflows still run.

### Deliverable shape

This is a narrow infrastructure phase.
It should be treated as foundational plumbing, not as the relation solution.

---

## Stage 2 — Canonical Schema Design

### Objective

Define the first durable KG-oriented schema slice before implementing more extraction or inference.

### Required outputs

1. **Hero fact schema**
   At minimum:
   - `capabilities`
   - `requirements`
   - `liabilities`
   - role distribution slot

2. **Relation schema**
   At minimum:
   - direction
   - relation kind
   - relation pattern
   - source feature
   - target feature
   - evidence block
   - confidence
   - provenance

3. **Context schema**
   Start with reserved fields even if sparsely populated:
   - `cohort`
   - `scope`
   - `source_roles`
   - `target_roles`
   - `lane_context`
   - `phase_context`
   - `archetype_context`

4. **View policy**
   Clarify what remains canonical versus denormalized:
   - hero files
   - relation files or relation index
   - summaries
   - graph cache

### Key design question

Should the first KG slice still be hero-file-centered, or should relation records become their own stored artifact immediately?

Current recommendation:

- keep hero files for continuity
- introduce relation records as their own canonical artifact as soon as the relation layer becomes structured enough to justify it

### Exit criteria

1. Schema docs exist and are internally consistent.
2. Vocabulary families are clearly separated.
3. We know what the canonical relation artifact is.
4. We know what remains view-only.

---

## Stage 3 — Vocabulary and Validation Foundation

### Objective

Create the smallest typed vocabulary and validator layer that can support a real first KG slice.

### Scope

Define:

- capability vocabulary
- requirement vocabulary
- liability vocabulary
- relation pattern vocabulary
- early evidence vocabulary if needed

Build validators for:

- vocabulary membership
- feature family correctness
- provenance completeness
- relation field integrity
- evidence field integrity

### Important principle

Keep the vocabulary intentionally small.

The goal here is not coverage maximalism.
The goal is to get a coherent, testable substrate for the first mechanics-first relation layer.

### Exit criteria

1. A closed first vocabulary exists.
2. Validators can reject malformed hero fact or relation records.
3. Gold examples can be expressed with the vocabulary without obvious distortion.

---

## Stage 4 — Hero Fact Extraction Redesign

### Objective

Upgrade hero extraction from flat tag lists toward typed fact profiles.

### Scope

Implement the first real hero fact model:

- extract or derive `capabilities`
- extract or derive `requirements`
- extract or derive `liabilities`

Potential sub-split:

- observed ability-level features
- hero-level synthesized features

This distinction should remain if it materially improves honesty, provenance, and debugging.

### Open implementation choice

Two viable paths:

1. **Single hero-level synthesis prompt**
   Faster to implement, weaker provenance granularity.

2. **Ability-level extraction plus hero-level synthesis**
   Stronger substrate, higher call cost, more faithful for relation inference.

Current recommendation:

- design for ability-level grounding
- but keep the first implemented slice small and cache-heavy

### Exit criteria

1. Hero facts are no longer represented only as one flat tag list.
2. We can express what a hero provides, needs, and suffers from.
3. Facts are provenance-traceable and validator-covered.

---

## Stage 5 — Mechanics-First Relation Inference

### Objective

Make relations a first-class structured product rather than a prose add-on to statistics.

### Scope

Implement a small relation inference engine driven by:

- hero capability profiles
- requirement/liability profiles
- reusable relation patterns

Early pattern set:

- `enabler_payoff`
- `setup_followup`
- `save_protection`
- `vision_exposure`
- `mobility_punish`
- `sustain_break`

### Output

Structured relation records that capture:

- source hero
- target hero
- relation kind
- pattern
- interacting features
- mechanical rationale or factors
- evidence block
- confidence

### What this stage should NOT depend on

- full lane modeling
- team identity
- rich planner API
- perfect drafting semantics

This is the first useful pairwise KG layer, not the final drafting brain.

### Exit criteria

1. Relation records can exist without prose text.
2. At least a small gold set of known pairs can be inferred mechanically.
3. Relation records can attach stats as support or contradiction.

---

## Stage 6 — Evidence Attachment

### Objective

Connect the mechanics-first relation layer to statistical sources without letting stats define ontology.

### Scope

For each inferred relation:

- attempt to attach STRATZ/OpenDota evidence when present
- represent support, weak support, absence, or contradiction

### Important principle

Do not silently discard mechanically meaningful edges because stats are sparse.
Do not automatically trust statistically strong edges if the mechanical layer cannot explain them.

Those are review cases, not schema excuses.

### Exit criteria

1. Relation records carry evidence in a structured block.
2. Mechanics and stats can disagree without breaking the representation.
3. Consumers can distinguish inferred-vs-supported relations.

---

## Stage 7 — Views and Reader API Reorientation

### Objective

Expose KG knowledge in ways the drafting agent will actually use.

### Scope

Refactor outputs and reader surfaces around draft-facing queries, not only hero lookup.

Likely surfaces:

- `hero_card(hero_id, patch, cohort, scope)`
- `relation(a, b, context=...)`
- `relations_for(hero_id, context=...)`
- `requirements_of(hero_id, context=...)`
- `requirements_filled(state, hero_id)`
- `candidate_bundle(state, hero_id, context=...)`

### Important principle

The API should be driven by draft questions, not by whatever is easiest to expose from hero JSON.

### Exit criteria

1. Core KG data can be queried without reading prose summaries.
2. Draft-state questions map naturally onto reader surfaces.
3. Existing validation and graph projections still work.

---

## Stage 8 — Draft Context Expansion

### Objective

Move from pairwise mechanics into draft-aware context.

### Scope

Add in sequence, not all at once:

1. role context
2. lane templates
3. draft traits
4. archetype context
5. team/player scope with roster-aware identity and backoff

### Important principle

Do not jump to team identity before the global mechanics-first relation layer is coherent.

Team identity is a multiplier on a good base, not a substitute for one.

### Exit criteria

1. Relation records can be conditioned on role and lane assumptions.
2. Lane-template reasoning becomes possible.
3. Team/player identity can be attached on a coherent scope axis.

---

## What To Deprioritize Now

These should not lead execution right now:

- better prose for the current stat-selected pair flow
- `no_data_matchups`
- expanding the current flat tag list without schema redesign
- team/player scope before base relation semantics exist
- planner surfaces built directly on top of weak hero-card semantics

These may still happen later, but they are not the leverage points now.

---

## Suggested Immediate Deliverables

The next concrete outputs should be:

1. A revised Phase 1.2 doc reduced to the infrastructure-only two-pass change.
2. A schema spec for hero fact profiles and relation records.
3. A first vocabulary spec for capabilities / requirements / liabilities / relation patterns.
4. A small gold-set spec for relation inference evaluation.

That gives the project a clean handoff from diagnosis to implementation.

---

## Recommended Sequencing

If we want the shortest path with the least wasted work:

1. Narrow and finish the two-pass infrastructure fix.
2. Write and review the canonical hero/relation schema spec.
3. Write and review the first typed vocabulary.
4. Define the first gold-set relation cases.
5. Implement hero fact extraction redesign.
6. Implement mechanics-first relation inference.
7. Attach statistical evidence.
8. Rebuild views and reader surfaces around KG queries.

This order keeps the code changes downstream of design decisions rather than mixing them together.

---

## Risks

### Risk 1 — Overdesign before the first real relation slice

Mitigation:
Keep the first relation pattern set small and concrete.

### Risk 2 — Rebuilding too much hero extraction before relation schemas are stable

Mitigation:
Lock the fact and relation schema together before broad extractor changes.

### Risk 3 — Letting stats sneak back into ontology by convenience

Mitigation:
Require relation records to remain meaningful without the statistical block.

### Risk 4 — Building draft-facing abstractions before pairwise relation semantics are solid

Mitigation:
Do pairwise relation structure first; then add lane/archetype/team layers.

### Risk 5 — Vocabulary explosion

Mitigation:
Keep a small controlled first vocabulary and grow only under review.

---

## Success Criteria

We should consider this direction successful when:

1. Invoker no longer depends on prose reasons as its main relation artifact.
2. Hero semantics explicitly encode capabilities, requirements, and liabilities.
3. Relation records are structured, directional, and evidence-backed.
4. Stats are attached as evidence rather than treated as the only pair source.
5. The drafting agent can query KG facts directly instead of reconstructing meaning from hero cards.

---

## Summary

The near-term plan is:

- keep the two-pass fix because it remains foundational
- stop investing in the current stat-first relation architecture as if it were the final destination
- design and implement the first real KG substrate in explicit steps

That gives us a path that is both practical and aligned with the actual project goal.
