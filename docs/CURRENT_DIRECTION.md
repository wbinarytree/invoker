# Current Direction

Last updated: 2026-04-26

This file is the shortest path to the active design direction. Anything not listed here or in `docs/architecture.md` is not authoritative.

## Active design

- Governing guide:
  [docs/specs/2026-04-18-kg-design-guidelines.md](/Users/yaoda/Projects/invoker/docs/specs/2026-04-18-kg-design-guidelines.md:1)
- Representation note:
  [docs/specs/2026-04-18-kg-relation-representation.md](/Users/yaoda/Projects/invoker/docs/specs/2026-04-18-kg-relation-representation.md:1)
- Benchmark schema and cases:
  [docs/specs/2026-04-18-benchmark-schema-and-cases.md](/Users/yaoda/Projects/invoker/docs/specs/2026-04-18-benchmark-schema-and-cases.md:1)
- Collaboration harness:
  [docs/specs/2026-04-26-collaboration-harness.md](/Users/yaoda/Projects/invoker/docs/specs/2026-04-26-collaboration-harness.md:1)
- Hero authoring context hardening:
  [docs/specs/2026-04-26-hero-authoring-context-hardening.md](/Users/yaoda/Projects/invoker/docs/specs/2026-04-26-hero-authoring-context-hardening.md:1)
- Game-file overlay (deferred follow-up; OpenDota/Stratz staleness):
  [docs/specs/2026-04-27-game-file-overlay.md](/Users/yaoda/Projects/invoker/docs/specs/2026-04-27-game-file-overlay.md:1)
- Vocabulary review log (live append):
  [docs/specs/kg-vocabulary-notes.md](/Users/yaoda/Projects/invoker/docs/specs/kg-vocabulary-notes.md:1)

## Active plans

- Current roadmap:
  [docs/plans/2026-04-22-manual-assisted-kg-plan.md](/Users/yaoda/Projects/invoker/docs/plans/2026-04-22-manual-assisted-kg-plan.md:1)
- KG execution plan:
  [docs/plans/2026-04-18-kg-execution-plan.md](/Users/yaoda/Projects/invoker/docs/plans/2026-04-18-kg-execution-plan.md:1)
- KG validation plan:
  [docs/plans/2026-04-18-kg-validation-plan.md](/Users/yaoda/Projects/invoker/docs/plans/2026-04-18-kg-validation-plan.md:1)

## Active handoff

- Stage 4 vocabulary review:
  [docs/handoff-2026-04-25-stage4-vocabulary-review.md](/Users/yaoda/Projects/invoker/docs/handoff-2026-04-25-stage4-vocabulary-review.md:1)

## Implementation source of truth

- [docs/architecture.md](/Users/yaoda/Projects/invoker/docs/architecture.md:1) — what the code actually does today.

## Notes

- Retrospective brainstorm/decision notes:
  [docs/notes/](/Users/yaoda/Projects/invoker/docs/notes:1)
- **OpenDota constants staleness** (not patch-versioned, silently drifts after patch):
  [docs/notes/2026-04-26-opendota-constants-not-patch-versioned.md](notes/2026-04-26-opendota-constants-not-patch-versioned.md)

## External input

- Expert review feeding the pivot:
  [docs/tmp/expert_review/review.md](/Users/yaoda/Projects/invoker/docs/tmp/expert_review/review.md:1)

## Current intent

The project shifted away from the old relation path:

- no longer optimize around STRATZ-selected pair reasoning
- use stats as evidence, not ontology
- validate the KG direction on a small benchmark before scaling
- keep only low-regret infrastructure work from the old plan

## Archive

Superseded specs and plans live under [docs/archive/](/Users/yaoda/Projects/invoker/docs/archive:1) with a `Status: superseded by …` header. They are not part of the active set — read them only when investigating *why* a decision was made, not to derive current behavior. See `GUIDELINES.md` → "Doc Lifecycle".
