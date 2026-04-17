# KG Validation Plan

**Date:** 2026-04-18
**Status:** draft — go/no-go evaluation plan
**Scope:** small benchmark, narrow vertical slice, explicit success/failure gates
**Governed by:** `docs/specs/2026-04-18-kg-design-guidelines.md`

---

## Purpose

This plan exists to prevent a large amount of implementation work from landing before we know whether the new KG direction is actually useful.

The project should validate the representation on a small, deliberately chosen benchmark before:

- scaling extraction to all heroes
- migrating broad schema surfaces
- investing heavily in relation storage
- rebuilding the reader API around unproven semantics

The goal is fast learning:

- early success if the representation is useful
- early failure if it is not

---

## What We Are Validating

We are **not** trying to validate full drafting intelligence yet.

We are validating whether the next representation is strong enough to support a real KG slice:

1. Can we represent what a hero provides, needs, and suffers from in a way that is clearer than flat tags?
2. Can we infer a small set of hero-to-hero relations from those facts without relying on STRATZ to define the pair list?
3. Are the resulting relation records more useful for draft reasoning than the old `score + prose reason` model?
4. Can statistical data attach as evidence rather than acting as the primary ontology?

If the answer to these is "no" on a small benchmark, scaling to all heroes should stop.

---

## Benchmark Set

Use a deliberately small hero set that stresses different relation classes.

Recommended first set:

- `Slardar`
- `Pangolier`
- `Oracle`
- `Riki`
- `Underlord`
- `Terrorblade`
- `Puck`
- `Nyx Assassin`

### Why this set

It covers useful stress cases:

- `Slardar` -> enabler/payoff, reveal, catch
- `Pangolier` -> mobile damage follow-up, timing overlap
- `Oracle` -> save/protection, anti-burst coverage
- `Riki` -> invis dependence, punishability by reveal
- `Underlord` -> waveclear, lane stabilization, sustain/control
- `Terrorblade` -> greed, scaling, save/frontline needs
- `Puck` -> elusive setup, mobility, silence/catch patterns
- `Nyx Assassin` -> anti-mobility, anti-caster, pickoff structure

This is enough variety to expose whether the representation is genuinely useful or just neat-looking.

---

## First Vocabulary Slice

Keep the first vocabulary intentionally small.

### Capabilities

- `initiation`
- `reliable_stun`
- `mobility`
- `vision_reveal`
- `armor_reduction`
- `physical_burst`
- `magic_burst`
- `wave_clear`
- `save`
- `silence`

### Requirements

- `needs_frontline`
- `needs_damage_followup`
- `needs_save`
- `needs_lockdown`

### Liabilities

- `weak_to_reveal`
- `weak_to_gap_close`
- `weak_to_kiting`
- `greedy`
- `low_waveclear`

### Relation patterns

- `enabler_payoff`
- `setup_followup`
- `save_protection`
- `vision_exposure`
- `mobility_punish`

If this first slice cannot express the benchmark cleanly, we should revisit the families before expanding.

---

## Prototype Scope

Build only a thin vertical slice:

1. Hero fact profile
   - `capabilities`
   - `requirements`
   - `liabilities`

2. Relation inference
   - small rule set over the benchmark heroes

3. Evidence attachment
   - optional STRATZ/OpenDota support on inferred relations

4. Output artifact
   - structured relation records
   - prose optional, secondary

Do **not** broaden to:

- all heroes
- team identity
- lane templates
- full graph migration
- big reader API redesign

This is a validation slice, not a broad buildout.

---

## Draft Questions The Slice Must Answer

The prototype is good only if the structured output helps answer real drafting questions.

Each benchmark hero should support questions like:

- What does this hero provide?
- What does this hero require from allies?
- What liabilities does picking this hero create?
- Which enemy traits does this hero punish?

Each benchmark relation should support questions like:

- Why is this pair good in structured terms?
- What feature on hero A interacts with what feature on hero B?
- Is the pair mechanically inferred, statistically supported, or both?
- Could a planner use this relation without re-reading prose?

If the output cannot answer those, the representation is not ready.

---

## Evaluation Gates

### Gate 1 — Hero fact quality

Pass only if:

- hero facts are clearly more informative than flat tags
- `capabilities`, `requirements`, and `liabilities` are not collapsing into one mixed list
- a reviewer can inspect a hero profile and understand what the hero brings and what it costs

Fail if:

- most fields are vague restatements of each other
- requirements/liabilities are mostly missing or generic
- the representation still behaves like a hero card with prettier labels

### Gate 2 — Relation usefulness

Pass only if:

- a small set of known benchmark interactions is captured cleanly with structured relation records
- relation records are clearly more useful than the old stat-selected prose explanation approach
- the records are understandable without prose text

Fail if:

- relations still need prose to be interpretable
- the relation patterns are too generic to distinguish meaningful mechanisms
- most good pairs still depend on manual special casing

### Gate 3 — Evidence integration

Pass only if:

- stats can attach to relations as support, weakness, absence, or contradiction
- the relation record still makes sense when the statistical block is absent

Fail if:

- the system quietly falls back into "pair exists because stats said so"
- mechanically inferred edges are unusable without stats

### Gate 4 — Scaling confidence

Pass only if:

- the benchmark slice suggests the vocabulary can expand without immediate collapse
- relation rules are reusable, not one-off hero hacks
- reviewers can name the next 20-30 heroes to onboard without needing a full redesign first

Fail if:

- every new hero seems likely to require bespoke relation logic
- the vocabulary is already straining under basic cases
- the schema feels likely to be reshaped again before broader rollout

---

## Kill Criteria

Stop the broader implementation and redesign before scaling if any of these happen:

1. Structured hero facts are not meaningfully better than flat tags.
2. Relation records are not materially more useful than `score + prose reason`.
3. The system still requires an LLM-style interpretation step to answer draft questions.
4. Context needs explode immediately in ways the current relation shape cannot hold.
5. Ad hoc hero-specific exceptions dominate the first benchmark slice.

These are not "we can improve later" issues.
They are signs that the representation itself is wrong.

---

## Suggested Work Sequence

1. Implement the narrow two-pass infrastructure fix.
2. Define the minimal benchmark schema for hero facts and relation records.
3. Build the benchmark-set prototype only.
4. Review outputs manually against the draft questions above.
5. Decide:
   - proceed
   - revise representation
   - stop and redesign

Do not expand to all heroes before step 5 is complete.

---

## Decision Outcomes

### If the slice passes

Proceed to:

- formalize schema
- widen vocabulary carefully
- onboard more heroes
- decide whether relation records become canonical on disk

### If the slice partially passes

Proceed only after:

- tightening the schema
- shrinking or revising the vocabulary
- adjusting relation pattern definitions

### If the slice fails

Do not scale.

Instead:

- record the failure precisely
- identify whether the problem is hero facts, relation shape, or context modeling
- redesign before more implementation lands

---

## Summary

The validation strategy is:

- start small
- prove value on a benchmark set
- use explicit gates
- scale only after the representation survives real draft-oriented review

That is the safest way to avoid a large, cleanly engineered dead end.
