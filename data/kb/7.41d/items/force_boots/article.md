---
title: Force Boots
kind: item
patch: 7.41d
card:
  entity: force_boots
  sentences:
  - text: Force Boots is a 0-gold item that grants 115 Movement Speed and 30 Health
      Regeneration, provides Force to push a target 750 units over 0.5 seconds, and
      provides Speed Unlock to remove the wearer's speed limit.
    marks:
    - gamefile:items/item_force_boots#cost
    - gamefile:items/item_force_boots#attribs
    - loc:DOTA_Tooltip_ability_item_force_boots_Description
  - text: Force has Unit Target behavior and DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK.
    marks:
    - gamefile:items/item_force_boots#mechanics
  - text: Force has 750 cast range.
    marks:
    - gamefile:items/item_force_boots#mechanics
  - text: Force costs 75 mana.
    marks:
    - gamefile:items/item_force_boots#mechanics
  - text: Force has an 8.0-second cooldown.
    marks:
    - gamefile:items/item_force_boots#mechanics
  - text: Force pushes the target in the direction they are facing.
    marks:
    - loc:DOTA_Tooltip_ability_item_force_boots_Description
  - text: Force applies a Basic Dispel when cast on an ally.
    marks:
    - loc:DOTA_Tooltip_ability_item_force_boots_Description
  - text: Movement Speed bonuses from multiple pairs of boots do not stack.
    marks:
    - loc:DOTA_Tooltip_ability_item_force_boots_Description
  - text: Its build formula is Force Boots (0 gold).
    marks:
    - gamefile:items/item_force_boots#cost
---

# Force Boots

Force Boots is an item that grants Movement Speed and Health Regeneration and provides the active Force and passive Speed Unlock. [gamefile:items/item_force_boots#cost] [gamefile:items/item_force_boots#attribs] [loc:DOTA_Tooltip_ability_item_force_boots_Description]

## Stats

| Stat | Value |
|---|---:|
| MOVEMENT SPEED | 115 |
| HEALTH REGENERATION | 30 |
| PUSH DURATION | 0.5 |
| PUSH LENGTH | 750 |

[gamefile:items/item_force_boots#attribs]

## Force

| Property | Value |
|---|---:|
| Behavior | Unit Target, DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK |
| Cast range | 750 |
| Mana cost | 75 |
| Cooldown | 8.0 |

[gamefile:items/item_force_boots#mechanics]

Force pushes the target in the direction they are facing. When cast on an ally, it applies a Basic Dispel. [loc:DOTA_Tooltip_ability_item_force_boots_Description]

## Speed Unlock

Speed Unlock completely removes the wearer's speed limit. Movement Speed bonuses from multiple pairs of boots do not stack. [loc:DOTA_Tooltip_ability_item_force_boots_Description]

## Components

| Item | Gold cost |
|---|---:|
| Force Boots | 0 gold |

[gamefile:items/item_force_boots#cost]

*Elusive marvels never successfully studied for proper classification in the archives.* [loc:DOTA_Tooltip_ability_item_force_boots_Lore]