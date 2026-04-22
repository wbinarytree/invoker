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

Repo ships as a framework with **no data**. Fresh clone = zero heroes until bootstrap runs. Everything under `data/` is gitignored.

- `data/raw/` — verbatim API responses. Never hand-edited.
- `data/derived/` — deterministic transform of raw + code (and, going forward, hand-authored fact profiles).
- `data/cache/` — regeneratable indexes (graph, vector, LLM cache).

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

## Working With Claude

- Non-trivial changes get a short spec in `docs/specs/YYYY-MM-DD-<topic>.md` with user sign-off before code.
- Claude asks before destructive or external-facing actions. See `CLAUDE.md`.

## Commits

Small, topical. Never commit `.env`, raw API dumps, cache files, or anything containing keys.
