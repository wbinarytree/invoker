> **Status: superseded by `docs/architecture.md` "Known Gaps" (2026-04-26).**
> References removed pipeline shape (`run_for_hero`, `finalize_patch`). Bundle/install remains a planned roadmap item — see the bundle/install entry under `docs/architecture.md` "Known Gaps" — but will be redesigned fresh from the manual-assisted-KG architecture, not from this spec. Kept only as historical trace.

# Bundle Assembly + Bootstrap Wiring

**Date:** 2026-04-16  
**Status:** approved  
**Scope:** small; new `pipeline/bundle.py`, updated `cli.py`

---

## Problem

`bootstrap` calls `fetch_all` but never calls `run_for_hero` or `finalize_patch`.  
The "bundle-assembly helper" stub in the CLI has been a blocker since the orchestrator landed.

---

## New module: `pipeline/bundle.py`

Single public function:

```python
def build_bundles(raw: dict, patch: str) -> list[HeroRawBundle]
```

Converts the `fetch_all` output dict into one `HeroRawBundle` per hero.

### Ability resolution

`raw["hero_abilities"]` maps `npc_dota_hero_<name>` → `{"abilities": [...], "talents": [...]}`.  
`raw["abilities"]` maps ability internal name → `{dname, desc, ...}`.

For each hero: look up its ability list, resolve each to `{"name": dname, "text": desc}`.  
Skip abilities with no `dname` or no `desc` (talent bonuses, hidden fillers).

### Meta stats

No source exists today for position counts, contest rate, or win rate without fetching  
individual match details (expensive). Explicit zeros are used — correct per GUIDELINES  
("null is correct when data is missing").

| Field | Value |
|-------|-------|
| `position_counts` | `{}` |
| `total_pro_games` | `0` |
| `window_days` | `0` |
| `contest_rate` | `0.0` |
| `win_rate` | `0.0` |
| `meta_history` | `[]` |

A future spec will add a proper stats source (e.g. OpenDota `/heroStats`).

---

## CLI wiring (`cli.py` `bootstrap`)

After fetch:

1. `build_bundles(raw, patch)` → list of bundles
2. Build `CachingLLMClient(make_client(cfg.llm_client), cache_dir)`
3. For each bundle: `run_for_hero(cfg.data_dir, patch, version, bundle, client)`
4. Print per-hero result (success / failure reason)
5. `finalize_patch(data_dir, patch, hero_ids, complete=hero_filter is None)`

`complete=False` when a filter is active — manifest marks the run as partial.

---

## Out of scope

- Pro match stats (separate spec)
- `--skip-extract` flag wiring (separate small task)
