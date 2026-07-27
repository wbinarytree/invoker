---
title: Safety Bubble
kind: item
patch: 7.41d
card:
  entity: safety_bubble
  sentences:
  - text: Safety Bubble is a 0-gold item whose passive Bubbled Up provides the equipped
      Hero with a 100 HP Barrier against enemy damage and has a Restore Time of 8.
    marks:
    - gamefile:items/item_safety_bubble#mechanics
    - loc:DOTA_Tooltip_ability_item_safety_bubble_Description
    - gamefile:items/item_safety_bubble#attribs
    - gamefile:items/item_safety_bubble#cost
  - text: It provides 0 Bonus HP Regen.
    marks:
    - gamefile:items/item_safety_bubble#attribs
  - text: The barrier fully regenerates after the equipped Hero avoids receiving damage
      for the required interval.
    marks:
    - loc:DOTA_Tooltip_ability_item_safety_bubble_Description
  - text: Self-inflicted damage bypasses the barrier.
    marks:
    - loc:DOTA_Tooltip_ability_item_safety_bubble_Description
---

# Safety Bubble

Safety Bubble is an item with the passive Bubbled Up, which provides the equipped Hero with an HP Barrier against enemy damage. [gamefile:items/item_safety_bubble#mechanics] [loc:DOTA_Tooltip_ability_item_safety_bubble_Description]

## Stats

| Stat | Value |
|---|---:|
| Bonus HP Regen | 0 |
| Restore Time | 8 |
| Shield | 100 |

[gamefile:items/item_safety_bubble#attribs]

## Cost

| Item | Gold cost |
|---|---:|
| Safety Bubble | 0 gold |

[gamefile:items/item_safety_bubble#cost]

## Mechanics

The barrier fully regenerates after the equipped Hero avoids receiving damage for the required interval. Self-inflicted damage bypasses the barrier. [loc:DOTA_Tooltip_ability_item_safety_bubble_Description]