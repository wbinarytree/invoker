# Invoker — Architecture (Implementation Artifact)

Last updated: 2026-04-17
Phase: 1.1 (near exit — see `docs/plans/2026-04-15-invoker-phase-1.1.md`; Phase 1.2 spec signed off, not yet implemented)

This document describes the actual current implementation. It is updated whenever an architectural decision changes. It is not a design spec — see `docs/specs/` for aspirational design. When the two conflict, this document reflects reality and the spec should be updated.

---

## Data Sources

| Source | What we use | Endpoint / Method |
|--------|-------------|-------------------|
| OpenDota | Hero list, roles, ability text, ability-hero mapping | `/api/heroes`, `/api/constants/abilities`, `/api/constants/hero_abilities` |
| OpenDota | Matchup win-rate stats | `/api/heroes/{id}/matchups` |
| STRATZ | Pro-match synergy/counter edges | GraphQL `matchUp` query (see below) |
| OpenDota | Pro match position counts, meta history | `/api/proMatches`, `/api/heroes/{id}/matchups` |

**Dropped:** Liquipedia (HTML scraping). Replaced entirely by OpenDota constants for ability text. Decision rationale: no HTML parsing, reliable structure, sufficient detail for LLM extraction.

---

## STRATZ GraphQL Query

Query name: `matchUp` (replaces the removed `heroVsHeroMatchup`).

```graphql
query MatchUp($heroId: Short!, $bracketIds: [RedisBracketBasicEnum]) {
  heroStats {
    matchUp(heroId: $heroId, bracketBasicIds: $bracketIds) {
      heroId
      with  { heroId2 synergy }
      vs    { heroId2 synergy }
    }
  }
}
```

Brackets used: `DIVINE_IMMORTAL`.

`flatten_edges(response, hero_id)` normalises the nested response into a flat list of dicts:
- `with` rows → positive synergy score (raw synergy value)
- `vs` rows → negated synergy score (win-rate advantage reversed to get counter score)

The query and bracket selection are not yet finalised — they will evolve as we learn which fields matter.

---

## LLM Layer

```
CachingLLMClient
  └── GeminiClient   (default for production)
  └── ManualClient   (for --manual / offline mode)
```

### CachingLLMClient (`src/invoker/llm/cache.py`)

Wraps any `LLMClient`. Before every call:
1. Compute `key = sha256(model_name + ":" + prompt_version + ":" + rendered_prompt)`
2. Check `data/cache/llm/<cache_tag>/<key[:2]>/<key>.json` (or `data/cache/llm/<key[:2]>/...` if no tag)
3. On hit: return cached response, strip any markdown fences, skip inner client entirely (no quota, no pacing wait)
4. On miss: call inner client, write response + rendered prompt to disk, return

Cache entry shape: `{text, model, prompt_version, cached_at, prompt}`. The `prompt` field makes entries human-readable and traceable without running the pipeline again.

`cache_tag` is an optional human-readable path segment (e.g. `extract/Slardar`, `reason/Axe`) that groups related entries into subdirectories.

Logging uses the standard library `logging` module with per-module loggers (`getLogger(__name__)`).
`invoker.logging.configure_logging()` sets handlers/formatters centrally; application code logs through normal `logger.debug/info/warning/exception(...)` calls.

### GeminiClient (`src/invoker/llm/gemini.py`)

- Configured by `GeminiModelConfig(model, rpm, rpd)`. Two named constants:
  - `GEMINI_2_5_FLASH` — `gemini-2.5-flash`, RPM=5, RPD=20
  - `GEMMA_4_31B` — `gemma-4-31b-it`, RPM=15, RPD=1500
