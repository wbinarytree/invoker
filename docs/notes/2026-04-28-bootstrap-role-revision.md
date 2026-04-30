# Bootstrap Role Revision Discussion

Date: 2026-04-28
Status: discussion point

## Context

`bootstrap` inherited its name and shape from the old automated KG pipeline:

- query an LLM backend to generate prompts or tags for every hero;
- run a second pass to generate relationships;
- write broad derived artifacts from that automated flow.

The current project direction is different. Hero fact authoring is now manual,
source-grounded, and reviewable. Relationships are deterministic outputs from
reviewed authored YAML and vocabulary rules. This is more reliable, but it
changes what a "bootstrap" command should mean.

## Discussion Point

Revisit whether `bootstrap` is still the right command boundary.

Questions to resolve before changing it:

- Should `bootstrap` remain the command that derives patch artifacts from
  reviewed authored facts?
- Should it be renamed to something more explicit, such as `build-derived` or
  `derive-kg`?
- Should relationship generation be a separate command from hero-view
  derivation?
- Should release creation depend on `bootstrap`, or should `publish` own more
  of the deterministic derivation step?
- Which outputs are still useful now that no LLM tagging or relationship pass
  runs in bootstrap?

Do not implement a command rename or split without a small spec first. This
touches CLI shape, release preconditions, docs, and local operator workflow.
