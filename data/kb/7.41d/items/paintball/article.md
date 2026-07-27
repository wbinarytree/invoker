---
title: Fae Grenade
kind: item
patch: 7.41d
card:
  entity: paintball
  sentences:
  - text: Fae Grenade is a 0-gold item with 40 DPS, 7 duration, and 20 movement speed
      whose Shadow Brand active has 900 cast range, 25 mana cost, and 20.0 cooldown
      and damages an enemy each second while providing vision.
    marks:
    - gamefile:items/item_paintball#attribs
    - gamefile:items/item_paintball#mechanics
    - gamefile:items/item_paintball#cost
    - loc:DOTA_Tooltip_Ability_item_paintball_Description
  - text: Shadow Brand throws a Mark toward an enemy within cast range and applies
      its debuff for the duration.
    marks:
    - loc:DOTA_Tooltip_Ability_item_paintball_Description
  - text: Its behavior is Unit Target and `DOTA_ABILITY_BEHAVIOR_DONT_PROC_OTHER_ABILITIES`.
    marks:
    - gamefile:items/item_paintball#mechanics
  - text: The debuff is dispellable.
    marks:
    - gamefile:items/item_paintball#mechanics
  - text: Those marked for death by the fae shine brightly to all manner of creatures
      in the shadow realm.
    marks:
    - loc:DOTA_Tooltip_Ability_item_paintball_Lore
---

# Fae Grenade

Fae Grenade is an item with DPS, duration, and movement speed effects; its Shadow Brand active damages an enemy each second and provides vision. [gamefile:items/item_paintball#attribs] [loc:DOTA_Tooltip_Ability_item_paintball_Description]

## Stats

| Stat | Value |
|---|---:|
| DPS | 40 |
| Duration | 7 |
| Movement speed | 20 |

[gamefile:items/item_paintball#attribs]

| Active stat | Value |
|---|---:|
| Cast range | 900 |
| Mana cost | 25 |
| Cooldown | 20.0 |

[gamefile:items/item_paintball#mechanics]

## Mechanics

Shadow Brand throws a Mark toward an enemy within cast range, applying a debuff that deals damage every second and provides vision of the unit for its duration. [loc:DOTA_Tooltip_Ability_item_paintball_Description]

Its behavior is Unit Target and `DOTA_ABILITY_BEHAVIOR_DONT_PROC_OTHER_ABILITIES`. The debuff is dispellable. [gamefile:items/item_paintball#mechanics]

## Cost

| Item | Gold cost |
|---|---:|
| Fae Grenade | 0 gold |

[gamefile:items/item_paintball#cost]

*Those marked for death by the fae shine brightly to all manner of creatures in the shadow realm.* [loc:DOTA_Tooltip_Ability_item_paintball_Lore]