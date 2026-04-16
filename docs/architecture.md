# Invoker — Architecture (Implementation Artifact)

Last updated: 2026-04-16
Phase: 1.1

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
2. Check `data/cache/llm/<key[:2]>/<key>.json`
3. On hit: return cached response, skip inner client entirely (no quota, no pacing wait)
4. On miss: call inner client, write response to disk, return

Trace output: `[llm] cache_hit key=<12chars> model=<name>` or `[llm] request key=<12chars> model=<name>`.

### GeminiClient (`src/invoker/llm/gemini.py`)

- Class-level rate limiter: minimum 12.5 s between calls (enforces ≤ 5 RPM free-tier).
- Retry: up to 3 retries on quota/rate errors; exponential backoff starting at 65 s, doubling each attempt.
- Non-quota errors are re-raised immediately (no retry).
- `model_name` is the Gemini model string used as the cache key dimension.

### ManualClient (`src/invoker/llm/manual.py`)

Writes the rendered prompt to a file and waits for a hand-written response file. Used when `--manual` flag is passed to the CLI.

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

### bundle (`pipeline/bundle.py`)

Converts `fetch_all` output into `HeroRawBundle` objects for the orchestrator.

- Resolves each hero's abilities by joining `hero_abilities` map → `abilities` dict, keeping only entries with a display name and description.
- Passes through per-hero matchups and STRATZ edges.
- Meta stats (`position_counts`, `contest_rate`, `win_rate`, `meta_history`) are zeroed — no source exists for these without fetching individual match details. Explicit zeros are used; consumers should treat `games=0` as "no data".

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

Two prompts: `synergy_reason`, `counter_reason`.
Input: `ReasonInput` with both hero names, tags, score, and game count.
Only `med` and `high` confidence edges get a reason call.
Hero B name and tags are loaded from the already-written hero file if it exists (`_try_load_hero_context`), or fall back to `("hero_{id}", [])`.

Grounding check: `validate_grounding(reason, a_tags, b_tags)` — rejects a reason that mentions no tag from either hero.

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

## Error Recovery

`run_for_hero()` returns `HeroResult(hero_id, success, reasons_written, reasons_skipped, failure_reason)`.

- Extraction failure → log, return `success=False`, continue next hero
- Reason failure → log, increment `reasons_skipped`, continue other reasons
- Hero still written even with missing reasons

`finalize_patch` only processes heroes whose output files exist — partial runs don't block finalisation.

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

`Config.load()` calls `load_dotenv()` first, so `.env` in the project root is honoured by the CLI. Required env vars: `GEMINI_API_KEY` (for Gemini client), `STRATZ_API_KEY` (optional; STRATZ works without auth but at lower rate limits).

### Dev Hero Filter

Gemini free tier caps at 20 calls/day. To avoid burning quota during development, a hero filter limits which heroes receive per-hero API calls and LLM extractions.

Two ways to set it (CLI flag takes precedence):

| Method | Example |
|--------|---------|
| `INVOKER_DEV_HEROES` env var | `INVOKER_DEV_HEROES=Pangolier,Slardar` in `.env` |
| `--heroes` CLI flag | `invoker bootstrap --patch 7.41b --heroes "Pangolier,Slardar"` |

Accepts hero **names** (case-insensitive) or numeric **ids**. The global hero roster fetch still runs (single cached call); only per-hero calls (matchups, STRATZ synergies) and LLM extractions are restricted. No filter = all heroes (production behaviour unchanged).

Milestone gate: Pangolier + Slardar pass `invoker validate` before full bootstrap is attempted.

---

## Prompts

All prompts live in `src/invoker/prompts/` as `.md` files with a `<!-- prompt_version: N -->` comment on line 1. The version is parsed at load time and included in cache keys and provenance. Changing a prompt text without bumping the version will produce stale cache hits — always bump the version when changing prompt logic.

---

## Cache Layout

```
data/
  cache/
    llm/
      <key[:2]>/
        <key>.json      # {text, model, prompt_version, cached_at}
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
