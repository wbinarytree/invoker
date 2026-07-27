---
title: Linken's Sphere
kind: item
patch: 7.41d
card:
  entity: sphere
  sentences:
  - text: Linken's Sphere is an epic item costing 4800 gold that grants 16 All Attributes,
      6.5 Health Regeneration, 4.25 Mana Regeneration, 300 Damage Absorb, and 10.0
      Upgrade Absorb Duration, with passive Spellblock once every 14.0 seconds and
      active Transfer Spellblock for 14.0 seconds.
    marks:
    - gamefile:items/item_sphere#cost
    - gamefile:items/item_sphere#attribs
    - loc:DOTA_Tooltip_ability_item_sphere_Description
  - text: The build formula is Perseverance for 1400 gold, Ultimate Orb for 2800 gold,
      and Recipe for 600 gold, totaling 4800 gold.
    marks:
    - gamefile:items/item_sphere#components
    - gamefile:items/item_sphere#cost
  - text: Block Cooldown is 14.0.
    marks:
    - gamefile:items/item_sphere#attribs
  - text: Spellblock blocks most targeted spells.
    marks:
    - loc:DOTA_Tooltip_ability_item_sphere_Description
  - text: Transfer Spellblock temporarily removes Spellblock from the item’s owner
      and transfers it to an allied unit.
    marks:
    - loc:DOTA_Tooltip_ability_item_sphere_Description
  - text: Transfer Spellblock has Unit Target behavior.
    marks:
    - gamefile:items/item_sphere#mechanics
  - text: Transfer Spellblock has 700 cast range.
    marks:
    - gamefile:items/item_sphere#mechanics
  - text: This magical sphere once protected one of the most famous heroes in history.
    marks:
    - loc:DOTA_Tooltip_ability_item_sphere_Lore
---

# Linken's Sphere

Linken's Sphere is an epic item with Block Cooldown, All Attributes, Health Regeneration, Mana Regeneration, Damage Absorb, and Upgrade Absorb Duration, plus passive Spellblock and active Transfer Spellblock. [gamefile:items/item_sphere#cost] [gamefile:items/item_sphere#attribs] [loc:DOTA_Tooltip_ability_item_sphere_Description]

## Stats

| Stat | Value |
|---|---:|
| Block Cooldown | 14.0 |
| All Attributes | 16 |
| Health Regeneration | 6.5 |
| Mana Regeneration | 4.25 |
| Damage Absorb | 300 |
| Upgrade Absorb Duration | 10.0 |

[gamefile:items/item_sphere#attribs]

## Components

| Component | Gold cost |
|---|---:|
| Perseverance | 1400 gold |
| Ultimate Orb | 2800 gold |
| Recipe | 600 gold |
| **Total** | **4800 gold** |

[gamefile:items/item_sphere#components] [gamefile:items/item_sphere#cost]

## Abilities

| Ability | Classification | Timing |
|---|---|---:|
| Spellblock | Passive | Once every 14.0 seconds |
| Transfer Spellblock | Active | 14.0 seconds |

[loc:DOTA_Tooltip_ability_item_sphere_Description]

Spellblock blocks most targeted spells. Transfer Spellblock temporarily removes Spellblock from the item’s owner and transfers it to an allied unit. [loc:DOTA_Tooltip_ability_item_sphere_Description]

| Behavior | Cast range |
|---|---:|
| Unit Target | 700 |

[gamefile:items/item_sphere#mechanics]

*This magical sphere once protected one of the most famous heroes in history.* [loc:DOTA_Tooltip_ability_item_sphere_Lore]