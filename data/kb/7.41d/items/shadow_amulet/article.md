---
title: Shadow Amulet
kind: item
patch: 7.41d
card:
  entity: shadow_amulet
  sentences:
  - text: Shadow Amulet is a 900-gold item whose active Fade targets the caster or
      an allied hero at 600 range for 0 mana, with 1.25 Fade Time, 3.5 Fade Duration,
      35% Movement Speed Reduction during invisibility, and an 18.0-second cooldown.
    marks:
    - gamefile:items/item_shadow_amulet#cost
    - loc:DOTA_Tooltip_ability_item_shadow_amulet_Description
    - gamefile:items/item_shadow_amulet#attribs
    - gamefile:items/item_shadow_amulet#mechanics
  - text: The build formula is Shadow Amulet (900 gold), and it builds into Glimmer
      Cape and Shadow Blade.
    marks:
    - gamefile:items/item_shadow_amulet#cost
    - gamefile:items/item_shadow_amulet#components
  - text: Fade is immediate and unit-targeted.
    marks:
    - gamefile:items/item_shadow_amulet#mechanics
  - text: Fade has DOTA_ABILITY_BEHAVIOR_IGNORE_CHANNEL and DOTA_ABILITY_BEHAVIOR_DONT_RESUME_MOVEMENT.
    marks:
    - gamefile:items/item_shadow_amulet#mechanics
  - text: Fade is dispellable.
    marks:
    - gamefile:items/item_shadow_amulet#mechanics
---

# Shadow Amulet

Shadow Amulet is an item with the active ability Fade, which grants invisibility to the caster or a target allied hero and applies Movement Speed Reduction during invisibility. [gamefile:items/item_shadow_amulet#cost] [loc:DOTA_Tooltip_ability_item_shadow_amulet_Description]

## Stats

| Stat | Value |
|---|---:|
| Fade Duration | 3.5 |
| Fade Time | 1.25 |
| Movement Speed Reduction | 35% |

[gamefile:items/item_shadow_amulet#attribs]

| Cast stat | Value |
|---|---:|
| Cast range | 600 |
| Mana cost | 0 |
| Cooldown | 18.0 |

[gamefile:items/item_shadow_amulet#mechanics]

## Components

| Item | Gold cost |
|---|---:|
| Shadow Amulet | 900 gold |

[gamefile:items/item_shadow_amulet#cost]

**Builds into:**

| Item | Gold cost |
|---|---:|
| Glimmer Cape | 2150 gold |
| Shadow Blade | 3250 gold |

[gamefile:items/item_shadow_amulet#components]

## Mechanics

Fade is immediate and unit-targeted, has `DOTA_ABILITY_BEHAVIOR_IGNORE_CHANNEL` and `DOTA_ABILITY_BEHAVIOR_DONT_RESUME_MOVEMENT`, and is dispellable. [gamefile:items/item_shadow_amulet#mechanics]

*A small talisman that clouds the senses of one's enemies when held perfectly still.* [loc:DOTA_Tooltip_ability_item_shadow_amulet_Lore]