- `make_model_config(model, rpm, rpd)` is a thin env-var adapter; the client no longer carries a per-model capability registry.
- **HTTP timeout:** client is constructed with `http_options={"timeout": 120_000}` (120 s). Calls that stall at the network level raise a timeout exception rather than hanging indefinitely.
- **JSON output:** every request sets `response_mime_type="application/json"`. When `schema` is provided, the same request also sets `response_schema=schema` so the API enforces the JSON shape. Markdown fences are stripped from all responses via `strip_fences()`.
- Class-level rate limiter enforces the RPM ceiling proactively (min interval = 60/rpm + 0.5 s). Pacing, requests, successful generations, empty responses, and retries are all emitted through the module logger.
- Retry: up to 3 retries.
  - Quota / rate errors (`429`, `ResourceExhausted`): exponential backoff starting at 65 s, doubling each attempt.
  - Timeout errors: fixed 20 s delay before retry.
  - All other errors: re-raised immediately (no retry).
- **Empty response handling:** when `resp.text` is empty, returns `LLMResponse(text="")` and caches it to prevent the same quota-burning call on the next run. Callers receive a Pydantic `ValidationError` when they attempt to parse the empty text.
- Model is selected at runtime via `INVOKER_LLM_MODEL` / `INVOKER_LLM_RPM` / `INVOKER_LLM_RPD` env vars (see Config).

### ManualClient (`src/invoker/llm/manual.py`)

File-based LLM loop for rate-limit emergencies and spot-checks.

- `bootstrap --manual` selects it for a single run (also available via `INVOKER_LLM_CLIENT=manual`).
- Prompts are written under `data/raw/manual_prompts/<cache_tag>/<hash>.md` and expected responses under `data/raw/manual_responses/<cache_tag>/<hash>.txt`; `cache_tag` comes from the caller (e.g. `extract/Slardar`, `reason/Axe`) and groups files by stage + hero. The prompt file starts with `<!-- cache_tag: ... prompt_version: ... -->` so a reader can tell what produced it.
- When the response file is missing the client raises `PendingManualResponseError` carrying both paths. The orchestrator catches it and marks the hero as `failure_reason="pending_manual"` (extract stage) or records the pending reason path on the successful hero result (reason stage). The CLI aggregates all pending paths into a single paste-and-rerun block at the end of the run — no traceback is surfaced to the operator.
- `CachingLLMClient` forwards `cache_tag` to the inner client, so the layout above works through the cache wrapper.

---

## Pipeline Stages

```
fetch → bundle → extract → derive → reason → assemble → write → summarize → finalize
```

### fetch (`pipeline/fetch.py`)

Fetches raw data from all sources:
- OpenDota: hero list, abilities dict, hero→ability map, pro matches, per-hero matchups
- STRATZ: `matchUp` edges per hero (optional; skipped if unavailable)

When `hero_filter` is set, per-hero calls (matchups, STRATZ) are restricted to the filtered set. Global calls (hero list, abilities, pro matches) always run.

Returns `hero_names: dict[int, str]` built from the **full pre-filter roster** so downstream stages can look up names for edge heroes that aren't in the filtered set.

The fetch layer also emits source-cache and source-request log lines from `CachedClient`, so bootstrap logs show when a call was reused from disk versus sent over the network.

`CachedClient` keys payloads on `(source, method, url, params, body)` and writes them to `data/raw/<source>/<patch>/<key>.json`. Cache is reused across runs unconditionally; there is no CLI flag to bypass it. To force a refetch for a specific endpoint, delete the matching file (or the patch subtree) and rerun. The `force=True` kwarg on `CachedClient.get/post` exists for a future targeted-refresh command and is not wired to any user-facing flag today.

### bundle (`pipeline/bundle.py`)

Converts `fetch_all` output into `HeroRawBundle` objects for the orchestrator.

- Resolves each hero's abilities by joining `hero_abilities` map → `abilities` dict, keeping only entries with a display name and description.
- Passes through per-hero matchups and STRATZ edges.
- Meta stats (`position_counts`, `contest_rate`, `win_rate`, `meta_history`) are still placeholders for now because the current bootstrap path does not derive them from `pro_matches`. This is a known Phase 1.1 gap, not a settled contract.

### extract (`pipeline/extract.py`)

Calls the LLM with prompt `extract_mechanical_tags` (version tracked in frontmatter).
Input: `HeroExtractionInput(hero_id, hero_name, roles, abilities)`
Output: `MechanicalExtraction` with `functional_tags`, `tag_sources`, and full provenance.

