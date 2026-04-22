# Invoker

Knowledge base framework for Dota 2 fundamentals — structured, patch-aware, LLM-consumable knowledge for downstream drafting and replay agents.

## Direction (2026-04-22)

The project is pivoting away from an **agentic automated-extraction pipeline** toward a **manual-with-LLM-assist** model:

- Hero fact profiles (capabilities / requirements / liabilities) are hand-authored per hero.
- Synergy and counter relations are inferred deterministically by a rule engine over those facts.
- Stat sources (STRATZ / OpenDota) serve as *evidence* for predicted relations, not as the ontology.
- LLMs are used interactively (outside the pipeline) to help draft fact profiles; they are not in the critical path.

Rationale: with ~120 heroes and incremental patches, a hand-curated substrate is cheaper and more honest than an automated extraction pipeline. Reworks require regenerating a single hero anyway.

The previous agentic-pipeline work is preserved on branch `archive/agentic-kg` in case we revisit that direction.

## What's here

The repo ships as a framework with **no data**. Authored facts and derived artifacts live under `data/` (gitignored) and are produced locally.

## Quick start

```bash
uv sync
cp .env.example .env                # fill in keys
uv run invoker --help
uv run invoker bootstrap --patch 7.41b
```

## Docs

- `GUIDELINES.md` — project rules (living)
- `CLAUDE.md` — AI collaboration rules
- `docs/architecture.md` — current implementation
- `docs/specs/` — design docs
- `docs/plans/` — implementation plans

## License

Private.
