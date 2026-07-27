---
title: Blast Rig
kind: item
patch: 7.41d
card:
  entity: black_powder_bag
  sentences:
  - text: Blast Rig is a passive item costing 0 gold that grants 7 Armor; Hair Trigger
      has 20 Cooldown and activates when a hero attacks the holder within 400 Radius,
      dealing 250 Damage to all enemies within that Radius and causing 100% missed
      attacks for 2 Blind Duration.
    marks:
    - gamefile:items/item_black_powder_bag#attribs
    - gamefile:items/item_black_powder_bag#mechanics
    - loc:DOTA_Tooltip_Ability_item_black_powder_bag_Description
    - gamefile:items/item_black_powder_bag#cost
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