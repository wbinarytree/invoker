> **Status: superseded by implementation (2026-04-26).**
> Implemented as `INVOKER_DEV_HEROES` in `src/invoker/config.py` and the `--heroes` flag on `bootstrap`. Spec is no longer pending sign-off.

# Dev Hero Filter

**Date:** 2026-04-16  
**Status:** draft — awaiting sign-off  
**Scope:** trivial-to-small; touches `fetch.py`, `cli.py`, `config.py`, `.env.example`

---

## Problem

Bootstrap fetches all ~130 heroes and runs one LLM extraction call per hero.  
Gemini free tier caps at 20 calls/day, making full-bootstrap unusable for iterative dev work.  
The `--heroes` CLI option exists but is not wired up anywhere.

---

## Solution

Wire a hero filter through the full pipeline so only a named subset is fetched and processed.  
Default dev set: **Pangolier + Slardar** (representative synergy/counter pair).

### Filter resolution

1. `fetch_all` fetches the global hero roster (single cheap cached call) as always.  
2. It then resolves the filter against that roster — accepts **hero names** (case-insensitive) or **numeric IDs**.  
3. Only the resolved heroes get per-hero API calls (matchups, STRATZ synergies) and LLM extractions.

### Two ways to set the filter

| Method | When to use |
|--------|-------------|
| `--heroes "Pangolier,Slardar"` CLI flag | One-off runs |
| `INVOKER_DEV_HEROES=Pangolier,Slardar` in `.env` | Day-to-day dev; set once, forget |

CLI flag takes precedence over env var. No filter = all heroes (production behaviour unchanged).

---

## Changes

| File | Change |
|------|--------|
| `config.py` | Add `dev_heroes: frozenset[str] \| None` field, read from `INVOKER_DEV_HEROES` |
| `pipeline/fetch.py` | Add `hero_filter: set[str \| int] \| None` param; filter hero list after roster fetch |
| `cli.py` | Parse `--heroes` string; merge with `cfg.dev_heroes`; pass to `fetch_all` |
| `.env.example` | Document `INVOKER_DEV_HEROES` |

---

## What does NOT change

- Global fetches (hero roster, abilities, pro matches) — always run; results cached.
- `run_for_hero`, `finalize_patch` — already operate per-hero; no change needed.
- `--skip-extract` — continues to work orthogonally.
- Production bootstrap (`--heroes` omitted, `INVOKER_DEV_HEROES` unset) — identical behaviour.

---

## Milestone gate

Once Pangolier + Slardar are clean end-to-end (fetch → extract → reason → graph), we run `invoker validate` against them as the green bar before lifting the filter for full bootstrap.
