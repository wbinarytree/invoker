---
title: Helm of the Overlord
kind: item
patch: 7.41d
card:
  entity: helm_of_the_overlord
  sentences:
  - text: Helm of the Overlord is a 5650-gold artifact item granting 7 armor, 7 health
      regeneration, 21 all attributes, and the active Dominate, which has 700 cast
      range, 50 mana cost, and 40 cooldown.
    marks:
    - gamefile:items/item_helm_of_the_overlord#cost
    - gamefile:items/item_helm_of_the_overlord#attribs
    - gamefile:items/item_helm_of_the_overlord#mechanics
    - loc:DOTA_Tooltip_ability_item_helm_of_the_overlord_Description
  - text: Its build formula is Helm of the Dominator (2550 gold), Ultimate Orb (2800
      gold), and Recipe (300 gold).
    marks:
    - gamefile:items/item_helm_of_the_overlord#components
  - text: Dominate takes control of a neutral target.
    marks:
    - loc:DOTA_Tooltip_ability_item_helm_of_the_overlord_Description
  - text: The dominated unit's movement speed is set to 380.
    marks:
    - gamefile:items/item_helm_of_the_overlord#attribs
    - loc:DOTA_Tooltip_ability_item_helm_of_the_overlord_Description
  - text: Its maximum health has a minimum of 1900, but a unit originally above 1900
      retains its original maximum health.
    marks:
    - gamefile:items/item_helm_of_the_overlord#attribs
    - loc:DOTA_Tooltip_ability_item_helm_of_the_overlord_Description
  - text: The unit gains 70 base attack damage, 12 health regeneration, 4 mana regeneration,
      and 7 armor.
    marks:
    - gamefile:items/item_helm_of_the_overlord#attribs
    - loc:DOTA_Tooltip_ability_item_helm_of_the_overlord_Description
  - text: Dominate improves some of the unit's abilities by 1 level.
    marks:
    - gamefile:items/item_helm_of_the_overlord#attribs
    - loc:DOTA_Tooltip_ability_item_helm_of_the_overlord_Description
  - text: Dominate has a count limit of 1.
    marks:
    - gamefile:items/item_helm_of_the_overlord#attribs
  - text: The caster receives the creep's gold and experience bounty, and the dominated
      unit's bounty is reset.
    marks:
    - loc:DOTA_Tooltip_ability_item_helm_of_the_overlord_Description
  - text: Abilities that otherwise instantly kill creeps cannot kill the dominated
      unit.
    marks:
    - loc:DOTA_Tooltip_ability_item_helm_of_the_overlord_Description
  - text: The Helm's damage-taken cooldown is 3 and begins after the dominated creep
      takes damage from an enemy hero or Roshan.
    marks:
    - gamefile:items/item_helm_of_the_overlord#attribs
    - loc:DOTA_Tooltip_ability_item_helm_of_the_overlord_Description
---

# Helm of the Overlord

Helm of the Overlord is an artifact item that provides Armor, Health Regeneration, and All Attributes and grants the active ability Dominate. [gamefile:items/item_helm_of_the_overlord#cost] [gamefile:items/item_helm_of_the_overlord#attribs] [loc:DOTA_Tooltip_ability_item_helm_of_the_overlord_Description]

## Cost

| Stat | Value |
|---|---:|
| Cost | 5650 gold |

[gamefile:items/item_helm_of_the_overlord#cost]

## Components

| Component | Gold cost |
|---|---:|
| Helm of the Dominator | 2550 gold |
| Ultimate Orb | 2800 gold |
| Recipe | 300 gold |

[gamefile:items/item_helm_of_the_overlord#components]

## Stats

| Stat | Value |
|---|---:|
| ARMOR | 7 |
| HEALTH REGENERATION | 7 |
| ALL ATTRIBUTES | 21 |
| BOUNTY GOLD | 250 |
| BOUNTY PCT | 100 |
| COUNT LIMIT | 1 |
| CREEP ABILITY LEVEL INCREASE | 1 |
| CREEP BONUS ARMOR | 7 |
| CREEP BONUS DAMAGE | 70 |
| CREEP BONUS HP REGEN | 12 |
| CREEP BONUS MP REGEN | 4 |
| CREEP DAMAGE TAKEN COOLDOWN | 3 |
| HEALTH MIN | 1900 |
| IS OVERLORD | 1 |
| MODEL SCALE | 20 |
| SPEED BASE | 380 |

[gamefile:items/item_helm_of_the_overlord#attribs]

## Dominate

| Property | Value |
|---|---:|
| Behavior | Unit Target, DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK |
| Cast range | 700 |
| Mana cost | 50 |
| Cooldown | 40 |

[gamefile:items/item_helm_of_the_overlord#mechanics]

Dominate takes control of a neutral target, sets its movement speed and minimum maximum health, grants base attack damage, health regeneration, mana regeneration, and armor, and improves some of its abilities. A dominated unit whose original maximum health exceeds the enforced minimum retains its original maximum health. The caster receives the creep’s gold and experience bounty; the dominated unit’s bounty is reset, and abilities that otherwise instantly kill creeps can no longer kill it. The Helm becomes unusable for its damage-taken cooldown after the dominated creep takes damage from an enemy hero or Roshan. [loc:DOTA_Tooltip_ability_item_helm_of_the_overlord_Description]

*The powerful headpiece of an undead necromancer.* [loc:DOTA_Tooltip_ability_item_helm_of_the_overlord_Lore]