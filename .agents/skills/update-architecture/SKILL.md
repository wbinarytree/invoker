---
name: update-architecture
description: Update docs/architecture.md to reflect an architectural change just made or about to be made.
---

You are updating `docs/architecture.md`, the living implementation artifact for the Invoker project.

This document is the source of truth for what is actually implemented — not what was designed or planned. Keep it accurate and concise. Do not add aspirational content.

## When to update

Update `docs/architecture.md` when any of the following changes:

- A new data source is added or an existing one is removed
- The STRATZ GraphQL query changes (fields, query name, brackets)
- The LLM layer changes (new client, new wrapper, retry/pacing logic)
- A new pipeline stage is added or an existing stage changes its contract
- The output schema (`HeroDerived` or sub-models) gains, loses, or renames a field
- The cache key strategy changes
- The prompt versioning convention changes
- A strategy decision is reversed (e.g. "we dropped X in favour of Y")
- The config / environment variable contract changes

Do NOT update for:
- Bug fixes that don't change the observable contract
- Test additions
- Refactors that keep the same behaviour
- Changes inside a single module that don't affect the pipeline contract

## How to update

1. Read `docs/architecture.md` to understand the current state.
2. Read any changed files to understand the new state.
3. Edit only the affected section(s) of `docs/architecture.md`. Do not rewrite sections that are unchanged.
4. Update the `Last updated` date at the top.
5. If a data source was dropped or a strategy reversed, record the decision and rationale clearly (e.g. "Dropped: Liquipedia — replaced by OpenDota constants").

Keep the document factual and present-tense. One sentence of rationale per major decision is enough.
