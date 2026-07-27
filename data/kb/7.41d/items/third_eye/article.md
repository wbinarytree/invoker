---
title: Third Eye
kind: item
patch: 7.41d
card:
  entity: third_eye
  sentences:
  - text: Third Eye is a passive item costing 0 gold that grants 7 All Attributes,
      300 Bonus Vision, and True Sight with a 500 radius.
    marks:
    - gamefile:items/item_third_eye#cost
    - gamefile:items/item_third_eye#attribs
    - gamefile:items/item_third_eye#mechanics
  - text: True Sight lets allied vision within the carrier’s range reveal invisible
      units and wards.
    marks:
    - loc:DOTA_Tooltip_ability_item_third_eye_Description
  - text: Charge Loss removes a charge when the carrier dies.
    marks:
    - loc:DOTA_Tooltip_ability_item_third_eye_Description
  - text: The item disappears after all charges are lost.
    marks:
    - loc:DOTA_Tooltip_ability_item_third_eye_Description
---

# Third Eye

Third Eye is a passive item that grants **All Attributes**, **Bonus Vision**, and **True Sight**. [gamefile:items/item_third_eye#attribs] [gamefile:items/item_third_eye#mechanics] [loc:DOTA_Tooltip_ability_item_third_eye_Description]

## Stats

| Stat | Value |
|---|---:|
| Cost | 0 gold |
| ALL ATTRIBUTES | 7 |
| BONUS VISION | 300 |
| TRUESIGHT RADIUS | 500 |

[gamefile:items/item_third_eye#cost] [gamefile:items/item_third_eye#attribs]

## Mechanics

True Sight allows any allied vision within the carrier’s range to see invisible units and wards. Charge Loss causes the item to lose a charge on death; after all charges are lost, the item disappears. [loc:DOTA_Tooltip_ability_item_third_eye_Description]