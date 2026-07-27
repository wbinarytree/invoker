---
title: Orb of Venom
kind: item
patch: 7.41d
card:
  entity: orb_of_venom
  sentences:
  - text: Orb of Venom is a 350 gold component item whose passive Poison Attack deals
      10 magical damage per second for 3.0 seconds at 1.0-second tick intervals.
    marks:
    - gamefile:items/item_orb_of_venom#cost
    - gamefile:items/item_orb_of_venom#attribs
    - loc:DOTA_Tooltip_ability_item_orb_of_venom_Description
  - text: Poison Attack has a 9.0-second cooldown.
    marks:
    - gamefile:items/item_orb_of_venom#mechanics
  - text: Poison Attack has the `DOTA_ABILITY_BEHAVIOR_DONT_PROC_OTHER_ABILITIES`
      behavior.
    marks:
    - gamefile:items/item_orb_of_venom#mechanics
  - text: Poison Attack is dispellable.
    marks:
    - gamefile:items/item_orb_of_venom#mechanics
  - text: 'Build formula: Orb of Venom (350 gold).'
    marks:
    - gamefile:items/item_orb_of_venom#cost
  - text: Orb of Venom builds into Hydra's Breath, Mage Slayer, and Witch Blade.
    marks:
    - gamefile:items/item_orb_of_venom#components
---

# Orb of Venom

Orb of Venom is a component item whose Poison Attack deals magical Damage and has Poison Duration and Tick Interval. [gamefile:items/item_orb_of_venom#cost] [gamefile:items/item_orb_of_venom#attribs] [loc:DOTA_Tooltip_ability_item_orb_of_venom_Description]

## Stats

| Stat | Value |
|---|---:|
| Damage | 10 |
| Poison Duration | 3.0 |
| Tick Interval | 1.0 |

[gamefile:items/item_orb_of_venom#attribs]

## Mechanics

Poison Attack is passive: it poisons the target and deals magical damage per second. [loc:DOTA_Tooltip_ability_item_orb_of_venom_Description]

It has the `DOTA_ABILITY_BEHAVIOR_DONT_PROC_OTHER_ABILITIES` behavior and is dispellable. [gamefile:items/item_orb_of_venom#mechanics]

| Stat | Value |
|---|---:|
| Cooldown | 9.0 |

[gamefile:items/item_orb_of_venom#mechanics]

## Components

| Item | Gold cost |
|---|---:|
| Orb of Venom | 350 gold |

[gamefile:items/item_orb_of_venom#cost]

**Builds into:**

| Item | Gold cost |
|---|---:|
| Hydra's Breath | 5900 gold |
| Mage Slayer | 3100 gold |
| Witch Blade | 2775 gold |

[gamefile:items/item_orb_of_venom#components]

*Envenoms your veapon with the venom of a venomous viper.* [loc:DOTA_Tooltip_ability_item_orb_of_venom_Lore]