---
title: Havoc Hammer
kind: item
patch: 7.41d
card:
  entity: havoc_hammer
  sentences:
  - text: Havoc Hammer is a 0-gold item granting 16 Damage and 14 Strength whose immediate,
      no-target Havoc active has a 10.0 cooldown, pulls surrounding enemies 100 toward
      the user within 400 range, slows them by 50% for 3 seconds, and deals 175 base
      magical damage plus 1.5 times the user’s Strength.
    marks:
    - gamefile:items/item_havoc_hammer#cost
    - gamefile:items/item_havoc_hammer#attribs
    - gamefile:items/item_havoc_hammer#mechanics
    - loc:DOTA_Tooltip_Ability_item_havoc_hammer_Description
  - text: Havoc has an angle of 360.
    marks:
    - gamefile:items/item_havoc_hammer#attribs
  - text: Havoc has a knockback duration of 0.2.
    marks:
    - gamefile:items/item_havoc_hammer#attribs
  - text: Its build formula is Havoc Hammer (0 gold).
    marks:
    - gamefile:items/item_havoc_hammer#cost
---

# Havoc Hammer

Havoc Hammer is an item that grants Damage and Strength and provides Havoc, an immediate, no-target active. [gamefile:items/item_havoc_hammer#cost] [gamefile:items/item_havoc_hammer#attribs] [gamefile:items/item_havoc_hammer#mechanics] [loc:DOTA_Tooltip_Ability_item_havoc_hammer_Description]

## Stats

| Stat | Value |
|---|---:|
| Angle | 360 |
| Damage | 16 |
| Strength | 14 |
| Knockback Duration | 0.2 |
| Nuke Base Damage | 175 |
| Nuke Strength Damage | 1.5 |
| Pull Distance | 100 |
| Range | 400 |
| Slow | 50% |
| Slow Duration | 3 |

[gamefile:items/item_havoc_hammer#attribs]

## Havoc

| Property | Value |
|---|---|
| Behavior | Immediate, No Target |
| Cooldown | 10.0 |

[gamefile:items/item_havoc_hammer#mechanics]

Havoc pulls surrounding enemies toward the user, slows them, and deals magical damage based partly on the user’s Strength. [loc:DOTA_Tooltip_Ability_item_havoc_hammer_Description]

## Components

| Component | Gold cost |
|---|---:|
| Havoc Hammer | 0 |

[gamefile:items/item_havoc_hammer#cost]