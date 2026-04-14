# CLAUDE.md — Collaboration Rules for AI Assistance

Rules Claude follows when working in this repo. Living document. Change it any time.

## Source of Truth

Read `GUIDELINES.md` first. If anything here conflicts with it, `GUIDELINES.md` wins. Flag the conflict so we can fix it.

## Dota Knowledge Is Never Asserted From Memory

This is the whole point of this project. Claude does not assert Dota-specific facts (hero roles, abilities, patch state, synergies, counters) from training memory.

- If a fact comes from an API response, cite the source file.
- If a fact comes from an LLM extraction, cite the prompt and the input mechanic.
- If Claude does not know, it says so and we add a data source.
- Do not "fill in" placeholder Dota content that looks plausible. Null is correct when data is missing.

## Workflow

- Not a TDD project. Ship the feature, include tests for behavior that matters. How tests get written is free.
- For non-trivial work, write a short spec in `docs/specs/` and get user sign-off before writing code. Trivial work skips the spec.
- Use the superpowers brainstorming / writing-plans / executing-plans skills when they fit. Skip them for small edits.
- Do not invoke `test-driven-development` skill by default.

## Destructive & External Actions — Ask First

Ask before doing any of:

- `git reset --hard`, force-push, branch/tag deletion, rewriting published history
- publishing a package, creating releases, tagging
- hitting a paid API beyond a tiny probe call
- deleting files outside the working change
- regenerating large derived artifacts that would wipe hand-edited content

Hitting OpenDota or STRATZ with a small fetch is fine. A full all-hero fetch is not — confirm first.

## LLM Artifact Hygiene

When Claude's own code invokes an LLM to produce data:

- prompts live in `src/invoker/prompts/`, not inline strings
- output gets validated before it lands in `data/derived/`
- provenance (model, prompt hash, input hash, timestamp) stored with the artifact
- do not silently retry to "fix" a bad extraction; surface the failure

## Code Style

- Follow `ruff` formatting; do not argue with it.
- Prefer editing existing files over creating new ones.
- Default to no comments. Add one only when the *why* is non-obvious.
- Do not add features, abstractions, or error handling that the task does not require.
- No backwards-compatibility shims while the project is pre-1.0.

## Memory

Claude has a persistent memory store for this project. Save:

- user preferences / working style
- project-specific constraints ("we decided X because Y")
- pointers to external resources

Do not save code patterns, file paths, or anything a fresh read of the repo reveals.

## When Stuck

Ask. A two-sentence clarification beats an hour of wrong direction.