Provenance stored: `model`, `prompt_version`, `prompt_hash`, `input_hash`, `extracted_at`.

### derive (`pipeline/derive.py`)

Pure computation from raw stats:
- `merge_matchups`: merges STRATZ edges and OpenDota matchups into unified `StatEdge` list
- `meta_tier`: classifies hero into tier based on contest_rate and win_rate
- `position_weights`: normalises position count dict to weights

### reason (`pipeline/reason.py`)

Single prompt: `edge_reasons_batch`.

All synergy and counter edges for a hero are batched into **one LLM call** per hero.
Hero A name and tags appear once in the prompt header; each edge item carries hero B info,
relation type, score, and game count. The model returns a JSON array parallel to the input.

Only `med` and `high` confidence edges are included. Edges are capped to `max_edges`
(default 5) per relation before batching — lists are already sorted by `|score|` descending
so the highest-signal edges are always kept.

Heroes appearing in both the synergy and counter candidate lists are excluded from the counter
list to prevent duplicate `hero_b_id` values in the batch prompt.

Hero B names are resolved from the written hero file if available, falling back to the full
roster `hero_names` map from `fetch_all`. Placeholder names like `hero_55` must be avoided —
thinking models enter infinite ID-verification loops when names are missing.

Call budget: `1 extract + 1 batch reason = 2 calls per hero`.

Grounding check: `validate_grounding(reason, a_tags, b_tags)` — rejects any item whose
reason cites no tag from either hero. Failing items are skipped; the rest are kept.

Batch validation is strict: the returned `hero_b_id` list must exactly match the input
edge order. Duplicate ids, missing ids, or reordered ids fail the whole batch.

### assemble (`pipeline/assemble.py`)

Combines all stage outputs into a `HeroDerived` model. No LLM calls.

### write / summarize (`pipeline/writer.py`, `pipeline/summarize.py`)

Writes `data/derived/<patch>/<hero_id>.json` and a human-readable summary.

### finalize (`pipeline/orchestrator.py:finalize_patch`)

Runs after all heroes are written:
1. Validates each written hero against `ValidationContext`
2. Builds and writes the patch manifest
3. Builds and caches the hero graph

---

## Known Gaps (Phase 1.2)

