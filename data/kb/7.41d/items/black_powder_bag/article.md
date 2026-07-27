---
title: Blast Rig
kind: item
patch: 7.41d
card:
  entity: black_powder_bag
  sentences:
  - text: Blast Rig is a 0-gold passive item that grants 7 Armor; Hair Trigger has
      a 20-second Cooldown and, when triggered by a hero attacking its holder within
      400 Radius, deals 250 Damage to all enemies within that Radius and causes 100%
      missed attacks for 2 seconds.
    marks:
    - gamefile:items/item_black_powder_bag#cost
    - gamefile:items/item_black_powder_bag#attribs
    - gamefile:items/item_black_powder_bag#mechanics
    - loc:DOTA_Tooltip_Ability_item_black_powder_bag_Description
  - text: Hair Trigger activates the next time the holder is attacked by a hero within
      its Radius.
    marks:
    - loc:DOTA_Tooltip_Ability_item_black_powder_bag_Description
  - text: One of a set of custom rigs once worn by infamous road agents in the Outlands,
      its siblings have been lost to misfires and the various tides of time.
    marks:
    - loc:DOTA_Tooltip_Ability_item_black_powder_bag_Lore
---

# Blast Rig

Blast Rig is a passive item that provides Armor and has Hair Trigger, which deals Damage in a Radius and causes missed attacks according to its Blind Pct and Blind Duration. [gamefile:items/item_black_powder_bag#attribs] [gamefile:items/item_black_powder_bag#mechanics] [loc:DOTA_Tooltip_Ability_item_black_powder_bag_Description]

## Stats

| Stat | Value |
|---|---:|
| Blind Duration | 2 |
| Blind Pct | 100% |
| Armor | 7 |
| Damage | 250 |
| Radius | 400 |
| Cooldown | 20 |

[gamefile:items/item_black_powder_bag#attribs] [gamefile:items/item_black_powder_bag#mechanics]

## Mechanics

Hair Trigger activates the next time the holder is attacked by a hero within the listed Radius. It deals the listed Damage to all enemies within that Radius and causes them to miss attacks according to Blind Pct for Blind Duration. [loc:DOTA_Tooltip_Ability_item_black_powder_bag_Description]

## Cost

| Item | Gold cost |
|---|---:|
| Blast Rig | 0 gold |

[gamefile:items/item_black_powder_bag#cost]

*One of a set of custom rigs once worn by infamous road agents in the Outlands, its siblings have been lost to misfires and the various tides of time.* [loc:DOTA_Tooltip_Ability_item_black_powder_bag_Lore]