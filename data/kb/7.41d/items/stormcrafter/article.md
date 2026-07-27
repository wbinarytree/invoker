---
title: Stormcrafter
kind: item
patch: 7.41d
card:
  entity: stormcrafter
  sentences:
  - text: Stormcrafter is a 0-gold item whose passive Bottled Lightning zaps enemy
      targets with Damage 70, Max Targets 2, Range 700, Slow 40%, and Slow Duration
      0.4.
    marks:
    - gamefile:items/item_stormcrafter#cost
    - gamefile:items/item_stormcrafter#attribs
    - loc:DOTA_Tooltip_Ability_item_stormcrafter_Description
  - text: Bottled Lightning has a cooldown of 6.
    marks:
    - gamefile:items/item_stormcrafter#mechanics
  - text: Stormcrafter provides 0 Bonus Mana Regen.
    marks:
    - gamefile:items/item_stormcrafter#attribs
  - text: Stormcrafter provides 0 Passive Movement Bonus.
    marks:
    - gamefile:items/item_stormcrafter#attribs
---

# Stormcrafter

Stormcrafter is an item whose passive Bottled Lightning uses Damage, Max Targets, Range, Slow, and Slow Duration. [gamefile:items/item_stormcrafter#attribs] [loc:DOTA_Tooltip_Ability_item_stormcrafter_Description]

## Stats

| Attribute | Value |
|---|---:|
| Bonus Mana Regen | 0 |
| Damage | 70 |
| Max Targets | 2 |
| Passive Movement Bonus | 0 |
| Range | 700 |
| Slow | 40% |
| Slow Duration | 0.4 |

[gamefile:items/item_stormcrafter#attribs]

## Cost

| Item | Gold cost |
|---|---:|
| Stormcrafter | 0 gold |

[gamefile:items/item_stormcrafter#cost]

## Bottled Lightning

Bottled Lightning zaps enemy targets within range, dealing damage and applying a slow. [loc:DOTA_Tooltip_Ability_item_stormcrafter_Description]

| Property | Value |
|---|---:|
| Behavior | Passive |
| Cooldown | 6 |

[gamefile:items/item_stormcrafter#mechanics]

*The accidental byproduct of a spell conjured to entrap a lesser god.* [loc:DOTA_Tooltip_Ability_item_stormcrafter_Lore]