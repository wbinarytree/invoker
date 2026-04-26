# docs/notes/

Retrospective notes from brainstorms, design discussions, and decisions that don't warrant a full spec.

## When to write a note

Write one whenever a conversation produces a non-obvious learning that the next session would benefit from knowing. Specifically:

- A design discussion that changed direction (capture *why* the old direction was wrong)
- A brainstorm that produced an option set, with the chosen path and the rejected ones
- A surprise found while implementing — something that should inform future work in this area
- A piece of guidance to your future self / a future agent

## When not to write a note

- Forward design that needs sign-off — that's a `docs/specs/` doc.
- Stage-completion summary — that's a `docs/handoff-...` doc.
- "What I changed in this PR" — that's the PR description.
- A code comment in disguise — put it in the code.

## Format

- File: `docs/notes/YYYY-MM-DD-<topic>.md`
- One page max. If it's longer, it's probably a spec.
- Suggested sections (skip what doesn't apply):
  - **Context** — one paragraph: what triggered this note.
  - **Decision / learning** — the durable takeaway.
  - **Why** — the reasoning, especially what made the alternative wrong.
  - **Implications** — how this should shape future code or process.

## Indexing

If a note is load-bearing for active design (i.e. agents should read it before working in that area), add a pointer in `docs/CURRENT_DIRECTION.md`. Otherwise the directory is the index — `ls docs/notes/` is enough.

## Lifecycle

Same rule as the rest of `docs/` — see `GUIDELINES.md` → "Doc Lifecycle". Superseded notes get deleted (if they'd only confuse) or moved to `docs/archive/notes/` with a `Status: superseded by …` line. Don't keep a stale note "just in case."
