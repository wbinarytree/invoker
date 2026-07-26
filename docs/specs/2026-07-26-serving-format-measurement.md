# Serving-Format Measurement Harness (+ Codex backend)

**Date:** 2026-07-26
**Status:** accepted 2026-07-26 (user direction: build the Codex backend
first); task 2 landed — see amendment 1
**Direction:** `docs/specs/2026-07-25-grounded-reasoner-rethink.md` (the
benchmark is the detector; validate before scaling)

## Outcomes

- Serving-format questions ("does mark density / card length / packet size
  hurt the model?") become measurable experiments on the existing benchmark
  rails instead of design debates. First application: inline-mark density
  before the hero slice commits to a kit-wide article format.
- Deterministic token accounting answers the cost half for free, including
  a hero-scale projection **before** the hero generator exists.
- A Codex app-server generation backend lets experiments run on the user's
  Codex token budget instead of the Anthropic one.

## Motivation (measured 2026-07-26)

Marks are 27% of the mage_slayer article body by characters, 32% of a
composed benchmark answer, 12% across all current KB serving bodies. The
agent-exposure model already budgets ~15 tokens/key (generators spec).
Whether that overhead ever hurts *behavior* is unmeasured — and the
`claude-cli` transport does not record real input token counts (33 calls
reported 66 input tokens total), so serving cost is currently invisible.

## Scope

Three measurement tiers plus two prerequisites. In:

1. **Prerequisite: real input-token recording.** Fix the `claude-cli`
   transport to record actual input tokens in `GenerationProvenance`;
   `null` when the transport genuinely does not report them — never an
   estimate stored as a count.
2. **Prerequisite: Codex backend.** A `GenerationBackend` implementation
   over the locally installed Codex CLI (observed 2026-07-26,
   codex-cli 0.139.0: `codex exec` — stable, per-call subprocess — and
   `codex app-server` — experimental persistent daemon). User direction
   is the app server; since an experiment makes many short calls, the
   daemon amortizes startup. Implementation order: pin the app-server
   protocol against the installed binary; fall back to `exec` only if
   the experimental surface proves unstable, recording which transport
   served each call. Same contract as `ClaudeCliClient`:
   `generate`, `generate_structured` (JSON validated against the pydantic
   model, `GenerationError` on mismatch — surfaced, never silently
   retried), provenance with `transport: "codex-app-server"`, model id as
   reported, token counts as reported or null. Runner/CLI grow per-role
   backend selection (answerer/judge/generator) — the judge is held
   constant within any experiment; only the condition under test varies.
3. **Tier 0 — deterministic accounting (no LLM).** A measurement command
   that reports, per KB artifact and per serving bundle (question + N
   articles): chars/estimated tokens total, mark share, distinct keys,
   key-length distribution. Plus a hero-scale projection: stitch a hero's
   existing kit contexts (ability/talent/stat modules — no hero generator
   needed) into a pseudo-serving-document at the observed marks-per-section
   density and report the same numbers.
4. **Tier 1 — serving-variant A/B.** A serving-transform hook in the
   answerer (function applied to article text before compose, recorded in
   provenance) and repeat-N runs with an aggregated report. First
   experiment: identity vs reference-compressed marks (`[1]`,`[2]` +
   legend, mechanically reversible — answers expand back before scoring)
   vs marks-stripped (attention ceiling; facts-only scoring). Metrics:
   fact verdicts, expected-mark hits, word counts, token counts.
5. **Tier 2 — density probes at hero scale.** Probe QA cases against the
   Tier-0 pseudo-document targeting mid-document facts
   (retrieval-under-density). Gold fields derived mechanically from the
   packet; user skim is the gate before any probe case is trusted.

Out of scope: adopting ref-compression or any serving change (separate
decision after data); the hero generator itself; treating small-N results
as statistics (below).

## Constraints

- **Decision rules fixed before running, not after.** Agreed 2026-07-26:
  under ~15% mark share at hero scale — no action; over ~30% — adopt
  serving-side ref-compression on cost grounds alone. A/B rule: if
  compression changes no fact verdicts across N runs and saves ≥25%
  serving tokens, adopt for serving; if inline marks degrade any fact
  retrieval at hero scale, adopt immediately.
- **Small-N honesty.** 4 answerable cases with nondeterministic compose
  (observed ±10-word swings on byte-identical input) detect only large
  effects. Results are engineering-grade evidence for the decision rules
  above, nothing more.
- The archive format is canonical and does not change: all variants are
  serving-time transforms, mechanically reversible where marks must
  survive.
- Cross-model comparability: an experiment varies exactly one thing.
  Backend changes and serving-transform changes are separate experiments.
- Token estimates (when a transport reports none) are labeled estimates;
  never stored in provenance count fields.
- Cost gate: rough order for the first A/B is N=8 × 4 cases × 2
  conditions ≈ 15 battery-equivalents; runs on the Codex backend per the
  user's token budget. Estimate cost from Tier-0 numbers before running.

## Prior decisions adopted

- Marks-not-verdicts and the ~15-token/key budget (generators spec).
- Benchmark-as-detector; provenance `request_sha256` as input-identity
  proof (used 2026-07-26 to separate sampling variance from causation).
- Null over placeholder; no silent retries; LLM output validated and
  surfaced (GUIDELINES hard lines).

## Task breakdown

1. Input-token recording in `claude-cli` transport (+ test).
2. `CodexClient` backend + per-role backend selection in runner/CLI
   (+ tests with a fake transport; live smoke against the installed CLI).
3. Tier-0 measurement command + hero-scale projection.
4. Serving-transform hook + repeat-N aggregation in the runner.
5. First experiment: mark-density A/B per the decision rules; result
   recorded in a `docs/notes/` retro note.
6. Tier-2 probe doc + probe cases (user-gated) — entry gate for the hero
   slice's article-format decision.

## Verification

- Tier-0 numbers reproduce the hand-measured 2026-07-26 figures for the
  current KB (27% / 32% / 12%).
- A/B provenance shows identical `request_sha256` within a condition's
  repeats (same input) and differing across conditions.
- Codex backend: benchmark battery completes with judge held constant;
  provenance records the transport and reported token counts.
- Experiment note in `docs/notes/` states the decision-rule outcome, not
  just raw numbers.

## Amendment 1 (2026-07-26): Codex backend landed

Task 2 built as `CodexClient` (`src/invoker/gen/codex.py`) over
`codex app-server`, protocol pinned against codex-cli **0.145.0**
(upgraded from the 0.139.0 observed at spec time — the target model
`gpt-5.6-sol`, now the backend default, needs ≥0.145). No `exec`
fallback was needed; `transport: "codex-app-server"` is recorded per
call. Findings from pinning live:

- The daemon reports real per-turn token counts
  (`thread/tokenUsage/updated`), including cached input — the counts the
  `claude-cli` transport cannot see. Prerequisite 1's provenance side
  landed as `input_tokens`/`output_tokens` becoming nullable; the
  `claude-cli` recording fix itself is still open.
- Codex injects a ~13-14k input-token harness floor per call even with
  `baseInstructions` replaced, MCP servers disabled, and an empty cwd.
  Constant within an experiment, so A/B comparisons hold; subtract it
  from absolute serving-cost numbers.
- The native `outputSchema` constraint runs OpenAI strict mode; schemas
  are mechanically adapted (objects closed, all properties required) at
  the transport boundary, with client-side pydantic validation unchanged.
- The user's `~/.codex/config.toml` default model must never be
  inherited: the backend pins `model` explicitly and refuses thread-echo
  mismatches and mid-turn reroutes.
- Verified end-to-end 2026-07-26: uphill-miss ran twice with both roles
  on codex — identical qa-select `request_sha256` across runs, one
  resolution-miss and one pass, confirming sampling variance separated
  from input identity exactly as the small-N honesty constraint expects.
