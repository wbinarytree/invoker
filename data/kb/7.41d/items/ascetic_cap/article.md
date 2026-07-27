---
title: Ascetic's Cap
kind: item
patch: 7.41d
card:
  entity: ascetic_cap
  sentences:
  - text: Ascetic's Cap is an item costing 0 gold whose passive Endurance grants %status_resistance%%%
      Status Resistance and %slow_resistance%%% Slow Resistance for %duration% seconds
      whenever a debuff would be applied, with a 25.0-second cooldown.
    marks:
    - gamefile:items/item_ascetic_cap#cost
    - loc:DOTA_Tooltip_Ability_item_ascetic_cap_Description
    - gamefile:items/item_ascetic_cap#mechanics
  - text: It grants 0 Bonus Health.
    marks:
    - gamefile:items/item_ascetic_cap#attribs
  - text: It grants 0 HP Regen.
    marks:
    - gamefile:items/item_ascetic_cap#attribs
  - text: Endurance has a mana cost of 0.
    marks:
    - gamefile:items/item_ascetic_cap#mechanics
  - text: It is built from Ascetic's Cap (0 gold).
    marks:
    - gamefile:items/item_ascetic_cap#cost
  - text: An austere hat thought to be of Turstarkuri origin.
    marks:
    - loc:DOTA_Tooltip_Ability_item_ascetic_cap_Lore
---

# Ascetic's Cap

Ascetic's Cap is an item with the passive Endurance, which grants Status Resistance and Slow Resistance whenever a debuff would be applied to its owner. [gamefile:items/item_ascetic_cap#cost] [loc:DOTA_Tooltip_Ability_item_ascetic_cap_Description]

## Attributes

| Stat | Value |
|---|---:|
| Bonus Health | 0 |
| HP Regen | 0 |

[gamefile:items/item_ascetic_cap#attribs]

## Endurance

| Property | Value |
|---|---:|
| Status Resistance | %status_resistance%%% |
| Slow Resistance | %slow_resistance%%% |
| Duration | %duration% seconds |
| Behavior | Passive |
| Mana cost | 0 |
| Cooldown | 25.0 |

[loc:DOTA_Tooltip_Ability_item_ascetic_cap_Description] [gamefile:items/item_ascetic_cap#mechanics]

## Components

| Entry | Gold cost |
|---|---:|
| Ascetic's Cap | 0 gold |

[gamefile:items/item_ascetic_cap#cost]

*An austere hat thought to be of Turstarkuri origin.* [loc:DOTA_Tooltip_Ability_item_ascetic_cap_Lore]