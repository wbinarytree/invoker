---
title: Unwavering Condition
kind: item
patch: 7.41d
card:
  entity: unwavering_condition
  sentences:
  - text: Unwavering Condition is an item that costs 0 gold, provides 95% MAGIC RESISTANCE,
      and fixes MAX HEALTH at 1800 so other effects and attributes cannot alter it.
    marks:
    - gamefile:items/item_unwavering_condition#cost
    - gamefile:items/item_unwavering_condition#attribs
    - gamefile:items/item_unwavering_condition#mechanics
  - text: Its build formula is Unwavering Condition (0 gold).
    marks:
    - gamefile:items/item_unwavering_condition#cost
  - text: Unwavering is passive.
    marks:
    - gamefile:items/item_unwavering_condition#mechanics
---

# Unwavering Condition

Unwavering Condition is an item that provides MAGIC RESISTANCE and sets MAX HEALTH to a fixed value that other effects and attributes cannot alter. [gamefile:items/item_unwavering_condition#attribs] [loc:DOTA_Tooltip_ability_item_unwavering_condition_Description]

## Stats

| Stat | Value |
|---|---:|
| MAGIC RESISTANCE | 95% |
| MAX HEALTH | 1800 |

[gamefile:items/item_unwavering_condition#attribs]

## Components

| Entry | Gold cost |
|---|---:|
| Unwavering Condition | 0 gold |

[gamefile:items/item_unwavering_condition#cost]

## Mechanics

Unwavering is passive. It sets the hero’s Max Health to the listed value, which cannot be altered by other effects or attributes. [gamefile:items/item_unwavering_condition#mechanics] [loc:DOTA_Tooltip_ability_item_unwavering_condition_Description]