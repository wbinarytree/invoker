---
title: Craggy Coat
kind: item
patch: 7.41d
card:
  entity: craggy_coat
  sentences:
  - text: Craggy Coat is a 0-gold item whose Toughen Up active grants 6 bonus armor
      for 6 seconds at the cost of 20 movement speed.
    marks:
    - gamefile:items/item_craggy_coat#cost
    - gamefile:items/item_craggy_coat#attribs
    - loc:DOTA_Tooltip_ability_item_craggy_coat_Description
  - text: Toughen Up has No Target, Immediate behavior.
    marks:
    - gamefile:items/item_craggy_coat#mechanics
  - text: Toughen Up has a 12-second cooldown.
    marks:
    - gamefile:items/item_craggy_coat#mechanics
  - text: Craggy Coat provides 0 Armor Bonus.
    marks:
    - gamefile:items/item_craggy_coat#attribs
  - text: Craggy Coat provides 0 Bonus Health.
    marks:
    - gamefile:items/item_craggy_coat#attribs
---

# Craggy Coat

Craggy Coat is an item with the Toughen Up active, which grants Bonus Armor at the cost of Movement Speed. [gamefile:items/item_craggy_coat#cost] [loc:DOTA_Tooltip_ability_item_craggy_coat_Description]

## Stats

| Stat | Value |
|---|---:|
| Active Armor | 6 |
| Active Duration | 6 |
| Armor Bonus | 0 |
| Bonus Health | 0 |
| Move Speed | 20 |

[gamefile:items/item_craggy_coat#attribs]

## Toughen Up

| Property | Value |
|---|---|
| Behavior | No Target, Immediate |
| Cooldown | 12 |

[gamefile:items/item_craggy_coat#mechanics]

Toughen Up temporarily applies its effects to the user. [loc:DOTA_Tooltip_ability_item_craggy_coat_Description]

## Cost

| Item | Gold cost |
|---|---:|
| Craggy Coat | 0 gold |

[gamefile:items/item_craggy_coat#cost]