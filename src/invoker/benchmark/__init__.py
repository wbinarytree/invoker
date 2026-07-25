"""Basic-QA benchmark: gold cases gating the foundation tier.

Cases live in benchmarks/basic-qa/ as YAML. Each encodes a question, the
facts a correct answer must state, assertions it must not make (traps
discovered through human correction), and the source marks a grounded
answer should cite. The runner that scores generated answers arrives with
Milestone 1; until then the loader keeps cases valid.
"""
