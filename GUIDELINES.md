# Invoker — Project Guidelines

Living document. Change any rule that stops being useful. v0.

## Stack & Layout

- Python 3.11+, `uv` for env/deps, `ruff` for lint+format, `pyright` non-strict.
- Formatter decides style. Do not bikeshed.
- Layout:
  - `src/invoker/` — source
  - `src/invoker/prompts/` — LLM prompts as versioned files, not string literals
  - `data/` — see Data Discipline
  - `docs/specs/` — design docs
  - `tests/` — tests (or next to code; pick per module, do not fight about it)

## Data Discipline

**The repo ships as a framework. No data lives in git.** All knowledge is bootstrapped by running the pipeline. A fresh clone has zero heroes, zero teams, zero edges until bootstrap runs.

Three tiers, all under `data/`, all gitignored:

- `data/raw/` — verbatim API responses. Fetched by `uv run invoker bootstrap` (or equivalent). Never edited by hand.
- `data/derived/` — everything produced by transforming raw (per-hero JSONs, team files, summaries, archetype definitions). Deterministic function of raw + code.
- `data/cache/` — regeneratable indexes (NetworkX pickle, vector index) to avoid rebuilding every run.

How consumers get the knowledge is a separate problem (published artifact, release bundle, S3 — future decision). The framework itself never carries a payload.

Every derived file carries a header:

```json
{
  "schema_version": 1,
  "generator_version": "invoker@0.1.0",
  "source_patch": "7.41b",
  "generated_at": "2026-04-14T18:00:00Z"
}
```

Schema changes bump `schema_version`. Consumers may refuse mismatched versions.

## Storage Model

JSON files are the source of truth. Two derived access layers, both rebuilt from JSON:

- **Graph**: NetworkX, in-process, used for structured multi-hop queries.
- **Vector index**: local (Chroma or FAISS), built over LLM-injectable summaries, used for fuzzy/semantic queries.

No graph database, no hosted vector store, no embeddings API lock-in until we hit a real ceiling. Graduation path (Neo4j, hosted vector DB) exists but is not taken speculatively.

## LLM-Generated Content

Any artifact touched by an LLM records, alongside the artifact:

- model name & version
- prompt file + hash
- input hash
- timestamp

LLM output lands in `data/derived/` only after a deterministic validator passes (schema check, required fields, tag-source presence). Validator failure blocks the write.

Prompts live in `src/invoker/prompts/` as `.md` or `.txt` files. Bump prompt version on behavior-changing edits.

## "No Data" Is Explicit

Missing knowledge is never silent omission. Use explicit nulls with zero sample size so downstream LLMs cannot confuse absence with neutrality.

## Secrets

- `.env` gitignored, `.env.example` committed.
- Keys referenced only via a single `config.py`.
- No key strings in code, tests, or fixtures.

## Testing

Pragmatic. Not TDD.

- Test the boundaries that matter: fetchers (with recorded fixtures), validators, query API, schema compatibility.
- Do not unit-test LLM prose. Test the validator that gates it.
- Fixtures = real recorded responses in `tests/fixtures/`, trimmed to what is needed.
- Test layout should stay navigable:
  - `tests/unit/<area>/` for isolated module tests
  - `tests/integration/` for multi-module flows
  - `tests/support/` for shared factories and helpers
  - `tests/fixtures/` for recorded payloads and gold files
- Test modules should not import helpers from other test modules. Shared builders belong in `tests/support/`.
- Write a test when a bug bites twice or when a contract crosses a module boundary.
- Do not test private helpers.

## Working With Claude

- Non-trivial changes get a short spec in `docs/specs/YYYY-MM-DD-<topic>.md` before coding, with user sign-off.
- Trivial changes skip the spec.
- Claude does not run destructive or external-facing actions (force-push, publishing, hitting paid APIs beyond a tiny probe) without checking first.
- See `CLAUDE.md` for collaboration rules specific to AI assistance.

## Commits

- Small, topical commits.
- Squash-or-not is your call per PR.
- Never commit `.env`, raw API dumps, cache files, or anything containing keys.

## Living Document

When a rule gets in the way, rewrite or delete it. Rules that survive rewrites earn their place.
