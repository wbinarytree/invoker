# Manual-Assisted KG Plan — Stages 2–6

**Date:** 2026-04-22
**Status:** draft — needs user sign-off before any code changes
**Supersedes:** Stages 2–8 of `docs/plans/2026-04-18-kg-execution-plan.md`
**Governed by:** `docs/specs/2026-04-18-kg-design-guidelines.md`
**Archive:** the automated agentic-extraction direction is preserved on branch `archive/agentic-kg`

---

## Why this plan exists

The 2026-04-18 execution plan assumed an automated pipeline that extracts hero facts via LLM, infers relations, and attaches evidence — all unattended. With ~120 heroes and incremental patches (reworks require regeneration per-hero anyway), that automation overhead is not earning its weight.

This plan replaces the automated substrate with a **manual-with-LLM-assist** model. The mechanics-first KG goal is unchanged; what changes is **who produces the hero fact profiles**: a human (optionally assisted by any LLM they like, in a separate window) instead of the pipeline.

The `src/invoker/kg/` prototype already proves the rule engine + relation shape work deterministically. This plan promotes that prototype into the production path and drops the automated-extraction surface.

---

## Principles (carried over from kg-design-guidelines)

These still hold; the pivot is about **how hero facts get authored**, not what the KG looks like:

- Facts, relations, and views are different layers.
- Stats are evidence, not ontology.
- Text is downstream, not source-of-truth.
- Patch scope is a first-class boundary.
- LLMs stay out of the query path and out of the build-time critical path. They remain useful for **prompt scaffolding** (pipeline renders the prompt; a human runs the LLM) and **vocabulary suggestion** (same pattern).

---

## Architecture overview

```
                                    ┌──────────────────────┐
 data/authored/<hero_slug>.yaml ──▶ │                      │
                                    │     fact loader      │
 data/raw/<source>/<patch>/… ─────▶ │   + stat merger      │ ──▶ data/derived/<patch>/heroes/<id>.json
                                    │                      │
                                    └──────────┬───────────┘
                                               │
                                               ▼
                                    ┌──────────────────────┐
                                    │   rule engine        │ ──▶ data/derived/<patch>/relations.json
                                    │   (kg/infer.py)      │
                                    └──────────┬───────────┘
                                               │
                                               ▼
                                    ┌──────────────────────┐
                                    │  evidence attachment │ ──▶ data/derived/<patch>/relations.json
                                    │  (stat alignment)    │      (enriched in place)
                                    └──────────┬───────────┘
                                               │
                                               ▼
                                      manifest + graph build
```

No LLM calls in this pipeline. LLM assistance lives in a separate authoring helper that writes a draft YAML the user edits (see Stage 3).

---

## Stage 2 — Canonical schema

### Goal

Promote the benchmark prototype schemas from `src/invoker/kg/schemas.py` into production-grade shapes and decide their storage location.

### Changes from prototype

- Add `targets` feature bucket to `HeroFactProfile` (from the kg-relation-representation spec, §"Proposed Hero Representation").
- Add `role_distribution: dict[str, float]` slot (pub cohort, populated from OpenDota meta; optional at first).
- Keep `provenance: dict` but type it: `{authored_by: "human", authored_at: iso, reviewed_at: iso, assist_model: str | null}`.
- `HeroRelation.evidence.statistical` becomes `list[RelationEvidenceStatistical]` (one hero may have STRATZ *and* OpenDota evidence for the same pair).

### What stays canonical

- `data/authored/<hero_slug>.yaml` = canonical hero *facts* source. Patch-invariant unless a hero is reworked (see Stage 3).
- `data/derived/<patch>/relations.json` = **the** canonical relation artifact. See "Relations artifact shape" below.
- `data/derived/<patch>/heroes/<hero_id>.json` = **facts-only view** (capabilities / requirements / liabilities / targets / role_distribution / provenance). Hero JSON files **do not embed their relations** — that would duplicate records and create sync bugs. Human-readable hero summaries (`summary_<hero_id>.md`) pull relations from `relations.json` at render time.

### Relations artifact shape

`data/derived/<patch>/relations.json` is a **flat array of `HeroRelation` records**. Each record is:

