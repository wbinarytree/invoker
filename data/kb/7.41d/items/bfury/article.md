---
title: Battle Fury
kind: item
patch: 7.41d
card:
  entity: bfury
  sentences:
  - text: Battle Fury is an epic 3900-gold item providing 50 Damage, 7.5 Health Regeneration,
      and 2.75 Mana Regeneration, with melee-only Cleave dealing 60% physical attack
      damage in a cone around the target, or 40% against creeps, up to 650 distance.
    marks:
    - gamefile:items/item_bfury#cost
    - gamefile:items/item_bfury#attribs
    - loc:DOTA_Tooltip_ability_item_bfury_Description
  - text: The Cleave cone has 150 starting width and 360 ending width.
    marks:
    - gamefile:items/item_bfury#attribs
  - text: Quell adds 10 attack damage for melee heroes and 5 for ranged heroes when
      attacking non-hero units.
    marks:
    - gamefile:items/item_bfury#attribs
    - loc:DOTA_Tooltip_ability_item_bfury_Description
  - text: Upgraded Cleave Bonus is 25.
    marks:
    - gamefile:items/item_bfury#attribs
  - text: Upgraded Damage Bonus is 15.
    marks:
    - gamefile:items/item_bfury#attribs
  - text: Its build formula is Perseverance for 1400 gold, Broadsword for 1000 gold,
      another Broadsword for 1000 gold, Quelling Blade for 100 gold, and a Recipe
      for 400 gold, totaling 3900 gold.
    marks:
    - gamefile:items/item_bfury#components
    - gamefile:items/item_bfury#cost
  - text: Chop Tree is a Unit Target active that destroys a target tree.
    marks:
    - gamefile:items/item_bfury#mechanics
    - loc:DOTA_Tooltip_ability_item_bfury_Description
  - text: Chop Tree has 350 cast range.
    marks:
    - gamefile:items/item_bfury#mechanics
  - text: Chop Tree has a 4.0 cooldown.
    marks:
    - gamefile:items/item_bfury#mechanics
  - text: The bearer of this mighty axe gains the ability to cut down swaths of enemies
      at once.
    marks:
    - loc:DOTA_Tooltip_ability_item_bfury_Lore
---

# Battle Fury

Battle Fury is an epic item providing Damage, Health Regeneration, Mana Regeneration, Cleave Damage Percent, Cleave Damage Percent Creep, Cleave Distance, Cleave Ending Width, Cleave Starting Width, Quelling Bonus, Quelling Bonus Ranged, Upgraded Cleave Bonus, and Upgraded Damage Bonus. [gamefile:items/item_bfury#cost] [gamefile:items/item_bfury#attribs]

## Stats

| Stat | Value | Qualifier |
|---|---:|---|
| Damage | 50 | — |
| Health Regeneration | 7.5 | — |
| Mana Regeneration | 2.75 | — |
| Cleave Damage Percent | 60% | Physical damage in a cone around the target; melee only |
| Cleave Damage Percent Creep | 40% | Against creeps |
| Cleave Distance | 650 | Up to |
| Cleave Ending Width | 360 | — |
| Cleave Starting Width | 150 | — |
| Quelling Bonus | 10 | Melee heroes attacking non-hero units |
| Quelling Bonus Ranged | 5 | Ranged heroes attacking non-hero units |
| Upgraded Cleave Bonus | 25 | — |
| Upgraded Damage Bonus | 15 | — |

[gamefile:items/item_bfury#attribs] [loc:DOTA_Tooltip_ability_item_bfury_Description]

## Components

| Component | Gold cost |
|---|---:|
| Perseverance | 1400 gold |
| Broadsword | 1000 gold |
| Broadsword | 1000 gold |
| Quelling Blade | 100 gold |
| Recipe | 400 gold |
| **Total cost** | **3900 gold** |

[gamefile:items/item_bfury#components] [gamefile:items/item_bfury#cost]

## Abilities and Mechanics

| Property | Value |
|---|---:|
| Behavior | Unit Target |
| Cast range | 350 |
| Cooldown | 4.0 |

[gamefile:items/item_bfury#mechanics]

**Chop Tree** is active and destroys a target tree. **Quell** and **Cleave** are passive; Quell increases attack damage against non-hero units for melee and ranged heroes, while Cleave deals physical damage based on attack damage in a cone around the target, uses a different amount against creeps, and is melee-only. [loc:DOTA_Tooltip_ability_item_bfury_Description]

*The bearer of this mighty axe gains the ability to cut down swaths of enemies at once.* [loc:DOTA_Tooltip_ability_item_bfury_Lore]