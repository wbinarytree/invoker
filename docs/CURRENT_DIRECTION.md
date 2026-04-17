# Current Direction

Last updated: 2026-04-18

This file is the shortest path to the active design direction.

## Active docs

- Governing guide:
  [docs/specs/2026-04-18-kg-design-guidelines.md](/Users/yaoda/Projects/invoker/docs/specs/2026-04-18-kg-design-guidelines.md:1)
- Representation note:
  [docs/specs/2026-04-18-kg-relation-representation.md](/Users/yaoda/Projects/invoker/docs/specs/2026-04-18-kg-relation-representation.md:1)
- Execution plan:
  [docs/plans/2026-04-18-kg-execution-plan.md](/Users/yaoda/Projects/invoker/docs/plans/2026-04-18-kg-execution-plan.md:1)
- Validation-gate plan:
  [docs/plans/2026-04-18-kg-validation-plan.md](/Users/yaoda/Projects/invoker/docs/plans/2026-04-18-kg-validation-plan.md:1)
- External review input:
  [docs/tmp/expert_review/review.md](/Users/yaoda/Projects/invoker/docs/tmp/expert_review/review.md:1)

## Current intent

The project has shifted away from the old relation path:

- no longer optimize around STRATZ-selected pair reasoning
- use stats as evidence, not ontology
- validate the KG direction on a small benchmark before scaling
- keep only low-regret infrastructure work from the old plan

## Superseded docs

These remain as historical trace, but they should not be treated as the active roadmap for relation design:

- [docs/specs/2026-04-16-batch-reason.md](/Users/yaoda/Projects/invoker/docs/specs/2026-04-16-batch-reason.md:1)
- [docs/specs/2026-04-17-phase-1.2-pipeline-correctness.md](/Users/yaoda/Projects/invoker/docs/specs/2026-04-17-phase-1.2-pipeline-correctness.md:1)
- [docs/specs/2026-04-17-phase-1.5-typed-tags.md](/Users/yaoda/Projects/invoker/docs/specs/2026-04-17-phase-1.5-typed-tags.md:1)

Those docs may still contain useful local ideas, but the active direction is the KG-first set above.
