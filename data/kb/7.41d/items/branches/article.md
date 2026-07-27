---
title: Iron Branch
kind: item
patch: 7.41d
card:
  entity: branches
  sentences:
  - text: Iron Branch is a 55-gold consumable-quality item that grants 1 ALL ATTRIBUTES
      and provides Plant Tree, which plants a tree for 20 seconds.
    marks:
    - gamefile:items/item_branches#cost
    - gamefile:items/item_branches#attribs
    - loc:DOTA_Tooltip_ability_item_branches_Description
  - text: Plant Tree has Point Target behavior, 400 cast range, and 0.0 cooldown.
    marks:
    - gamefile:items/item_branches#mechanics
  - text: Iron Branch costs 55 gold and builds into Magic Wand.
    marks:
    - gamefile:items/item_branches#cost
    - gamefile:items/item_branches#components
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