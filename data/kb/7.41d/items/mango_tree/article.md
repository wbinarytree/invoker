---
title: Mango Tree
kind: item
patch: 7.41d
card:
  entity: mango_tree
  sentences:
  - text: Mango Tree is a consumable point-target item with 200 cast range that plants
      a mango tree, generates Enchanted Mangoes at a listed interval of 60 seconds,
      and provides unobstructed vision in the area.
    marks:
    - gamefile:items/item_mango_tree#cost
    - gamefile:items/item_mango_tree#mechanics
    - gamefile:items/item_mango_tree#attribs
    - loc:DOTA_Tooltip_ability_item_mango_tree_Description
  - text: The item targets the ground to plant the tree.
    marks:
    - loc:DOTA_Tooltip_ability_item_mango_tree_Description
  - text: The tree provides unlimited mango power.
    marks:
    - loc:DOTA_Tooltip_ability_item_mango_tree_Description
---

# Mango Tree

**Mango Tree** is a consumable item with **Plant a Mango Tree**, which plants a mango tree that generates **Enchanted Mangoes** and provides **unobstructed vision** in the area. [gamefile:items/item_mango_tree#cost] [loc:DOTA_Tooltip_ability_item_mango_tree_Description]

## Stats

| Attribute | Value |
|---|---:|
| SECONDS | 60 |

[gamefile:items/item_mango_tree#attribs]

| Casting property | Value |
|---|---:|
| Behavior | Point Target |
| Cast range | 200 |

[gamefile:items/item_mango_tree#mechanics]

## Use

The item targets the ground to plant the mango tree. The tree provides unlimited mango power, generates Enchanted Mangoes at the listed interval, and provides unobstructed vision in the area. [loc:DOTA_Tooltip_ability_item_mango_tree_Description]