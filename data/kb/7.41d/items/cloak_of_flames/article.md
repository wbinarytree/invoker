---
title: Cloak of Flames
kind: item
patch: 7.41d
card:
  entity: cloak_of_flames
  sentences:
  - text: Cloak of Flames is a 0-gold item whose passive Immolate deals 40 damage
      per second to nearby enemy units within 375 radius and 25 damage per second
      when used by illusions.
    marks:
    - gamefile:items/item_cloak_of_flames#attribs
    - loc:DOTA_Tooltip_Ability_item_cloak_of_flames_Description
    - gamefile:items/item_cloak_of_flames#cost
  - text: It provides 0 armor.
    marks:
    - gamefile:items/item_cloak_of_flames#attribs
  - text: It provides 0 magic resistance.
    marks:
    - gamefile:items/item_cloak_of_flames#attribs
  - text: It has the `DOTA_ABILITY_BEHAVIOR_DONT_PROC_OTHER_ABILITIES` flag.
    marks:
    - gamefile:items/item_cloak_of_flames#mechanics
---

# Cloak of Flames

Cloak of Flames is an item with the passive Immolate effect, which deals DAMAGE per second to nearby enemy units and DAMAGE ILLUSIONS per second from illusions. [gamefile:items/item_cloak_of_flames#attribs] [loc:DOTA_Tooltip_Ability_item_cloak_of_flames_Description]

## Stats

| Stat | Value |
|---|---:|
| ARMOR | 0 |
| DAMAGE | 40 |
| DAMAGE ILLUSIONS | 25 |
| MAGIC RESISTANCE | 0 |
| RADIUS | 375 |

[gamefile:items/item_cloak_of_flames#attribs]

## Cost

| Item | Gold cost |
|---|---:|
| Cloak of Flames | 0 |

[gamefile:items/item_cloak_of_flames#cost]

## Mechanics

Immolate affects enemy units within its radius; illusions use its separate illusion damage. [loc:DOTA_Tooltip_Ability_item_cloak_of_flames_Description]

It has Passive behavior and the `DOTA_ABILITY_BEHAVIOR_DONT_PROC_OTHER_ABILITIES` flag. [gamefile:items/item_cloak_of_flames#mechanics]

*A very fine cloak that plays host to an overly-protective living flame.* [loc:DOTA_Tooltip_Ability_item_cloak_of_flames_Lore]