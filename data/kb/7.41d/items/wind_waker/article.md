---
title: Wind Waker
kind: item
patch: 7.41d
card:
  entity: wind_waker
  sentences:
  - text: Wind Waker is a rare 6800-gold item granting 35 Intelligence, 3.0 Mana Regeneration,
      and 30 Movement Speed; its Cyclone active targets a unit at 550 range, costs
      175 mana, has a 19.0-second cooldown, and makes the target invulnerable for
      2.5 seconds.
    marks:
    - gamefile:items/item_wind_waker#cost
    - gamefile:items/item_wind_waker#attribs
    - gamefile:items/item_wind_waker#mechanics
    - loc:DOTA_Tooltip_ability_item_wind_waker_Description
  - text: It is built from Eul's Scepter of Divinity for 2600 gold, Mystic Staff for
      2800 gold, and a Recipe for 1400 gold.
    marks:
    - gamefile:items/item_wind_waker#components
  - text: Cyclone can target the caster, an allied unit, or an enemy unit.
    marks:
    - loc:DOTA_Tooltip_ability_item_wind_waker_Description
  - text: On self-cast, the tornado can be moved at 300 speed.
    marks:
    - gamefile:items/item_wind_waker#attribs
    - loc:DOTA_Tooltip_ability_item_wind_waker_Description
  - text: Enemy targets take 50 magical damage upon landing.
    marks:
    - gamefile:items/item_wind_waker#attribs
    - loc:DOTA_Tooltip_ability_item_wind_waker_Description
  - text: Cyclone's dispel type is Basic Dispel.
    marks:
    - loc:DOTA_Tooltip_ability_item_wind_waker_Description
  - text: Cyclone is dispellable.
    marks:
    - gamefile:items/item_wind_waker#mechanics
  - text: Cyclone has Unit Target and DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK behavior.
    marks:
    - gamefile:items/item_wind_waker#mechanics
  - text: Proof enough to some that unseen forces manipulate the happenings of the
      material plane.
    marks:
    - loc:DOTA_Tooltip_ability_item_wind_waker_Lore
---

# Wind Waker

Wind Waker is a rare item that grants Intelligence, Mana Regeneration, and Movement Speed and provides the Cyclone active ability. [gamefile:items/item_wind_waker#cost] [gamefile:items/item_wind_waker#attribs] [loc:DOTA_Tooltip_ability_item_wind_waker_Description]

## Stats

| Stat | Value |
|---|---:|
| Cost | 6800 gold |
| Intelligence | 35 |
| Mana Regeneration | 3.0 |
| Movement Speed | 30 |
| Cyclone Duration | 2.5 |
| Tooltip Drop Damage | 50 |
| Tornado Speed | 300 |

[gamefile:items/item_wind_waker#cost] [gamefile:items/item_wind_waker#attribs]

## Components

| Component | Gold cost |
|---|---:|
| Eul's Scepter of Divinity | 2600 gold |
| Mystic Staff | 2800 gold |
| Recipe | 1400 gold |

[gamefile:items/item_wind_waker#components]

## Cyclone

| Property | Value |
|---|---|
| Behavior | Unit Target, DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK |
| Dispellable | Yes |
| Cast range | 550 |
| Mana cost | 175 |
| Cooldown | 19.0 |

[gamefile:items/item_wind_waker#mechanics]

Cyclone can target the caster, an allied unit, or an enemy unit, making the target invulnerable. On self-cast, the tornado can be moved. Enemy targets take magical damage upon landing. Its dispel type is Basic Dispel. [loc:DOTA_Tooltip_ability_item_wind_waker_Description]

*Proof enough to some that unseen forces manipulate the happenings of the material plane.* [loc:DOTA_Tooltip_ability_item_wind_waker_Lore]