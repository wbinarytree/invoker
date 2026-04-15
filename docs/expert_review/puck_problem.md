Yes — this is exactly the dangerous case.
Officially, Puck’s Curveball facet was nerfed from 5% to 3% bonus damage per tick in 7.39e; the current official Puck page still shows Illusory Orb dealing an additional 3% of its impact damage every 0.5s, and 7.41a also reduced Illusory Orb’s impact damage from 75/150/225/300 to 70/140/210/280. Those all look like “small numeric” edits, but they can create a binary gameplay difference when they cross a lane-clear or kill threshold. (Dota 2)
That is the key rule:
LLMs are weak at threshold effects.
They often smooth “5% to 3%” into “small nerf,” even when the real gameplay consequence is “this no longer clears ranged creep” or “this combo now leaves a target alive.”
So for your system, the answer is:
Do not rely on the LLM to infer threshold consequences from raw numbers
Use the LLM for:
semantic extraction,
typed relation explanation,
natural-language reasoning.
Use code or explicit derived facts for:
lane-clear breakpoints,
kill thresholds,
mana-to-full-combo thresholds,
tower-shot / creep-shot thresholds,
neutral clear breakpoints,
“survives with sliver vs dies” transitions.
That is the right split.
A good mental model
You have 3 classes of truth:
1. Qualitative facts
Examples:
Puck has mobility
Puck has wave damage
Slardar amplifies physical damage
Drow wants protection and spacing
These are safe for LLM extraction.
2. Raw numeric facts
Examples:
3% per tick
280 impact damage
625 cast range
1.3 mana regen
These should be stored exactly, not paraphrased.
3. Threshold facts
Examples:
“with Curveball, this no longer clears ranged creep at level X”
“this combo kills a 700 HP support only with one extra right-click”
“this hero can full-waveclear one level later than before”
These should be computed or explicitly authored, not guessed by the LLM.
That third category is where most draft and lane reasoning quality comes from.
So what should go into prompts?
In the permanent system prompt
Only put the rule:
Treat threshold-crossing numeric changes as qualitatively important when explicit breakpoint evidence is provided. Do not downplay them as minor tuning.
That belongs in the prompt.
In patch/reference context
Put:
raw ability numbers,
creep HP / armor / bounty tables,
level scaling rules,
facet values,
attribute values.
In derived runtime facts
Put things like:
ranged_creep_clear_lvl3 = false
full_wave_clear_lvl5 = true
combo_kill_700hp_support = borderline
orb_plus_attack_secures_ranged = true
Those are what the LLM should actually consume when making lane or draft judgments.
For your KG / Invoker design, I would add a new layer
Not inside the pure hero-card facts, but adjacent to them:
{
  "hero_id": 13,
  "patch": "7.41b",
  "mechanics": {
    "illusory_orb": {
      "impact_damage": [70, 140, 210, 280],
      "bonus_damage_per_tick_pct": 0.03
    }
  },
  "material_thresholds": {
    "lane": [
      {
        "id": "curveball_ranged_creep_clear",
        "context": {
          "facet": "Curveball",
          "spell_level": 2
        },
        "result": false,
        "source": "computed",
        "confidence": "high"
      }
    ]
  }
}

That way:
the raw mechanic stays exact,
the threshold consequence is explicit,
the LLM does not have to do hidden arithmetic.
What this means for extraction
For extract_mechanical_tags, I would not ask the LLM to decide:
whether Puck clears ranged creep,
whether a spell kills a creep,
whether a lane matchup flips.
I would ask it to extract:
wave damage,
DoT,
burst,
mobility,
cast pattern,
AoE profile,
relevant mechanic tags.
Then let a deterministic layer compute tactical consequences.
What this means for synergy / lane reasoning
For generate_synergy_reason, I would let the LLM use threshold facts only when they are already present.
Good:
“Current patch Puck has weaker early shove because the Curveball breakpoint is no longer met.”
“This lane still works, but it no longer guarantees ranged-creep cleanup on orb alone.”
Bad:
“3% seems close to 5%, so laning is mostly unchanged.”
That second sentence is exactly the kind of smoothing error LLMs make.
The practical rule
Numbers matter when they cause a state transition.
Small changes are usually safe to leave abstract when they only change magnitude a bit.
Small changes are not safe when they change:
clear vs not clear,
kill vs not kill,
survive vs die,
sustain combo vs cannot sustain combo,
reveal timing vs hidden timing.
Those need explicit handling.
How I would implement this in your pipeline
LLM extraction layer
Extract mechanics and tags only.
Deterministic breakpoint layer
Compute tactical thresholds from patch data and formulas.
LLM reasoning layer
Read both mechanic facts and breakpoint facts.
That gives you the best of both:
flexibility,
groundedness,
and far fewer “close but wrong” draft reads.
My direct answer
So yes: your instinct is correct.
A tiny numeric tweak can be strategically huge when it crosses a breakpoint, and the LLM should not be trusted to notice that from raw numbers alone.
The clean design is:
LLM for semantics, code for breakpoints, LLM again for explanation.
The next thing I would add to Invoker is a small material_thresholds or breakpoints artifact family, because that is the layer that turns “hero encyclopedia” into “draft-useful knowledge.”

