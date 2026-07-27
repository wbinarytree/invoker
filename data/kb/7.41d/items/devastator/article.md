---
title: Parasma
kind: item
patch: 7.41d
card:
  entity: devastator
  sentences:
  - text: Parasma is a rare 5975-gold item granting 7 Armor, 40 Attack Speed, 40 Intelligence,
      1.5 Mana Regeneration, and 300 Projectile Speed; every 4 seconds, Witch Blade
      gives the next attack true strike and a poison with a 25% slow for 4 seconds
      and a 0.75 Intelligence damage multiplier every second, while Magic Corruption
      reduces enemy Magic resistance by 20% for 4 seconds.
    marks:
    - gamefile:items/item_devastator#cost
    - gamefile:items/item_devastator#attribs
    - gamefile:items/item_devastator#mechanics
    - loc:DOTA_Tooltip_ability_item_devastator_Description
  - text: It is built from Witch Blade (2775 gold), Mystic Staff (2800 gold), and
      a Recipe (400 gold).
    marks:
    - gamefile:items/item_devastator#components
  - text: Witch Blade causes the next attack to have true strike and apply a poison
      that slows and deals damage based on the wielder’s Intelligence every second.
    marks:
    - loc:DOTA_Tooltip_ability_item_devastator_Description
  - text: Magic Corruption causes attacks to reduce the enemy’s Magic resistance for
      4 seconds.
    marks:
    - loc:DOTA_Tooltip_ability_item_devastator_Description
  - text: '“Warning: There is no antidote if picked up by the wrong end.”'
    marks:
    - loc:DOTA_Tooltip_ability_item_devastator_Lore
---

# Parasma

Parasma is a rare item that grants Armor, Attack Speed, Intelligence, Mana Regeneration, and Projectile Speed and has the passive effects Witch Blade—true strike, poison, slow, and Intelligence-based damage every second—and Magic Corruption—enemy Magic resistance reduction. [gamefile:items/item_devastator#cost] [gamefile:items/item_devastator#attribs] [gamefile:items/item_devastator#mechanics] [loc:DOTA_Tooltip_ability_item_devastator_Description]

## Cost

| Stat | Value |
|---|---:|
| Cost | 5975 gold |

[gamefile:items/item_devastator#cost]

## Stats

| Stat | Value |
|---|---:|
| ACTIVE MRES REDUCTION | 20% |
| ARMOR | 7 |
| ATTACK SPEED | 40 |
| INTELLIGENCE | 40 |
| MANA REGENERATION | 1.5 |
| INT DAMAGE MULTIPLIER | 0.75 |
| PASSIVE COOLDOWN | 4 |
| PROJECTILE SPEED | 300 |
| SLOW | 25% |
| SLOW DURATION | 4 |

[gamefile:items/item_devastator#attribs]

## Components

| Component | Gold cost |
|---|---:|
| Witch Blade | 2775 gold |
| Mystic Staff | 2800 gold |
| Recipe | 400 gold |

[gamefile:items/item_devastator#components]

## Mechanics

Witch Blade causes the next attack to have true strike and apply a poison that slows and deals damage based on the wielder’s Intelligence every second. Magic Corruption causes attacks to reduce the enemy’s Magic resistance; the reduction lasts 4 seconds. [loc:DOTA_Tooltip_ability_item_devastator_Description]

*Warning: There is no antidote if picked up by the wrong end.* [loc:DOTA_Tooltip_ability_item_devastator_Lore]