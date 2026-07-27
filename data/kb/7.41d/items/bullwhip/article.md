---
title: Bullwhip
kind: item
patch: 7.41d
card:
  entity: bullwhip
  sentences:
  - text: Bullwhip is an item costing 0 gold whose Whip active grants an ally 25%
      Movement Speed or applies a 25% Movement Speed slow to an enemy for 4 seconds
      after a 0.3-second delay.
    marks:
    - gamefile:items/item_bullwhip#cost
    - gamefile:items/item_bullwhip#attribs
    - loc:DOTA_Tooltip_ability_item_bullwhip_Description
  - text: Whip is an immediate unit-target active.
    marks:
    - gamefile:items/item_bullwhip#mechanics
  - text: Whip has 850 cast range.
    marks:
    - gamefile:items/item_bullwhip#mechanics
  - text: Whip has an 11.0-second cooldown.
    marks:
    - gamefile:items/item_bullwhip#mechanics
  - text: Bullwhip provides 0 bonus health regeneration.
    marks:
    - gamefile:items/item_bullwhip#attribs
  - text: Bullwhip provides 0 bonus mana regeneration.
    marks:
    - gamefile:items/item_bullwhip#attribs
  - text: Bullwhip is built from Bullwhip (0 gold).
    marks:
    - gamefile:items/item_bullwhip#cost
---

# Bullwhip

Bullwhip is an item whose Whip active grants Movement Speed to allies and reduces Movement Speed for enemies. [loc:DOTA_Tooltip_ability_item_bullwhip_Description]

## Stats

| Stat | Value |
|---|---:|
| Bonus Health Regen | 0 |
| Bonus Mana Regen | 0 |
| Bullwhip Delay Time | 0.3 |
| Duration | 4 |
| Movement Speed / Movement Speed Slow | 25% |

[gamefile:items/item_bullwhip#attribs] [loc:DOTA_Tooltip_ability_item_bullwhip_Description]

## Active: Whip

| Property | Value |
|---|---|
| Behavior | Unit Target, Immediate |
| Cast range | 850 |
| Cooldown | 11.0 |

[gamefile:items/item_bullwhip#mechanics]

## Components

| Entry | Gold cost |
|---|---:|
| Bullwhip | 0 gold |

[gamefile:items/item_bullwhip#cost]

*Once the favored lash of an infamous broker of pit fighters and other live trade.* [loc:DOTA_Tooltip_ability_item_bullwhip_Lore]