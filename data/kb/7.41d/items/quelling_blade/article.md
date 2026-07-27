---
title: Quelling Blade
kind: item
patch: 7.41d
card:
  entity: quelling_blade
  sentences:
  - text: Quelling Blade is a 100-gold component item whose Chop Tree active destroys
      a target tree and whose Quell passive grants 8 melee or 4 ranged attack damage
      against non-hero units.
    marks:
    - gamefile:items/item_quelling_blade#cost
    - gamefile:items/item_quelling_blade#attribs
    - loc:DOTA_Tooltip_ability_item_quelling_blade_Description
  - text: Its build formula is Quelling Blade (100 gold).
    marks:
    - gamefile:items/item_quelling_blade#cost
    - gamefile:items/item_quelling_blade#components
  - text: It builds into Battle Fury and Iron Talon.
    marks:
    - gamefile:items/item_quelling_blade#components
  - text: Quelling Range Tooltip is 350.
    marks:
    - gamefile:items/item_quelling_blade#attribs
  - text: Chop Tree has Unit Target behavior.
    marks:
    - gamefile:items/item_quelling_blade#mechanics
  - text: Its cast range is 350.
    marks:
    - gamefile:items/item_quelling_blade#mechanics
  - text: Its mana cost is 0.
    marks:
    - gamefile:items/item_quelling_blade#mechanics
  - text: Its cooldown is 4.0.
    marks:
    - gamefile:items/item_quelling_blade#mechanics
---

# Quelling Blade

Quelling Blade is a component item with the Chop Tree active and Quell passive, which provides Damage Bonus and Damage Bonus Ranged. [gamefile:items/item_quelling_blade#cost] [gamefile:items/item_quelling_blade#attribs] [loc:DOTA_Tooltip_ability_item_quelling_blade_Description]

## Components

| Relation | Item | Gold cost |
|---|---|---:|
| Item | Quelling Blade | 100 |
| Builds into | Battle Fury | 3900 |
| Builds into | Iron Talon | 0 |

[gamefile:items/item_quelling_blade#cost] [gamefile:items/item_quelling_blade#components]

## Stats

| Stat | Value |
|---|---:|
| Damage Bonus | 8 |
| Damage Bonus Ranged | 4 |
| Quelling Range Tooltip | 350 |

[gamefile:items/item_quelling_blade#attribs]

## Mechanics

| Property | Value |
|---|---:|
| Behavior | Unit Target |
| Cast range | 350 |
| Mana cost | 0 |
| Cooldown | 4.0 |

[gamefile:items/item_quelling_blade#mechanics]

Chop Tree destroys a target tree. Quell increases attack damage against non-hero units, with separate bonuses for melee and ranged heroes. [loc:DOTA_Tooltip_ability_item_quelling_blade_Description]

*The axe of a fallen gnome, it allows you to effectively maneuver the forest.* [loc:DOTA_Tooltip_ability_item_quelling_blade_Lore]