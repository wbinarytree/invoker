# Harness Establishment

Date: 2026-04-26

## Context

Stage 4 vocabulary review is mostly landed. Before opening more PRs, we wanted process hygiene that any coding agent (Claude Code, Codex, others) could pick up and follow without re-deriving the rules.

## Decisions

- **`AGENTS.md` is the single agent entrypoint.** It points to `GUIDELINES.md` and `CLAUDE.md` rather than duplicating them. Kept short because it's effectively part of every agent's system prompt.
- **Sub-agent review is mandatory, every PR.** Claude Sonnet 4.6 (or equivalent) in a fresh context. Different model from the implementing agent so the review carries a different angle. Brief lives in the harness spec.
- **Architecture doc updates are strict same-PR** for any shape change. Bug fixes are exempt. Stale architecture docs were the failure mode we're avoiding.
- **`docs/notes/` for retrospective brainstorm learnings.** Separate from `docs/specs/` (forward design) and `docs/handoff-...` (stage handoffs).

## Why

- Anthropic's published harness work shows separating "doer" from "judge" agents materially improves output quality on long-running coding tasks. The fresh-context review pass operationalizes that locally.
- Industry has converged on `AGENTS.md` as the cross-tool convention (60K+ repos as of early 2026). Adopting it costs us nothing and unlocks every agent tool's default support.
- Spec-driven development's six-element template (outcomes, scope, constraints, prior decisions, task breakdown, verification) gives specs a predictable shape so reviewers — human or agent — know where to look.
- Architecture docs rot fast when updates lag. Same-PR enforcement is the cheapest sustainable rule.

## Rejected alternatives

- **Following PRs for architecture-doc updates.** Considered, rejected — the gap between code and doc is exactly what we're trying to eliminate.
- **Sub-agent review only on non-trivial PRs.** Rejected — defining "trivial" is itself a judgment call that gets gamed. Cheaper to always run the review; trivial PRs produce trivial reviews.
- **Folding notes into `docs/specs/`.** Rejected — different intent (retrospective vs. forward) and different review bar (no sign-off needed for notes).

## Implications

- Future PR descriptions include a `## Sub-agent review` section.
- A PR that should have updated `docs/architecture.md` but didn't is a blocker, not a nit.
- After ~5 PRs, revisit the rules: anything consistently skipped should be dropped or automated. Don't keep dead rules.
