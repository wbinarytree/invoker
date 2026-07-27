---
title: Blink Dagger
kind: item
patch: 7.41d
card:
  entity: blink
  sentences:
  - text: Blink Dagger is a 2250-gold component item whose active Blink provides target-point
      teleportation with 1200 Blink Range, 960 Blink Range Clamp, and 3.0 Blink Damage
      Cooldown.
    marks:
    - gamefile:items/item_blink#cost
    - loc:DOTA_Tooltip_ability_item_blink_Description
    - gamefile:items/item_blink#attribs
  - text: Blink Dagger costs 2250 gold and builds into Arcane Blink, Overwhelming
      Blink, and Swift Blink.
    marks:
    - gamefile:items/item_blink#cost
    - gamefile:items/item_blink#components
  - text: Blink has Point Target, DOTA_ABILITY_BEHAVIOR_DIRECTIONAL, DOTA_ABILITY_BEHAVIOR_ROOT_DISABLES,
      and DOTA_ABILITY_BEHAVIOR_OVERSHOOT behavior.
    marks:
    - gamefile:items/item_blink#mechanics
  - text: Blink has 1200 cast range.
    marks:
    - gamefile:items/item_blink#mechanics
  - text: Blink has 0 mana cost.
    marks:
    - gamefile:items/item_blink#mechanics
  - text: Blink has a 15.0 cooldown.
    marks:
    - gamefile:items/item_blink#mechanics
  - text: Taking damage from an enemy hero or Roshan prevents Blink Dagger from being
      used during its 3.0 Blink Damage Cooldown.
    marks:
    - loc:DOTA_Tooltip_ability_item_blink_Description
    - gamefile:items/item_blink#attribs
---

# Blink Dagger

Blink Dagger is a component item with the active Blink, which provides target-point teleportation and has Blink Damage Cooldown, Blink Range, and Blink Range Clamp. [gamefile:items/item_blink#cost] [loc:DOTA_Tooltip_ability_item_blink_Description] [gamefile:items/item_blink#attribs]

## Build

| Role | Item | Gold cost |
|---|---|---:|
| Item | Blink Dagger | 2250 gold |
| Builds into | Arcane Blink | 6800 gold |
| Builds into | Overwhelming Blink | 6800 gold |
| Builds into | Swift Blink | 6800 gold |

[gamefile:items/item_blink#cost] [gamefile:items/item_blink#components]

## Stats

| Stat | Value |
|---|---:|
| Blink Damage Cooldown | 3.0 |
| Blink Range | 1200 |
| Blink Range Clamp | 960 |

[gamefile:items/item_blink#attribs]

| Ability property | Value |
|---|---|
| Behavior | Point Target, DOTA_ABILITY_BEHAVIOR_DIRECTIONAL, DOTA_ABILITY_BEHAVIOR_ROOT_DISABLES, DOTA_ABILITY_BEHAVIOR_OVERSHOOT |
| Cast range | 1200 |
| Mana cost | 0 |
| Cooldown | 15.0 |

[gamefile:items/item_blink#mechanics]

## Mechanics

Taking damage from an enemy hero or Roshan prevents Blink Dagger from being used during its Blink Damage Cooldown. [loc:DOTA_Tooltip_ability_item_blink_Description]

*The fabled dagger used by the fastest assassin ever to walk the lands.* [loc:DOTA_Tooltip_ability_item_blink_Lore]