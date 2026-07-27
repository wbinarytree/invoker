---
title: Doubloon
kind: item
patch: 7.41d
card:
  entity: doubloon
  sentences:
  - text: Doubloon is a 0-gold item whose No Target Flip toggle converts Max Health
      to Max Mana or Max Mana to Max Health with 30% Conversion Pct and 5 cooldown.
    marks:
    - gamefile:items/item_doubloon#cost
    - loc:DOTA_Tooltip_ability_item_doubloon_Description
    - gamefile:items/item_doubloon#attribs
    - gamefile:items/item_doubloon#mechanics
  - text: Bonus Health Regen is 0.
    marks:
    - gamefile:items/item_doubloon#attribs
  - text: Bonus Mana Regen is 0.
    marks:
    - gamefile:items/item_doubloon#attribs
  - text: Regen Bonus Pct is 0.
    marks:
    - gamefile:items/item_doubloon#attribs
---

# Doubloon

Doubloon is an item whose Flip toggle converts Max Health to Max Mana or Max Mana to Max Health. [gamefile:items/item_doubloon#cost] [loc:DOTA_Tooltip_ability_item_doubloon_Description]

## Cost

| Item | Gold cost |
|---|---:|
| Doubloon | 0 gold |

[gamefile:items/item_doubloon#cost]

## Attributes

| Stat | Value |
|---|---:|
| Bonus Health Regen | 0 |
| Bonus Mana Regen | 0 |
| Conversion Pct | 30% |
| Regen Bonus Pct | 0 |

[gamefile:items/item_doubloon#attribs]

## Mechanics

| Property | Value |
|---|---|
| Behavior | No Target, Toggle |
| Cooldown | 5 |

[gamefile:items/item_doubloon#mechanics]