"""Basic-QA benchmark: gold cases gating the foundation tier.

Cases live in benchmarks/basic-qa/ as YAML. Each encodes a question, the
facts a correct answer must state, assertions it must not make (traps
discovered through human correction), and the source marks a grounded
answer should cite.

The runner (`invoker run-benchmark`) is the end-to-end eval for the KB:
an answerer composes each answer from KB artifacts + changelog only, a
scorer grades it — mechanical checks for marks and concision, an LLM
judge for fact presence and traps — and a run report with full provenance
lands under data/benchmark-runs/. Spec:
docs/specs/2026-07-25-basic-qa-benchmark-runner.md.
"""
