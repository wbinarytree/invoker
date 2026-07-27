---
title: Bottle
kind: item
patch: 7.41d
card:
  entity: bottle
  sentences:
  - text: Bottle is a common item costing 675 gold whose Regenerate consumes a charge
      from a maximum of 3 to restore 110 Health and 60 Mana over 2.7 seconds, and
      whose Store Rune stores a Rune for 90.0 seconds.
    marks:
    - gamefile:items/item_bottle#cost
    - gamefile:items/item_bottle#attribs
    - loc:DOTA_Tooltip_ability_item_bottle_Description
  - text: Bottle's build formula is Bottle (675 gold).
    marks:
    - gamefile:items/item_bottle#cost
  - text: Its cast range is 350.
    marks:
    - gamefile:items/item_bottle#mechanics
  - text: Its cooldown is 0.5.
    marks:
    - gamefile:items/item_bottle#mechanics
  - text: Regenerate ends if the affected hero is attacked by an enemy hero or Roshan.
    marks:
    - loc:DOTA_Tooltip_ability_item_bottle_Description
  - text: Bottle refills automatically at the fountain.
    marks:
    - loc:DOTA_Tooltip_ability_item_bottle_Description
  - text: Holding Control uses Bottle on an allied hero.
    marks:
    - loc:DOTA_Tooltip_ability_item_bottle_Description
  - text: Its behaviors are Immediate, No Target, optional unit target, and suppress
      associated consumable.
    marks:
    - gamefile:items/item_bottle#mechanics
  - text: Runes can be stored for later use by right-clicking them.
    marks:
    - loc:DOTA_Tooltip_ability_item_bottle_Description
  - text: Unused stored Runes activate automatically when their storage time expires.
    marks:
    - loc:DOTA_Tooltip_ability_item_bottle_Description
  - text: Using a stored Rune fully refills Bottle.
    marks:
    - loc:DOTA_Tooltip_ability_item_bottle_Description
  - text: An old bottle that survived the ages, the contents placed inside become
      enchanted.
    marks:
    - loc:DOTA_Tooltip_ability_item_bottle_Lore
---

# Bottle

Bottle is a common item whose active Regenerate restores Health and Mana and whose passive Store Rune stores Runes. [gamefile:items/item_bottle#cost] [loc:DOTA_Tooltip_ability_item_bottle_Description]

## Components

| Item | Cost |
|---|---:|
| Bottle | 675 gold |

[gamefile:items/item_bottle#cost]

## Stats

| Stat | Value |
|---|---:|
| Break on Hero Damage | 1 |
| Health Restore | 110 |
| Health Restore Pct | 0 |
| Mana Restore | 60 |
| Mana Restore Pct | 0 |
| Max Charges | 3 |
| Restore Time | 2.7 |
| Rune Expire Time | 90.0 |

[gamefile:items/item_bottle#attribs]

| Cast property | Value |
|---|---:|
| Cast Range | 350 |
| Cooldown | 0.5 |

[gamefile:items/item_bottle#mechanics]

## Mechanics

Regenerate consumes a charge to restore Health and Mana over time. The effect is lost if the affected hero is attacked by an enemy hero or Roshan. Bottle refills automatically at the fountain, and holding Control uses it on an allied hero. [loc:DOTA_Tooltip_ability_item_bottle_Description]

Its behaviors are Immediate, No Target, optional unit target, and suppress associated consumable. [gamefile:items/item_bottle#mechanics]

Runes can be stored for later use by right-clicking them. Unused stored Runes activate automatically when their storage time expires, while using a stored Rune fully refills Bottle. [loc:DOTA_Tooltip_ability_item_bottle_Description]

*An old bottle that survived the ages, the contents placed inside become enchanted.* [loc:DOTA_Tooltip_ability_item_bottle_Lore]