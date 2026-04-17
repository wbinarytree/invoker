# KG Design Guidelines

**Date:** 2026-04-18
**Status:** draft — governing design guidance
**Scope:** architecture and decision rules for future Invoker work
**Applies to:** schema design, pipeline design, extraction, relation inference, graph building, reader API

---

## Purpose

This document is the governing guide for the next stage of Invoker.

It exists to prevent the project from drifting into a hero encyclopedia with lightly explained pair stats when the actual goal is different:

- build a patch-aware knowledge graph
- encode real mechanical and drafting-relevant relations
- support a strong drafting agent with structured facts and evidence

This is not a detailed implementation spec. It is a design rulebook for deciding what belongs in the system and what does not.

---

## Product Goal

Invoker is not trying to be primarily:

- a wiki-like hero card database
- a report of STRATZ/OpenDota pair correlations
- a prompt bundle that asks an LLM to improvise draft logic from prose

Invoker is trying to be:

- a patch-scoped Dota knowledge substrate
- with structured hero facts
- structured relation records
- explicit evidence
- and query surfaces that a drafting agent can use without depending on free-text interpretation

Text explanations are secondary conveniences.
Structured relation facts are primary.

---

## Core Design Stance

### 1. Patch scope is a first-class boundary

Dota knowledge is patch-sensitive. Hero facts, relation evidence, and derived planning surfaces should be partitioned by patch by default.

Do not design for a timeless KG.

Cross-patch comparison may exist later, but patch-local truth is the default storage and reasoning boundary.

### 2. Facts, relations, and views are different things

The system should distinguish:

- **facts**: hero capabilities, requirements, liabilities, draft traits, role distributions
- **relations**: structured hero-to-hero or hero-to-template edges with evidence
- **views**: hero cards, summaries, denormalized JSON, graph projections, planner-oriented query results

Per-hero JSON may continue to exist, but it should be treated as a view or convenient packaging format, not as the only possible canonical truth for every kind of data.

### 3. Stats are evidence, not ontology

Statistical sources should support relation records, not define the entire relation layer.

Do not let the system mean:

`pair exists because STRATZ says so`

Prefer:

`pair is mechanically inferred, and STRATZ/OpenDota provide supporting, weak, absent, or contradictory evidence`

### 4. Text is downstream, not source-of-truth

Natural-language reasons may be stored as convenience fields, but they should not be the durable core representation.

The durable representation should be typed features, typed relation patterns, and explicit evidence components.

If a relation object is not useful without its prose sentence, the representation is too weak.

### 5. Context is part of the relation, not a later add-on

Drafting is not only hero-to-hero. It is hero-to-hero under assumptions:

- source role
- target role
- lane context
- phase context
- lineup archetype
- cohort and scope

Context does not have to be fully modeled on day one, but the schema and plan should reserve for it early.

### 6. Separate mechanics from draft evaluation

Hero mechanics, draft requirements, liabilities, and team identity are related but distinct layers.

Do not flatten them all into one tag list.

At minimum, keep separate:

- `capabilities`
- `requirements`
- `liabilities`
- `draft_traits` when ready

### 7. Incremental truth beats ambitious prose

Prefer a small structured vocabulary with enforceable validators over a richer but vague prompt-driven artifact.

If a feature cannot be tested, validated, or meaningfully consumed by the planner, it should not be central.

### 8. Query-time LLM dependence should remain excluded

The drafting agent may use an LLM on top of the KG, but Invoker should not require live LLM calls to answer core KG queries.

Extraction-time and build-time LLM use is acceptable.
Query-time dependence for core knowledge is not.

---

## Required Representation Layers

Invoker should converge on these layers:

### Hero facts

Per hero, patch-scoped:

- capability profile
- requirement profile
- liability profile
- role distribution
- later: draft traits, modifier-sensitive profiles

### Relation records

Structured edges that express:

- direction
- relation kind
- pattern or mechanism
- context
- evidence
- confidence

### Template / motif nodes

As the system matures, not all useful drafting knowledge should be hero-pair edges.

Invoker should be able to represent reusable abstractions such as:

- lane templates
- teamfight structures
- tempo motifs
- lineup archetypes

### Views

Useful projections may include:

- hero-centric JSON
- summary text
- graph cache
- draft-state helper results

Views are important, but they should not dictate the core semantics.

---

## Representation Rules

### Hero representation rule

Do not store only flat mechanical tags as the long-term hero semantic layer.

The minimum meaningful split is:

- `capabilities`
- `requirements`
- `liabilities`

`draft_traits` should be added when the project is ready to model reveal cost, flex value, first-phase safety, and related drafting concerns.

### Relation representation rule

A relation record should answer:

- who affects whom
- in what direction
- under what context
- through which interacting features
- with what evidence

If it only answers "these two heroes are good together" with a score and a sentence, it is not sufficient for the drafting goal.

### Evidence representation rule

Evidence should be attachable in components, for example:

