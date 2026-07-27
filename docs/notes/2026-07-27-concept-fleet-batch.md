# Retro: Concept Fleet — Full 7.41d Corpus Generated on Codex

**Date:** 2026-07-27 (fleet ran the night of 2026-07-26)
**Spec:** `docs/specs/2026-07-26-batch-kb-generation.md` (+ amendments 1-2)

## Outcome

All 98 corpus concepts have artifacts: **86 guard-clean, 12 flagged,
0 failed, 0 unguarded**. 96 generated this run (2 canonical
pre-existed), every call on the codex backend (`gpt-5.6-sol` via
`codex-app-server`). Recorded spend on surviving artifacts + guards:
5.59M input / 0.95M output tokens; with failed attempts (~144 manifest
attempts total), roughly 8-9M input for the night. The 86 clean are
committed (acceptance); the 11 new flagged artifacts stay uncommitted
pending per-artifact review; canonical `evasion` keeps its known
caption flag.

## The iteration ladder

Failures arrived in layers; each got a versioned fix, never a silent
retry (rejects in `data/logs/rejected/`, attempts in
`data/logs/batch/`):

- **v6**: patch context leaked into article titles ("Aura (7.41d)") —
  patch is context, never stated. Numbers never derived/summed/counted.
- **v7**: cards counted table rows; articles expanded "3 to 9" ranges
  into integer lists.
- **Check: structural digits are not claims** — headings mirror source
  section titles ("Example 3") and ordered-list numbering is the
  model's own; both were false-positive aborts. Content stays checked.
- **v8**: the bare-`[KEY]` trap named (packet headers show the bare
  key; marks need the `corpus:` prefix); one-line sections still cited.
- **Packet hygiene**: degenerate sections dropped — a MediaWiki error
  string was the whole `creep_control_techniques` lead; a 20-char
  "Main Article: Rubick" stub was `cast_animation#Spell_Steal`.
  Coverage-forcing contentless sections invites fabrication; 4 passing
  artifacts that had been forced to cite stubs were regenerated.
- **v9**: consolidated stat tables may carry marks for every
  contributing section ("single narrowest" fought the attribute pages
  whose every "invented" number was in the packet, just misattributed).
- **v10**: marks FOLLOW the content they vouch for — `strength` failed
  5× (incl. effort high) because the model marked the table's intro
  sentence and `article_segments` attributed the table to the next
  segment. Correct by human convention, misread by the checker; both
  holdouts passed clean on the first v10 attempt.

## Operational lessons

- The circuit breaker paid for itself immediately (round 1: 11/17
  failures, 76 entities untouched) but consecutive-failure counting is
  completion-ordered: fast-failers finish first at high concurrency
  and can trip it before slower successes land.
- The session harness kills background commands around the 10-minute
  ceiling; the fleet ran as single-wave chunks (`--limit` ≈
  concurrency) with disk-state resume. Kills only ever cost in-flight
  calls.
- Rejected-output persistence turned every failure into evidence — the
  v10 diagnosis came straight from a preserved reject.
- Deterministic-looking failures deserve forensics before retries:
  every "chronic" page traced to a specific cause (broken substrate
  data, a checker convention, a prompt contradiction) and none needed
  more than one attempt once the cause was fixed.

## Open

- 12 flagged artifacts await per-artifact review (guard flags, 1-3
  each).
- Item run (290 in scope) deferred; inherits the driver, the check
  refinements, and the prompt ladder. Item scope enumerator and pilot
  design are in the spec.
- Guard-call floor optimization (batching small guards) noted in the
  spec before the item run.
