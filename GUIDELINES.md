# Invoker — Project Guidelines

Living doc. Rewrite any rule that stops being useful. v0.

## Stack & Layout

- Python 3.11+, `uv` for env/deps, `ruff` for lint+format, `pyright` non-strict. Formatter decides style.
- `src/invoker/` — source
- `src/invoker/prompts/` — versioned prompt files (never inline strings)
- `data/` — see Data Discipline
- `docs/specs/` — design docs, `docs/plans/` — implementation plans
- `tests/` mirrors `src/invoker/` under `tests/invoker/`; shared helpers in `tests/support/`, recorded payloads in `tests/fixtures/`

## Data Discipline

Repo ships as a framework with **no fetched data**. Fresh clone = zero heroes until bootstrap runs. Everything under `data/` is gitignored, with one exception: `data/kb/` — generated encyclopedia artifacts — is committed for archival (decision 2026-07-25; see `data/kb/README.md` for licensing).

- `data/raw/` — verbatim API responses. Never hand-edited.
- `data/derived/` — deterministic transform of raw + code (and, going forward, hand-authored fact profiles).
- `data/cache/` — regeneratable indexes (graph, vector, LLM cache).
- `data/kb/` — generated, provenance-pinned encyclopedia artifacts. Committed.

Every derived file carries a header with `schema_version`, `generator_version`, `source_patch`, `generated_at`. Schema changes bump `schema_version`; consumers may refuse mismatched versions.

How consumers ship the knowledge (release bundle, S3, etc.) is a separate future decision. The framework never carries a payload.

## Storage Model

JSON files are the source of truth. Derived access layers (NetworkX graph, local vector index) rebuild from JSON. No graph DB or hosted vector store until we hit a real ceiling.

## LLM-Generated Content

Any artifact our code produces via an LLM records model, prompt file + hash, input hash, timestamp. A deterministic validator gates writes to `data/derived/` — validator failure blocks the write. Prompts live in `src/invoker/prompts/` as `.md` files; bump prompt version on behavior-changing edits.

Missing knowledge is explicit: null + zero sample size, never plausible-looking placeholders.

## Secrets

`.env` gitignored, `.env.example` committed. Keys referenced only via `config.py`. No key strings in code, tests, or fixtures.

## Testing

Pragmatic. Not TDD.

- Test the boundaries that matter: fetchers (with recorded fixtures), validators, query API, schema compatibility.
- Do not unit-test LLM prose. Test the validator that gates it.
- Write a test when a bug bites twice or a contract crosses a module boundary. Don't test private helpers.

## Design Discipline

- Non-trivial changes get a short spec in `docs/specs/YYYY-MM-DD-<topic>.md` with user sign-off before code.
- A spec covers: outcomes, scope boundaries, constraints, prior decisions, task breakdown, verification criteria. Skip sections that don't apply; don't pad.
- Retrospective notes from a brainstorm or design discussion go in `docs/notes/YYYY-MM-DD-<topic>.md`, one page max. Index from `docs/CURRENT_DIRECTION.md` if load-bearing.
- Stage handoffs (long-form context for the next session) go in `docs/handoff-YYYY-MM-DD-<topic>.md`.
- `docs/CURRENT_DIRECTION.md` is the index for the active design set. Keep it current.
- Claude asks before destructive or external-facing actions. See `CLAUDE.md`.

## Architecture Doc Is Source of Truth

`docs/architecture.md` is the root implementation record and links to companion docs
(`docs/cli.md`, `docs/context-modules.md`, and future additions). Together they
describe only the code that exists today — not aspirational design.

- A PR that adds or modifies a CLI command **must** update `docs/cli.md` in the same PR.
- A PR that adds or modifies a context module **must** update `docs/context-modules.md` in the same PR.
- A PR that adds or modifies a schema, validation layer, pipeline step, or any module without a dedicated doc **must** update `docs/architecture.md` in the same PR.
- Every PR that touches any architecture doc **must** bump `Last updated:` in `docs/architecture.md`.
- Bug fixes that don't change shape are exempt.
- When these docs conflict with a spec or plan, the architecture docs win. Stale plans are not silent overrides.

## Doc Lifecycle

Stale docs mislead. Treat doc removal with the same rigor as doc creation.

- When a spec, plan, handoff, or note is superseded, decide: **delete** (if it would only confuse) or **archive** (if useful as historical trace).
- Archived docs go to `docs/archive/<original-subpath>/` with a one-line `Status: superseded by …` at the top, pointing at what replaced it.
- Archived docs are out of the active set. Do not read them to derive current behavior. Read them only when investigating the history of a decision, and only when necessary.
- `docs/CURRENT_DIRECTION.md` and `docs/architecture.md` are the active index. A doc not referenced from either is not authoritative — flag it for triage rather than treating it as load-bearing.
- When deleting a doc, the commit message names what replaced it (or notes "no replacement; obsolete"). Same for archives.

## Change Flow

Every change goes through this loop. No exceptions on `main`.

1. Branch off `main` for any change.
2. Write tests for behavior that changes — see Testing.
3. `uv run pytest`, `uv run pyright`, `uv run ruff check` all pass.
4. **On user approval to open the PR**, run the sub-agent review pass with Claude Sonnet 4.6 (or equivalent) in a fresh context. The trigger is explicit user approval ("ready to ship", "open the PR", or similar) — not after every commit, not mid-flight. Brief lives in `docs/specs/2026-04-26-collaboration-harness.md`.
5. **Decide on the review.** Surface the verdict and findings to the user and ask whether to address now, push as-is with follow-ups captured, or fix a subset. Do not push silently — a review the user never decides on is wasted token spend. Paste the final review summary into the PR description regardless of which path is chosen.
6. Architecture doc updated in the same PR if the change has shape impact.
7. Open PR. One logical change per commit.

## Hard Lines (Non-goals)

- No LLMs in `bootstrap` or the query path. LLMs are interactive only (authoring helper).
- No Dota facts asserted from training memory anywhere in code, data, or docs.
- No silent retries to "fix" a bad LLM extraction — surface the failure.
- No backwards-compat shims while pre-1.0.

## Commits

Small, topical. Each commit stands on its own. Never commit `.env`, raw API dumps, cache files, or anything containing keys.

Changes to `GUIDELINES.md` go in their own commit with a short rationale, so rule history is auditable.
