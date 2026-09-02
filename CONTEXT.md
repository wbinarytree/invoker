# Dota Knowledge

This context defines the product language for building and distributing useful
Dota knowledge to agent builders. It separates the knowledge itself from the
interfaces and storage used to consume it. Revised 2026-09-02 with the
decisions in `docs/notes/2026-09-02-knowledge-artifact-first-principles-review.md`.

## Product

**Dota Knowledge Base**:
The current-patch body of generated Dota knowledge: entities, mechanics with
their interaction roles and rules, hero and item pages with hooks, derived
pair pages, and their supporting material.
_Avoid_: MCP, graph, database, stats

**Knowledge Artifact**:
A versioned, portable release of the Dota Knowledge Base: the Markdown vault
(canonical) plus its derived indexes (catalog, graph file, SQLite). Consumers
use it without running the generation pipeline.
_Avoid_: database dump, service, SQLite file

**Agent Builder**:
A developer who uses the Knowledge Artifact to supply Dota context to an agent
or other product. The KB explains; the agent builder's product decides.
_Avoid_: end user, player

## Knowledge

**Substrate**:
Current-patch game data and other source material from which generated
knowledge is built.
_Avoid_: knowledge base, dossier

**Mechanics Library**:
The existing collection of generated mechanism articles derived from the
pinned Liquipedia corpus. Each concept page carries an Interactions block.
_Avoid_: ontology, glossary

**Role**:
A named, one-line-defined position a hero or item can take with respect to
one mechanic (a source that grants cooldown reduction to allies; a sink whose
kit is cooldown-bound). Declared on the concept page. Closed per concept,
open overall.
_Avoid_: tag, capability, feature type

**Rule**:
A declaration on a concept page that two roles meeting produce an ally
synergy or an enemy counter, with direction and a one-line mechanism.
_Avoid_: relation rule, inference rule, score

**Hook**:
A short paragraph on a hero or item page stating that the entity takes one
role on one concept, with reasoning, refs to the source ability, and
conditions (level, item, phase) inside the text.
_Avoid_: tag, fact, capability, claim

**Hero Dossier**:
The generated page for one hero: kit facts and milestones grounded in game
files, Valve's role tags, and hooks. Never builds, skill order, or lane.
_Avoid_: hero card, fact profile, build guide

**Pair Dossier**:
The derived page for two heroes: the candidates produced by joining their
hooks through concept rules, ranked, pruned, and each given one connecting
sentence. Never enumerated directly.
_Avoid_: synergy edge, pair score, pair article

**Interaction Observation**:
The smallest independently retrievable unit of pair knowledge: a matched hook
pair plus its connecting text, or a flagged escape-hatch observation. Carries
refs; carries no marks, grade, or confidence.
_Avoid_: claim, graph edge, citation

**Escape-hatch observation**:
An observation the pair job adds without a hook match, flagged as such and
counted. A recurring kind of escape-hatch observation means a missing hook or
rule.
_Avoid_: exception, override

**Alias Ledger**:
The curated file of community names for entities that Valve does not ship
(滚滚, 蓝猫, "qop"), one source-tagged line per alias, entering only on the
user's acceptance. Index data, not content.
_Avoid_: slang list, embedding, fuzzy match

**Context Packet**:
A bounded selection of relevant knowledge assembled from the Knowledge
Artifact for a consumer's entities and intent.
_Avoid_: answer, prompt

## Process

**Generation Provider**:
The replaceable model-backed system that produces Interactions blocks, hooks,
and derived pair pages.
_Avoid_: generator model

**Evaluation Provider**:
The replaceable system that runs or judges benchmark cases against generated
knowledge.
_Avoid_: judge model

**Vertical Slice**:
A roster sampled from a real professional final's picks, the pairs that
co-occurred in those games, and the full build, artifact, retrieval, graph,
and evaluation loop over them, used to prove the direction before scaling.
_Avoid_: pilot corpus, demo

**Graph Explorer**:
A human-facing projection of the vault's typed links (link, hook, pair) —
Obsidian over the vault, and one static page over the graph file — that
exposes the knowledge without becoming its canonical representation.
_Avoid_: knowledge graph, graph database