- mechanical inference
- statistical support
- statistical contradiction
- source provenance

Avoid collapsing all evidence into a single opaque confidence string unless a richer decomposition is also retained.

### Context representation rule

Contexts should be modeled explicitly, even if early values are sparse or mostly defaulted.

Useful context axes include:

- `cohort`
- `scope`
- `source_roles`
- `target_roles`
- `lane_context`
- `phase_context`
- `archetype_context`

### Provenance rule

All extracted or inferred knowledge should remain traceable to:

- patch
- source snapshot or fetch window
- prompt version or inference rule version
- generator version
- timestamps or sample windows where relevant

This rule is already a project strength and should not be weakened.

---

## Storage Guidance

### Recommended canonical split

Mentally, and eventually on disk, prefer this split:

- `facts/`
- `relations/`
- `views/`

That does not require an immediate storage migration. It does require that future schema decisions stop assuming hero-centric JSON must be the only canonical shape.

### Hero files

Hero files remain useful as denormalized bundles for:

- inspection
- quick validation
- bootstrap output
- simple consumers

But they should not force all future relation intelligence to live duplicated across hero files.

### Relation records

Relation records should become canonical once the relation layer is strong enough to justify them.

That is especially important for:

- context-aware edges
- typed reason factors
- evidence decomposition

---

## Vocabulary Guidance

### Start small and typed

Vocabulary growth should happen in typed families, not a single mixed namespace.

Recommended early families:

- capabilities
- requirements
- liabilities
- relation patterns
- later: draft traits

### Prefer interpretable terms

Terms should be:

- stable enough to validate
- meaningful to planners
- derivable from source evidence or explicit synthesis rules

Avoid prematurely adding many fuzzy, overlapping concepts that the validator cannot police.

### Distinguish observed from synthesized where honesty matters

Some hero properties are directly seen in ability text.
Others are synthesized from kit interaction.

If that distinction materially affects trust or debugging, keep it explicit in the representation.

---

## Inference Guidance

### Hero extraction

Build hero semantics first.
Relation logic should run only after hero semantics are materialized.

This is why the two-pass boundary still matters even after the project shifts to KG-first design.

### Relation inference

Relations should be inferred through reusable typed patterns rather than one-off prose generation.

Examples:

- `enabler_payoff`
- `setup_followup`
- `save_protection`
- `vision_exposure`
- `mobility_punish`
- `sustain_break`

### Statistical attachment

When stats are present:

- use them to support or challenge relation records
- do not let them be the only reason a relation exists in the graph

---

## Drafting-Oriented Guidance

### Drafting is action-in-context-centric

The drafting agent does not mainly need:

- isolated hero descriptions
- isolated pair scores

It needs:

- what this pick opens
- what this pick closes
- what this pick requires next
- what liabilities this pick imposes
- what lane structures it enables or weakens
- how much information it reveals

That means Invoker should gradually expand from hero mechanics into draft-facing abstractions.

### Lane templates should arrive early

Many draft-relevant synergies are actually lane-structure relations, not simple hero-pair facts.

Lane templates should therefore be considered early, not as a distant cleanup.

### Team/player identity is a separate scope axis

Do not overload the bracket axis with `team:<slug>` or `player:<slug>`.

Prefer:

- `cohort`: pro, immortal_pub, pub_all, etc.
- `scope`: global, team-era, player-era, etc.

Team identity should also be roster-aware once it exists.

---

## Decision Filters

When deciding whether a new feature belongs, ask:

1. Does this produce structured knowledge or only prettier prose?
2. Can the drafting agent consume it without a fresh LLM interpretation step?
3. Is it patch-scoped and provenance-traceable?
4. Is it a fact, a relation, or only a view?
5. Does it preserve or improve interpretability?
6. Can we validate it meaningfully?
7. Is it solving a real drafting problem or just enriching hero cards?

If the answer skews toward prose, decoration, or hero-card enrichment without planner utility, it should not lead the roadmap.

---

## Immediate Implications

These guidelines imply:

1. The current "stats first, explanation second" relation shape should not be polished into the long-term solution.
2. A narrow two-pass pipeline fix is still worth doing as infrastructure.
3. The next real architecture step should be explicit relation records and typed hero semantics.
4. The planning docs should distinguish short-term infrastructure work from long-term KG work.
5. Future schema work should be evaluated against the drafting use case, not only hero lookup convenience.

---

## Non-goals For This Guide

This guide does not settle:

- the final on-disk directory structure
- the final relation schema field names
- the exact first vocabulary
- the exact first lane template catalog
- the exact first reader API method list

Those belong in implementation specs and execution plans.

This guide exists so those later specs move in a coherent direction.

---

## Summary

Invoker should proceed as a KG-first system:

- patch-aware
- provenance-first
- mechanics-first
- relation-centric
- context-aware
- evidence-backed

Hero cards and prose summaries remain useful outputs.
They should no longer define the architecture.
