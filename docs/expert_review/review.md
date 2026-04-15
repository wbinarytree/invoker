This is a strong Phase 1 design for a Dota knowledge substrate. Using OpenDota, STRATZ, and Liquipedia is a sensible source mix: OpenDota exposes hero/pro-match/parsed-match data, STRATZ offers a GraphQL API with tokenized developer access, and Liquipedia plus the underlying MediaWiki API give you structured wiki-style metadata. Given how fast patch state moves, making the artifacts patch-scoped is exactly the right default; 7.41b officially landed on April 7, 2026. (OpenDota)
My real take, from the agent angle, is this:
I like the architecture. I would not ship the schema exactly as written.
It is already good at being a hero knowledge base.
It is not yet shaped like a draft-decision knowledge base.
That distinction matters a lot.
My overall verdict
I would describe your current plan as:
8/10 as a patch-aware hero KB
5.5/10 as a substrate for a drafting agent
Why the gap?
Because a drafting agent does not mainly need facts like:
what Slardar does
which heroes are statistically good with Slardar
which heroes counter Slardar
It mainly needs facts like:
when Slardar is good
in which role
with which lane template
at which draft phase
for which team persona
with what reveal cost
what future branches it opens or closes
Your current design is still mostly hero-centric. Drafting is action-in-context-centric.

What is already very good
1. Patch-scoped artifacts
This is correct.
Do not let anyone talk you into a timeless KG for Dota. Patch churn destroys timelessness. Your patch partitioning is one of the best design choices in the doc.
2. Provenance-first design
This is excellent.
The fact that you track:
prompt hash,
input hash,
source snapshots,
timestamps,
generator version,
means you are thinking like a real data platform, not just an agent hobby project.
That will save you later when a draft recommendation looks wrong and you need to ask:
“bad data, bad relation, bad prompt, or bad planner?”
3. Query-time LLM exclusion
Also excellent.
Invoker should not be calling LLMs at query time. That is the right boundary. The KB should serve facts and evidence; the draft agent can use an LLM on top.
4. Gold-set and validator mindset
Very strong.
Most KG projects fail because they feel elegant but are impossible to calibrate. Your gold-set idea is one of the few things that will keep this system honest.

Where I think the design is off
1. The graph is still too hero-card shaped
Your per-hero JSON is strong as a hero card.
But for drafting, the real unit of intelligence is not the hero card.
It is the relation under context.
Right now you have things like:
Slardar has tags
Slardar synergizes with Pangolier
Slardar is countered by Centaur
That is useful, but too coarse.
For a draft agent, the system needs relations like:
Slardar as 3 synergizes with Pangolier as 2 more than with Pangolier as 3
Slardar + Pangolier is stronger in skirmish-tempo lineups than in hard-scaling lineups
Slardar opener has low flex value
Slardar pick here reveals too much if your team profile prefers hidden carry last-pick
Slardar solves enemy low-armor melee cores but worsens your waveclear deficit
That is the missing layer.
2. Your hero→hero edges need context fields, not just one score
This is the biggest schema change I would push.
Right now this:
{
  "hero_id": 120,
  "score": 0.08,
  "games": 50,
  "confidence": "high",
  "reason": "Armor reduction amplifies Pangolier's physical burst."
}

is okay for a wiki-like KB.
But for a drafter, it is underspecified.
I would want relation records to carry at least:
relation_type
directionality
self_role_context
other_role_context
lane_context
phase_context
archetype_context
patch_window
sample_size
confidence_numeric
evidence_components
optional llm_reason
So the core record becomes less like “Slardar likes Pangolier” and more like “this relation is strong under these role/lane/plan assumptions.”
That is how the graph becomes draft-useful.
3. Your LLM-generated reason is too close to source-of-truth
This is subtle but important.
I do not want natural-language reasons to be a primary data artifact.
I want the primary artifact to be something like:
"reason_factors": [
  "armor_reduction",
  "physical_burst_followup",
  "frontline_plus_mobile_damage"
]

