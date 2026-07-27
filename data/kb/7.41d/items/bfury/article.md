---
title: Battle Fury
kind: item
patch: 7.41d
card:
  entity: bfury
  sentences:
  - text: Battle Fury is an epic item costing 3900 gold that grants 50 damage, 7.5
      health regeneration, and 2.75 mana regeneration, adds 10 melee or 5 ranged damage
      against non-hero units through Quell, gives melee attacks 60% physical Cleave
      damage with 40% against creeps, and provides Chop Tree.
    marks:
    - gamefile:items/item_bfury#cost
    - gamefile:items/item_bfury#attribs
    - loc:DOTA_Tooltip_ability_item_bfury_Description
  - text: Its build formula is Perseverance for 1400 gold, Broadsword for 1000 gold,
      Broadsword for 1000 gold, Quelling Blade for 100 gold, and a 400 gold recipe.
    marks:
    - gamefile:items/item_bfury#components
  - text: The Cleave cone has 650 distance, 150 starting width, and 360 ending width.
    marks:
    - gamefile:items/item_bfury#attribs
  - text: Upgraded Cleave Bonus is 25.
    marks:
    - gamefile:items/item_bfury#attribs
  - text: Upgraded Damage Bonus is 15.
    marks:
    - gamefile:items/item_bfury#attribs
  - text: The unit-targeted active has 350 cast range and a 4.0 cooldown.
    marks:
    - gamefile:items/item_bfury#mechanics
  - text: Chop Tree destroys a target tree.
    marks:
    - loc:DOTA_Tooltip_ability_item_bfury_Description
  - text: Cleave deals physical attack damage in a cone around the target and is melee-only.
    marks:
    - loc:DOTA_Tooltip_ability_item_bfury_Description
---

# Battle Fury

Battle Fury is an epic item that grants damage, health regeneration, mana regeneration, Quell, and Cleave, and provides Chop Tree. [gamefile:items/item_bfury#cost] [gamefile:items/item_bfury#attribs] [loc:DOTA_Tooltip_ability_item_bfury_Description]

## Build Formula

| Component | Cost |
|---|---:|
| Perseverance | 1400 gold |
| Broadsword | 1000 gold |
| Broadsword | 1000 gold |
| Quelling Blade | 100 gold |
| Recipe | 400 gold |
| **Battle Fury** | **3900 gold** |

[gamefile:items/item_bfury#components] [gamefile:items/item_bfury#cost]

## Stats

| Stat | Value |
|---|---:|
| DAMAGE | 50 |
| HEALTH REGENERATION | 7.5 |
| MANA REGENERATION | 2.75 |
| CLEAVE DAMAGE PERCENT | 60% |
| CLEAVE DAMAGE PERCENT CREEP | 40% |
| CLEAVE DISTANCE | 650 |
| CLEAVE ENDING WIDTH | 360 |
| CLEAVE STARTING WIDTH | 150 |
| QUELLING BONUS | 10 |
| QUELLING BONUS RANGED | 5 |
| UPGRADED CLEAVE BONUS | 25 |
| UPGRADED DAMAGE BONUS | 15 |

[gamefile:items/item_bfury#attribs]

| Cast property | Value |
|---|---:|
| Behavior | Unit Target |
| Cast range | 350 |
| Cooldown | 4.0 |

[gamefile:items/item_bfury#mechanics]

## Abilities

**Chop Tree** destroys a target tree. **Quell** increases attack damage against non-hero units, with separate bonuses for melee and ranged heroes. **Cleave** deals physical attack damage in a cone around the target, uses a separate damage percentage against creeps, and is melee-only. [loc:DOTA_Tooltip_ability_item_bfury_Description]

*The bearer of this mighty axe gains the ability to cut down swaths of enemies at once.* [loc:DOTA_Tooltip_ability_item_bfury_Lore]