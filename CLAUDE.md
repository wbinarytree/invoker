# CLAUDE.md — AI Collaboration Rules

Read `GUIDELINES.md` first. This file covers AI-specific rules only. If anything here conflicts with `GUIDELINES.md`, that doc wins — flag the conflict.

## Dota Knowledge Is Never Asserted From Memory

The whole point of this project. Claude does not assert Dota-specific facts (hero roles, abilities, patch state, synergies, counters) from training memory.

- Facts from API responses cite the source file.
- Facts from LLM extractions cite the prompt and input mechanic.
- Unknown = say so and add a data source. Never fill plausible-looking placeholders. Null is correct when data is missing.

## Workflow

- Not a TDD project. Ship the feature with tests for behavior that matters; how tests get written is free.
- Use the superpowers brainstorming / writing-plans / executing-plans skills when they fit; skip for small edits.
- Do not invoke `test-driven-development` by default.
- **Specs go in `docs/specs/` before discussion, not inline in conversation.** Any non-trivial design (new module, changed contract, open questions requiring sign-off) must be written to `docs/specs/YYYY-MM-DD-<topic>.md` first. Present the file path and the open questions — do not substitute a markdown block in chat for the actual spec file.

## Destructive & External Actions — Ask First

Beyond the defaults, specifically confirm before:

- `git reset --hard`, force-push, branch/tag deletion, rewriting published history
- publishing a package, creating releases, tagging
- a full all-hero API fetch (small single-hero probes are fine)
- deleting files outside the working change
- regenerating large derived artifacts that would wipe hand-edited content

## LLM Artifact Hygiene

When Claude's own code invokes an LLM, do not silently retry to "fix" a bad extraction — surface the failure. (Provenance and prompt-file rules are in `GUIDELINES.md`.)

## Code Style

- Default to no comments. Add one only when the *why* is non-obvious.
- Do not add features, abstractions, or error handling the task does not require.
- No backwards-compatibility shims while pre-1.0.

## Memory

Persistent memory store for this project. Save:

- user preferences / working style
- project-specific constraints ("we decided X because Y")
- pointers to external resources

Do not save code patterns, file paths, or anything a fresh read of the repo reveals.

## When Stuck

Ask. A two-sentence clarification beats an hour of wrong direction.
