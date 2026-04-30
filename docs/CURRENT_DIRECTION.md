# Current Direction

Last updated: 2026-04-28

This file is the shortest path to the active design direction. Anything not listed here or in `docs/architecture.md` is not authoritative.

## Active design

- Governing guide:
  [docs/specs/2026-04-18-kg-design-guidelines.md](specs/2026-04-18-kg-design-guidelines.md)
- Representation note:
  [docs/specs/2026-04-18-kg-relation-representation.md](specs/2026-04-18-kg-relation-representation.md)
- Benchmark schema and cases:
  [docs/specs/2026-04-18-benchmark-schema-and-cases.md](specs/2026-04-18-benchmark-schema-and-cases.md)
- Collaboration harness:
  [docs/specs/2026-04-26-collaboration-harness.md](specs/2026-04-26-collaboration-harness.md)
- Vocabulary review log (live append):
  [docs/specs/kg-vocabulary-notes.md](specs/kg-vocabulary-notes.md)
- Release process for authored KG artifacts:
  [docs/specs/2026-04-28-release-process.md](specs/2026-04-28-release-process.md)

## Active plans

- Current roadmap:
  [docs/plans/2026-04-22-manual-assisted-kg-plan.md](plans/2026-04-22-manual-assisted-kg-plan.md)
- KG execution plan:
  [docs/plans/2026-04-18-kg-execution-plan.md](plans/2026-04-18-kg-execution-plan.md)
- KG validation plan:
  [docs/plans/2026-04-18-kg-validation-plan.md](plans/2026-04-18-kg-validation-plan.md)

## Active handoff

- Stage 4 vocabulary review:
  [docs/handoff-2026-04-25-stage4-vocabulary-review.md](handoff-2026-04-25-stage4-vocabulary-review.md)

## Implementation source of truth

- [docs/architecture.md](architecture.md) — what the code actually does today.
- [docs/context-modules.md](context-modules.md) — implemented static hero context packet, stat context, ability/talent context, and mechanism primer.
- [docs/game-files-snapshot.md](game-files-snapshot.md) — implemented game-file snapshot refresh playbook and JSON contract.

## Recently completed

The Stage 4 hero-authoring context hardening work and Phase 5a/5b game-file
constants work are implemented. Current behavior is documented in
`docs/architecture.md`, `docs/context-modules.md`, `docs/cli.md`,
`docs/opendota-cache.md`, and `docs/game-files-snapshot.md`.

Historical design specs were archived on 2026-04-28:

- [docs/archive/specs/2026-04-26-hero-authoring-context-hardening.md](archive/specs/2026-04-26-hero-authoring-context-hardening.md)
- [docs/archive/specs/2026-04-26-pr3-ability-talent-context.md](archive/specs/2026-04-26-pr3-ability-talent-context.md)
- [docs/archive/specs/2026-04-27-game-files-as-primary-constants.md](archive/specs/2026-04-27-game-files-as-primary-constants.md)

## Notes

- Retrospective brainstorm/decision notes:
  [docs/notes/](notes/)
- **OpenDota constants staleness** (not patch-versioned, silently drifts after patch):
  [docs/notes/2026-04-26-opendota-constants-not-patch-versioned.md](notes/2026-04-26-opendota-constants-not-patch-versioned.md)
- **Legacy OpenDota constants cache payloads**:
  [docs/notes/2026-04-28-opendota-constants-cache-legacy.md](notes/2026-04-28-opendota-constants-cache-legacy.md)
- **Game-file overlay design exploration** (superseded; retained as design note):
  [docs/notes/2026-04-27-game-file-overlay.md](notes/2026-04-27-game-file-overlay.md)
- **Localization lookup follow-ups**:
  [docs/notes/2026-04-27-localization-lookup-followups.md](notes/2026-04-27-localization-lookup-followups.md)
- **Bootstrap role revision discussion**:
  [docs/notes/2026-04-28-bootstrap-role-revision.md](notes/2026-04-28-bootstrap-role-revision.md)

## External input

- Expert review feeding the pivot:
  [docs/tmp/expert_review/review.md](tmp/expert_review/review.md)

## Current intent

The project shifted away from the old relation path:

- no longer optimize around STRATZ-selected pair reasoning
- use stats as evidence, not ontology
- validate the KG direction on a small benchmark before scaling
- keep only low-regret infrastructure work from the old plan

## Archive

Superseded specs and plans live under [docs/archive/](archive/) with a `Status: superseded by …` header. They are not part of the active set — read them only when investigating *why* a decision was made, not to derive current behavior. See `GUIDELINES.md` → "Doc Lifecycle".
