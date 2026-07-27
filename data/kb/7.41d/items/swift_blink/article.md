---
title: Swift Blink
kind: item
patch: 7.41d
card:
  entity: swift_blink
  sentences:
  - text: Swift Blink is a 6800-gold component-quality item that grants 25 Agility;
      its active teleports up to 1200 range, then grants 40% phased movement speed
      and 35 bonus Agility for 6 seconds.
    marks:
    - gamefile:items/item_swift_blink#cost
    - gamefile:items/item_swift_blink#attribs
    - loc:DOTA_Tooltip_ability_item_swift_blink_Description
  - text: Swift Blink has a 960 blink range clamp.
    marks:
    - gamefile:items/item_swift_blink#attribs
  - text: Its active has a 15.0-second cooldown.
    marks:
    - gamefile:items/item_swift_blink#mechanics
  - text: Its active costs 0 mana.
    marks:
    - gamefile:items/item_swift_blink#mechanics
  - text: Damage from an enemy hero or Roshan prevents Swift Blink from being used
      for 3.0 seconds.
    marks:
    - gamefile:items/item_swift_blink#attribs
    - loc:DOTA_Tooltip_ability_item_swift_blink_Description
  - text: The build formula is Blink Dagger (2250 gold) + Eaglesong (2800 gold) +
      Recipe (1750 gold).
    marks:
    - gamefile:items/item_swift_blink#components
---

# Swift Blink

Swift Blink is a component-quality item that grants Agility and has the Swift Blink active, which teleports the user and grants phased movement speed and bonus Agility. [gamefile:items/item_swift_blink#cost] [gamefile:items/item_swift_blink#attribs] [loc:DOTA_Tooltip_ability_item_swift_blink_Description]

## Stats

| Stat | Value |
|---|---:|
| Blink damage cooldown | 3.0 |
| Blink range | 1200 |
| Blink range clamp | 960 |
| Bonus Agility active | 35 |
| Agility | 25 |
| Bonus movement | 40% |
| Duration | 6 |

[gamefile:items/item_swift_blink#attribs]

## Swift Blink

| Property | Value |
|---|---|
| Behavior | Point Target, DOTA_ABILITY_BEHAVIOR_DIRECTIONAL, DOTA_ABILITY_BEHAVIOR_ROOT_DISABLES, DOTA_ABILITY_BEHAVIOR_OVERSHOOT |
| Cast range | 1200 |
| Mana cost | 0 |
| Cooldown | 15.0 |

[gamefile:items/item_swift_blink#mechanics]

The active teleports the user to a target point. After teleportation, it grants phased movement speed and bonus Agility for a duration. Damage from an enemy hero or Roshan temporarily prevents Swift Blink from being used. [loc:DOTA_Tooltip_ability_item_swift_blink_Description]

## Components

| Component | Gold cost |
|---|---:|
| Blink Dagger | 2250 gold |
| Eaglesong | 2800 gold |
| Recipe | 1750 gold |
| **Swift Blink** | **6800 gold** |

[gamefile:items/item_swift_blink#components] [gamefile:items/item_swift_blink#cost]

*A cunning blade able to anticipate and enable its bearer's movements.* [loc:DOTA_Tooltip_ability_item_swift_blink_Lore]