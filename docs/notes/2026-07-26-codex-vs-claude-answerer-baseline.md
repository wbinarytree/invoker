# Codex vs claude-cli Answerer: First Baseline Comparison

Date: 2026-07-26
Status: recorded result (engineering-grade, N=2 per arm — large effects only)
Spec: `docs/specs/2026-07-26-serving-format-measurement.md` (backend
comparison; the mark-density A/B is a separate experiment)

## Setup

One condition varied: the answerer backend. Judge held constant at
`claude-cli`/`claude-opus-5` in all four runs. Full 5-case basic-QA
battery, 2 runs per arm, same KB (`kb_sha256 47767a66…`), changelog
available.

- **codex arm**: answerer `codex-app-server`/`gpt-5.6-sol`
  (runs `20260726-143650-134366`, `20260726-143942-471013`)
- **claude arm**: answerer `claude-cli`/`claude-opus-5`
  (runs `20260726-143651-671582`, `20260726-143925-833554`)

Input identity held: within each arm, every case's `qa-select`
`request_sha256` is identical across repeats. All divergence below is
sampling behavior, not input drift.

## Results

| case | codex#1 | codex#2 | claude#1 | claude#2 |
|---|---|---|---|---|
| corrosive-haze | resolution-miss | resolution-miss | resolution-miss | resolution-miss |
| facet-removal | PASS | PASS | PASS | PASS |
| mage-slayer | fact-missing | PASS | PASS | PASS |
| pseudo-random-distribution | PASS | fact-missing | PASS | PASS |
| uphill-miss | resolution-miss | resolution-miss | over-length (126w) | over-length (135w) |
| **battery** | **2/5** | **2/5** | **3/5** | **3/5** |

## Reading

- **Shared true miss.** corrosive-haze resolution-misses in both arms,
  every run — the KB has no ability artifacts yet. Cross-backend
  agreement on the gap is the expected demand signal, working.
- **Complementary failure directions on the same rails.**
  `gpt-5.6-sol` errs *terse*: answers run 40-48 words (vs 88-135 for
  opus), and that brevity drops required facts — mage_slayer's 3100-gold
  price in one run, PRD's "used instead of true random" framing in the
  other. It also declines selection outright: on "What is uphill miss?"
  its `qa-select` returned empty in 3 of 4 tries today (2 battery runs
  here + 2 single-case runs during backend verification; 1 pass).
  `claude-opus-5` errs *verbose*: it reliably opens the evasion article
  for the same question, then composes past the 120-word cap both runs.
  Same inputs, opposite failure modes.
- **Token accounting is now half-real.** The codex arm records true
  input tokens: ~114k per battery run, dominated by the ~13-14k/call
  harness floor (8 answerer calls). Real output: 662-924 tokens/run.
  The claude arm again recorded a nonsense 18 input tokens per battery —
  live re-confirmation that spec task 1 (claude-cli input-token
  recording) is still open. Claude output: 1698-2280 tokens/run.

## Implications

- Neither backend is "better" at N=2; they trade fact-completeness
  against length discipline. The compose prompt's "fewest words that
  answer completely" instruction lands differently per model — worth
  remembering when reading any cross-backend experiment: answerer-model
  effects are large relative to the serving-format effects the harness
  will probe.
- For serving-format A/Bs on the codex backend, the select flakiness on
  uphill-miss means per-case repeats must tolerate resolution-miss noise
  or condition on successful selection.
- claude arm's uphill-miss over-length (126/135 vs 120) is a baseline
  behavior of the current answerer prompt, not a codex-work regression;
  it predates any serving-format change and is visible only because the
  battery was re-run today.
