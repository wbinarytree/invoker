# Stage 4 Vocabulary Review Handoff

Date: 2026-04-25

## Context

The project is in Stage 4 of `docs/plans/2026-04-22-manual-assisted-kg-plan.md`.
Stage 2 and Stage 3 are closed enough to move on: authored hero YAML exists,
the deterministic relation engine runs, and current architecture is documented in
`docs/architecture.md`.

Stage 4's goal is to improve the vocabulary contract before Stage 5 expands the
rule engine. The chosen workflow is human-first:

1. inspect current live vocabulary terms
2. record human natural-language review notes
3. inspect vocabulary gaps produced by hero authoring
4. record human decisions for those gaps
5. compose a compact JSON-output prompt for an external LLM
6. later parse LLM proposals into a review queue and promote accepted changes

The LLM should edit from human intent, not invent the taxonomy from scratch.

## Current Implementation

Live vocabulary is now metadata-backed:

- `src/invoker/kg/vocabulary.yaml` is the reviewable source of vocabulary terms.
- `src/invoker/kg/vocabulary.py` remains the compatibility layer exporting
  `CAPABILITIES`, `REQUIREMENTS`, `LIABILITIES`, `TARGETS`,
  `RELATION_PATTERNS`, and `STATISTICAL_ALIGNMENT`.

Audit guardrail:

- `src/invoker/kg/vocab_audit.py`
- CLI: `uv run invoker vocab-audit`

The audit reports blocking issues for unknown authored terms and rule references
to non-live vocabulary. It reports warnings for unused live terms, live terms
without consuming rules, relation patterns without rules, and open gaps.

Human review:

- `src/invoker/kg/vocabulary_review.py`
- live-term review command:
  `uv run invoker review-vocabulary [--bucket <bucket>] [--term <term>]`
- gap review command:
  `uv run invoker review-vocab-gaps [--bucket <bucket>] [--candidate-term <term>]`
- prompt composition command:
  `uv run invoker compose-vocabulary-prompt [--bucket <bucket>] [--term <term>] [--reviewed-only]`

Prompt template:

- `src/invoker/prompts/revise_vocabulary.md`
- It asks for JSON output only, matching the manual hero authoring process.
- It uses a compact JSON context packet instead of raw full-file dumps.

## Review Artifacts

Canonical vocabulary stays clean. Human review notes live in local authored data:

- `data/authored/vocab-review.yaml`
- `data/authored/vocab-review-log.jsonl`
- `data/authored/vocab-gap-review.yaml`
- `data/authored/vocab-gap-review-log.jsonl`

Existing Stage 3 gap inbox:

- `data/authored/vocab-gaps.yaml`

Manual LLM handoff prompt/response files are written under:

- `data/raw/manual_prompts/revise-vocabulary/...`
- `data/raw/manual_responses/revise-vocabulary/...`

These data files are local workspace artifacts and are not necessarily tracked.

## Recommended Workflow

Start with audit:

```bash
uv run invoker vocab-audit
```

Review live terms in small sessions:

```bash
uv run invoker review-vocabulary --bucket capabilities
uv run invoker review-vocabulary --bucket liabilities
uv run invoker review-vocabulary --bucket requirements
uv run invoker review-vocabulary --bucket targets
uv run invoker review-vocabulary --bucket relation_patterns
```

Review missing concepts from authored heroes:

```bash
uv run invoker review-vocab-gaps --bucket capabilities
uv run invoker review-vocab-gaps --bucket liabilities
uv run invoker review-vocab-gaps --bucket requirements
uv run invoker review-vocab-gaps --bucket targets
```

Compose a scoped prompt after enough human review exists:

```bash
uv run invoker compose-vocabulary-prompt --bucket capabilities --reviewed-only
```

Then paste the generated prompt into an external LLM and save the JSON response
into the matching response file path printed by the command.

## Current Observations

At the time this handoff was written, `vocab-audit` passed against the local
authored corpus:

- 11 canonical authored hero files
- 32 open vocabulary gaps
- no unknown authored terms
- no rule references to non-live vocabulary

Warnings are expected because Stage 5 rule expansion has not happened:

- some accepted terms are unused
- many accepted terms have no consuming rule yet
- `enabler_payoff` has no current rule

The user has already started reviewing capabilities locally. Example themes from
their notes:

- `magic_burst` needs clearer distinction from physical damage; Pangolier should
  not be considered magic burst.
- `mobility` is too broad; blink, high movement speed, and teleport may need
  distinct terms.
- `reliable_stun` needs distinction from mini-stun, debuff-immunity-piercing
  stun, and other control.
- `save` is too broad; healing, pulls, dispels, and untargetability are different
  mechanics.

Those notes should be treated as high-priority constraints in LLM revision.

## Remaining Work

The implemented workflow now reaches the proposal inbox and guarded promotion.
Available commands:

```bash
uv run invoker parse-vocabulary-response data/raw/manual_responses/revise-vocabulary/capabilities/7f6f707397ab.txt
uv run invoker review-vocabulary-proposals --bucket capabilities
uv run invoker promote-vocabulary --bucket capabilities --dry-run
uv run invoker promote-vocabulary --bucket capabilities
```

New manual response placeholders should use `.json`; the `.txt` path above is
an older local response from before the suffix change.

The first capabilities response has been parsed locally into
`data/authored/vocab-proposals.yaml` with 53 pending proposals.

Still needed:

1. Review pending proposals and mark a small first batch accepted/rejected/deferred.
2. Promote accepted proposals into `src/invoker/kg/vocabulary.yaml`.
3. After vocabulary promotion, update affected authored hero YAML files.
4. Run:

```bash
uv run invoker vocab-audit
uv run pytest
uv run pyright
uv run ruff check
```

## Important Design Decisions

- Human notes are not stored in `vocabulary.yaml`.
- Gaps are reviewed separately from live terms because gaps are proposal queue
  items, not accepted vocabulary.
- LLM output should be JSON, not YAML. ChatGPT was unreliable with YAML in the
  manual hero process.
- Prompt generation should be scoped by bucket or term where possible to reduce
  duplication and improve LLM quality.
- `RULE_FEATURE_REFERENCES` in `src/invoker/kg/infer.py` is currently metadata
  for audit only. It duplicates rule references from executable inference logic.
  Stage 5 may replace that duplication with rule objects that both infer and
  expose their vocabulary references.
