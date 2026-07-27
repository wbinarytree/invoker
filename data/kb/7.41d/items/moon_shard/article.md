---
title: Moon Shard
kind: item
patch: 7.41d
card:
  entity: moon_shard
  sentences:
  - text: Moon Shard is a 4000-gold consumable item that grants 140 attack speed and
      400 bonus night vision, while Consume permanently grants 60 attack speed and
      200 bonus night vision.
    marks:
    - gamefile:items/item_moon_shard#cost
    - gamefile:items/item_moon_shard#attribs
    - loc:DOTA_Tooltip_ability_item_moon_shard_Description
  - text: Its build formula is Hyperstone (2000 gold) plus Hyperstone (2000 gold).
    marks:
    - gamefile:items/item_moon_shard#components
  - text: Moon Shard has Unit Target and Immediate behavior.
    marks:
    - gamefile:items/item_moon_shard#mechanics
  - text: Consume is limited to one use.
    marks:
    - loc:DOTA_Tooltip_ability_item_moon_shard_Description
  - text: Shade Sight passively grants bonus night vision.
    marks:
    - loc:DOTA_Tooltip_ability_item_moon_shard_Description
---

# Moon Shard

Moon Shard is a consumable item that grants Attack Speed and Bonus Night Vision, while Consume permanently grants Attack Speed and Bonus Night Vision. [gamefile:items/item_moon_shard#cost] [gamefile:items/item_moon_shard#attribs] [loc:DOTA_Tooltip_ability_item_moon_shard_Description]

## Stats

| Stat | Value |
|---|---:|
| ATTACK SPEED | 140 |
| BONUS NIGHT VISION | 400 |
| CONSUMED BONUS | 60 |
| CONSUMED BONUS NIGHT VISION | 200 |

[gamefile:items/item_moon_shard#attribs]

## Components

| Component | Gold cost |
|---|---:|
| Hyperstone | 2000 gold |
| Hyperstone | 2000 gold |
| **Total cost** | **4000 gold** |

[gamefile:items/item_moon_shard#components] [gamefile:items/item_moon_shard#cost]

## Mechanics

Moon Shard has Unit Target and Immediate behavior. [gamefile:items/item_moon_shard#mechanics]

Consume permanently applies its consumed bonuses and is limited to one use. Shade Sight passively grants bonus night vision. [loc:DOTA_Tooltip_ability_item_moon_shard_Description]

*Said to be a tear from the lunar goddess Selemene.* [loc:DOTA_Tooltip_ability_item_moon_shard_Lore]