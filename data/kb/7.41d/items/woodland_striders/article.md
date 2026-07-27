---
title: Woodland Striders
kind: item
patch: 7.41d
card:
  entity: woodland_striders
  sentences:
  - text: Woodland Striders is a 0 gold item that provides 60 Health Regeneration
      and 140 Movement Speed; its Woodland Stride has Active Duration 3 and creates
      trees with Tree Duration 15, while Tree Walking removes the movement speed limit
      and permits free pathing through trees.
    marks:
    - gamefile:items/item_woodland_striders#attribs
    - gamefile:items/item_woodland_striders#cost
    - loc:DOTA_Tooltip_Ability_item_woodland_striders_Description
  - text: Woodland Stride has Immediate, No Target behavior and a 20.0 cooldown.
    marks:
    - gamefile:items/item_woodland_striders#mechanics
  - text: Woodland Stride creates a path of trees behind the user for its active duration,
      and the trees remain for up to their tree duration.
    marks:
    - loc:DOTA_Tooltip_Ability_item_woodland_striders_Description
  - text: Tree Walking removes the movement speed limit and permits free pathing through
      trees.
    marks:
    - loc:DOTA_Tooltip_Ability_item_woodland_striders_Description
  - text: Movement Speed bonuses from multiple pairs of boots do not stack.
    marks:
    - loc:DOTA_Tooltip_Ability_item_woodland_striders_Description
---

# Woodland Striders

Woodland Striders is an item that provides Health Regeneration and Movement Speed and grants the active Woodland Stride and passive Tree Walking. [gamefile:items/item_woodland_striders#attribs] [loc:DOTA_Tooltip_Ability_item_woodland_striders_Description]

## Stats

| Stat | Value |
|---|---:|
| Active Duration | 3 |
| Health Regeneration | 60 |
| Movement Speed | 140 |
| Tree Duration | 15 |

[gamefile:items/item_woodland_striders#attribs]

| Property | Value |
|---|---|
| Behavior | Immediate, No Target |
| Cooldown | 20.0 |

[gamefile:items/item_woodland_striders#mechanics]

## Cost

| Item | Gold Cost |
|---|---:|
| Woodland Striders | 0 gold |

[gamefile:items/item_woodland_striders#cost]

## Mechanics

Woodland Stride creates a path of trees behind the user for its active duration; the trees remain for up to their tree duration. [loc:DOTA_Tooltip_Ability_item_woodland_striders_Description]

Tree Walking removes the movement speed limit and permits free pathing through trees. Movement Speed bonuses from multiple pairs of boots do not stack. [loc:DOTA_Tooltip_Ability_item_woodland_striders_Description]