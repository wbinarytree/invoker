---
title: Iron Branch
kind: item
patch: 7.41d
card:
  entity: branches
  sentences:
  - text: Iron Branch is a consumable-quality item costing 55 gold that grants 1 ALL
      ATTRIBUTES and provides point-target Plant Tree with TREE DURATION 20, cast
      range 400, and cooldown 0.0.
    marks:
    - gamefile:items/item_branches#cost
    - gamefile:items/item_branches#attribs
    - gamefile:items/item_branches#mechanics
    - loc:DOTA_Tooltip_ability_item_branches_Description
  - text: Plant Tree targets the ground to plant a tree.
    marks:
    - loc:DOTA_Tooltip_ability_item_branches_Description
  - text: Iron Branch (55 gold) builds into Magic Wand.
    marks:
    - gamefile:items/item_branches#cost
    - gamefile:items/item_branches#components
  - text: A seemingly ordinary branch, its ironlike qualities are bestowed upon the
      bearer.
    marks:
    - loc:DOTA_Tooltip_ability_item_branches_Lore
---

# Iron Branch

Iron Branch is a consumable-quality item that grants **ALL ATTRIBUTES** and provides **Plant Tree**. [gamefile:items/item_branches#cost] [gamefile:items/item_branches#attribs] [loc:DOTA_Tooltip_ability_item_branches_Description]

## Stats

| Stat | Value |
|---|---:|
| ALL ATTRIBUTES | 1 |
| TREE DURATION | 20 |

[gamefile:items/item_branches#attribs]

## Plant Tree

| Property | Value |
|---|---:|
| Behavior | Point Target |
| Cast range | 400 |
| Cooldown | 0.0 |

[gamefile:items/item_branches#mechanics]

Plant Tree targets the ground to plant a happy little tree. [loc:DOTA_Tooltip_ability_item_branches_Description]

## Components

| Entry | Gold cost |
|---|---:|
| Iron Branch | 55 gold |
| Builds into: Magic Wand | 460 gold |

[gamefile:items/item_branches#cost] [gamefile:items/item_branches#components]

*A seemingly ordinary branch, its ironlike qualities are bestowed upon the bearer.* [loc:DOTA_Tooltip_ability_item_branches_Lore]