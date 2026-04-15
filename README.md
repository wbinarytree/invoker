# Invoker

Knowledge base framework for Dota 2 fundamentals - structured, patch-aware, LLM-consumable knowledge for downstream drafting and replay agents.

## What's here

The repo ships as a framework with **no data**. All knowledge is bootstrapped from public sources (OpenDota, STRATZ, Liquipedia) and enriched with LLM-extracted mechanical tags.

## Quick start

```bash
uv sync
cp .env.example .env                # fill in keys
uv run invoker --help
uv run invoker bootstrap --patch 7.41b
```

## Docs

- `GUIDELINES.md` - project rules (living)
- `CLAUDE.md` - AI collaboration rules
- `docs/specs/` - architecture design docs
- `docs/plans/` - implementation plans

## License

Private.
