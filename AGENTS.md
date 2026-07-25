# AGENTS.md

Entrypoint for any coding agent on this repo.

## Sources of truth

Docs first, code second. If you're grepping the source to answer "what does X do?", stop and read:

- `docs/architecture.md` — what the code does today; update it in the same PR as any shape change (new command, schema, pipeline step, module) and bump `Last updated:`
- `docs/CURRENT_DIRECTION.md` — index of active design docs; anything not listed there or in architecture.md is not authoritative
- `GUIDELINES.md` — project rules: stack, data discipline, provenance, testing, design discipline

## Hard lines

- No Dota facts from training memory. Cite a source file or mark unknown; null is correct when data is missing — never a plausible placeholder.
- LLM generation is pipeline-legal (rethink 2026-07-25) but never a fact source: generated prose cites substrate keys, faithfulness checks are mechanical, and bad LLM output is surfaced, never silently retried or repaired.
- `data/` is gitignored except `data/kb/` (committed encyclopedia artifacts). No raw or fetched data in git.
- Design before code: non-trivial changes get a spec in `docs/specs/YYYY-MM-DD-<topic>.md`, discussed and signed off before implementation. A chat message is not a spec.
- Ask before destructive or external-facing actions: force-push, history rewrites, branch/tag deletion, deleting outside the working change, full all-hero API fetches, publishing/releases, regenerating large derived artifacts.

## The loop

1. Feature branch — never commit on `main`. One logical change per commit.
2. Tests for behavior that changes; don't unit-test LLM prose. `uv run pytest`, `uv run pyright`, `uv run ruff check` must pass.
3. On the user's "ready to ship" signal (not mid-flight): fresh-context sub-agent review on Claude Opus 5 (`claude-opus-5`) per the brief in `docs/specs/2026-04-26-collaboration-harness.md`. Surface findings verbatim, get the user's fix-now / follow-up decision, paste the review into the PR body.

## Repo gotchas

- Game files assert removed mechanics (7.41d still ships `Facets` blocks though facets were removed in 7.41) — presence-in-files ≠ presence-in-game; the in-game changelog is the detector.
- Some effects exist only as display string + engine code (code-only talents) — ability questions need the full kit joined with localization, not ad-hoc lookups.
- Superseded docs mislead: delete (if confusing) or archive to `docs/archive/` with a `Status: superseded by …` header. Archived docs explain *why* past decisions happened, never current behavior.
- File homes: specs `docs/specs/`, plans `docs/plans/`, stage handoffs `docs/handoff-*.md`, retro notes `docs/notes/`.
- Pre-1.0: no backwards-compat shims. Not a TDD project — ship features with tests for behavior that matters.
