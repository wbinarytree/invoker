---
title: Eul's Scepter of Divinity
kind: item
patch: 7.41d
card:
  entity: cyclone
  sentences:
  - text: Eul's Scepter of Divinity is a rare 2600-gold item granting 10 Intelligence,
      2.5 Mana Regeneration, and 20 Movement Speed, with Cyclone making an enemy or
      the wielder invulnerable for 2.5 seconds and dealing 50 magical damage to an
      enemy upon landing.
    marks:
    - gamefile:items/item_cyclone#cost
    - gamefile:items/item_cyclone#attribs
    - loc:DOTA_Tooltip_ability_item_cyclone_Description
  - text: Cyclone has Unit Target and DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK behavior.
    marks:
    - gamefile:items/item_cyclone#mechanics
  - text: Cyclone is dispellable.
    marks:
    - gamefile:items/item_cyclone#mechanics
  - text: Cyclone has 550 cast range.
    marks:
    - gamefile:items/item_cyclone#mechanics
  - text: Cyclone costs 175 mana.
    marks:
    - gamefile:items/item_cyclone#mechanics
  - text: Cyclone has a 23.0 cooldown.
    marks:
    - gamefile:items/item_cyclone#mechanics
  - text: Cyclone has a Basic Dispel type.
    marks:
    - loc:DOTA_Tooltip_ability_item_cyclone_Description
  - text: It is built from Staff of Wizardry (1000 gold), Void Stone (700 gold), Wind
      Lace (225 gold), and Recipe (675 gold), and builds into Wind Waker.
    marks:
    - gamefile:items/item_cyclone#components
  - text: A mysterious scepter passed down through the ages, its disruptive winds
      can be used for good or evil.
    marks:
    - loc:DOTA_Tooltip_ability_item_cyclone_Lore
---

# Eul's Scepter of Divinity

Eul's Scepter of Divinity is a rare item that provides Intelligence, Mana Regeneration, Movement Speed, and the Cyclone active. [gamefile:items/item_cyclone#cost] [gamefile:items/item_cyclone#attribs] [loc:DOTA_Tooltip_ability_item_cyclone_Description]

## Stats

| Stat | Value |
|---|---:|
| Cost | 2600 gold |

[gamefile:items/item_cyclone#cost]

| Stat | Value |
|---|---:|
| INTELLIGENCE | 10 |
| MANA REGENERATION | 2.5 |
| MOVEMENT SPEED | 20 |
| CYCLONE DURATION | 2.5 |
| TOOLTIP DROP DAMAGE | 50 |

[gamefile:items/item_cyclone#attribs]

## Components

| Component | Gold cost |
|---|---:|
| Staff of Wizardry | 1000 gold |
| Void Stone | 700 gold |
| Wind Lace | 225 gold |
| Recipe | 675 gold |

[gamefile:items/item_cyclone#components]

| Builds into | Gold cost |
|---|---:|
| Wind Waker | 6800 gold |

[gamefile:items/item_cyclone#components]

## Cyclone

| Property | Value |
|---|---|
| Behavior | Unit Target, DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK |
| Dispellable | Yes |
| Cast range | 550 |
| Mana cost | 175 |
| Cooldown | 23.0 |

[gamefile:items/item_cyclone#mechanics]

Cyclone can target an enemy unit or the wielder, sweeping the target into a cyclone and making it invulnerable. Enemy units take magical damage upon landing. It has a Basic Dispel type. [loc:DOTA_Tooltip_ability_item_cyclone_Description]

*A mysterious scepter passed down through the ages, its disruptive winds can be used for good or evil.* [loc:DOTA_Tooltip_ability_item_cyclone_Lore]