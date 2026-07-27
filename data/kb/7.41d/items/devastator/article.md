---
title: Parasma
kind: item
patch: 7.41d
card:
  entity: devastator
  sentences:
  - text: Parasma is a rare 5975-gold item granting 7 Armor, 40 Attack Speed, 40 Intelligence,
      1.5 Mana Regeneration, and 300 Projectile Speed, whose Witch Blade slows by
      25% and whose Magic Corruption reduces magic resistance by 20% for 4 seconds.
    marks:
    - gamefile:items/item_devastator#cost
    - gamefile:items/item_devastator#attribs
    - loc:DOTA_Tooltip_ability_item_devastator_Description
  - text: It is built from Witch Blade for 2775 gold, Mystic Staff for 2800 gold,
      and a Recipe for 400 gold.
    marks:
    - gamefile:items/item_devastator#components
  - text: Witch Blade causes the next attack to have true strike and apply a poison
      that deals intelligence-based damage every second.
    marks:
    - loc:DOTA_Tooltip_ability_item_devastator_Description
  - text: The INT DAMAGE MULTIPLIER is 0.75.
    marks:
    - gamefile:items/item_devastator#attribs
  - text: The SLOW DURATION is 4.
    marks:
    - gamefile:items/item_devastator#attribs
  - text: The statistics list PASSIVE COOLDOWN as 4.
    marks:
    - gamefile:items/item_devastator#attribs
  - text: The mechanics list its Behavior as Passive.
    marks:
    - gamefile:items/item_devastator#mechanics
  - text: The mechanics list its Cooldown as 7.
    marks:
    - gamefile:items/item_devastator#mechanics
  - text: Magic Corruption causes attacks to reduce the enemy’s Magic resistance.
    marks:
    - loc:DOTA_Tooltip_ability_item_devastator_Description
---

# Parasma

Parasma is a rare item that grants Armor, Attack Speed, Intelligence, Mana Regeneration, and Projectile Speed, and provides the Witch Blade and Magic Corruption passives. [gamefile:items/item_devastator#cost] [gamefile:items/item_devastator#attribs] [loc:DOTA_Tooltip_ability_item_devastator_Description]

## Components

| Component | Gold cost |
|---|---:|
| Witch Blade | 2775 gold |
| Mystic Staff | 2800 gold |
| Recipe | 400 gold |
| **Parasma** | **5975 gold** |

[gamefile:items/item_devastator#components] [gamefile:items/item_devastator#cost]

## Statistics

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
| Magic Corruption duration | 4 seconds |

[gamefile:items/item_devastator#attribs] [loc:DOTA_Tooltip_ability_item_devastator_Description]

## Mechanics

| Property | Value |
|---|---:|
| Behavior | Passive |
| Cooldown | 7 |

[gamefile:items/item_devastator#mechanics]

**Witch Blade** causes the next attack to have true strike and apply a poison that slows and deals damage based on intelligence every second. **Magic Corruption** causes attacks to reduce the enemy’s Magic resistance. [loc:DOTA_Tooltip_ability_item_devastator_Description]

*Warning: There is no antidote if picked up by the wrong end.* [loc:DOTA_Tooltip_ability_item_devastator_Lore]