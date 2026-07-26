# Generation Completeness Gates (coverage check + compression guard)

**Date:** 2026-07-26
**Status:** accepted 2026-07-26 (user sign-off; guard-first order).
Tasks 2-4 landed the same day — guard, CLI wiring, prompt v5 with both
codex concepts regenerating to guard-clean. Task 1 (mechanical
citation-coverage check in `gen/checks.py`) landed 2026-07-26: verified
against the stored artifacts — codex v4 evasion fails with exactly its
8 missing sections, all three canonical artifacts pass (References
allowlisted), and both codex mage_slayer variants fail on the uncited
lore section (a drop the guard's load-bearing definition ignores).
Lore stays required, never allowlisted (user direction 2026-07-26: the
lore is the encyclopedia's fun and belongs in the record); item prompt
v5 demands a closing lore line so the gate is achievable on any
backend. Task 5 (guard the full canonical KB) remains open.
**Direction:** articles are lossless compressions of their packets.
Related: `2026-07-26-game-file-grounded-generators.md` (marks, packets),
`2026-07-26-serving-format-measurement.md` (backend experiments that
exposed the gap).

## Motivation (measured 2026-07-26)

Regenerating the KB on the Codex backend produced articles that pass
every existing gate while silently dropping content: the codex evasion
article cites 11 of 19 packet sections (counter-item enumeration, talent
ladder, cleave rules gone), and the current benchmark cannot see it —
all uphill-miss facts survive, so the battery would report a false tie.
Worse, a fresh-session LLM probe found the *canonical claude article*
also drops enumerable tails inside sections it cites (True Strike source
lists), invisible to citation counting and hard to catch by skim. Mark
faithfulness (nothing invented) is gated; compression losslessness
(nothing dropped) is not.

## Outcomes

- Two new generation gates, layered under the existing mark/number
  checks:
  1. **Citation coverage (mechanical):** every packet section is cited
     by the article, or generation aborts listing the missing sections.
  2. **Compression guard (LLM, fresh session):** a separate
     held-constant session compares packet to article and reports every
     packet fact absent from the article. Nonempty report → loud
     failure; a human reads the report and decides.
- Guard reports are **flat — no severity classes**. Absence is a
  checkable claim (each flag cites its packet section key); importance
  is not checkable and is not known beforehand (we do not know which
  mechanisms matter until questions hit them — user direction
  2026-07-26). The guard states what is missing, never what matters.
- The concept prompt is tightened so a clean pass is achievable: the
  mage_slayer measurement showed hard structural demands (item prompt)
  hold models within 10% of each other while the loose concept prompt
  diverges 4× — format constraints dominate model temperament.

## Scope

1. **Coverage check** in `gen/checks.py`, same shape as the mark check:
   set of packet section keys minus cited keys must be empty, minus a
   boilerplate allowlist (`References`). Runs for concepts and items.
2. **Compression guard** (`gen/guard.py`): one `generate_structured`
   call on a configurable backend (default `codex`/gpt-5.6-sol — the
   larger token budget, user direction 2026-07-26; must be a fresh
   session, never the generating conversation — fresh-session is the
   hard requirement, model choice is a budget call). Input: the exact
   packet the generator saw + the finished article. Output schema: flat
   `missing: [{section, fact}]`, validated; the report and its own
   `GenerationProvenance` are written as `completeness.json` next to the
   artifact. Every flag's `section` must be a real packet key or the
   guard output itself fails validation.
3. **Wiring:** `generate-concept`/`generate-item` run the guard after a
   successful write; nonempty report → exit 1, report path printed.
   `--skip-guard` opts out (experiments, cost control);
   `--guard-backend`/`--guard-model` override the default. A standalone
   `invoker guard-artifact <artifact.json>` re-guards any existing
   artifact (rebuilds the packet; if the rebuilt packet sha differs from
   the recorded one, say so in the report — the verdict is against
   today's substrate, not the generation-time packet).
4. **Concept prompt bump** (v5): every packet section must be
   represented; enumerations (source lists, talent ladders, value
   tables) are carried in full, as tables where the section is tabular.
   Card prompt unchanged.
5. **Calibration fixture:** the 2026-07-26 probe is the reference —
   codex evasion variant: 39 flags including 6/6 hand-verified section
   drops; claude canonical: 15 flags (real in-section losses). Any guard
   prompt change is re-run against these two stored artifacts and must
   keep the direction (codex ≫ claude) and recover the hand-verified
   drops. Live check, not CI — no LLM calls in tests.

## Constraints

- The guard is a detector, never a fact source or an editor: flags never
  modify articles, and a flagged generation is never silently
  regenerated (hard line). The human regenerates, amends the prompt, or
  accepts — committing the artifact is the acceptance act; there is no
  waiver machinery.
- No severity, no ranking, no "load-bearing" classification by the
  guard. If a run produces unreadably many flags, the fix is a better
  article or a better prompt, not a filter on the report.
- Nondeterminism honesty: flag lists vary between runs; a clean report
  is evidence, not proof. The report records model, transport, and
  request sha like any generation output.
- Guard cost is ~one article-generation call per artifact. Acceptable at
  current scale; the hero slice revisits.
- Existing-KB rollout: guard the current canonical artifacts once and
  record the reports; whether to regenerate them under the v5 prompt is
  decided per artifact by skim of the reports (no bulk regeneration
  without the user's go — destructive-action rule).

## Out of scope

- Severity/weighting taxonomies (rejected above).
- Auto-regeneration or repair loops on flags.
- Guarding answerer/benchmark output — that path already has the judge;
  this gate is generation-side only.
- Serving-format changes (separate spec).

## Task breakdown

1. Coverage check in `gen/checks.py` + wiring in both generators
   (+ tests; codex evasion variant is the natural failing fixture).
2. `gen/guard.py` + `completeness.json` shape (+ tests with fake
   backend: clean pass, flags, invalid section key, provenance
   recording).
3. CLI wiring: inline guard, `--skip-guard`, `--guard-backend`,
   `guard-artifact` command; docs (`architecture.md`, `cli.md`).
4. Concept prompt v5; regenerate evasion + random_distribution on both
   backends; gates + guard + skim; record flag-count deltas.
5. Guard the canonical KB once; reports reviewed by user skim.

## Verification

- Coverage check fails the stored codex evasion variant with exactly its
  8 missing sections and passes the claude canonical artifacts
  (References allowlisted).
- Guard calibration reproduces the 2026-07-26 direction on the two
  stored evasion artifacts.
- v5 prompt on the incumbent backend cuts the claude evasion flag count
  materially (target: near-zero on enumerations); result recorded in a
  `docs/notes/` retro note with the decision-rule outcome.
