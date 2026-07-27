# KB Exposure — Service Ladder + Consumer Bundle

**Date:** 2026-07-27
**Status:** draft (pending discussion)
**Direction:** `docs/specs/2026-07-25-grounded-reasoner-rethink.md` (agent
exposure model). First implementation slice of the exposure milestone,
scoped by the 2026-07-27 collaboration decisions with phylactery (below).

## Goal

Make the committed KB (`data/kb/<patch>/` — 98 concepts + 292 items on
7.41d) consumable outside this repository, two adapters over one data
contract:

1. **Service ladder** — `KnowledgeService` methods implementing the
   granularity ladder from the rethink spec (catalog → resolve → card →
   article → changelog), exposed through the existing HTTP and MCP-style
   adapters for free. This is the "MCP exposure" milestone: any agent
   (phylactery dev sessions, Claude sessions, future consumers) can query
   the KB progressively without it ever entering context wholesale.
2. **Consumer bundle** — a patch-pinned KB export in the resource-bundle
   layout so downstream projects vendor the KB as data. Phylactery stages
   it (same pattern as its vendored 7.41c game-resource bundle) and builds
   its own bounded coach tools plus a user-facing reference view ("mini
   wiki") over it. No runtime dependency between the repos.

## Consumer decisions (2026-07-27, with phylactery)

- **The boundary is the bundle, not a service.** Phylactery's desktop app
  cannot depend on a live invoker process on end-user machines; it vendors
  data contracts today (`phylactery.game_data`). The service exists for
  agents and development, the bundle for the shipped product.
- **Native tools, ladder only.** Phylactery's coach is already an
  agent-with-tools with its own tool-doc discipline; it pulls cards and
  articles itself. No nested `ask()` answerer-as-a-tool.
- **Mini wiki is a real consumer.** The same vendored artifact feeds both
  coach tools and an in-app reference tab rendering articles with their
  citations, so the bundle must carry enough to render marks as pinned
  source links (the KB site renderer already proves this mapping).
- **Heroes deferred** until the hero generator lands; the layout grammar
  already reserves `heroes/<slug>/`.

## Design

### Bundle contract

Extend the service resource-bundle layout (architecture.md → "Local
knowledge service") with a KB tree per patch:

```text
kb/<patch>/
  index.json
  sources.json
  concepts/<slug>/article.md
  concepts/<slug>/artifact.json
  items/<slug>/article.md
  items/<slug>/artifact.json
```

- `index.json` — `schema_version`, `patch`, KB content fingerprint
  (reuse the benchmark report's KB fingerprint machinery, so a consumer
  can tell "KB changed" without diffing trees), and one entry per entity:
  `{id: "<kind>/<slug>", kind, slug, title, identity_line}`. The identity
  line is the card's first sentence — the same summary the answerer index
  uses for select.
- `sources.json` — corpus host metadata needed to resolve `corpus:` marks
  into pinned live links (`<base_url>/index.php?oldid=<rev>#<anchor>`,
  the site renderer's rule) plus per-host license (CC-BY-SA). Citations
  stay pointers: the bundle never carries corpus page content.
- `article.md` / `artifact.json` — copied verbatim from `data/kb/`.
  `article_sha256` binding already travels in `artifact.json`.

Export command: `invoker export-kb --patch <patch> --out-dir <dir>`.
It loads every entity via `load_entity_article` before copying, so a
drifted or stale-schema artifact fails the export loudly. The command
writes into a resource-bundle root; `bundle.json` records which patches
have KB trees (schema bump), and service KB calls against a bundle
without `kb/<patch>/` fail with the export command to run — same
failure discipline as missing team profiles.

The game-constants tree gains `changelog.json` (already produced by the
snapshot flow, not yet in the bundle layout) so the changelog rung works
offline from the bundle alone.

### Service ladder (`service/core.py`)

New methods on `KnowledgeService`, surfaced by both adapters through the
existing method-per-route/tool pattern:

- `kb_catalog(patch=None, kind=None)` — the entries from `index.json`,
  filterable by kind. ~20 tokens/entry; this is the select surface for
  agents that need discovery, not lookup.
- `kb_resolve(query, patch=None)` — deterministic and conservative,
  matching the existing resolution rules: exact `<kind>/<slug>` ids,
  slugs, casefolded titles; for items additionally localized display
  names and source-backed aliases from the game-constants snapshot
  already in the bundle (the `lookup_hero` machinery, pointed at items).
  Ambiguity returns candidates; getters fail rather than choose; no
  fuzzy matching.
- `kb_card(id, patch=None)` — title, identity line, card sentences with
  their marks, prompt/provenance summary. The ~300-token load-bearing
  tier.
- `kb_article(id, patch=None)` — the full `article.md` text verbatim
  (frontmatter included) plus parsed metadata. Read-time verification via
  `load_entity_article`; a drifted file fails the call, never serves
  silently.
- `search_changelog(query, patch=None)` — wraps the existing
  `snapshot/changelog.py` search over the bundled `changelog.json`,
  returning per-patch hits with locale text. Missing changelog fails
  with the snapshot playbook pointer, mirroring the benchmark's loud
  temporal-case warning.

No `ask()` method. No write surface. Service reads stay network-free.

### What consumers do with marks

Cards and articles are served with `[kind:KEY]` marks inline — they are
the product, not noise. Coach tools keep them so generated advice can
carry resolvable pointers; the mini wiki renders them as superscript
links (`corpus:` via `sources.json`, `gamefile:`/`loc:` as provenance
badges over bundle-internal data). Stripping marks is a consumer display
choice, never an export-time transformation.

## Non-goals

- `heroes/<slug>/` export and hero packets (deferred with the hero
  generator).
- `claims.json` (S4) and the `verify()` primitive — next rung of the
  exposure model, not this slice.
- `ask()` / answerer-as-a-tool.
- Fuzzy resolution or search-by-content (the catalog + resolve rungs
  cover this slice; ranked retrieval is a later decision).
- Phylactery-side work: coach tools, staging, wiki tab — specced in that
  repo against this contract once it freezes.
- Serving raw corpus documents through the service or bundle.

## Acceptance

- `invoker export-kb --patch 7.41d --out-dir <bundle>` produces a
  verified KB tree + index + sources; re-export over an unchanged KB is
  byte-stable (fingerprint unchanged).
- A `KnowledgeService` over that bundle answers the full ladder for a
  concept (`concept/evasion`) and an item (`item/black_king_bar`
  resolved from the alias "bkb"), and `search_changelog` answers a
  removed-mechanic query (facets) from the bundle alone.
- MCP `list_tools` and HTTP routes expose the five new methods; contract
  failures (missing kb tree, drifted article, ambiguous resolve, missing
  changelog) fail loudly with actionable messages.
- Tests for index build, resolve semantics (exact / alias / ambiguous /
  missing), drift refusal, and changelog availability; `pytest`,
  `pyright`, `ruff` clean.
- `docs/architecture.md` service + bundle sections updated;
  `docs/CURRENT_DIRECTION.md` entry added.

## Open questions

1. **One bundle root or two?** This spec assumes the KB rides in the same
   resource-bundle root as game constants and teams (one root, one
   service). The alternative — a standalone KB-only bundle — makes
   phylactery's staging smaller but splits `bundle.json` governance.
   Recommend: same root.
2. **Concept aliases.** Items get source-backed aliases from
   localization; concepts have only slug + title in this slice. Is
   title/slug resolution enough for now, or should the corpus registry
   contribute redirect titles as aliases?
3. **Card payload shape.** `kb_card` returns structured sentences (text +
   marks per sentence, as stored). Confirm phylactery's wiki/tool side
   prefers structured over a rendered markdown string — the artifact
   stores structure, so serving structure is the no-loss default.