The current orchestrator runs extract → reason → write per hero in a single sequential pass. This means hero B's functional tags are often unavailable when hero A's reason batch runs (hero B hasn't been extracted yet). Consequences:

- All `hero_b_tags` in the reason prompt show `(no tags)`, forcing the model to ground every reason in hero A's tags only.
- When hero A has relational tags like `physical_damage_amplifier`, the LLM has no context for what hero B offers and may enter a thinking loop, returning an empty response.

Phase 1.2 will split the orchestrator into two explicit passes (extract all → reason all) and add a guard that skips the reason batch when no hero_b has tags. It will also introduce a `tag_affinity.py` module so that extracted tags supplement Stratz/OpenDota as a candidate source. See `docs/specs/2026-04-17-phase-1.2-pipeline-correctness.md`.

---

## Error Recovery

`run_for_hero()` returns `HeroResult(hero_id, success, reasons_written, reasons_skipped, failure_reason)`.

- Extraction failure → log, return `success=False`, continue next hero
- Reason failure → log, increment `reasons_skipped`, continue other reasons
- Hero still written even with missing reasons

`finalize_patch` only processes heroes whose output files exist — partial runs don't block finalisation.
The manifest is marked `complete` only when there is no hero filter and every requested
hero succeeded. Filtered runs and failed full-roster runs both write `partial`.

---

## Output Schema (`HeroDerived`)

Key fields:

| Field | Type | Notes |
|-------|------|-------|
| `hero_id` | int | OpenDota hero id |
| `roles` | list[str] | From OpenDota `/api/heroes` |
| `functional_tags` | list[str] | LLM-extracted from ability text |
| `tag_sources` | list[TagSource] | Evidence quotes for each tag |
| `positions` | dict[str, PositionBlock] | Keyed by context (e.g. `"pro"`) |
| `synergies` | dict[str, list[StatEdge]] | Keyed by context |
| `counters` | dict[str, list[StatEdge]] | Keyed by context |
| `meta` | dict[str, MetaBlock] | Keyed by context |
| `provenance` | Provenance | `mechanical` + `statistical` sub-dicts |

`schema_version` is bumped on breaking schema changes.

---

## Config and Environment

`Config.load()` calls `load_dotenv()` first, so `.env` in the project root is honoured by the CLI. Required env vars: `GOOGLE_API_KEY` (for Gemini client), `STRATZ_API_KEY` (optional; STRATZ works without auth but at lower rate limits).

`INVOKER_LOG_LEVEL` controls process logging. The CLI configures the root logger at startup and defaults to `INFO`.

### Dev Hero Filter

Gemini free tier caps at 20 calls/day. To avoid burning quota during development, a hero filter limits which heroes receive per-hero API calls and LLM extractions.

Two ways to set it (CLI flag takes precedence):

| Method | Example |
|--------|---------|
| `INVOKER_DEV_HEROES` env var | `INVOKER_DEV_HEROES=Pangolier,Slardar` in `.env` |
| `--heroes` CLI flag | `invoker bootstrap --patch 7.41b --heroes "Pangolier,Slardar"` |

Accepts hero **names** (case-insensitive) or numeric **ids**. The global hero roster fetch still runs (single cached call); only per-hero calls (matchups, STRATZ synergies) and LLM extractions are restricted. No filter = all heroes (production behaviour unchanged).

Milestone gate: Pangolier + Slardar pass `invoker validate` before full bootstrap is attempted.

### Bootstrap CLI options

| Flag | Effect |
|------|--------|
| `--patch` | Required. Patch string, e.g. `7.41b`. |
| `--heroes <ids-or-names>` | Subset mode. Overrides `INVOKER_DEV_HEROES`. Manifest is written as `partial`. |
| `--skip-extract` | Reserved flag; currently a no-op pending hook into the extract stage. |
| `--skip-reasons` | Write heroes with stat edges only — no reason LLM call at all. |
| `--max-reason-edges N` | Cap edges fed to the batch reason call per relation per hero (default 5). |
| `--manual` | Force the manual file-based client for this run. |

Before the orchestrator loop runs, bootstrap prints a worst-case LLM call estimate (`heroes × (1 extract + 1 reason)`; `1` when `--skip-reasons`) so the operator can compare it against the daily quota. At the end of the run it prints an aggregate summary (heroes requested / written / failed, reasons written / skipped) plus per-hero failure reasons, and — in manual mode — a paste-and-rerun block listing every pending prompt path.

---

## Prompts

All prompts live in `src/invoker/prompts/` as `.md` files with a `<!-- prompt_version: N -->` comment on line 1. The version is parsed at load time and included in cache keys and provenance. Changing a prompt text without bumping the version will produce stale cache hits — always bump the version when changing prompt logic.

## Test Layout

Tests live outside the package under `tests/` and mirror the source tree under `tests/invoker/...`.
Shared builders and helpers live in `tests/support/`, and recorded payloads remain in `tests/fixtures/`.
Pytest runs in `importlib` mode so mirrored test modules do not rely on path-based imports.

---

## Cache Layout

```
data/
  raw/
    <source>/           # opendota, stratz
      <patch>/
        <key>.json      # CachedClient payload; key = sha256(method,url,params,body)[:16]
    manual_prompts/     # manual LLM mode
      <cache_tag>/
        <hash>.md
    manual_responses/
      <cache_tag>/
        <hash>.txt
  cache/
    llm/
      <tag>/            # optional; e.g. extract/Slardar, reason/Axe
        <key[:2]>/
          <key>.json    # {text, model, prompt_version, cached_at, prompt}
  derived/
    <patch>/
      <hero_id>.json    # HeroDerived
      summary_<hero_id>.md
  graph/
    <patch>/
      graph.json
  manifests/
    <patch>.json
```
