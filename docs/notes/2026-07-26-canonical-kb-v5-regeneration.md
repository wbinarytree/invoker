# Canonical KB Under v5: Guard Reports and Regeneration

Date: 2026-07-26
Status: recorded result
Spec: `docs/specs/2026-07-26-generation-completeness-gates.md` (tasks 1, 5)

## Loop

Canonical (claude-cli/claude-opus-5) artifacts guarded once on
codex/gpt-5.6-sol (task 5), reports skimmed, user decision: regenerate
all three under the v5 prompts. Generation through the full gate stack —
marks, coverage (new, task 1), numbers, then the fresh-session guard.

## Numbers

| artifact | pre-v5 flags | v5 flags | coverage | body words |
|---|---|---|---|---|
| random_distribution | 37 | **0** | 12/13 (References exempt) | ~2717 |
| mage_slayer | 4 | **0** | 6/6 (lore line, prompt v5) | ~206 |
| evasion | 14 | **1** | 19/19 | ~2959 (was ~1440) |

Decision-rule outcome (spec verification): v5 on the incumbent backend
cuts the claude evasion flag count 14 → 1 — near-zero on enumerations,
target met. The pre-v5 reports are in git history (acceptance evidence
for the regeneration decision); the committed `completeness.json` files
are the current verdicts.

With the claude-cli token fix, article-call input tokens are real for
the first time: 12,536 (evasion) / 10,374 (random_distribution) /
2,771 (mage_slayer).

## The surviving evasion flag

`#Accuracy`: "Average DPS increase of Accuracy against Evasion up to
35%." — the packet line is an image caption whose chart did not survive
corpus extraction; no DPS data exists in the packet behind it. The same
flag appeared in the pre-v5 report (persistent, not sampling noise).
Regeneration cannot fix it and the article carrying a dangling caption
would add noise. Substrate-side chart/image extraction is the real fix,
out of scope here. Acceptance is the user's per-artifact call
(commit = acceptance).

## Behavioral gate (battery, same day)

Two runs on the v5 canonical KB, answerer/judge claude-cli/claude-opus-5
— identical config to the 2026-07-26 baseline claude arm (3/5 both
runs): **4/5 then 3/5** (runs `20260726-184504-502535`,
`20260726-184738-611754`). corrosive-haze resolution-missed every run
(no ability artifacts — the standing demand signal, unchanged).
uphill-miss composed 102/120 words (pass) then 131/120 (over-length) vs
the baseline's 126/135 — the known compose-length variance of the
answerer prompt, not a v5 effect. No fact verdict regressed; the ~2×
article growth did not measurably hurt retrieval or compose at N=2
(large effects only). Completeness-gates loop closed.