- **Directional** — `from_hero_id` (source) and `to_hero_id` (target) are not interchangeable. `A counters B` is a different record from `B counters A`; only one fires unless both directions have a triggering rule.
- **Per-rule-firing** — one pair typically produces several records. Example: Pangolier (120) against a squishy immobile enemy Y produces `120→Y:counter:mobility_punish:aoe_lockdown` (Rolling Thunder locks down low-mobility targets); with a magic-burst ally Z he produces `120→Z:synergy:setup_followup:aoe_lockdown` (his R sets up the ally's burst).
- **Self-describing** — `relation_id = "{from}->{to}:{kind}:{pattern}:{source_feature}"` is the unique key; stable across runs because rule inference is deterministic.
- **Cohort-scoped** — every record carries `cohort` (`pub`, `pro_global`, later `pro_team:<slug>`). Same mechanical relation can exist in multiple cohorts with different evidence attached. See §"Cohort and team context" below.

Illustrative file (hero IDs are examples, not assertions):

```json
{
  "schema_version": 2,
  "source_patch": "7.41b",
  "cohort": "pro_global",
  "generated_at": "2026-04-22T18:00:00Z",
  "relations": [
    {
      "relation_id": "120->Z:synergy:setup_followup:aoe_lockdown",
      "from_hero_id": 120,
      "to_hero_id": 52,
      "relation_kind": "synergy",
      "pattern": "setup_followup",
      "source_feature": "aoe_lockdown",
      "target_feature": "magic_burst",
      "mechanical_rationale": "Rolling Thunder locks down clustered enemies for a magic-burst ally to follow up",
      "cohort": "pro_global",
      "evidence": {
        "mechanical": {"confidence": 0.8, "basis": ["Pangolier.capabilities includes aoe_lockdown", "ally.capabilities includes magic_burst"]},
        "statistical": [{"source": "stratz", "score": 0.06, "games": 80, "alignment": "aligned"}]
      },
      "confidence": "high"
    }
  ]
}
```

### Scale

~120 heroes × 119 targets × ~15 rules = ~215k trigger attempts per patch; realistically 5–20k fire. A single file loads in well under a second; no sharding needed.

### Query surface (reader API)

`src/invoker/kg/reader.py` (new in Stage 2) loads `relations.json` once and builds in-memory indexes. Minimum surface:

| Method | Returns |
|--------|---------|
| `relations_for(hero_id)` | every record where hero is source OR target |
| `relations_from(hero_id)` | records where hero is source (what this hero does to others) |
| `relations_to(hero_id)` | records where hero is target (what others do to this hero) |
| `relations_between(a, b)` | records in either direction for the pair |
| `synergies_with(hero_id)` | `relations_for(hero_id)` filtered to `kind == "synergy"` |
| `counters_of(hero_id)` | records where `to == hero_id` and `kind == "counter"` (who counters this hero) |
| `countered_by(hero_id)` | records where `from == hero_id` and `kind == "counter"` (who this hero counters) |
| `relations_by_pattern(pattern)` | records emitted by a specific rule pattern |

The NetworkX graph cache at `data/cache/graph/<patch>/graph.json` remains available for multi-hop queries; the reader API handles direct lookups without needing the graph.

### Decisions deferred

- Whether to split `relations.json` into per-pattern shards — wait until file size or diff noise forces it.
- Full context schema (`lane_context`, `phase_context`, `archetype_context`). Reserve fields, leave populated as null; real values land in a later plan.

### Exit criteria

1. Schemas in `src/invoker/kg/schemas.py` updated and re-tested.
2. `HeroFactProfile` round-trips through YAML (authored format) and JSON (derived view).
3. `src/invoker/kg/reader.py` exposes the query surface above and has unit tests covering direction and kind filtering.
4. Pangolier authored end-to-end as the smoke-test hero and a manifest lists it.

---

## Stage 3 — Authoring workflow

### Goal

Make hand-authoring one hero take ~15–30 minutes, not an afternoon. The LLM assist is a helper command; the human is the editor.

### Authored file format

`data/authored/<hero_slug>.yaml`. YAML because humans edit this. Illustrative (real values come from author review, not asserted here):

```yaml
hero_id: 120
hero_slug: pangolier
localized_name: Pangolier
capabilities:
  - type: mobility
    score: 0.9
    evidence: ["Swashbuckle dashes; Shield Crash jumps"]
  - type: aoe_lockdown
    score: 0.8
    evidence: ["Rolling Thunder is an AoE stun on roll contact"]
  - type: disengage
    score: 0.8
    evidence: ["Rolling Thunder + Shield Crash provide escape tools"]
  - type: silence
    score: 0.3
    evidence: ["Lucky Shot has a chance to silence"]
requirements:
  - type: needs_damage_followup
    score: 0.7
liabilities:
  - type: weak_to_silence
    score: 0.6
    evidence: ["Rolling Thunder requires a cast; pre-R silence denies the engage"]
targets:
  - type: punishes_immobile_backline
    score: 0.8
provenance:
  authored_by: human
  authored_at: 2026-04-22
  assist_model: claude-opus-4-7
```

### Why YAML, not JSON

- Humans edit this. JSON's lack of comments and its quoting noise hurt review.
- The pipeline converts YAML → validated `HeroFactProfile` on load.

### `invoker draft-facts <hero>` — prompt-in-pipeline, LLM-in-human-loop

Prompt *generation* is part of the pipeline. The LLM call itself is performed by the human in whatever chat window they prefer. The helper:

- Resolves hero roster metadata from the same static hero map already used by the framework (hero id, slug, localized name, roles).
- Fetches ability text from OpenDota for the hero (cached under `data/raw/opendota/<patch>/...`), or reuses the cached payload if present.
- Renders `src/invoker/prompts/draft_fact_profile.md` into a concrete prompt with hero name, roles, and full ability text substituted in, plus the current vocabulary as an allowed-terms list.
- Writes the rendered prompt to `data/raw/manual_prompts/draft-facts/<hero_slug>.md` via `ManualClient`.
- On rerun, reads `data/raw/manual_responses/draft-facts/<hero_slug>.txt`, parses into YAML, writes to `data/authored/<hero_slug>.yaml` **only if the file does not already exist**. Otherwise writes `data/authored/<hero_slug>.draft.yaml` for diff review.
- If the response is missing, prints the pending prompt path and exits cleanly (no traceback).

Why this split: prompt rendering is deterministic, mechanical, and benefits from versioning — it belongs in the pipeline. Which model runs the prompt, and what prompting ergonomics the user prefers, belong outside the pipeline.

### Source-of-truth note for Stage 3

Stage 2 removes the old fetch-bundle-orchestrator production path, so `draft-facts` must not depend on that deleted surface. Stage 3 should build its prompt context from two explicit inputs only:

- hero roster metadata from the repo's canonical hero map / source adapters;
- raw ability text cached under `data/raw/`, fetched on demand when missing.

That keeps authoring helpers decoupled from bootstrap and avoids reintroducing the deprecated agentic pipeline by accident.

### Review loop

- `invoker validate-facts <hero>` checks vocabulary membership, score bounds, evidence presence, required buckets.
- `invoker show-relations <hero>` runs the rule engine against current authored facts and prints inferred relations. Quick sanity-check during authoring.
- `data/authored/vocab-gaps.yaml` captures important mechanics that could not be represented with the live vocabulary. These entries are **not** facts and do not affect relation inference; they are grounded Stage 4 input.

### Lossiness guardrail

The draft response may include `vocabulary_gaps`, but `draft-facts` must strip that field before writing canonical `<hero>.yaml`. Canonical authored YAML stays strict and validator-owned; unexpressed mechanics go to `vocab-gaps.yaml` as a review inbox with hero, bucket, concept, evidence, candidate term, and status. Regenerated drafts use `<hero>.draft.yaml` so editors still recognize them as YAML.

### Exit criteria

1. `draft-facts` renders a prompt whose pasted-back response parses into a YAML draft that `validate-facts` accepts unmodified for at least one hero.
2. A human can author a hero in under 30 minutes following a short README at `data/authored/README.md`.
3. At least one draft response with a real missing concept writes `data/authored/vocab-gaps.yaml` while keeping the authored hero YAML valid and free of review-only fields.
4. Pangolier authored, then nine more heroes — picked to exercise at least half the initial capability vocabulary (cover one each of: physical-burst core, magic-burst core, reliable-stun support, save-giver support, mana-burn hero, invisibility hero, sustain tank, high-mobility carry, wave-clear mid).

---

## Stage 4 — LLM-assisted vocabulary curation

### Goal

The vocabulary is the contract between authors, the rule engine, and the validator. Neither the author nor the plan writer has deep enough Dota 2 expertise to hand-design it perfectly. So vocabulary evolves **LLM-assisted, human-reviewed** — same split as authoring: pipeline renders the prompt, a human runs the LLM, pipeline parses the response.

### Seed vocabulary

The initial set in `src/invoker/kg/vocabulary.py` is a **starting point, not a lockdown**. Extend once with an obvious expansion pass so Stage 5's rule engine has something to reason about:

- **Capabilities (seed ~20):** current 10 + `aoe_lockdown`, `healing_reduction`, `sustain`, `tower_damage`, `physical_burst`, `long_fight_scaling`, `setup`, `disengage`, `dispel`, `pickoff`.
- **Requirements (seed ~6):** current 4 + `needs_vision`, `needs_lane_stability`.
- **Liabilities (seed ~10):** current 6 + `weak_to_silence`, `weak_to_dispel`, `weak_to_bkb_timing`, `relies_on_invisibility`.
- **Targets (seed ~6, new bucket):** `punishes_low_armor`, `punishes_invisibility`, `punishes_summons`, `punishes_channeling`, `punishes_sustain`, `punishes_immobile_backline`.
- **Relation patterns (seed ~7):** current 6 + `sustain_break`.

### `invoker suggest-vocabulary` — LLM-assisted expansion

Same prompt-in-pipeline / LLM-in-human-loop split as `draft-facts`:

- Collects all authored heroes (post-Stage 3, at least 10) and their ability text.
- Renders `src/invoker/prompts/suggest_vocabulary.md` with: current vocabulary, authored heroes' ability text, and a request to propose missing terms per bucket along with: (a) proposed term, (b) definition, (c) example hero(es) where it applies, (d) proposed rules it would enable.
- Writes the prompt to `data/raw/manual_prompts/suggest-vocabulary/<timestamp>.md`.
- On rerun, parses `data/raw/manual_responses/suggest-vocabulary/<timestamp>.txt` into `data/authored/vocab-proposals.yaml` — an inbox, not live vocabulary.

### Review and promotion

`data/authored/vocab-proposals.yaml` is the author's review queue. Each entry: `{term, bucket, definition, examples, status}` where `status ∈ {proposed, accepted, rejected, defer}`.

Accepted entries land in `vocabulary.py` via a small `invoker promote-vocabulary` command that:
- appends the term to the right `frozenset`,
- writes a one-line note to `docs/specs/kg-vocabulary-notes.md`,
- refuses to promote a term that no authored hero uses (forces at least one real consumer).

Rejected and deferred entries stay in the YAML as a paper trail — useful when the same proposal resurfaces.

### Guardrails

- A new capability/liability without a consuming rule is permitted but flagged in `show-relations` output so it doesn't silently become dead vocabulary.
- Vocabulary size targets are soft ceilings, not hard limits — but crossing +10 in a single promotion round triggers a mandatory re-read of kg-design-guidelines §"Vocabulary Guidance" before the command succeeds.

### Exit criteria

1. Seed vocabulary committed to `vocabulary.py`.
2. `suggest-vocabulary` has been run against ≥10 authored heroes at least once, producing a reviewed `vocab-proposals.yaml`.
3. At least three terms promoted from the proposal queue into live vocabulary via `promote-vocabulary`, with notes in `kg-vocabulary-notes.md`.
4. Validator rejects any term outside live vocabulary with a clear error.

---

## Stage 5 — Rule engine promotion

### Goal

Move `src/invoker/kg/infer.py` from benchmark-only to the production path and expand its rule set to cover the vocabulary.

### What the engine does

- Input: list of validated `HeroFactProfile`.
- Output: list of `HeroRelation`, one per (source, target, pattern) triple that fires.
- Purely deterministic — no LLM, no randomness.

### Rule shape (unchanged from prototype)

Each rule reads as `if src has capability X and tgt has liability/requirement/capability Y → emit relation with pattern P`. Keep each rule a short function; no rule DSL until it hurts.

### Expansion list (mapped from the expanded vocabulary)

Target ~15 rules total. Each rule lists: source-feature → target-feature → pattern → kind → default confidence. Draft table:

| Source (capability) | Target (bucket:type)        | Pattern            | Kind    | Conf |
|---------------------|----------------------------|--------------------|---------|------|
| mana_burn           | liab:mana_dependence       | resource_punish    | counter | high |
| vision_reveal       | liab:relies_on_invisibility| vision_exposure    | counter | high |
| reliable_stun       | cap:magic_burst            | setup_followup     | synergy | med  |
| reliable_stun       | cap:physical_burst         | setup_followup     | synergy | med  |
| reliable_stun       | cap:mobility               | mobility_punish    | counter | med  |
| armor_reduction     | cap:physical_burst         | enabler_payoff     | synergy | high |
| save                | req:needs_save             | save_protection    | synergy | med  |
| silence             | liab:weak_to_silence       | resource_punish    | counter | high |
| dispel              | liab:weak_to_dispel        | resource_punish    | counter | high |
| healing_reduction   | cap:sustain                | sustain_break      | counter | high |
| aoe_lockdown        | liab:weak_to_kiting        | mobility_punish    | counter | med  |
| setup               | req:needs_damage_followup  | setup_followup     | synergy | med  |
| disengage           | req:needs_save             | save_protection    | synergy | low  |
| wave_clear          | liab:low_waveclear         | (complement)       | synergy | low  |
| pickoff             | tgt:punishes_immobile_backline | enabler_payoff | synergy | med  |

Exact confidence values tuned against the validation slice, not this table.

### Exit criteria

1. Rule engine runs against all authored heroes and produces a relations.json.
2. The validation slice in `tests/invoker/test_kg_prototype.py` still passes after expansion.
3. Gold relations from `docs/specs/2026-04-18-benchmark-schema-and-cases.md` are all inferred.
4. No statistical evidence attachment happens in this stage; relation records may still carry empty `evidence.statistical` arrays until Stage 6 lands.

---

## Stage 6 — Evidence attachment

### Goal

Attach STRATZ and OpenDota pair stats to inferred relations as *evidence*, not as the source of truth. A relation with no stat support still exists; a stat-strong pair with no rule still produces nothing.

### Mechanism

After the rule engine produces relations, a separate pass (`src/invoker/kg/evidence.py`, new) walks the stat edges from `data/raw/` and for each inferred relation:

- looks up (`from_hero_id`, `to_hero_id`) in STRATZ + OpenDota pair tables,
- classifies alignment as one of `aligned` / `weakly_aligned` / `unobserved` / `contradicted` (thresholds defined in the module; tunable),
- appends a `RelationEvidenceStatistical` entry per (source, cohort). STRATZ pro-match stats populate `cohort=pro_global`; OpenDota pub matchups populate `cohort=pub`. The same mechanical relation record can carry evidence from both cohorts side-by-side.

Thresholds (first pass, tune against gold set):
- `aligned`: stat sign matches relation kind, magnitude ≥ baseline + 1 SD, games ≥ 30.
- `weakly_aligned`: sign matches, magnitude above baseline but < 1 SD.
- `contradicted`: sign opposite, magnitude ≥ 1 SD.
- `unobserved`: games < 30 or pair missing.

### Review outputs

`invoker report evidence --patch <p>` emits:

- Contradicted relations (a rule fires but stats disagree) — review candidates.
- Strong stat edges with no rule firing — vocabulary gap candidates.
- Unobserved high-confidence rules — fine, but surfaced for awareness.

### Exit criteria

1. Relations carry structured evidence blocks; absence is explicit, not implicit.
2. The contradicted-list is short (<10% of relations) — if not, rules or vocabulary need revision before shipping.
3. The "stat edges with no rule" list is reviewable in one sitting per patch.

---

## Cohort and team context — forward-compatible hooks

Dota drafting is cohort-specific: pub synergy, pro global synergy, and "what Team Spirit likes to pick" are three different things. This plan wires the first two and **reserves** the third so it can land without schema churn.

### What this plan implements

- `cohort` field on every `HeroRelation` record (already in prototype schema).
- `cohort="pub"` populated from OpenDota matchups.
- `cohort="pro_global"` populated from STRATZ pro-match `matchUp` data. Both evidence blocks can coexist on the same mechanical relation.
- `cohort` value `"pro_global"` = "observed across pro matches regardless of team."

### What this plan reserves but does not implement

- `cohort="pro_team:<slug>"` — the hook for team-specific preferences (Team Spirit's Magnus+Tiny, OG's five-pos Grimstroke, etc.). Slug format and data source (parsed from specific pro match sets) stay undefined here.
- **Motifs** — multi-hero bundles (duo, trio, lineup) that express *why* a team picks a pattern together, when the value is not reducible to pairwise edges. Not pair relations; their own artifact. Reserve `data/derived/<patch>/motifs.json` with two shapes:

  **Abstract motif** — a lineup template keyed by role + required capability, no hero IDs. Generic, cohort-agnostic:
  ```yaml
  motif_id: reverse_polarity_magic_followup
  participants:
    - role: gatherer
      required_capability: mass_lockdown
    - role: burst
      required_capability: aoe_magic_burst
  requirements: [initiation_tool, magic_damage_core]
  benefits: [teamfight_wipe]
  ```

  **Instantiated motif** — an abstract motif + specific heroes + optional cohort tag. This is where "Team Spirit's Magnus+Tiny" sits:
  ```yaml
  motif_id: reverse_polarity_magic_followup/spirit_magnus_tiny
  instantiates: reverse_polarity_magic_followup
  example_heroes:
    - {role: gatherer, hero_id: 97}
    - {role: burst, hero_id: 19}
  cohort: pro_team:team_spirit
  evidence: {games: 18, win_rate: 0.66}
  ```

### Why keep this forward-compat but out of scope

- Motif inference needs input that doesn't exist yet: team-tagged match histories, lineup role vocabulary, draft-level context features. Designing the abstract motif set from memory without that grounding produces plausible-looking but untethered entries — the exact failure mode CLAUDE.md forbids.
- Putting `cohort` on the pair relation today means a later team-layer PR is **additive**: attach a new evidence block with `cohort=pro_team:spirit`, write `motifs.json`, done. No schema break.

### What to tell the user now

When someone asks "where do Team Spirit's duo picks go?", the answer is:
- pair-level mechanical relations exist regardless of team and appear in `relations.json`;
- team preference **reinforces** those relations via a cohort-scoped evidence block (future PR);
- team-specific duo/trio *patterns that are not reducible to pair mechanics* live in `motifs.json` (future PR).

That distinction — generic pair mechanics vs. team-preferred motif — is the decision this plan makes now so later PRs don't relitigate it.

---

## Migration & deprecation

### Remove immediately (Stage 2 start)

- `src/invoker/pipeline/extract.py` — replaced by fact loader.
- `src/invoker/pipeline/reason.py` — replaced by rule engine.
- `src/invoker/pipeline/orchestrator.py` two-pass logic, `tagged == 0` guard, batch reason call budget.
- `src/invoker/llm/gemini.py` — production path no longer calls it. Keep `ManualClient` for the draft-facts helper; delete `GeminiClient`, `CachingLLMClient` quota/retry, and RPM/RPD env plumbing. (If the draft-facts helper wants an automated LLM later, it can live in a separate `tools/` area, not the pipeline.)
- `functional_tags` / `tag_sources` fields on `HeroDerived`.
- `--skip-reasons`, `--max-reason-edges`, `--manual` flags on `bootstrap` (manual becomes the only mode).

### Keep

- `fetch` + `CachedClient` — stats still need refresh per patch.
- `derive` stat-edge merging (now feeds Stage 6 evidence attachment, not ontology).
- `finalize_patch` manifest + graph build.
- **Prompt rendering infrastructure** — the prompt file loader, version parsing, and `ManualClient` file-based loop stay. Rendering `src/invoker/prompts/*.md` with hero ability text is a pipeline concern (Stage 3 `draft-facts`, Stage 4 `suggest-vocabulary`). Only `GeminiClient` and its quota plumbing go.

### Schema migration

`HeroDerived.schema_version` bumps from whatever it is now → next. Old per-patch derived files become unreadable, which is fine — `data/` is not checked in and patches are re-buildable.

### Authored data policy for this plan

For Stages 2–6, use local files first.

- canonical authored facts live under `data/authored/*.yaml` in the local workspace;
- bootstrap and validation commands read those files directly;
- derived outputs under `data/derived/` and fetched raw payloads under `data/raw/` remain untracked build artifacts.

This keeps the current implementation simple and avoids blocking Stage 3 on bundle/release design.

### Deferred packaging decision

A separate bundle/install flow is still a plausible future direction, but it is explicitly **out of scope for this plan revision**.

If we later need cleaner distribution, we can add a follow-up plan for:

- moving canonical authored YAML into a secondary source;
- publishing a versioned authored-data bundle;
- adding install/fetch commands in this repo.

For now, none of that should shape Stage 3 implementation.

---

## Rollout sequence

One stage per PR. Each stage's exit criteria must pass before the next starts. Estimated lines of change per stage in parentheses; these are ceilings, not targets.

1. **Stage 2 schema + teardown** (~500 lines net delete). Promote prototype schemas, delete extract/reason/GeminiClient. Pangolier authored by hand as smoke test. **Commit boundary.**
2. **Stage 3 authoring workflow** (~500 lines). Fact loader, YAML parser, `draft-facts` prompt renderer, `validate-facts`, `show-relations`, `data/authored/README.md`. Author Pangolier + 9 more heroes covering a diverse vocabulary slice. **Commit boundary.**
3. **Stage 4 LLM-assisted vocabulary** (~250 lines). `suggest-vocabulary` prompt renderer, `vocab-proposals.yaml` inbox, `promote-vocabulary` command, `kg-vocabulary-notes.md`. Run one full suggest-review-promote cycle against the 10 authored heroes. **Commit boundary.**
4. **Stage 5 rule engine expansion** (~300 lines). Add rules per the table above, port validation slice tests. **Commit boundary.**
5. **Stage 6 evidence attachment** (~300 lines). New `evidence.py`, cohort-scoped stat classification, `report evidence` CLI, threshold tuning. **Commit boundary.**

Total ceiling ~1850 lines of change, mostly net-deletion in Stage 2. Realistic calendar: one focused week per stage if authoring heroes in parallel; Stage 3's 10-hero authoring is the long pole.

---

## Non-goals (explicit)

These are explicitly out of scope for this plan. Defer to a later plan:

- Lane templates, teamfight motifs, tempo profiles (forward-compat home: `motifs.json`; see §"Cohort and team context").
- Team/player identity and roster-aware scope (forward-compat hook: `cohort="pro_team:<slug>"`).
- Draft-state reader API (`candidate_bundle`, `requirements_filled`).
- Cross-patch diff reasoning.
- Automated re-authoring when a patch reworks a hero — we'll regenerate manually and keep it simple.

---

## Risks

- **Authoring drift between heroes.** Mitigation: `data/authored/README.md` carries a short style guide and examples. Review every authored hero against it for the first ~30 heroes.
- **Vocabulary explosion under authoring pressure.** Mitigation: vocabulary additions are a separate PR with two-hero justification (Stage 4).
- **Stat contradictions that aren't reviewed.** Mitigation: Stage 6 `report evidence` command makes the contradiction list a visible artifact per patch.
- **Human inconsistency on score values.** Mitigation: scores are advisory at first; the rule engine uses only presence/absence. If score-weighted ranking becomes important, calibration comes in a later plan.

---

## Sign-off

### Resolved

- **YAML for authored files.** Format isn't critical; YAML wins on multiline evidence + comments.
- **Delete obsolete pipeline modules.** `pipeline/extract.py`, `pipeline/reason.py`, `llm/gemini.py` deleted in Stage 2 — `archive/agentic-kg` covers rollback. (`GeminiClient` goes with them; `ManualClient` is the only LLM client.)
- **Motif work fully deferred.** The `cohort` hook on pair relations is the forward-compat contract. Motif schema landing is a separate future plan once team-match data exists.
- **Authored facts are local files for now.** `data/authored/` is the working source for this plan; bundle/release mechanics are deferred to a later plan.
