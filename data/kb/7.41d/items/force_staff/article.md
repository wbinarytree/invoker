---
title: Force Staff
kind: item
patch: 7.41d
card:
  entity: force_staff
  sentences:
  - text: Force Staff is a rare 2200-gold item that grants 175 Health and 10 Intelligence
      and provides Force, which pushes a target unit 600 units in its facing direction
      over 0.5 seconds.
    marks:
    - gamefile:items/item_force_staff#cost
    - gamefile:items/item_force_staff#attribs
    - gamefile:items/item_force_staff#mechanics
    - loc:DOTA_Tooltip_ability_item_force_staff_Description
  - text: Force has Unit Target behavior.
    marks:
    - gamefile:items/item_force_staff#mechanics
  - text: Force does not resume attacks.
    marks:
    - gamefile:items/item_force_staff#mechanics
  - text: Force has 550 cast range, 150 mana cost, and 19.0 cooldown.
    marks:
    - gamefile:items/item_force_staff#mechanics
  - text: Its Enemy Cast Range is 850.
    marks:
    - gamefile:items/item_force_staff#attribs
  - text: 'Build formula: Staff of Wizardry (1000 gold) + Fluffy Hat (250 gold) +
      Recipe (950 gold).'
    marks:
    - gamefile:items/item_force_staff#components
  - text: Force Staff builds into Hurricane Pike.
    marks:
    - gamefile:items/item_force_staff#components
---

# Force Staff

Force Staff is a rare item that grants Health and Intelligence and provides the active ability Force. [gamefile:items/item_force_staff#cost] [gamefile:items/item_force_staff#attribs] [loc:DOTA_Tooltip_ability_item_force_staff_Description]

## Stats

| Stat | Value |
|---|---:|
| Health | 175 |
| Intelligence | 10 |
| Enemy Cast Range | 850 |
| Push Length | 600 |
| Push Time | 0.5 |

[gamefile:items/item_force_staff#attribs]

| Ability stat | Value |
|---|---:|
| Cast range | 550 |
| Mana cost | 150 |
| Cooldown | 19.0 |

[gamefile:items/item_force_staff#mechanics]

## Components

| Type | Item | Gold cost |
|---|---|---:|
| Item cost | Force Staff | 2200 |
| Component | Staff of Wizardry | 1000 |
| Component | Fluffy Hat | 250 |
| Recipe | Recipe | 950 |
| Builds into | Hurricane Pike | 4450 |

[gamefile:items/item_force_staff#cost] [gamefile:items/item_force_staff#components]

## Force

Force has Unit Target behavior and does not resume attacks. It pushes any target unit in the direction it is facing. [gamefile:items/item_force_staff#mechanics] [loc:DOTA_Tooltip_ability_item_force_staff_Description]

*Allows you to manipulate others, for good or evil.* [loc:DOTA_Tooltip_ability_item_force_staff_Lore]