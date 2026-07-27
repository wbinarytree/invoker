---
title: Helm of the Dominator
kind: item
patch: 7.41d
card:
  entity: helm_of_the_dominator
  sentences:
  - text: Helm of the Dominator is a 2550-gold artifact item granting 6 Armor, 6 Health
      Regeneration, and 6 All Attributes; Dominate controls up to 1 neutral, non-ancient
      unit at 700 cast range for 50 mana with a 45.0-second cooldown.
    marks:
    - gamefile:items/item_helm_of_the_dominator#cost
    - gamefile:items/item_helm_of_the_dominator#attribs
    - gamefile:items/item_helm_of_the_dominator#mechanics
    - loc:DOTA_Tooltip_ability_item_helm_of_the_dominator_Description
  - text: Dominate has Unit Target and DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK behavior.
    marks:
    - gamefile:items/item_helm_of_the_dominator#mechanics
  - text: Dominate applies 370 base Movement Speed, a minimum of 1000 Max Health,
      25 bonus Base Attack Damage, 12 bonus Health Regeneration, 4 bonus Mana Regeneration,
      and 4 bonus Armor.
    marks:
    - gamefile:items/item_helm_of_the_dominator#attribs
    - loc:DOTA_Tooltip_ability_item_helm_of_the_dominator_Description
  - text: A dominated unit already exceeding 1000 Max Health retains its original
      Max Health.
    marks:
    - gamefile:items/item_helm_of_the_dominator#attribs
    - loc:DOTA_Tooltip_ability_item_helm_of_the_dominator_Description
  - text: The caster receives 50% of the dominated creep’s gold and experience bounty.
    marks:
    - gamefile:items/item_helm_of_the_dominator#attribs
    - loc:DOTA_Tooltip_ability_item_helm_of_the_dominator_Description
  - text: The dominated unit’s bounty is set to 100 gold.
    marks:
    - gamefile:items/item_helm_of_the_dominator#attribs
    - loc:DOTA_Tooltip_ability_item_helm_of_the_dominator_Description
  - text: The dominated unit cannot be killed by abilities that instantly kill creeps.
    marks:
    - loc:DOTA_Tooltip_ability_item_helm_of_the_dominator_Description
  - text: After the dominated unit takes damage from an enemy hero or Roshan, the
      Helm is unavailable for 3 seconds.
    marks:
    - gamefile:items/item_helm_of_the_dominator#attribs
    - loc:DOTA_Tooltip_ability_item_helm_of_the_dominator_Description
  - text: Its build formula is Helm of Iron Will (975 gold) + Crown (450 gold) + Recipe
      (1125 gold); it builds into Helm of the Overlord.
    marks:
    - gamefile:items/item_helm_of_the_dominator#components
---

# Helm of the Dominator

Helm of the Dominator is an artifact item that grants Armor, Health Regeneration, and All Attributes and provides the Dominate active. [gamefile:items/item_helm_of_the_dominator#cost] [gamefile:items/item_helm_of_the_dominator#attribs] [loc:DOTA_Tooltip_ability_item_helm_of_the_dominator_Description]

## Cost

| Stat | Value |
|---|---:|
| Cost | 2550 gold |

[gamefile:items/item_helm_of_the_dominator#cost]

## Stats

| Stat | Value |
|---|---:|
| ARMOR | 6 |
| HEALTH REGENERATION | 6 |
| ALL ATTRIBUTES | 6 |
| BOUNTY GOLD | 100 |
| BOUNTY PCT | 50% |
| COUNT LIMIT | 1 |
| CREEP ABILITY LEVEL INCREASE | 0 |
| CREEP BONUS ARMOR | 4 |
| CREEP BONUS DAMAGE | 25 |
| CREEP BONUS HP REGEN | 12 |
| CREEP BONUS MP REGEN | 4 |
| CREEP DAMAGE TAKEN COOLDOWN | 3 |
| HEALTH MIN | 1000 |
| MODEL SCALE | 0 |
| SPEED BASE | 370 |

[gamefile:items/item_helm_of_the_dominator#attribs]

## Active

| Stat | Value |
|---|---|
| Behavior | Unit Target, DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK |
| Cast range | 700 |
| Mana cost | 50 |
| Cooldown | 45.0 |

[gamefile:items/item_helm_of_the_dominator#mechanics]

Dominate takes control of a neutral, non-ancient target unit and applies the listed Movement Speed, minimum Max Health, Base Attack Damage, Health Regeneration, Mana Regeneration, and Armor settings. A unit whose Max Health already exceeds the listed minimum retains its original Max Health. [loc:DOTA_Tooltip_ability_item_helm_of_the_dominator_Description]

The caster receives the listed share of the dominated creep’s gold and experience bounty, while the unit’s bounty is set to the listed amount. The dominated unit can no longer be killed by abilities that otherwise instantly kill creeps. After it takes damage from an enemy hero or Roshan, the Helm becomes unavailable for the listed lockout. [loc:DOTA_Tooltip_ability_item_helm_of_the_dominator_Description]

## Components

| Role | Item | Cost |
|---|---|---:|
| Component | Helm of Iron Will | 975 gold |
| Component | Crown | 450 gold |
| Recipe | Recipe | 1125 gold |
| Builds into | Helm of the Overlord | 5650 gold |

[gamefile:items/item_helm_of_the_dominator#components]

*The powerful headpiece of a dead necromancer.* [loc:DOTA_Tooltip_ability_item_helm_of_the_dominator_Lore]