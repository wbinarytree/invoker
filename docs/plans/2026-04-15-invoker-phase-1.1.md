# Invoker Phase 1.1 — Stabilization Plan

Status: Draft
Date: 2026-04-15
Scope: Close the Phase 1 operational gaps discovered during initial real-world trials before moving to Phase 1.5 or Phase 2.

## Goal

Phase 1 gave us the skeleton of a patch-aware hero knowledge base. Phase 1.1 is about making that skeleton usable:

- subset bootstrap must be practical to run
- LLM-backed steps must be observable, recoverable, and cheap to rerun
- source extraction must be trustworthy enough for manual inspection
- partial runs must not waste quota or produce silent confusion

This is not a schema-expansion phase. It is a reliability and operator-experience phase.

## Exit Criteria

We consider Phase 1.1 done when all of the following are true:

1. `invoker bootstrap --patch <v> --heroes <id,id>` is a dependable way to trial 1-2 heroes end to end.
2. Manual mode is usable without stack traces or guesswork.
3. LLM retries, pacing, and cache behavior are visible and do not waste prior successful work.
4. A failed reason does not kill a hero, and a failed hero does not kill the whole subset run.
5. Ability extraction for known-problem heroes like Puck produces sane core spell text.
6. Rerunning the same subset after partial success reuses prior successful LLM outputs.

## Workstreams

### 1. Hero-Limited Bootstrap Completion

Why:
We now have a subset bootstrap path, but it is still only suitable for controlled testing. It must become the supported Phase 1 operator path.

Tasks:

- [ ] Wire `bootstrap --heroes ...` into the real current pipeline.
- [ ] Mark subset runs as `partial`.
- [ ] Propagate `force` through source fetchers.
- [ ] Add explicit CLI messaging about what subset mode does and does not populate.
- [ ] Add a small success summary at the end:
  - heroes requested
  - heroes written
  - heroes skipped
  - reasons written
  - reasons skipped

### 2. LLM Pacing, Retry, and Budget Controls

Why:
The first Gemini trials immediately hit RPM and then daily quota issues. The system cannot depend on users discovering provider limits through failures.

Tasks:

- [ ] Add proactive Gemini pacing for the known free-tier `5 RPM` cap.
- [ ] Add bounded retry/backoff for quota-style responses.
- [ ] Add explicit reason-budget controls:
  - `--skip-reasons`
  - or `--max-reason-edges <n>`
- [ ] Distinguish high-value and low-value retries:
  - extraction may retry more
  - reasons should retry less
- [ ] Surface estimated request count before subset bootstrap begins.

### 3. LLM Response Cache

Why:
We already burned quota on successful calls that were not reused. This is the biggest remaining operational flaw.

Tasks:

- [ ] Add an on-disk cache for successful LLM responses at the `LLMClient` boundary.
- [ ] Key cache entries by:
  - provider/model
  - prompt version
  - rendered prompt hash
- [ ] Store cache under `data/cache/llm/`.
- [ ] Emit trace lines for:
  - request
  - cache hit
  - retry
  - final failure
- [ ] Ensure repeated subset reruns reuse extraction and reason outputs automatically.

### 4. Recoverable Pipeline Semantics

Why:
Today the pipeline is still too all-or-nothing. One failure can waste earlier successful work.

Tasks:

- [ ] If extraction fails for one hero after retries:
  - log it
  - skip that hero
  - continue remaining heroes
- [ ] If one reason call fails:
  - omit that reason
  - still write the hero artifact
- [ ] Persist successful hero output even when some reasons are missing.
- [ ] Finalization should still run for successfully written heroes.
- [ ] Manifest should reflect partial success honestly.

### 5. Manual Mode UX

Why:
Manual mode currently writes prompts and then crashes with a traceback. That is not a usable operator workflow.

Tasks:

- [ ] Catch manual-response-missing errors in the CLI.
- [ ] Replace stack traces with direct instructions:
  - prompt path
  - response path
  - rerun guidance
- [ ] Show which hero and stage generated the prompt:
  - extract
  - synergy reason
  - counter reason
- [ ] Make rerunning the same command continue cleanly once the response file exists.
- [ ] Add a manual-mode smoke test through the CLI, not just the client helper.

### 6. Source Quality: Ability Extraction

Why:
The Puck trial showed the current Liquipedia spell extraction is not reliable enough. Bad source text poisons the prompt before the LLM even starts.

Tasks:

- [ ] Fix `LiquipediaFetcher.extract_abilities()` so it prefers the main spell description.
- [ ] Exclude or separately handle:
  - alt-cast notes
  - shard/scepter upgrade text
  - unrelated nested fragments
- [ ] Add a regression fixture/test for the Puck page.
- [ ] Add at least one more tricky-hero parser regression test after Puck.
- [ ] If Liquipedia extraction is incomplete, prefer a cleaner fallback from OpenDota ability descriptions where possible.

### 7. LLM Call Tracing

Why:
We need to know what the pipeline is doing before and during provider calls.

Tasks:

- [ ] Add structured trace lines around each LLM-backed stage.
- [ ] Include:
  - stage
  - hero id
  - hero name
  - relation type when relevant
  - other hero id when relevant
  - cache hit / request / retry / fail
- [ ] Keep output concise enough to read during subset bootstrap.

### 8. Reason Generation Quality Baseline

Why:
Even within Phase 1, relation reasoning is weaker than advertised because the second hero context is not properly provided.

Tasks:

- [ ] Pass real second-hero name and tags into reason generation for subset runs where data is available.
- [ ] Tighten reason validation toward grounding in both sides, not only hero A.
- [ ] Add tests for the improved reason input path.

This remains Phase 1.1 because it is a quality correction to an existing feature, not a new drafting-context schema.

### 9. No-Data Contract Fixes

Why:
The repo rules say absence should be explicit, but the current derive path still drops zero-game edges.

Tasks:

- [ ] Emit explicit no-data edges where the Phase 1 contract says they should exist.
- [ ] Add a validator or regression test that protects this behavior.

## Deliberately Deferred To Later Phases

These came up in review, but they are not Phase 1.1 work:

- role-aware / lane-aware / archetype-aware relation schema
- breakpoint / threshold artifact family
- team identity backoff layers
- player affinity artifacts
- lane template nodes
- draft-trait taxonomy expansion
- vector index work
- Phase 1.5 or 2 consumer-facing drafting logic

## Recommended Order

1. LLM response cache
2. Recoverable pipeline semantics
3. Manual mode UX
4. Ability extraction fix with Puck regression
5. Reason budget controls
6. LLM tracing polish
7. Reason generation quality correction
8. No-data contract fix

Rationale:
cache + recoverability stop quota waste first; manual mode and source quality make the system operable; quality corrections come after the pipeline stops wasting work.
