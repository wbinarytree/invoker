# AGENTS.md

Entrypoint for any coding agent on this repo (Claude Code, Codex CLI, Cursor, Aider, others).

## Read docs before code

When something is unclear, read the docs first. Only fall back to the source when the docs don't answer it. The docs are the source of truth; the code is the implementation.

- `docs/architecture.md` — current implementation; source of truth for system shape, modules, schemas
- `docs/CURRENT_DIRECTION.md` — index of active design docs
- `docs/context-modules.md`, `docs/cli.md`, `docs/opendota-cache.md` — module-level references linked from architecture.md
- `GUIDELINES.md` — project rules (stack, data discipline, testing, design discipline)

If you find yourself grepping the codebase to answer "what does X do?" before checking these, stop and check them first.

## Hard lines

- No Dota facts from training memory. Cite a source file or mark unknown. Null is correct when data is missing — never fill plausible placeholders.
- No LLM in the bootstrap or query path. LLMs are interactive only (authoring helper).
- No silent retries on bad LLM extractions — surface the failure.
- `data/` is gitignored. No data committed.
- Specs go in `docs/specs/YYYY-MM-DD-<topic>.md` *before* discussion. Don't substitute a chat markdown block for the spec file.
- Trigger discussion mode before implementation when a change needs design, vision, or plan alignment.
- Ask before destructive or external-facing actions: force-push, rewriting history, branch/tag deletion, full all-hero API fetch, deleting outside the working change, publishing/releases/tagging, regenerating large derived artifacts.

## Branch & PR loop

1. Never commit on `main`. Create a feature branch first.
2. Write tests for behavior that changes — validators, query API, schema, CLI surface. Don't unit-test LLM prose.
3. `uv run pytest`, `uv run pyright`, `uv run ruff check` must pass.
4. **Sub-agent review on user's "ready to ship" signal, not mid-flight.** Brief in `docs/specs/2026-04-26-collaboration-harness.md`. Surface findings; ask whether to fix-now / push-as-is with follow-ups / cherry-pick. Paste the review summary into the PR body either way.
5. **Architecture-doc update, same PR.** If the change adds/modifies a CLI command, schema, validation layer, pipeline step, or new module, update `docs/architecture.md` (and any module doc it links to) and bump `Last updated:`. Bug fixes that don't change shape are exempt.
6. One logical change per commit.

## Doc lifecycle

Stale docs mislead. When a doc is superseded:

- **Confusion-only → delete.**
- **Historical trace → archive.** Move to `docs/archive/<original-subpath>/` with a `Status: superseded by …` line at the top.
- Don't read archived docs to derive current behavior — only to investigate *why* a past decision was made.
- If a doc is not in `docs/CURRENT_DIRECTION.md` or `docs/architecture.md`, treat it as not authoritative.

## Where things go

- Forward design (sign-off required for non-trivial): `docs/specs/YYYY-MM-DD-<topic>.md`
- Stage handoffs: `docs/handoff-YYYY-MM-DD-<topic>.md`
- Retrospective notes: `docs/notes/YYYY-MM-DD-<topic>.md`
- Implementation plans: `docs/plans/YYYY-MM-DD-<topic>.md`

## Project-specific style

- Not a TDD project. Ship features with tests for behavior that matters; how tests get written is free.
- No backwards-compatibility shims while pre-1.0.

## Stack quick-ref

Python 3.11+, `uv` for env/deps, `ruff` for lint+format, `pyright` non-strict. Tests live in `tests/invoker/` mirroring `src/invoker/`.
