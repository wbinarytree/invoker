# AGENTS.md

Entrypoint for any coding agent on this repo (Claude Code, Codex CLI, Cursor, Aider, others).

This file is intentionally short. Read these next:

- `GUIDELINES.md` — project rules (stack, data discipline, testing, design discipline)
- `CLAUDE.md` — collaboration rules; applies to any agent, not just Claude
- `docs/architecture.md` — current implementation; source of truth
- `docs/CURRENT_DIRECTION.md` — index of active design docs

## Branch & PR loop

1. Never commit on `main`. Create a feature branch first.
2. Write tests for behavior that changes. Boundaries that matter: validators, query API, schema, CLI surface. Don't unit-test LLM prose.
3. Run `uv run pytest`, `uv run pyright`, `uv run ruff check` — all must pass.
4. **Sub-agent review on approval, not mid-flight.** Do not run the review after every commit. When the user says the PR is ready (explicit "open the PR" / "ready to ship" / similar), then run a fresh-context review with Claude Sonnet 4.6 (or equivalent). Use the brief in `docs/specs/2026-04-26-collaboration-harness.md`. If you're unsure whether the user means "ready," ask.
5. **Act on the review before pushing.** When the review returns, surface the verdict and findings to the user and ask whether to (a) address findings now, (b) push as-is and capture findings as follow-ups in the PR description, or (c) cherry-pick a subset to fix now. Don't open the PR silently — a review the user never decides on is wasted. Paste the final review summary into the PR description either way.
6. **Architecture-doc update, same PR.** If the change adds/modifies a CLI command, schema, validation layer, pipeline step, or new module, update `docs/architecture.md` and bump its `Last updated:` line. Bug fixes that don't change shape are exempt.
7. One logical change per commit. Each commit should stand on its own.

## Where things go

- Forward design (sign-off required for non-trivial): `docs/specs/YYYY-MM-DD-<topic>.md`
- Stage handoffs (long-form context for the next session): `docs/handoff-YYYY-MM-DD-<topic>.md`
- Retrospective brainstorm notes (one page max): `docs/notes/YYYY-MM-DD-<topic>.md`
- Implementation plans: `docs/plans/YYYY-MM-DD-<topic>.md`

## Doc lifecycle

Stale docs are worse than missing docs — they mislead. When a spec, plan, handoff, or note becomes superseded:

- **Confusion-only → delete.** If keeping it around will only confuse a fresh agent, remove it.
- **Useful as historical trace → archive.** Move to `docs/archive/<original-subpath>/` and add a one-line `Status: superseded by …` at the top.
- **Don't query archived docs unless absolutely necessary.** They are explicitly out of the active set. Read them only when investigating *why* a decision was made, never to derive current behavior.
- `docs/CURRENT_DIRECTION.md` lists what's active. If a doc isn't there or in `docs/architecture.md`, treat it as not authoritative.

## Hard lines

- No Dota facts from training memory. Cite a source file or mark unknown.
- No LLM in the bootstrap or query path. LLMs are interactive only (authoring helper).
- No data committed. `data/` is gitignored.
- No silent retries on bad LLM extractions — surface failures.
- Trigger discussion mode before implementation when a change needs design, vision, or plan alignment. Do not jump directly from a strategic concern into code.
- Ask before destructive or external-facing actions (force-push, rewriting history, full all-hero API fetch, deleting outside the working change).

## Stack quick-ref

Python 3.11+, `uv` for env/deps, `ruff` for lint+format, `pyright` non-strict. Tests live in `tests/invoker/` mirroring `src/invoker/`.
