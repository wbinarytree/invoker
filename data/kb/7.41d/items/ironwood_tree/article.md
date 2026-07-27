---
title: Ironwood Tree
kind: item
patch: 7.41d
card:
  entity: ironwood_tree
  sentences:
  - text: Ironwood Tree is a 0-gold item that grants 5 All Attributes and provides
      Plant Tree with Tree Duration 20.
    marks:
    - gamefile:items/item_ironwood_tree#cost
    - gamefile:items/item_ironwood_tree#attribs
    - loc:DOTA_Tooltip_ability_item_ironwood_tree_Description
  - text: Plant Tree targets the ground.
    marks:
    - loc:DOTA_Tooltip_ability_item_ironwood_tree_Description
  - text: Plant Tree has Point Target behavior.
    marks:
    - gamefile:items/item_ironwood_tree#mechanics
  - text: Plant Tree has 400 cast range.
    marks:
    - gamefile:items/item_ironwood_tree#mechanics
  - text: Plant Tree has a 15.0 cooldown.
    marks:
    - gamefile:items/item_ironwood_tree#mechanics
---

# Ironwood Tree

Ironwood Tree is an item that grants All Attributes and provides the Plant Tree use. [gamefile:items/item_ironwood_tree#attribs] [loc:DOTA_Tooltip_ability_item_ironwood_tree_Description]

## Cost

| Item | Gold cost |
|---|---:|
| Ironwood Tree | 0 gold |

[gamefile:items/item_ironwood_tree#cost]

## Stats

| Stat | Value |
|---|---:|
| All Attributes | 5 |
| Tree Duration | 20 |

[gamefile:items/item_ironwood_tree#attribs]

## Plant Tree

| Property | Value |
|---|---|
| Behavior | Point Target |
| Cast range | 400 |
| Cooldown | 15.0 |

[gamefile:items/item_ironwood_tree#mechanics]

Targets the ground to plant a happy little tree. [loc:DOTA_Tooltip_ability_item_ironwood_tree_Description]

*Precious. And hearty as a weed.* [loc:DOTA_Tooltip_ability_item_ironwood_tree_Lore]