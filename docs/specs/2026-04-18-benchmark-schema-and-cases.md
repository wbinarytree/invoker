# Benchmark Schema And Cases

**Date:** 2026-04-18
**Status:** draft — review before implementation
**Scope:** first KG validation slice only
**Governed by:** `docs/specs/2026-04-18-kg-design-guidelines.md`
**Feeds:** `docs/plans/2026-04-18-kg-validation-plan.md`

---

## Purpose

This document defines the smallest concrete artifact contract for the first KG validation slice.

It answers two questions that the higher-level plans leave open:

1. What exact structured objects should the benchmark prototype produce?
2. What concrete hero facts and relation cases should the prototype succeed or fail on?

This document is intentionally narrower than a full production schema spec.

It is for the benchmark slice only:

- small hero set
- small vocabulary
- small relation pattern set
- explicit evaluation cases

If this slice fails, we should redesign before broad rollout.

---

## Benchmark Scope

The benchmark uses this hero set:

- `Anti-Mage (#1)`
- `Puck (#13)`
- `Slardar (#25)`
- `Riki (#48)`
- `Nyx Assassin (#88)`
- `Medusa (#96)`
- `Oracle (#109)`
- `Underlord (#112)`
- `Pangolier (#115)`

The benchmark artifact set is:

1. `HeroFactProfile`
2. `HeroRelation`
3. `RelationEvidence`

Nothing else is required for the first validation gate.

---

## Design Constraints

The benchmark contract should satisfy these rules:

- useful without prose
- mechanically interpretable
- small enough to inspect manually
- expressive enough to answer the benchmark draft questions
- not dependent on full-roster execution
- not dependent on team identity, lane templates, or reader API redesign

---

## How Relations Should Be Generated

The benchmark should **not** assume that relation records are typed in by hand.

Recommended generation path:

1. Build `HeroFactProfile` artifacts first.
   These may use LLM extraction, deterministic transforms, or a hybrid, but the output must be typed hero facts.

2. Infer `HeroRelation` records from those typed hero facts using explicit relation rules.
   For the benchmark slice, the preferred default is deterministic inference over typed facts:
   - `A.capability -> B.capability`
   - `A.capability -> B.liability`
   - `A.capability -> B.requirement`

This is intentional for the benchmark phase.

We are trying to validate the representation itself:

- are the hero fact objects useful?
- are the relation objects useful?
- are the patterns expressive enough?

If we asked an LLM to infer the relations at this stage, we would blur two different questions:

1. is the representation good?
2. is the LLM good at discovering relations through it?

For the first validation slice, deterministic inference is better because it makes failure easier to diagnose.

3. Attach `RelationEvidence` afterward.
   Stats support or challenge the inferred relation; they do not define it.

4. Optional only: use an LLM to render a short rationale sentence from the structured relation.
   That prose is convenience output, not the canonical relation.

### What humans should and should not do

Humans **should**:

- define the benchmark vocabulary
- define the relation patterns
- define the benchmark review cases
- review whether the produced relations are good

Humans should **not**:

- manually author the relation records as the system output
- serve as the hidden ontology that the prototype merely copies

If the benchmark only works because humans hand-type the relations, then the representation has not been validated.

---

## Artifact 1 — HeroFactProfile

### Purpose

Represent what a hero provides, needs, and suffers from in a way that is more useful than a flat tag list.

### Shape

```json
{
  "hero_id": 28,
  "localized_name": "Slardar",
  "source_patch": "7.41b",
  "cohort": "pro",
  "capabilities": [
    {
      "type": "armor_reduction",
      "strength": 0.9,
      "evidence": ["Corrosive Haze reduces armor and grants reveal"]
    },
    {
      "type": "vision_reveal",
      "strength": 1.0,
      "evidence": ["Corrosive Haze reveals the target"]
    }
  ],
  "requirements": [
    {
      "type": "needs_damage_followup",
      "importance": 0.8,
      "evidence": ["Provides setup and amplification more than burst conversion"]
    }
  ],
  "liabilities": [
    {
      "type": "weak_to_kiting",
      "severity": 0.7,
      "evidence": ["Most impact requires committing into melee range"]
    }
  ],
  "provenance": {
    "mechanical_source": "llm_extraction",
    "prompt_version": 1
  }
}
```

