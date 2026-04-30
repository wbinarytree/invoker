# Authored Hero Facts

This directory is the local working source for hand-authored hero fact YAML during the current manual-assisted KG workflow.

`teams.yaml` is a separate team registry for team-profile resolution and display
metadata. It is not a hero fact file and must not be used as an authoritative
roster source.

## Workflow

1. Run `invoker draft-facts <hero> [hero ...]` to generate prompts from cached hero metadata and ability text.
2. Paste that prompt into your external LLM of choice.
3. Save the JSON response into the matching manual response file.
4. Rerun `invoker draft-facts <hero> [hero ...]` to write `<hero>.yaml` or `<hero>.draft.yaml`.
5. Review any new entries in `vocab-gaps.yaml`; these are not live facts, only Stage 4 input.
6. Run `invoker validate-facts <hero>`.
7. Run `invoker show-relations <hero>` to inspect what the current authored corpus implies.

To accept regenerated drafts after review, run `invoker promote-draft <hero> [hero ...]`.
This validates each `<hero>.draft.yaml`, backs up the current canonical YAML under
`.backups/`, and copies the draft into `<hero>.yaml`. Add `--delete-draft` if you
want draft files removed after promotion.

## Bucket guidance

- `capabilities`: what the hero mechanically does well.
- `requirements`: what the hero needs from allies or game state to function reliably.
- `liabilities`: what mechanically punishes or constrains the hero.
- `targets`: what class of enemy profile the hero naturally punishes.

More specific guidance:

- `capabilities` are positive, self-owned mechanics from the kit.
- `requirements` are external dependencies, not just "things every hero likes."
- `liabilities` should be reserved for live-vocabulary punish patterns we actively want the graph to reason about.
- `targets` should describe enemy profiles the hero can reach, trap, expose, or punish.

Anti-patterns:

- Do not duplicate the same concept across buckets.
- Do not force every bucket to be populated with many entries.
- Do not add a plausible concept that the live vocabulary cannot currently express.
- If a concept feels true but fails validation, that is usually a vocabulary-gap note for later, not a validator bug.

## Vocabulary gaps

- `vocab-gaps.yaml` captures important mechanics that the live vocabulary cannot express yet.
- Gap entries are review inbox items, not canonical hero facts.
- Do not work around a missing term by forcing a weak existing term into the authored YAML.
- Stage 4 should promote only gaps with concrete hero evidence and a clear rule or planner use.

## Scoring

- Scores are advisory and should stay between `0.0` and `1.0`.
- Use higher scores when the mechanic is central to the hero, not just present.
- Do not force precision that the source text does not justify.

## Evidence

- `capabilities`, `liabilities`, and `targets` should include short concrete evidence.
- `requirements` may omit evidence when the judgment is a kit-level inference.
- Evidence should point to mechanics from ability text, not vibes or matchup anecdotes.

## Style

- Prefer a small number of defensible entries over a broad speculative list.
- Use only live vocabulary terms.
- If a term is missing, stop and update the vocabulary in a later stage rather than inventing a new one locally.
