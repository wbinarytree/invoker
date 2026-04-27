@AGENTS.md

# Claude-specific addenda

`AGENTS.md` (imported above) is the cross-agent source of truth — branch/PR loop, doc lifecycle, hard lines, and stack quick-ref live there. The rules below apply only to Claude Code and supplement, not replace, those.

## Dota Knowledge — Elaboration of the Hard Line

Reinforcing the AGENTS.md hard line ("No Dota facts from training memory"):

- Facts from API responses cite the source file.
- Facts from LLM extractions cite the prompt and input mechanic.
- Unknown = say so and add a data source. Never fill plausible-looking placeholders. Null is correct when data is missing.

## Destructive Actions — Project-Specific Additions

Beyond the AGENTS.md "ask before destructive" rule and the Claude defaults, also confirm before:

- publishing a package, creating releases, tagging
- regenerating large derived artifacts that would wipe hand-edited content

## Workflow

- Not a TDD project. Ship the feature with tests for behavior that matters; how tests get written is free.
- Use the superpowers brainstorming / writing-plans / executing-plans skills when they fit; skip for small edits.
- Do not invoke `test-driven-development` by default.
- **Specs go in `docs/specs/` before discussion, not inline in conversation.** Any non-trivial design (new module, changed contract, open questions requiring sign-off) must be written to `docs/specs/YYYY-MM-DD-<topic>.md` first. Present the file path and the open questions — do not substitute a markdown block in chat for the actual spec file.

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
