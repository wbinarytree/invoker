# Basic-QA Benchmark Runner

**Date:** 2026-07-25
**Status:** draft — awaiting sign-off
**Direction:** `docs/specs/2026-07-25-grounded-reasoner-rethink.md` (Milestone 1
gate). Cases and loader exist (`benchmarks/basic-qa/*.yaml`,
`src/invoker/benchmark/`); this spec adds the scoring runner.

## Goal

The runner is the eval for the KB: it answers each gold case's question from
the generated encyclopedia and scores the answer against the case. It is the
Milestone 1 gate ("foundation tier passes basic QA"), the regression harness
for every generation-affecting change (prompt version, generator model,
packet builder), and the accumulation point for human corrections (every
correction becomes a case; the runner re-checks it on every rebuild).

It is an **end-to-end** eval: it scores the KB through the ask-path
(question → resolve → card/article → answer), because the product surface is
answers, not artifacts. Generation-time faithfulness checks (marks resolve
against the packet, numbers match) remain the per-artifact quality layer;
the runner is the sampled end-to-end battery on top.

## Shape: answerer + scorer

Two halves with a hard boundary between them. The answerer never sees gold
fields; the scorer never re-derives answers.

### Answerer

Produces an answer to `case.question` using only the KB's knowledge
surfaces:

- **KB artifacts** under `data/kb/<patch>/` — cards first (the ~300-token
  marked tier), full `article.md` on demand.
- **Changelog** — `changelog.json` search (temporal questions are a
  base-tier class; `facet-removal` expects a `changelog:` mark).

Explicitly **not** raw substrate (game-file snapshot values, corpus pages):
substrate facts reach answers only through generated artifacts that cite
them. This keeps the benchmark measuring the KB. A case whose facts are not
yet in any artifact fails with `resolution-miss` — that failure is the
demand signal for the next generator slice (today: `mage-slayer` → item
generator, `corrosive-haze` → hero generator).

M1 form — two `GenerationClient` calls (reusing the S1 client, model pinned
in provenance):

1. **Select:** question + artifact index (slugs + card first-sentences +
   changelog availability) → which artifacts/changelog queries to open.
   Bounded fan-out (≤4 artifacts). May return "nothing resolves" →
   `resolution-miss`, no compose call.
2. **Compose:** question + selected cards/articles/changelog hits → concise
   answer in which every factual sentence carries inline marks
   (`[corpus:…]`, `[gamefile:…]`, `[loc:…]`, `[changelog:…]`), same syntax
   as articles.

The eventual form is agent-with-tools over the KnowledgeService MCP ladder
(spec: agent exposure model); the two-call form is the M1 stand-in and
shares its contract: answers are composed from resolved KB material with
marks carried through.

### Scorer

Hybrid, matching the four case fields:

| Case field | Check | How |
|---|---|---|
| `expected_marks` | each pattern matched by ≥1 mark in the answer, and that mark resolves | mechanical |
| `max_answer_words` | prose word count within bound (mark tokens excluded from the count) | mechanical |
| `expected_facts` | each fact stated by the answer | LLM judge, per fact: present / absent / contradicted |
| `forbidden_assertions` | no trap asserted | LLM judge, per assertion: asserted / not asserted |

**Mark resolution** reuses/extends the generation-side check: `corpus:`
against the pinned corpus registry revisions, `gamefile:`/`loc:` against the
patch snapshot, `changelog:` against `changelog.json`. Resolution here is
traceability, not truth (marks-not-verdicts stance).

**Judge discipline:** one fact per call, binary verdict + one-sentence
rationale (stored in the report for audit). The judge sees the answer and
the single fact/assertion — never the sources, never the other gold fields.
Judge model pinned per run and recorded in provenance, independently of the
answerer model. Judging "does this paragraph state X" is the cheap-verifier
case where LLM use is sound (feasibility bounds in the rethink spec);
generation-quality prose judgment is out of scope.

No silent retries: an answerer or judge call that fails structurally
(transport error, malformed structured output) marks the case
`answerer-error` / `judge-error` and surfaces in the report; it never
silently retries or scores as a content failure.

### Pass semantics

A case **passes** iff:

- every `required: true` (default) expected fact is `present`,
- no expected fact is `contradicted` (including optional ones),
- no forbidden assertion is asserted,
- every `expected_marks` pattern is matched by ≥1 resolvable mark,
- word count ≤ `max_answer_words` (when set).

Optional facts (`required: false`) are reported as coverage but never gate.
The run **fails** (nonzero exit) if any case fails.

### Failure taxonomy

Every failing check is classified so the report implicates the right layer —
answerer, KB content, or the case itself:

`resolution-miss` (no artifact selected) · `fact-missing` ·
`fact-contradicted` · `trap-triggered` · `mark-pattern-missing` ·
`mark-unresolvable` · `over-length` · `answerer-error` · `judge-error`

## Report and provenance

- **Console:** per-case table (verdict, facts hit/missed, traps, marks,
  words) + summary line. Exit 0/1.
- **Run report JSON** under `data/benchmark-runs/<patch>/<run-id>/`
  (gitignored, disposable): full answers, per-fact judge verdicts with
  rationales, selected artifacts, resolved marks, and provenance —
  answerer model + prompt versions, judge model + prompt version, KB
  manifest content hashes, case-set hash. Reports are not committed;
  numbers travel in PR descriptions.

Comparing two runs (before/after a prompt bump) is reading two report
files; a diff convenience can come later if it earns its keep.

## CLI

```
invoker run-benchmark --patch 7.41d [--case <id> ...] [--answerer-model …] [--judge-model …]
```

Models default to the pinned generation config; overrides recorded in
provenance.

## Testing

- Mechanical scorer (mark patterns, resolution wiring, word count, pass
  semantics, taxonomy) unit-tested with synthetic answers.
- Answerer/judge plumbing tested against a fake `GenerationClient`
  (structured-output shapes, error surfacing, no-retry behavior).
- No unit tests on judge/answerer prose (project rule).

## Out of scope (evolution path, not M1)

- Agent-with-tools answerer scoring mark coverage over live MCP calls
  (contractual enforcement in the rethink spec).
- `verify(assertions[])` as a service primitive — it will reuse this
  scorer's fact-judgment + mark-resolution machinery; build here so it
  isn't built twice.
- Best-of-N rejection sampling at generation time against the same checks.
- Judge-model upgrade gating policy (open question 2 in the rethink spec)
  — the runner enables it; policy decided when a model swap is actually
  proposed.

## Decisions needing sign-off

1. **Answerer source scope:** KB artifacts + changelog only (recommended,
   above) vs also allowing direct substrate value lookup. Direct substrate
   would let `mage-slayer` pass before the item generator exists, but then
   the benchmark measures ad-hoc context assembly, not the KB.
2. **Judge model:** pinned same as generator vs deliberately different.
   Recommendation: same pinned model to start (fewer moving parts); the
   provenance field keeps them independently swappable.
3. **Word-count rule:** marks excluded from the count (recommended — the
   bound targets prose concision, and mark density shouldn't penalize
   citation discipline).
