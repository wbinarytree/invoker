# Invoker — Architecture Design

Status: **Draft — pending user review**
Date: 2026-04-14
Scope: Phase 1 foundation and the architecture it must be able to grow into.

## 1. Purpose

Invoker is a standalone Dota 2 knowledge framework. It produces structured, patch-aware, LLM-consumable knowledge about heroes, synergies, counters, and (in later phases) team identity, player affinity, and itemization.

The framework holds no data. Consumers bootstrap it. Knowledge is always sourced; no Dota-specific fact in Invoker is asserted from LLM training memory.

**Phase 1 consumer:** dota2bp, as a Python package in-process.
**Phase 2+ consumer:** dota2 replay analyzer, via an interface yet to be defined.

## 2. Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│  Data sources (external)                                    │
│  OpenDota /heroes /abilities /matchups  │  STRATZ GraphQL   │
└──────────────────────┬──────────────────────────────────────┘
                       │  fetch
                       ▼
                 data/raw/<patch>/       (gitignored)
                       │
                       ▼
              ┌────────────────┐
              │  extraction    │  mechanical tags (Opus-tier LLM)
              │  + derivation  │  statistical rollups (no LLM)
              └────────┬───────┘
                       │
                       ▼
                 data/derived/<patch>/   (gitignored, regeneratable)
                   heroes/<hero_id>.json
                   summaries/<hero_id>.txt
                   manifest.json
                       │
                       ▼
              ┌────────────────┐
              │  graph builder │  NetworkX pickle
              └────────┬───────┘
                       │
                       ▼
                 data/cache/<patch>/graph.pkl    (gitignored)
                       │
                       ▼
              ┌────────────────┐
              │   query API    │  get_hero, query_archetype, neighbors...
              └────────┬───────┘
                       │
                       ▼
                  consumers (dota2bp)