and then the natural-language sentence is either:
generated on demand, or
cached as a convenience field.
Why I care:
Because text reasons are hard to validate deeply.
Typed factors are easy to validate, easy to compare, and easy to pass into the planner.
So I would keep reason, but demote it.
The durable truth should be typed reason factors, not prose.
4. “team:” as a bracket is the wrong axis
This is one of the most important structural issues in the doc.
pro, immortal_pub, pub_all are cohorts.
team:<slug> and player:<slug> are not cohorts.
They are subjects / scopes.
Those should not live on the same axis.
I would separate them into something like:
cohort = pro | immortal_pub | pub_all
scope = global | team:<team_key> | player:<player_key>
and for team data I would strongly avoid bare team_slug as the key.
Use something like:
team_slug
roster_hash
window_start / window_end
Because in pro Dota, roster-era identity is much more real than org identity.
“Tundra” with one roster and “Tundra” with another roster are not the same draft persona.
5. Patch-standalone is right for hero facts, but not enough for team identity
This is another major one.
For hero mechanics and patch meta, standalone patch snapshots are excellent.
For team identity, they will often be too sparse.
A team profile usually needs hierarchical backoff like:
current patch, exact roster
same major patch family, exact roster
recent 90 days, exact roster
current roster, cross-patch decayed
org/team history only as weak prior
global pro baseline
So I would keep patch-standalone for hero artifacts, but design team/player identity to support backoff layers, or you will end up with empty or noisy team personas early in each patch.
6. Your graph nodes are too thin for draft reasoning
Heroes + tags is not enough.
For a real draft graph, I would add these node families much earlier:
Role
Capability
Requirement
Liability
LaneTemplate
Archetype
Especially LaneTemplate.
That is because many “combos” are not really hero-pair facts.
They are lane-structure facts.
Example:
“ranged carry + melee protector” is a draftable concept.
It should be representable directly, not only reconstructed from many pairwise hero edges.
7. Your taxonomy is strong for mechanics, but weak for drafting unless expanded
Your current tag philosophy is mostly mechanical:
armor reduction
initiation
disable
vision control
Good start.
But drafting also needs tags in at least four families:
Capabilities
save
catch
tower pressure
waveclear
Roshan
frontline
burst
sustained damage
Requirements
needs setup
needs frontline
wants vision
wants save
wants fast fights
wants long fights
Liabilities / costs
low waveclear
reveal-heavy opener
greed
kiteable
weak lane anchor
unreliable disable
Draft traits
first-phase safe
high flex
low reveal
counterpick hero
cheese potential
teamfight anchor
lane stabilizer
If you only extract from ability text, you will capture mechanics but miss a lot of these draft traits.
And those draft traits are often what the agent actually needs.

What I would change before locking the design
First change: split the data into facts, relations, and views
Right now the per-hero JSON is doing too much.
I would restructure mentally like this:
hero facts: stable hero properties
relation evidence: pairwise / role-aware / lane-aware edges
views: hero-centric assembled files, text summaries, graph projection
That way, the canonical source of truth for “Slardar ↔ Pangolier synergy in pro 7.41b” is a relation record, not just two duplicated hero files.
You can still publish hero-centric JSON, but it should be a denormalized view, not the only truth.
Second change: add context-aware relation records
Something like:
{
  "relation_id": "synergy:28:120:pro:7.41b",
  "relation_type": "synergy",
  "source_hero_id": 28,
  "target_hero_id": 120,
  "scope": { "cohort": "pro", "patch": "7.41b" },
  "contexts": [
    {
      "source_roles": ["3"],
      "target_roles": ["2","3"],
      "lane_context": "cross_lane",
      "archetype_context": ["skirmish_tempo"],
      "weight": 0.08,
      "games": 50,
      "confidence": 0.71
    }
  ],
  "reason_factors": [
    "armor_reduction",
    "physical_burst_followup"
  ],
  "llm_reason": "Armor reduction amplifies Pangolier's physical burst."
}

That is much closer to what your agent actually needs.
Third change: separate capabilities from requirements from liabilities
For each hero, I would explicitly store:
capabilities
requirements
liabilities
draft_traits
That single change will help your later scoring/search system more than adding another hundred synergy edges.
Because drafting is often:
“what are we missing?” and “what are we overexposing?”
Those are requirement/liability questions, not just capability questions.
Fourth change: promote lane templates earlier
I would not wait too long on this.
Even a tiny seed set of lane templates will help more than a lot of generic pairwise synergy prose.
Examples:
ranged_core_melee_protector
kill_offlane
stable_farm_safelane
double_melee_pressure
defensive_waveclear_lane
Then heroes connect to those templates with strengths and caveats.
That gives your draft agent much more realistic lane understanding.
Fifth change: redesign the reader API around draft queries, not hero lookup
Your current reader API is fine for validation.
But the future API shape should be driven by agent questions like:
hero_card(hero_id, patch, cohort)
relation(a, b, context=...)
lane_templates(hero_id, role=...)
candidate_bundle(state, hero_id, team_scope=..., opponent_scope=...)
requirements_filled(state, hero_id)
requirements_broken(state, hero_id)
That is how you make the KB useful for planning rather than just retrieval.

What I would keep exactly as-is
I would keep these decisions:
JSON artifacts as source of truth
manifest + content hashes
idempotent bootstrap pipeline
no query-time LLM inside Invoker
NetworkX for Phase 1
validator-first design
manual fallback client
patch-scoped directories
No issue there.
Also, I agree with not introducing Neo4j yet.
Your problem is not “we need graph infrastructure.”
Your problem is “we need the right relation schema.”

What I would demote
I would demote two things from “central” to “nice to have”:
1. Natural-language .txt summaries
Useful, but not central.
They should be convenience artifacts for LLM prompting, not your primary interface for the agent.
2. Bulk LLM reason generation
Still useful, but not where I’d spend most of the design energy.
I would invest more in:
typed relation factors,
role/lane context,
requirement/liability tags,
and action-centric query surfaces.
Those will matter more than prettier reasons.

The sharpest summary I can give
Your current plan is a very good hero encyclopedia with provenance.
To become a draft agent substrate, it needs four upgrades:
contextual relations instead of flat hero-pair scores
requirements and liabilities, not just capabilities
lane-template and archetype structure
team/player scope separated from bracket/cohort
If you fix those, the architecture becomes genuinely aligned with the draft-agent problem.
If you do not fix those, you may still build something polished, but it will mostly retrieve hero facts and synergy trivia rather than support real draft planning.
The next thing I would rewrite is §3.3, §3.5, and §9 so the schema is centered on draft-state queries, not just hero lookup.
