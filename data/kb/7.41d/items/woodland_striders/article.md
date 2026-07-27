---
title: Woodland Striders
kind: item
patch: 7.41d
card:
  entity: woodland_striders
  sentences:
  - text: Woodland Striders is a 0-gold item providing 60 Health Regeneration and
      140 Movement Speed; its 3-second Woodland Stride active creates trees behind
      the user that remain for up to 15 seconds, while passive Tree Walking removes
      the movement speed limit and permits free pathing through trees.
    marks:
    - gamefile:items/item_woodland_striders#cost
    - gamefile:items/item_woodland_striders#attribs
    - loc:DOTA_Tooltip_Ability_item_woodland_striders_Description
  - text: Woodland Stride is an immediate, no-target active with a 20.0-second cooldown.
    marks:
    - gamefile:items/item_woodland_striders#mechanics
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