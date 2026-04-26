> **Status: superseded by `docs/architecture.md` (2026-04-26).**
> Project pivoted away from the agentic LLM-extraction pipeline described here. Read `docs/architecture.md` for what actually exists today; this is kept only as historical trace of the original design intent.

# Invoker — Architecture Design

Status: **Draft — pending user review (revision 2)**
Date: 2026-04-14
Scope: Phase 1 foundation and the architecture it must grow into.

## 1. Purpose

Invoker is a standalone Dota 2 knowledge framework. It produces structured, patch-aware, LLM-consumable knowledge about heroes, synergies, counters, and (in later phases) team identity, player affinity, and itemization.

The framework holds no data. A fresh clone has zero knowledge until `invoker bootstrap` runs. Knowledge is always sourced; no Dota-specific fact in Invoker is asserted from LLM training memory.

**Phase 1 consumer:** none in production. The internal reader API exists for validation and future dota2bp integration; its shape is not yet a stable contract.

## 2. Architecture Overview

```
┌──────────────────────────────────────────────────────────────────┐
│  Data sources (external)                                         │
│  OpenDota /heroes /abilities /matchups /proMatches               │
│  STRATZ GraphQL (synergies, filtered by bracket & isTournament)  │
│  Liquipedia (MediaWiki API — hero roles, facets, abilities)      │
└──────────────────────────────┬───────────────────────────────────┘
                               │ rate-limited, cached fetch
                               ▼
                     data/raw/<source>/<patch>/     (gitignored)
                               │
                               ▼
                    ┌──────────────────────┐
                    │  extraction          │  mechanical tags (Flash)
                    │  + reason generation │  synergy/counter reasons
                    │  + statistical merge │  no LLM for stats rollup
                    └──────────┬───────────┘
                               │
                               ▼
                     data/derived/<patch>/           (gitignored)
                       heroes/<hero_id>.json
                       summaries/<bracket>/<hero_id>.txt
                       manifest.json
                               │
                               ▼
                    ┌──────────────────────┐
                    │  graph builder       │
                    └──────────┬───────────┘
                               │
                               ▼
                     data/cache/<patch>/graph.pkl    (gitignored)
                               │
                               ▼
                    ┌──────────────────────┐
                    │  internal reader API │  (Python, not stable contract)
                    └──────────┬───────────┘
                               │
                               ▼
                    validation + future consumers
```