### Required fields

- `hero_id`
- `localized_name`
- `source_patch`
- `cohort`
- `capabilities`
- `requirements`
- `liabilities`
- `provenance`

### Rules

- `capabilities`, `requirements`, and `liabilities` must remain separate lists.
- Every feature item must contain one typed label and one short evidence payload.
- The evidence payload may be quoted or synthesized, but it must be understandable by a reviewer.
- `strength`, `importance`, and `severity` are optional during the very first prototype if they slow down extraction too much. The typed label is mandatory; the scalar is negotiable.

### Benchmark-specific note

This artifact is still hero-centric. That is acceptable for the benchmark slice. The goal here is to prove typed hero semantics, not to settle final storage layout.

---

## Artifact 2 — HeroRelation

### Purpose

Represent a hero-to-hero relation as a structured object, not as a score plus prose.

### Shape

```json
{
  "relation_id": "28->120:synergy:enabler_payoff:armor_reduction",
  "source_patch": "7.41b",
  "cohort": "pro",
  "from_hero_id": 28,
  "to_hero_id": 120,
  "relation_kind": "synergy",
  "pattern": "enabler_payoff",
  "source_feature": "armor_reduction",
  "target_feature": "physical_burst",
  "mechanical_rationale": "armor reduction amplifies physical damage conversion",
  "context": {
    "source_roles": [],
    "target_roles": [],
    "lane_context": null,
    "phase_context": null,
    "archetype_context": []
  },
  "evidence": {
    "mechanical": {
      "confidence": 0.9
    },
    "statistical": null
  },
  "confidence": "med"
}
```

### Required fields

- `relation_id`
- `source_patch`
- `cohort`
- `from_hero_id`
- `to_hero_id`
- `relation_kind`
- `pattern`
- `source_feature`
- `target_feature`
- `mechanical_rationale`
- `context`
- `evidence`
- `confidence`

### Rules

- The relation must still make sense if `statistical` evidence is `null`.
- `pattern` must come from the first benchmark relation-pattern vocabulary.
- `source_feature` and `target_feature` must be traceable to the two heroes' fact profiles.
- `mechanical_rationale` should be one short structured explanation, not free-form essay text.
- `context` fields may be empty in the benchmark slice, but the object must exist.

### Why keep context now

The benchmark should reserve space for context immediately, even if most fields are defaulted, so the relation object does not have to be reshaped again the moment role or lane assumptions matter.

---

## Artifact 3 — RelationEvidence

### Purpose

Attach support, absence, or contradiction without letting stats define ontology.

### Shape

```json
{
  "mechanical": {
    "confidence": 0.9,
    "basis": [
      "Slardar.capabilities includes armor_reduction",
      "Pangolier.capabilities includes physical_burst"
    ]
  },
  "statistical": {
    "source": "stratz",
    "score": 0.08,
    "games": 50,
    "alignment": "aligned"
  }
}
```

### Required behavior

The benchmark prototype must distinguish at least these cases:

- `aligned`
- `weakly_aligned`
- `unobserved`
- `contradicted`

If the first slice cannot carry those four states, the evidence layer is too weak.

---

## First Vocabulary Contract

Use exactly the small vocabulary from the validation plan for the first slice.

### Capabilities

- `mana_burn`
- `initiation`
- `reliable_stun`
- `mobility`
- `vision_reveal`
- `armor_reduction`
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

- `mana_dependence`
- `weak_to_reveal`
- `weak_to_gap_close`
- `weak_to_kiting`
- `greedy`
- `low_waveclear`

### Relation patterns

- `resource_punish`
- `enabler_payoff`
- `setup_followup`
- `save_protection`
- `vision_exposure`
- `mobility_punish`

