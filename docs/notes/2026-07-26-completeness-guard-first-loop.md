# Completeness Guard: First Feedback-Loop Iteration

Date: 2026-07-26
Status: recorded result
Spec: `docs/specs/2026-07-26-generation-completeness-gates.md`

## Loop

guard report → prompt change → regenerate → guard again. One iteration,
codex backend (`gpt-5.6-sol`) generating and guarding (fresh sessions).

## Numbers

| artifact | v4 flags | v5 flags | citations | words |
|---|---|---|---|---|
| codex evasion | 44 | **0** (clean ×2) | 11/19 → 19/19 | 436 → 3424 |
| codex random_distribution | 122 | **0** (clean ×2) | 8/13 → 12/13 | 315 → 2520 |
| codex mage_slayer (item prompt) | 0 | — | — | — |
| claude evasion (canonical, v4) | 14 | not regenerated | 19/19 | 1440 |

Claude-vs-codex guard agreement on identical artifacts: 15 vs 14
(claude canonical) and 39 vs 44 (codex v4 evasion) — the verdict is
guard-model-robust, and gpt flags its own model's output freely.

## Reading

- The v4 concept prompt's "concise reference prose" was the cause of the
  codex completeness gap, not model capability: with v5 demanding
  lossless compression and full enumerations, gpt-5.6-sol covers the
  packet completely in one shot. The item prompt (already structural)
  was clean before and needed nothing.
- The trade moved to length: v5 codex articles run ~2× the claude v4
  baseline (which itself carries 14-15 flags of dropped enumerations, so
  some growth is legitimate content). Whether archive articles this size
  cost too much at serving time is the serving-format spec's question,
  measured there — not a completeness question.
- Two consecutive clean guard passes per artifact; per spec, evidence
  not proof.

## Open

- Regenerate the canonical (claude) concepts under v5 and guard — decides
  whether the canonical KB gets the same treatment (per-artifact user
  decision).
- Battery over the v5 variant KB with answerer/judge held constant
  (Part 1 behavioral gate) once the user's skim passes the v5 articles.
- The claude-cli input-token recording fix (spec task 1) remains open.