Every arrow is deterministic given its inputs, modulo LLM drift (addressed in §7).

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

  "liquipedia_roles": ["Initiator", "Durable", "Disabler", "Escape", "Pusher"],

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

  "positions": {
    "pro": {
      "weights": {"1": 0.0, "2": 0.0, "3": 1.0, "4": 0.0, "5": 0.0},
      "games": 34,
      "window_days": 90
    }
  },

  "synergies": {
    "pro": [
      {
        "hero_id": 120, "score": 0.08, "games": 50, "confidence": "high",
        "source": "stratz",
        "reason": "Armor reduction (Corrosive Haze) amplifies Pangolier's physical burst from Swashbuckle.",
        "reason_provenance": {"model": "gemini-2.5-flash", "prompt_version": 1}
      },
      {
        "hero_id": 70, "score": 0.06, "games": 38, "confidence": "med",
        "source": "stratz",
        "reason": "Armor shred amplifies Ursa's Fury Swipes stacking physical damage.",
        "reason_provenance": {"model": "gemini-2.5-flash", "prompt_version": 1}
      }
    ]
  },

  "counters": {
    "pro": [
      {
        "hero_id": 96, "score": -0.07, "games": 34, "confidence": "med",
        "source": "opendota",
        "reason": "Centaur's base armor and Return passive resist Slardar's physical initiation.",
        "reason_provenance": {"model": "gemini-2.5-flash", "prompt_version": 1}
      }
    ]
  },

  "meta": {
    "pro": {"contest_rate": 0.12, "win_rate": 0.51, "tier": "situational", "games": 34}
  },

  "meta_history": [
    {"patch": "7.41",  "bracket": "pro", "contest_rate": 0.65, "win_rate": 0.54, "tier": "first_phase_priority"},
    {"patch": "7.41a", "bracket": "pro", "contest_rate": 0.41, "win_rate": 0.52, "tier": "high_priority"},
    {"patch": "7.41b", "bracket": "pro", "contest_rate": 0.12, "win_rate": 0.49, "tier": "situational"}
  ],

  "provenance": {
    "mechanical": {
      "model": "gemini-2.5-flash",
      "prompt_file": "extract_mechanical_tags.md",
      "prompt_version": 1,
      "prompt_hash": "sha256:...",
      "input_hash": "sha256:...",
      "extracted_at": "2026-04-14T18:00:00Z",
      "liquipedia_snapshot": "liquipedia:Slardar@2026-04-14"
    },
    "statistical": {
      "pro": {
        "sources": ["stratz:TrueSynergy@2026-04-13", "opendota:matchups-tournament@2026-04-13"],
        "window_days": 90
      }
    }
  }
}
```

### 3.3 Brackets

Every statistical block is nested by bracket:

| Bracket | Source | Phase |
|---|---|---|
| `pro` | OpenDota `/proMatches` + STRATZ `matchFilter.isTournament` | **Phase 1** |
| `immortal_pub` | STRATZ rank filter | Phase 1.5 |
| `pub_all` | OpenDota unfiltered | Phase 1.5 |
| `team:<slug>` | Phase 2 — team identity migration | Phase 2 |
| `player:<slug>` | Phase 2 — player affinity | Phase 2 |

**Phase 1 populates `pro` only.** The schema supports all from day 1 — no refactor when we add brackets.

### 3.4 Positions as weights

Per-bracket position weights derived from game counts. Noise below a floor (e.g., 0.03 after normalization) is zeroed. A pos-1 flex reads `{"1": 0.48, "2": 0.52}`; a strict pos-3 reads `{"3": 1.0}`; a mid-transitioning hero reads `{"1": 0.88, "2": 0.12}`.

### 3.5 Synergy / counter reasons

Every edge in `confidence ∈ {med, high}` carries a `reason`: one or two sentences grounded in both heroes' functional tags. Generated by the extraction LLM during derivation.

Edges at `confidence ∈ {low, none}` do **not** carry a reason — the sample is too weak to justify a narrative.

Validator rule: every `reason` must cite at least one tag from either hero. Ungrounded reasons are rejected. This blocks hallucinated flavor text.

### 3.6 No-data edges

```json
{"hero_id": 92, "score": null, "games": 0, "confidence": "none", "source": "stratz"}
```

Silence is never neutral.

### 3.7 Summary files

`data/derived/<patch>/summaries/<bracket>/<hero_id>.txt`:

```
Slardar [pos3 — armor-reduction initiator]
Functions: armor_reduction, single_target_disable, physical_damage_amplifier, vision_control
Key mechanics: Corrosive Haze (permanent armor reduction), Slithereen Crush (AoE stun + shred)
Pro synergies (7.41b, med+): Pangolier +8% (50g) — armor shred amplifies physical burst; Ursa +6% (38g) — stacks with Fury Swipes
Pro counters (7.41b, med+): Centaur Warrunner -7% (34g) — natural tankiness resists physical
Pro meta (7.41b): contest 12%, win 51%, tier: situational [was first_phase_priority in 7.41]
```

Phase 1 generates the `pro` summary only. Other brackets can be added later without schema change.

### 3.8 Manifest

`data/derived/<patch>/manifest.json` — lists every hero file, its content hash, which brackets were populated, and the overall build status (partial / complete). Consumers use it to detect aborted generations and invalidate graph caches.

### 3.9 Deferred schemas

Sketched locations; detailed designs come with their phases:

- `data/derived/<patch>/teams/<team_slug>.json` — Phase 2
- `data/derived/<patch>/players/<player_slug>.json` — Phase 2
- `data/derived/archetypes.json` — Phase 1.5 (needs human-authored seed)

## 4. Storage Model

JSON files in `data/derived/<patch>/` are the source of truth. Duplication across patches is accepted — at this scale (~11MB/year) the complexity cost of content-addressable storage isn't justified.

One derived access layer in Phase 1:

- **Graph**: NetworkX, in-process. Nodes: heroes + tags. Edges: hero→tag, hero→hero (synergy/counter, per bracket). Built once per session, cached at `data/cache/<patch>/graph.pkl`. Invalidated when manifest hash changes.

Vector index, Neo4j, hosted stores: graduation paths, not current dependencies.

## 5. Pipeline

```
invoker bootstrap --patch 7.41b [--bracket pro] [--force]

  1. fetch      — OpenDota + STRATZ + Liquipedia → data/raw/<source>/<patch>/
                   rate-limited (STRATZ 250/min 10k/day, OpenDota 60/min 3k/day,
                   Liquipedia ≤0.5/sec); cache honored unless --force
  2. validate   — raw response schema + page-structure checks
  3. extract    — LLM produces mechanical tags with Liquipedia roles as prior evidence;
                   only heroes whose ability text or Liquipedia page changed since
                   last run are re-extracted
  4. reason     — LLM produces synergy/counter reasons for med+ confidence edges
  5. derive     — merge stats per bracket, compute meta tiers, write per-hero files
  6. summarize  — generate LLM-injectable .txt per hero per bracket
  7. manifest   — write manifest.json with hashes and build status
  8. index      — build NetworkX graph → data/cache/<patch>/graph.pkl