No vocabulary expansion should happen during the first prototype unless the benchmark review shows a specific representation failure.

---

## Benchmark Hero Fact Cases

These are not full gold labels. They are minimum expectations for the first slice.

### Anti-Mage (#1)

Expected likely capabilities:

- `mana_burn`
- `mobility`

Expected likely relation use:

- strong source for `resource_punish`

Why included:

- this is one of the cleanest externally validated counter-pick examples in Dota
- Anti-Mage directly attacks mana and then converts missing mana into damage with Mana Void

### Slardar (#25)

Expected likely capabilities:

- `armor_reduction`
- `vision_reveal`
- `initiation`
- `reliable_stun`

Expected likely requirements:

- `needs_damage_followup`

Expected likely liabilities:

- `weak_to_kiting`

Why included:

- tests whether the model can separate enablement from payoff
- tests whether reveal and initiation are represented distinctly

### Pangolier (#115)

Expected likely capabilities:

- `mobility`
- `magic_burst` or burst-like conversion pressure is plausible; do not require a specific damage label too early
- `initiation`

Expected likely requirements:

- none are strictly required for the benchmark; the slice may or may not surface one

Expected likely liabilities:

- none required for pass; avoid forcing weak labels here

Why included:

- tests whether a mobile damage-conversion hero is represented as payoff, not only as generic mobility

### Oracle (#109)

Expected likely capabilities:

- `save`

Expected likely requirements:

- `needs_frontline` is plausible but not mandatory for the first pass

Expected likely liabilities:

- none required for pass

Why included:

- tests defensive/protective hero semantics
- forces the benchmark to avoid inventing capabilities that do not exist in the kit

### Riki (#48)

Expected likely capabilities:

- `mobility`
- `silence`

Expected likely liabilities:

- `weak_to_reveal`

Why included:

- tests invisibility-linked liability handling

### Underlord (#112)

Expected likely capabilities:

- `wave_clear`
- `initiation` or control-like setup is plausible but not mandatory

Expected likely liabilities:

- none required for pass

Why included:

- tests lane-stability / macro-style semantics without forcing too much draft context yet

### Puck (#13)

Expected likely capabilities:

- `mobility`
- `silence`
- `initiation`

Expected likely liabilities:

- none required for pass

Why included:

- tests elusive initiator semantics

### Nyx Assassin (#88)

Expected likely capabilities:

- `reliable_stun`
- `mobility`

Expected likely relation use:

- likely source for `mobility_punish` or anti-caster-style reasoning later

Why included:

- tests pickoff-oriented relation generation

### Medusa (#96)

Expected likely requirements:

- none required for pass

Expected likely liabilities:

- `mana_dependence`

Why included:

- this is the natural counterpart to Anti-Mage in the benchmark
- Medusa is an ideal test for whether the prototype can encode a liability that another hero directly punishes

---

## Benchmark Relation Cases

These are the most important benchmark cases. The first slice should be evaluated against them directly.

### Case 1 — Anti-Mage (#1) -> Medusa (#96)

Expected:

- one negative relation
- `relation_kind = counter`
- `pattern = resource_punish`
- `source_feature = mana_burn`
- `target_feature = mana_dependence`

Why:

- this is both mechanically clear and statistically supported in the current public matchup data
- Anti-Mage burns mana with Mana Break and deals damage based on missing mana with Mana Void, while Medusa's durability is heavily tied to Mana Shield
- current Dotabuff matchup data also shows Anti-Mage as one of Medusa's strongest counters and Medusa as one of Anti-Mage's strongest counters in the opposite direction table

Failure modes to watch:

- relation only exists because statistics said so, with no typed liability on Medusa
- the system cannot represent resource-linked counters at all
- the first vocabulary is too thin for an obviously important counter relationship

### Case 2 — Slardar (#25) -> Riki (#48)

Expected:

