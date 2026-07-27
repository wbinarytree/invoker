---
title: Harpoon
kind: item
patch: 7.41d
card:
  entity: harpoon
  sentences:
  - text: Harpoon is a 4700-gold item granting 10 Agility, 25 Damage, 10 Intelligence,
      2.0 Mana Regeneration, and 25 Strength; its 50-mana, 19.0-cooldown Draw Forth
      pulls the caster and an enemy closer together, while Echo Strike makes melee
      attacks attack twice in quick succession.
    marks:
    - gamefile:items/item_harpoon#cost
    - gamefile:items/item_harpoon#attribs
    - gamefile:items/item_harpoon#mechanics
    - loc:DOTA_Tooltip_Ability_item_harpoon_Description
  - text: 'Build formula: Echo Sabre (2700 gold) + Diadem (1000 gold) + Recipe (1000
      gold).'
    marks:
    - gamefile:items/item_harpoon#components
    - gamefile:items/item_harpoon#cost
  - text: Draw Forth targets an enemy and fires a harpoon that pulls the caster and
      target closer together.
    marks:
    - loc:DOTA_Tooltip_Ability_item_harpoon_Description
  - text: For a melee caster, Draw Forth always pulls the hero and target within melee
      distance of each other.
    marks:
    - loc:DOTA_Tooltip_Ability_item_harpoon_Description
  - text: Targeting a tree with Draw Forth instead pulls the caster all the way to
      it.
    marks:
    - loc:DOTA_Tooltip_Ability_item_harpoon_Description
  - text: Draw Forth has 700 cast range and 2000 projectile speed.
    marks:
    - gamefile:items/item_harpoon#attribs
    - gamefile:items/item_harpoon#mechanics
  - text: Its maximum distance is 1000 and minimum distance is 100.
    marks:
    - gamefile:items/item_harpoon#attribs
    - gamefile:items/item_harpoon#mechanics
  - text: Its pull distance percentage is 35% and pull duration is 0.3.
    marks:
    - gamefile:items/item_harpoon#attribs
    - gamefile:items/item_harpoon#mechanics
  - text: Its push length is 600.
    marks:
    - gamefile:items/item_harpoon#attribs
    - gamefile:items/item_harpoon#mechanics
  - text: Echo Strike's first strike applies a 100% movement slow for 1.0.
    marks:
    - gamefile:items/item_harpoon#attribs
    - gamefile:items/item_harpoon#mechanics
    - loc:DOTA_Tooltip_Ability_item_harpoon_Description
  - text: Echo Strike has a passive cooldown of 5.
    marks:
    - gamefile:items/item_harpoon#attribs
    - gamefile:items/item_harpoon#mechanics
---

# Harpoon

Harpoon is an item that grants Agility, Damage, Intelligence, Mana Regeneration, and Strength and provides the active Draw Forth and passive Echo Strike. [gamefile:items/item_harpoon#attribs] [loc:DOTA_Tooltip_Ability_item_harpoon_Description]

## Components

| Component | Gold cost |
|---|---:|
| Echo Sabre | 2700 |
| Diadem | 1000 |
| Recipe | 1000 |
| **Harpoon** | **4700** |

[gamefile:items/item_harpoon#components] [gamefile:items/item_harpoon#cost]

## Stats

| Stat | Value |
|---|---:|
| AGILITY | 10 |
| DAMAGE | 25 |
| INTELLIGENCE | 10 |
| MANA REGENERATION | 2.0 |
| STRENGTH | 25 |
| CAST RANGE ENEMY / Cast range | 700 |
| MAX DISTANCE | 1000 |
| MIN DISTANCE | 100 |
| MOVEMENT SLOW | 100% |
| PASSIVE COOLDOWN | 5 |
| PROJECTILE SPEED | 2000 |
| PULL DISTANCE PCT | 35% |
| PULL DURATION | 0.3 |
| PUSH LENGTH | 600 |
| SLOW DURATION | 1.0 |

[gamefile:items/item_harpoon#attribs] [gamefile:items/item_harpoon#mechanics]

| Active property | Value |
|---|---:|
| Behavior | Unit Target, DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK |
| Mana cost | 50 |
| Cooldown | 19.0 |

[gamefile:items/item_harpoon#mechanics]

## Mechanics

**Draw Forth** targets an enemy and fires a harpoon that pulls the caster and target closer together. For a melee caster, the hero and target are always pulled within melee distance of each other. Targeting a tree instead pulls the caster all the way to it. [loc:DOTA_Tooltip_Ability_item_harpoon_Description]

**Echo Strike** causes melee attacks to attack twice in quick succession, with the first strike applying the movement slow. [loc:DOTA_Tooltip_Ability_item_harpoon_Description]

*A perfect solution for the flight of foes.* [loc:DOTA_Tooltip_Ability_item_harpoon_Lore]