```

Each phase is idempotent and independently re-runnable. The extract and reason phases are the only LLM-cost gates; both short-circuit on unchanged inputs.

CLI (Phase 1):

```
invoker bootstrap --patch <v> [--heroes <id,id,...>] [--skip-extract] [--force]
invoker status    --patch <v>
invoker validate  --patch <v>
invoker publish   --patch <v>          # writes dist/invoker-kb-<patch>.tar.gz
```

## 6. LLM Strategy

### Extraction tier (rare, structured)
Runs during `extract` and `reason` phases. Default model: **Google Gemini 2.5 Flash (free tier)** via `google-generativeai`. Acceptable for this workload (closed taxonomy, grounded output, validator-gated).

### Client abstraction
Thin `LLMClient` protocol:

```python
class LLMClient(Protocol):
    def extract_tags(self, hero_context: HeroContext) -> TagExtraction: ...
    def synergy_reason(self, a: HeroCard, b: HeroCard, score: float) -> str: ...
```

Alternate implementations (`ClaudeClient`, `OpenAIClient`) swap with one line of config. A **`ManualClient`** writes prompts to `data/raw/manual_prompts/` and reads responses from `data/raw/manual_responses/`, letting you paste into a ChatGPT or Claude.ai session during rate-limit emergencies.

### Query tier
**Not run by Invoker.** The internal reader serves structured data and summaries to consumers. Consumers call whatever model they use for reasoning. Invoker does not invoke LLMs at query time.

### Cost envelope (Phase 1, Gemini Flash free tier)

| Phase | Calls per full bootstrap |
|---|---|
| extract (mechanical) | ~124 |
| reason (synergy + counter) | ~124 × ~15 edges ≈ ~1,860 |
| Total | ~2,000 |

Well within Flash's free-tier daily limits. Falls to ~0 on reruns with unchanged inputs.

## 7. Prompt Engineering

Prompts are the quality bottleneck of the mechanical layer. The approach:

### 7.1 Closed tag taxonomy
We define the vocabulary in `src/invoker/prompts/taxonomy.yaml` — ~40–60 tags, each with:
- a short definition
- where relevant, a **quantitative threshold** (e.g., *`big_burst`: ≥200 magical damage at max level in a single cast window*)
- 2–3 example heroes that legitimately carry the tag

The LLM picks from this list. It never invents a tag. Additions to the taxonomy are a deliberate human change.

### 7.2 Few-shot prompt
Extraction prompt includes 5–10 hand-labeled example heroes covering diverse archetypes (carry, support, pusher, tempo). Inline, not retrieved.

### 7.3 Liquipedia roles as prior evidence
The prompt shows Liquipedia's curated role labels for the target hero and says: *"These are expert-labeled roles. Map them to our taxonomy where applicable, but your tag choices must still be justified by the ability text."* Anchor without anchor-bias.

### 7.4 Structured output
Temperature 0. JSON-schema-constrained output. Each tag must come with the cited ability name and evidence quote.

### 7.5 Gold set
`tests/fixtures/gold/` contains 15–20 hand-labeled heroes covering edge cases. Prompt edits run against the gold set; regressions block merge. This is the feedback loop that makes prompt tuning tractable.

### 7.6 Optional critic pass
A second LLM call reviews the first for consistency (every tag cited, no duplicates, no out-of-taxonomy entries). Cheap on Flash. Turn on if the gold-set agreement rate falls below target.

## 8. Provenance & Validation

### Provenance blocks
Every derived artifact records:
- **Mechanical**: model, prompt file, prompt version, prompt hash, input hash, timestamp, liquipedia snapshot id.
- **Reason (per edge)**: model, prompt version.
- **Statistical (per bracket)**: list of source+timestamp pairs, time window.

### Validators (block write on failure)
- **Schema check** — JSON Schema validity.
- **Tag-source completeness** — every tag in `functional_tags` has ≥1 entry in `tag_sources`.
- **Tag taxonomy** — every tag appears in `taxonomy.yaml`.
- **Reason grounding** — every `reason` mentions a tag present on at least one of the two heroes.
- **Statistical sanity** — `games ≥ 0`; `score is null` iff `games == 0`; `confidence` matches the bucket.
- **ID integrity** — every `hero_id` resolves to the current patch roster.
- **Bracket consistency** — every populated bracket declares a `window_days` and `games`.

### Reproducibility
Extraction drift is accepted but bounded: temperature 0, prompt hashing, input hashing. Reruns with unchanged inputs short-circuit.

## 9. Internal Reader API (Phase 1, not a stable contract)

Used by validators, tests, and future consumers. Expect breakage between Phase 1 and Phase 2.

```python
from invoker import KnowledgeBase

