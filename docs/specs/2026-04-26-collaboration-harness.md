# Collaboration Harness — Spec

Date: 2026-04-26
Status: accepted

## Outcomes

- Every PR ships with tests, a fresh-context sub-agent review, and an up-to-date `docs/architecture.md`.
- Any coding agent (Claude Code, Codex CLI, Cursor, Aider) can pick up this repo from a single entrypoint (`AGENTS.md`) and follow the same process.
- Brainstorm and architectural decisions are captured durably so the next session does not relitigate them.

## Scope

- Process and documentation. No runtime code changes.
- Files in scope: `AGENTS.md`, `GUIDELINES.md`, `docs/architecture.md`, `docs/notes/`, this spec.
- Out of scope: CI enforcement, automated PR-template injection, automated review bots. Those are future work; for now the harness is a checklist.

## Constraints

- `AGENTS.md` stays short — agents read it as system prompt.
- Sub-agent review uses Claude Opus 5 (`claude-opus-5`; user decision 2026-07-25 — originally Claude Sonnet 4.6), not the same conversation running the implementation, so the review has fresh context and a different angle.
- Sub-agent review fires on **explicit user approval to open the PR**, not after every commit. Mid-flight reviews waste tokens reviewing churn that's about to change.
- Architecture-doc updates are strict same-PR. No follow-ups, no "I'll do it later" — keeps doc and code in lockstep.
- Notes (`docs/notes/`) are retrospective and short (one page). Specs (`docs/specs/`) are forward-looking and may be longer.
- Doc lifecycle is symmetric with doc creation: superseded docs get deleted (if confusing) or archived to `docs/archive/` (if historically useful). Archived docs are not read to derive current behavior.

## Prior decisions adopted

- AGENTS.md convention (60K+ repos as of early 2026; Anthropic + OpenAI Codex both default to it). Pure markdown, README-for-agents.
- Anthropic's "separate doer from judge" pattern from their long-running-agent harness work — sub-agent review is a separate, fresh-context evaluator pass.
- Spec-driven development's six-element template — outcomes, scope, constraints, prior decisions, task breakdown, verification — applied to specs in this repo going forward.
- Retain existing handoff convention (`docs/handoff-...`) for stage handoffs. Notes are different: shorter, retrospective, brainstorm-derived.

## Sub-agent review brief

Use this brief verbatim (or as close as a non-Claude agent allows). Paste output into the PR description under a `## Sub-agent review` heading.

> You are reviewing a pending change on a feature branch. You have not seen this change before. The implementing agent may be biased toward shipping; your job is to be the second pair of eyes.
>
> Read:
> - `git diff main...HEAD`
> - `git log main..HEAD`
> - Files changed (open the full file, not just the diff hunk)
> - `AGENTS.md`, `GUIDELINES.md`, `CLAUDE.md`, `docs/architecture.md`
>
> Then answer, briefly:
>
> 1. **Shape & intent** — what is this change actually doing? One paragraph in your own words.
> 2. **Tests** — does the test coverage match the behavior that changed? Any boundary not tested? Any test that asserts on incidental detail rather than contract?
> 3. **Architecture doc** — was `docs/architecture.md` updated where it should have been? Any new command, schema, validation layer, pipeline step, or module that's not reflected?
> 4. **Hard lines** — does this respect the non-goals in `GUIDELINES.md`? (No LLM in bootstrap/query path, no Dota facts from memory, no silent retries, etc.)
> 5. **Different-angle concerns** — what would a senior engineer who didn't write this catch? Naming, hidden coupling, code that will rot, a simpler alternative the author didn't consider, a future maintenance trap.
> 6. **Verdict** — `ship`, `ship-with-nits`, or `block`. If block, list the must-fix items.
>
> Keep the whole review under 400 words. Be specific, not generic.

## Acting on the review

When the review returns, the implementing agent does **not** push immediately. The flow is:

1. Surface the verdict and findings to the user verbatim (or close to it — don't paraphrase findings into vagueness).
2. Ask the user explicitly: address findings now, push as-is and capture findings as follow-ups in the PR description, or fix a subset and defer the rest?
3. If the user picks "address now," fix, re-run tests, and re-run the review on the new state before pushing. (A second review on a small delta is fine; it does not re-burn the full review cost if scoped to "did the previous findings get addressed?".)
4. If the user picks "push as-is," ensure every reviewer finding appears as a checklist item in the PR description so it can't get silently dropped.
5. **Mandatory exception:** any reviewer finding that contradicts a rule this codebase establishes (architecture-doc lockstep, hard lines in `GUIDELINES.md`, etc.) gets fixed before push regardless of the user's "now or later" preference. The harness rules are not negotiable per-PR.

A review the user never decides on is wasted. The decision step is part of the harness, not optional.

## Task breakdown (this PR)

1. Rewrite `AGENTS.md` as agent-neutral entrypoint.
2. Add change-flow, design-discipline, architecture-doc, and hard-lines sections to `GUIDELINES.md`.
3. Write this spec.
4. Add `docs/notes/README.md` and the first retrospective note.
5. Add an "update discipline" note to `docs/architecture.md` and bump `Last updated:`.

## Verification

- `AGENTS.md` reads cleanly as a system-prompt-sized briefing for a fresh agent.
- `GUIDELINES.md` rules are testable: a contributor can answer "did I follow this?" yes/no per rule.
- Spec has six elements present (this one).
- Sub-agent review brief produces a concrete review when run on a real diff (will be verified on the next PR).
- Architecture doc lists `Last updated: 2026-04-26` after this PR.

## Future iterations

- Automate the sub-agent review trigger via a pre-PR hook or GitHub Action once the workflow has settled.
- Extract the brief into a reusable agent definition under `.claude/agents/` once Claude Code subagent definitions stabilize for this repo.
- Re-evaluate after ~5 PRs: if any rule is consistently skipped, either drop it or automate it. Don't keep dead rules.

## Considered and deferred

- **Three-agent harness (planner / generator / evaluator).** Anthropic's published harness work uses three agents for long-running app development. For a small repo with discrete PR-sized changes, our single implementer + fresh-context reviewer captures most of the value. Revisit if a single PR ever spans more than a session.
- **Spec-as-source.** The strongest form of spec-driven development edits specs rather than code. Too aggressive for stage 4. Stick with spec-first (sign-off before code) for now.
- **Rolling progress file (`claude-progress.txt` style).** Anthropic uses a single rolling progress file across context resets. Invoker's per-stage `docs/handoff-...` files cover the same need because work is naturally staged here.