```

Every arrow is deterministic given its inputs. A fresh clone produces identical derived output from identical raw input, modulo the extraction LLM's run-to-run drift (addressed in §7).

## 3. Data Model

### 3.1 Hero identity

Heroes keyed internally by OpenDota `hero_id` (int). `localized_name` carried for display. All lookups accept either.

### 3.2 Per-hero file

`data/derived/<patch>/heroes/<hero_id>.json`:

```json
{
  "schema_version": 1,
  "generator_version": "invoker@0.1.0",
  "source_patch": "7.41b",
  "generated_at": "2026-04-14T18:00:00Z",

  "hero_id": 28,
  "localized_name": "Slardar",
  "internal_name": "npc_dota_hero_slardar",

  "positions": {"primary": [3], "secondary": []},

  "functional_tags": [
    "armor_reduction",
    "single_target_disable",
    "physical_damage_amplifier",
    "initiation",
    "vision_control"
  ],

  "tag_sources": [
    {"tag": "armor_reduction", "ability": "Corrosive Haze", "evidence": "reduces enemy armor by 20 for 25s"},
    {"tag": "single_target_disable", "ability": "Slithereen Crush", "evidence": "stuns target for 1.6s"},
    {"tag": "single_target_disable", "ability": "Bash of the Deep", "evidence": "passive stun on attack"},
    {"tag": "vision_control", "ability": "Amplify Damage", "evidence": "grants True Sight on target"}
  ],

  "synergies": [
    {"hero_id": 120, "score": 0.08, "games_played": 50, "confidence": "med", "source": "stratz"},
    {"hero_id": 70,  "score": 0.06, "games_played": 38, "confidence": "med", "source": "stratz"}
  ],

  "counters": [
    {"hero_id": 96, "score": -0.07, "games_played": 34, "confidence": "med", "source": "opendota"},
    {"hero_id": 89, "score": -0.05, "games_played": 22, "confidence": "low", "source": "opendota"}
  ],

  "meta": {
    "contest_rate": 0.12,
    "win_rate": 0.51,
    "tier": "situational"
  },

  "meta_history": [
    {"patch": "7.41",  "contest_rate": 0.65, "win_rate": 0.54, "tier": "first_phase_priority"},
    {"patch": "7.41a", "contest_rate": 0.41, "win_rate": 0.52, "tier": "high_priority"},
    {"patch": "7.41b", "contest_rate": 0.12, "win_rate": 0.49, "tier": "situational"}
  ],

  "provenance": {
    "mechanical": {
      "model": "claude-opus-4-6",
      "prompt_file": "extract_mechanical_tags.md",
      "prompt_hash": "sha256:...",
      "input_hash": "sha256:...",
      "extracted_at": "2026-04-14T18:00:00Z"
    },
    "statistical": {
      "sources": ["stratz:TrueSynergy@2026-04-13", "opendota:matchups@2026-04-13"]
    }
  }
}
```

**Confidence bucketing** (statistical edges):

| games_played | confidence |
|---|---|
| 0         | `none`  |
| 1–9       | `low`   |
| 10–39     | `med`   |
| 40+       | `high`  |

Tunable later. LLM consumers see the label; downstream code can still read the raw number.

### 3.3 No-data edges

Every synergy/counter list entry is explicit, even when missing:

```json
{"hero_id": 92, "score": null, "games_played": 0, "confidence": "none", "source": "stratz"}
```

Silence is never neutral.

### 3.4 Hero LLM-injectable summary

`data/derived/<patch>/summaries/<hero_id>.txt`:

```
Slardar [pos3 — armor-reduction initiator]
Functions: armor_reduction, single_target_disable, physical_damage_amplifier, vision_control
Key mechanics: Corrosive Haze (permanent armor reduction debuff), Slithereen Crush (AoE stun + armor shred)
Synergizes (7.41b, med+ confidence): Pangolier +8% (50g), Ursa +6% (38g)
Countered (7.41b, med+ confidence): Centaur Warrunner -7% (34g)
Meta (7.41b): contest 12%, win 51%, tier: situational [was first_phase_priority in 7.41]
```

Compact, sourced, patch-labeled, velocity-aware. Fits in a prompt.

### 3.5 Manifest

`data/derived/<patch>/manifest.json` — small file listing every hero file + its content hash. Consumers use it to detect partial/aborted generations and to invalidate the graph cache.

### 3.6 Team identity, player affinity, archetypes

Schemas sketched but not populated in Phase 1. Planned locations:

- `data/derived/<patch>/teams/<team_slug>.json`
- `data/derived/<patch>/players/<player_slug>.json`
- `data/derived/archetypes.json` (patch-agnostic or versioned separately)

Schema details deferred to the Phase 1.5 / Phase 2 design docs.

## 4. Storage Model

JSON files in `data/derived/` are the source of truth. Two derived access layers, both rebuilt from JSON on demand:

- **Graph**: NetworkX, in-process, one node per hero/tag/archetype/team/player (Phase 1 uses hero + tag only), edges carry patch + sample metadata. Built once per session, cached in `data/cache/<patch>/graph.pkl`. Invalidated when manifest hash changes.
- **Vector index** (Phase 2+): local Chroma or FAISS over summaries. Deferred; no confirmed consumer yet.

Neo4j / hosted vector DB are graduation options, not current dependencies.

## 5. Pipeline

Phases of the bootstrap:

```
invoker bootstrap --patch 7.41b
  1. fetch   — OpenDota + STRATZ → data/raw/<patch>/
  2. validate — raw response schema checks
  3. extract — mechanical tags via LLM → intermediate artifacts
  4. derive  — merge stats, compute meta tiers, build per-hero files
  5. summarize — generate LLM-injectable .txt per hero
  6. manifest — write manifest.json with hashes
  7. index   — build NetworkX graph, write to data/cache/<patch>/
```

Each phase is idempotent and independently rerunnable. Phase 3 (extract) is expensive and gated: it only re-runs heroes whose ability text has changed since the last run.

CLI surface (Phase 1):

```
invoker bootstrap --patch <v> [--heroes <id,id,...>] [--skip-extract]
invoker status    --patch <v>
invoker validate  --patch <v>
```

## 6. LLM Strategy

### Extraction tier (rare, powerful)
Runs during bootstrap's `extract` phase and after hero reworks. Uses Claude Opus (or equivalent most-capable). Reads ability text from OpenDota; produces functional tags with cited sources. Cost is acceptable because this runs monthly at most.

### Query tier (frequent, light)
Runs in the *consumer*, not in Invoker. Invoker gives the consumer structured data and LLM-injectable summaries; the consumer calls whatever model it uses (Haiku, local Ollama, etc.) to reason with them. Invoker does not invoke LLMs at query time.

### Prompts

Versioned files in `src/invoker/prompts/`. Behavior-changing edits bump a version number recorded in the provenance block.

## 7. Provenance & Validation

Every derived file's `provenance` block records, for the mechanical layer: model, prompt file, prompt hash, input hash, timestamp. For the statistical layer: source + fetch timestamp per upstream API.

Validators run before a derived file lands on disk:

- **Schema check** — structural validity against a JSON Schema.
- **Tag-source completeness** — every tag in `functional_tags` has ≥1 entry in `tag_sources`.
- **Statistical sanity** — no edge has `games_played < 0`, `score` is null iff `games_played == 0`, `confidence` matches the bucket for `games_played`.
- **ID integrity** — every `hero_id` resolves to a hero in the current patch roster.

A validator failure blocks the write and surfaces an error. The pipeline does not silently retry to "fix" an extraction.

**Reproducibility caveat**: the extraction LLM can produce slightly different tags on reruns. This is accepted. Mitigations:
- fix temperature = 0 for extraction,
- manifest records prompt + input hashes so reruns with unchanged inputs are short-circuitable.

## 8. Consumer Interface (Phase 1)

Python package, in-process:

```python
from invoker import KnowledgeBase

