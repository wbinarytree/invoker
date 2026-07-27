---
title: Shiva's Guard
kind: item
patch: 7.41d
card:
  entity: shivas_guard
  sentences:
  - text: Shiva's Guard is a 4500-gold epic item that provides 17 Armor and 0 Health
      Regeneration, grants Arctic Blast for 260 magical damage and -40% movement speed
      with a 4.0 debuff duration in an 825 radius, and grants Freezing Aura for -40
      attack speed in a 1200 radius.
    marks:
    - gamefile:items/item_shivas_guard#cost
    - gamefile:items/item_shivas_guard#attribs
    - loc:DOTA_Tooltip_ability_item_shivas_guard_Description
  - text: It is built from Platemail (1400 gold), Splintmail (950 gold), Chasm Stone
      (800 gold), and a Recipe (1350 gold).
    marks:
    - gamefile:items/item_shivas_guard#components
    - gamefile:items/item_shivas_guard#cost
  - text: Arctic Blast has Immediate, No Target, and DOTA_ABILITY_BEHAVIOR_IGNORE_CHANNEL
      behavior.
    marks:
    - gamefile:items/item_shivas_guard#mechanics
  - text: Arctic Blast costs 75 mana.
    marks:
    - gamefile:items/item_shivas_guard#mechanics
  - text: Arctic Blast has a 27 cooldown.
    marks:
    - gamefile:items/item_shivas_guard#mechanics
  - text: Arctic Blast is dispellable.
    marks:
    - gamefile:items/item_shivas_guard#mechanics
  - text: The freezing wave has 400 Blast Speed.
    marks:
    - gamefile:items/item_shivas_guard#attribs
  - text: Its Area of Effect is 75.
    marks:
    - gamefile:items/item_shivas_guard#attribs
---

# Shiva's Guard

Shiva's Guard is an epic item that provides Armor and Health Regeneration and grants Arctic Blast and Freezing Aura. [gamefile:items/item_shivas_guard#cost] [gamefile:items/item_shivas_guard#attribs] [loc:DOTA_Tooltip_ability_item_shivas_guard_Description]

## Components

| Part | Gold cost |
|---|---:|
| Platemail | 1400 gold |
| Splintmail | 950 gold |
| Chasm Stone | 800 gold |
| Recipe | 1350 gold |
| **Shiva's Guard** | **4500 gold** |

[gamefile:items/item_shivas_guard#components] [gamefile:items/item_shivas_guard#cost]

## Stats

| Stat | Value |
|---|---:|
| Aura Attack Speed | -40 |
| Aura Radius | 1200 |
| Blast Damage | 260 |
| Blast Debuff Duration | 4.0 |
| Blast Movement Speed | -40% |
| Blast Radius | 825 |
| Blast Speed | 400 |
| Area of Effect | 75 |
| Armor | 17 |
| Health Regeneration | 0 |

[gamefile:items/item_shivas_guard#attribs]

## Mechanics

| Property | Value |
|---|---|
| Behavior | Immediate, No Target, DOTA_ABILITY_BEHAVIOR_IGNORE_CHANNEL |
| Dispellable | Yes |
| Mana cost | 75 |
| Cooldown | 27 |

[gamefile:items/item_shivas_guard#mechanics]

Arctic Blast emits a freezing wave that deals magical damage to enemies and slows their movement. Freezing Aura reduces the attack speed of all enemies. [loc:DOTA_Tooltip_ability_item_shivas_guard_Description]

*Said to have belonged to a goddess, today it retains much of its former power.* [loc:DOTA_Tooltip_ability_item_shivas_guard_Lore]