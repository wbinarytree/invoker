---
title: Ghost Scepter
kind: item
patch: 7.41d
card:
  entity: ghost
  sentences:
  - text: Ghost Scepter is a 1500 gold component item that grants 5 ALL ATTRIBUTES
      and provides Ghost Form for a DURATION of 4.0, granting physical damage immunity,
      preventing attacks, and increasing magic damage vulnerability with -30% EXTRA
      SPELL DAMAGE PERCENT.
    marks:
    - gamefile:items/item_ghost#cost
    - gamefile:items/item_ghost#attribs
    - loc:DOTA_Tooltip_ability_item_ghost_Description
  - text: Ghost Form has No Target, Immediate behavior.
    marks:
    - gamefile:items/item_ghost#mechanics
  - text: Ghost Form is dispellable.
    marks:
    - gamefile:items/item_ghost#mechanics
  - text: Ghost Form has a 22.0 cooldown.
    marks:
    - gamefile:items/item_ghost#mechanics
  - text: The build formula is Ghost Scepter (1500 gold), and it builds into Crella's
      Crozier and Ethereal Blade.
    marks:
    - gamefile:items/item_ghost#cost
    - gamefile:items/item_ghost#components
---

# Ghost Scepter

Ghost Scepter is a component item that grants ALL ATTRIBUTES and provides Ghost Form, which grants physical damage immunity, prevents attacking, and increases magic damage vulnerability. [gamefile:items/item_ghost#cost] [gamefile:items/item_ghost#attribs] [loc:DOTA_Tooltip_ability_item_ghost_Description]

## Stats

| Stat | Value |
|---|---:|
| ALL ATTRIBUTES | 5 |
| DURATION | 4.0 |
| EXTRA SPELL DAMAGE PERCENT | -30% |

[gamefile:items/item_ghost#attribs]

## Ghost Form

| Property | Value |
|---|---|
| Behavior | No Target, Immediate |
| Dispellable | Yes |
| Cooldown | 22.0 |

[gamefile:items/item_ghost#mechanics]

Ghost Form makes the user immune to physical damage and unable to attack while increasing their vulnerability to magic damage. [loc:DOTA_Tooltip_ability_item_ghost_Description]

## Components

| Item | Gold cost |
|---|---:|
| Ghost Scepter | 1500 gold |

[gamefile:items/item_ghost#cost]

**Builds into:**

| Item | Gold cost |
|---|---:|
| Crella's Crozier | 4800 gold |
| Ethereal Blade | 5200 gold |

[gamefile:items/item_ghost#components]

*Imbues the wielder with a ghostly presence, allowing them to evade physical damage.* [loc:DOTA_Tooltip_ability_item_ghost_Lore]