kb = KnowledgeBase(patch="7.41b", bracket="pro")

kb.hero(28)                                 # by id
kb.hero("Slardar")                          # by name
kb.synergies(28, min_confidence="med")
kb.counters(28, min_confidence="med")
kb.neighbors(28, relation="synergy", top_k=5)
kb.summary(28)                              # returns .txt content for prompt injection
kb.by_tag("armor_reduction")
kb.brackets()                               # list populated brackets for this patch
kb.patches()                                # list available patches
```

Return types: dataclasses, not raw dicts.

## 10. Phase 1 Scope

**In:**

- Fetch layer: OpenDota + STRATZ (if key) + Liquipedia
- Rate-limited, cached HTTP client
- Mechanical extraction for all heroes (Gemini Flash default, pluggable, manual fallback)
- Liquipedia role labels as prior evidence in extraction prompt
- Synergy & counter reason generation for med+ confidence edges
- Statistical layer for `pro` bracket
- Per-hero JSON + `pro` bracket summaries
- Manifest + content hashes
- NetworkX graph builder
- Gold-set regression harness
- Internal reader API
- `bootstrap`, `status`, `validate`, `publish` CLI
- Basic test suite

**Out (by phase):**

- **Phase 1.5**: archetypes (human-authored seed); `immortal_pub` and `pub_all` brackets; STRATZ fallback strategy if no key.
- **Phase 2**: team identity migration from dota2bp; player affinity; vector index (once a consumer requests semantic search); stable consumer contract.
- **Phase 3**: itemization; replay analyzer interface; automated patch detection.
- **Later**: lane matchup data; published distribution channel (GitHub releases / S3 / data-only repo).

## 11. Dependencies (tentative)

| Dependency | Purpose |
|---|---|
| `httpx` | async HTTP to OpenDota / STRATZ / Liquipedia |
| `pydantic` v2 | schemas for raw + derived |
| `networkx` | in-process graph |
| `google-generativeai` | default extraction client |
| `typer` | CLI |
| `pytest` + recorded fixtures | tests |
| `ruff`, `pyright` | lint + type-check |
| `pyyaml` | taxonomy loading |
| `beautifulsoup4` or `mwparserfromhell` | Liquipedia page parsing |

## 12. Open Questions (tracked, not blocking design)

1. **STRATZ access.** If no key: `pro` stats narrow to OpenDota `/proMatches`-derived only. Coverage thinner, still functional.
2. **Liquipedia scraping etiquette.** Honor Terms of Use: proper User-Agent, rate limit ≤0.5 req/sec, cache aggressively, attribute in the published bundle.
3. **Gold-set authorship.** Needs someone (you + me iterating) to label 15–20 heroes. Phase 1 task.
4. **Taxonomy authorship.** Similar — needs a first pass of ~40–60 tags with thresholds. Phase 1 task.
5. **Publish bundle distribution.** Tarball lives in `dist/`; how consumers retrieve it is Phase 2.
6. **Claude cost envelope for extraction if we switch from Flash.** ~2,000 calls at Haiku tier is still cheap; Opus would be ~$20–50 per full rebuild. Revisit if Flash quality is insufficient.

## 13. Non-Goals

- Persistent service / daemon / hosted API.
- Graph database.
- Web UI.
- Cross-patch knowledge fusion (each patch is standalone; consumers reason about deltas themselves).
- Natural-language query endpoint inside Invoker (consumers own reasoning; Invoker exposes structured data and summaries).