kb = KnowledgeBase(patch="7.41b")              # loads graph, manifests

kb.hero(28)                                    # by id
kb.hero("Slardar")                             # by name
kb.synergies(28, min_confidence="med")
kb.counters(28, min_confidence="med")
kb.neighbors(28, relation="synergy", top_k=5)
kb.summary(28)                                 # returns the .txt content for prompt injection
kb.by_tag("armor_reduction", position=3)
kb.patches()                                   # list available patches
```

Return types are dataclasses, not raw dicts, so consumers get autocomplete and mypy/pyright help.

## 9. Phase 1 Scope

**In:**

- fetch layer: OpenDota heroes/abilities/matchups, STRATZ TrueSynergy (if key available — see §11)
- mechanical extraction for all heroes (Opus-tier), with validated provenance
- statistical rollup for the current patch
- per-hero JSON files + LLM-injectable summaries
- manifest
- NetworkX graph builder
- Python query API (§8)
- bootstrap CLI
- basic test suite: fetchers w/ recorded fixtures, validators, query API
- one-page README pointing at `docs/specs/`

**Out (deferred by phase):**

- **Phase 1.5**: archetypes (needs a human-authored seed set); STRATZ fallback logic once the key situation is resolved.
- **Phase 2**: team identity migration from dota2bp; player affinity; vector index once a consumer requests semantic search.
- **Phase 3**: itemization; replay analyzer interface; automated patch detection & scheduling.
- **Later**: lane matchup data; published artifact distribution for consumers that do not want to bootstrap themselves.

## 10. Dependencies (tentative)

| Dependency | Purpose |
|---|---|
| `httpx` | async HTTP to OpenDota/STRATZ |
| `pydantic` v2 | schemas + validation for raw + derived |
| `networkx` | in-process graph |
| `anthropic` | extraction-tier LLM client |
| `typer` | CLI |
| `pytest` + `vcrpy` or hand-recorded fixtures | tests |
| `ruff`, `pyright` | lint + type-check |

Nothing exotic; all pure-Python or widely-packaged.

## 11. Open Questions (tracked, not blocking design)

1. **STRATZ access.** If no key, Phase 1 runs on OpenDota matchups only. Confidence scoring still works; synergy coverage is thinner.
2. **Synergy time window.** STRATZ aggregates across time windows that may span sub-patches. Default: accept STRATZ's returned window, record it in provenance, label downstream. Revisit if this causes draft-advice drift.
3. **Archetype authorship.** Deferred to Phase 1.5; needs human Dota expertise.
4. **Replay analyzer output format.** Unknown. Interface design deferred to Phase 2.
5. **Consumer distribution.** Phase 1 consumers bootstrap themselves. A published artifact channel (release bundles, private PyPI, S3) is a Phase 2+ question once a second consumer exists.
6. **Claude API cost envelope for extraction.** ~124 heroes × one Opus call each ≈ a few dollars per full rebuild. Acceptable at monthly cadence. Re-check if cadence increases.

## 12. Non-Goals

Explicitly not part of this design:

- A persistent service / daemon / hosted API.
- A graph database.
- A web UI.
- Cross-patch knowledge fusion (we present each patch standalone; consumers reason about deltas).
- Natural-language query endpoint inside Invoker (consumers own reasoning; Invoker exposes structured data and summaries).