- one negative relation
- `relation_kind = counter`
- `pattern = vision_exposure`
- `source_feature = vision_reveal`
- `target_feature = weak_to_reveal`

Why:

- tests whether the representation can connect a capability on A to a liability on B
- the relation is directly grounded in Slardar's Corrosive Haze providing shared vision and True Sight and Riki's reliance on invisibility

Failure modes to watch:

- liability is missing from the hero fact profile
- relation ends up prose-only

### Case 3 — Slardar (#25) -> Pangolier (#115)

Expected:

- one positive relation is plausible
- `relation_kind = synergy`
- `pattern = enabler_payoff`
- `source_feature = armor_reduction`
- `target_feature = physical_burst` or another clearly damage-conversion-oriented capability if the vocabulary is adjusted during review

Why:

- this remains a useful benchmark for "enablement -> payoff," but it should be treated as a reviewed hypothesis, not as unquestioned truth from memory
- this case is weaker than Anti-Mage -> Medusa, so it should not be the only benchmark anchor

Failure modes to watch:

- Pangolier gets only mobility labels and no conversion semantics
- the pair is accepted only because a human thinks it sounds right, not because the artifact can explain it structurally

### Case 4 — Negative control: Underlord (#112) -> Pangolier (#115)

Expected:

- no strong benchmark relation required

Why:

- the system should be able to produce no clear relation instead of forcing one from weak overlap

Failure modes to watch:

- overgeneration from generic tags
- every hero pair gets a shallow relation record

### Case 5 — Negative control: Oracle (#109) -> Nyx Assassin (#88)

Expected:

- no forced benchmark relation

Why:

- checks whether the prototype can avoid inventing relations from generic support/control overlap

---

## Benchmark Review Questions

The reviewer should be able to inspect the produced artifacts and answer:

1. Does each `HeroFactProfile` clearly say what the hero provides, needs, and suffers from?
2. Does each `HeroRelation` stand on its own without needing the prose sentence?
3. Do relations connect typed features rather than vague hero-level impressions?
4. Is the evidence block clearly secondary to the mechanical relation?
5. Are the negative-control cases left mostly empty rather than overgenerated?

If the answer is "no" on the benchmark slice, the representation should be revised before more implementation lands.

---

## Research Notes For The Benchmark

These cases were revised after review to avoid relying only on prior model intuition.

External grounding used for the current benchmark draft:

- Anti-Mage ability semantics:
  Mana Break burns mana on attack and Mana Void damage depends on missing mana.
  Source: Dota 2 Wiki hero page for Anti-Mage.
- Medusa reliance on mana for durability:
  Mana Shield is a central survivability mechanic, and current public matchup pages show Anti-Mage as a major Medusa counter.
  Sources: Dota 2 Wiki hero page for Medusa, current Dotabuff matchup pages.
- Oracle correction:
  Oracle should not be used as a silence example in the benchmark.
  Oracle's visible core kit points much more clearly to save/protection than to silence.
  Source: official Oracle release page on dota2.com.
- Terrorblade caution:
  Terrorblade absolutely becomes a huge physical damage carry in real play, but that does not mean the benchmark should force `physical_burst` as a first-slice typed capability straight from ability text.
  Sources: Dota 2 Wiki / official hero descriptions for Metamorphosis and Conjure Image.

The benchmark should continue to prefer cases that are both:

- mechanically legible from hero semantics
- and externally defensible from public hero or matchup information

---

## Recommended Immediate Follow-up

After this document is reviewed, the next implementation package should be:

1. Add a prototype module for the benchmark schema only.
2. Build benchmark hero fact profiles for the listed heroes.
3. Infer only the listed relation patterns.
4. Evaluate the produced artifacts against the benchmark cases above.

Do not expand to full-roster extraction until that review is complete.

---

## Summary

This benchmark spec exists to force a concrete review before scaling:

- exact first artifact shapes
- exact first vocabulary
- exact first expected hero facts
- exact first expected relations
- explicit negative controls

That should make the next step much safer than broad schema work without a falsifiable slice.
