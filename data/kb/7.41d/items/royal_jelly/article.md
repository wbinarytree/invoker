---
title: Royal Jelly
kind: item
patch: 7.41d
card:
  entity: royal_jelly
  sentences:
  - text: Royal Jelly is a 0-gold consumable with 10 maximum charges whose Consume
      active grants a target allied unit 2.5 Health Regen and 1.25 Mana Regen per
      charge for 8 seconds, with a 12-second cooldown.
    marks:
    - gamefile:items/item_royal_jelly#cost
    - gamefile:items/item_royal_jelly#attribs
    - loc:DOTA_Tooltip_ability_item_royal_jelly_Description
  - text: Its listed Health and Mana values are 50 each.
    marks:
    - gamefile:items/item_royal_jelly#attribs
  - text: Consume has 300 cast range.
    marks:
    - gamefile:items/item_royal_jelly#mechanics
  - text: Consume is unit-targeted.
    marks:
    - gamefile:items/item_royal_jelly#mechanics
  - text: Consume is immediate.
    marks:
    - gamefile:items/item_royal_jelly#mechanics
  - text: Consume does not resume attacks.
    marks:
    - gamefile:items/item_royal_jelly#mechanics
  - text: Using Consume expends all charges.
    marks:
    - loc:DOTA_Tooltip_ability_item_royal_jelly_Description
  - text: The buff is lost if the affected unit is attacked by an enemy hero or Roshan.
    marks:
    - loc:DOTA_Tooltip_ability_item_royal_jelly_Description
---

# Royal Jelly

Royal Jelly is a consumable item whose Consume active grants Health Regen and Mana Regen to a target allied unit. [gamefile:items/item_royal_jelly#cost] [loc:DOTA_Tooltip_ability_item_royal_jelly_Description]

## Cost

| Property | Value |
|---|---:|
| Cost | 0 gold |

[gamefile:items/item_royal_jelly#cost]

## Stats

| Stat | Value |
|---|---:|
| HEALTH | 50 |
| MANA | 50 |
| HEALTH REGEN | 2.5 |
| MANA REGEN | 1.25 |
| MAX CHARGES | 10 |
| REGEN DURATION | 8 |
| USE COOLDOWN | 12 |

[gamefile:items/item_royal_jelly#attribs]

| Property | Value |
|---|---:|
| Cast range | 300 |

[gamefile:items/item_royal_jelly#mechanics]

## Consume

Consume is unit-targeted and immediate, and does not resume attacks. [gamefile:items/item_royal_jelly#mechanics]

Using Consume expends all charges. Its buff provides Health Regen and Mana Regen per charge and is lost if the affected unit is attacked by an enemy hero or Roshan. [loc:DOTA_Tooltip_ability_item_royal_jelly_Description]

*To those who harvest olgru jelly, success serves more than mere profit—it is often the means to survival, for only the jelly itself can cure the ravages caused by a sting from the vigilant denizens of the giant hives.* [loc:DOTA_Tooltip_ability_item_royal_jelly_Lore]