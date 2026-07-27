---
title: Faerie Fire
kind: item
patch: 7.41d
card:
  entity: faerie_fire
  sentences:
  - text: Faerie Fire is a consumable item costing 65 gold that grants 2 DAMAGE and
      has Imbue, which instantly provides 85 HP RESTORE.
    marks:
    - gamefile:items/item_faerie_fire#cost
    - gamefile:items/item_faerie_fire#attribs
    - loc:DOTA_Tooltip_ability_item_faerie_fire_Description
  - text: Imbue has Immediate, No Target behavior.
    marks:
    - gamefile:items/item_faerie_fire#mechanics
  - text: Imbue has a 5.0 cooldown.
    marks:
    - gamefile:items/item_faerie_fire#mechanics
  - text: The ethereal flames from the ever-burning ruins of Kindertree ignite across
      realities.
    marks:
    - loc:DOTA_Tooltip_ability_item_faerie_fire_Lore
---

# Faerie Fire

Faerie Fire is a consumable item that grants DAMAGE and has Imbue, which provides HP RESTORE. [gamefile:items/item_faerie_fire#cost] [gamefile:items/item_faerie_fire#attribs] [loc:DOTA_Tooltip_ability_item_faerie_fire_Description]

## Cost

| Item | Cost |
|---|---:|
| Faerie Fire | 65 gold |

[gamefile:items/item_faerie_fire#cost]

## Stats

| Stat | Value |
|---|---:|
| DAMAGE | 2 |
| HP RESTORE | 85 |

[gamefile:items/item_faerie_fire#attribs]

## Imbue

| Property | Value |
|---|---:|
| Behavior | Immediate, No Target |
| Cooldown | 5.0 |

[gamefile:items/item_faerie_fire#mechanics]

Imbue instantly restores health. [loc:DOTA_Tooltip_ability_item_faerie_fire_Description]

*The ethereal flames from the ever-burning ruins of Kindertree ignite across realities.* [loc:DOTA_Tooltip_ability_item_faerie_fire_Lore]