---
title: Clumsy Net
kind: item
patch: 7.41d
card:
  entity: clumsy_net
  sentences:
  - text: Clumsy Net is a 0-gold item with Ensnare, a Unit Target active with 600
      cast range and 25.0 cooldown that ensnares a targeted enemy and the user for
      1.75 duration.
    marks:
    - gamefile:items/item_clumsy_net#cost
    - gamefile:items/item_clumsy_net#attribs
    - gamefile:items/item_clumsy_net#mechanics
    - loc:DOTA_Tooltip_Ability_item_clumsy_net_Description
  - text: It grants 0 ALL STATS and 0 MANA REGEN.
    marks:
    - gamefile:items/item_clumsy_net#attribs
---

# Clumsy Net

Clumsy Net is an item with the Ensnare active and the ALL STATS and MANA REGEN attributes. [gamefile:items/item_clumsy_net#cost] [gamefile:items/item_clumsy_net#attribs] [loc:DOTA_Tooltip_Ability_item_clumsy_net_Description]

## Cost

| Item | Gold cost |
|---|---:|
| Clumsy Net | 0 gold |

[gamefile:items/item_clumsy_net#cost]

## Stats

| Stat | Value |
|---|---:|
| ALL STATS | 0 |
| DURATION | 1.75 |
| MANA REGEN | 0 |

[gamefile:items/item_clumsy_net#attribs]

## Active

| Property | Value |
|---|---:|
| Behavior | Unit Target |
| Cast range | 600 |
| Cooldown | 25.0 |

[gamefile:items/item_clumsy_net#mechanics]

Ensnare targets an enemy and ensnares both that enemy and the user for the listed duration. [loc:DOTA_Tooltip_Ability_item_clumsy_net_Description]