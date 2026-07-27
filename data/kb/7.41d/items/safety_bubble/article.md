---
title: Safety Bubble
kind: item
patch: 7.41d
card:
  entity: safety_bubble
  sentences:
  - text: Safety Bubble is a Passive item costing 0 gold whose Bubbled Up passive
      gives the equipped Hero an HP Barrier against enemy damage, with Bonus HP Regen
      0, Restore Time 8, and Shield 100.
    marks:
    - gamefile:items/item_safety_bubble#mechanics
    - gamefile:items/item_safety_bubble#attribs
    - loc:DOTA_Tooltip_ability_item_safety_bubble_Description
    - gamefile:items/item_safety_bubble#cost
  - text: 'Its build formula is Cost: 0 gold.'
    marks:
    - gamefile:items/item_safety_bubble#cost
  - text: The barrier fully regenerates after the Hero avoids damage for the listed
      Restore Time.
    marks:
    - loc:DOTA_Tooltip_ability_item_safety_bubble_Description
  - text: Self-inflicted damage bypasses the barrier.
    marks:
    - loc:DOTA_Tooltip_ability_item_safety_bubble_Description
---

# Safety Bubble

Safety Bubble is an item with Passive behavior whose listed effects are Bonus HP Regen, Restore Time, and Shield; its passive is Bubbled Up. [gamefile:items/item_safety_bubble#mechanics] [gamefile:items/item_safety_bubble#attribs] [loc:DOTA_Tooltip_ability_item_safety_bubble_Description]

## Stats

| Stat | Value |
|---|---:|
| BONUS HP REGEN | 0 |
| RESTORE TIME | 8 |
| SHIELD | 100 |

[gamefile:items/item_safety_bubble#attribs]

## Components

| Entry | Gold cost |
|---|---:|
| Cost | 0 gold |

[gamefile:items/item_safety_bubble#cost]

## Mechanics

Bubbled Up gives the equipped Hero an HP Barrier against enemy damage. The barrier fully regenerates after the Hero avoids damage for the listed Restore Time. Self-inflicted damage bypasses the barrier. [loc:DOTA_Tooltip_ability_item_safety_bubble_Description]