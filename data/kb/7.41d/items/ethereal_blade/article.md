---
title: Ethereal Blade
kind: item
patch: 7.41d
card:
  entity: ethereal_blade
  sentences:
  - text: Ethereal Blade is an epic item costing 5200 gold that grants 24 All Attributes,
      24 Bonus Intellect, and 24 Bonus Strength and provides Ether Blast, which converts
      a target to ethereal form for 4.0 seconds.
    marks:
    - gamefile:items/item_ethereal_blade#cost
    - gamefile:items/item_ethereal_blade#attribs
    - loc:DOTA_Tooltip_ability_item_ethereal_blade_Description
  - text: In ethereal form, the target is immune to physical damage, cannot attack,
      and is more vulnerable to magic damage.
    marks:
    - loc:DOTA_Tooltip_ability_item_ethereal_blade_Description
  - text: Enemy targets receive -80% Blast Movement Slow.
    marks:
    - gamefile:items/item_ethereal_blade#attribs
    - loc:DOTA_Tooltip_ability_item_ethereal_blade_Description
  - text: Enemy targets take 50 base magical damage plus 1.0 times the sum of the
      caster’s attributes.
    marks:
    - gamefile:items/item_ethereal_blade#attribs
    - loc:DOTA_Tooltip_ability_item_ethereal_blade_Description
  - text: Ethereal Damage Bonus is -30%.
    marks:
    - gamefile:items/item_ethereal_blade#attribs
  - text: The build formula is Ultimate Orb for 2800 gold, Ghost Scepter for 1500
      gold, and a Recipe for 900 gold.
    marks:
    - gamefile:items/item_ethereal_blade#components
  - text: Ether Blast is Unit Target.
    marks:
    - gamefile:items/item_ethereal_blade#mechanics
  - text: Ether Blast is dispellable.
    marks:
    - gamefile:items/item_ethereal_blade#mechanics
  - text: Ether Blast has 800 cast range.
    marks:
    - gamefile:items/item_ethereal_blade#mechanics
  - text: Ether Blast costs 100 mana.
    marks:
    - gamefile:items/item_ethereal_blade#mechanics
  - text: Ether Blast has a 22.0 cooldown.
    marks:
    - gamefile:items/item_ethereal_blade#mechanics
  - text: A flickering blade of a ghastly nature, capable of dealing damage in both
      magical and physical planes.
    marks:
    - loc:DOTA_Tooltip_ability_item_ethereal_blade_Lore
---

# Ethereal Blade

Ethereal Blade is an epic item that grants All Attributes, Bonus Intellect, and Bonus Strength and provides the active ability Ether Blast. [gamefile:items/item_ethereal_blade#cost] [gamefile:items/item_ethereal_blade#attribs] [loc:DOTA_Tooltip_ability_item_ethereal_blade_Description]

## Stats

| Stat | Value |
|---|---:|
| Cost | 5200 gold |

[gamefile:items/item_ethereal_blade#cost]

| Stat | Value |
|---|---:|
| BLAST DAMAGE BASE | 50 |
| BLAST MOVEMENT SLOW | -80% |
| BLAST STAT MULTIPLIER | 1.0 |
| ALL ATTRIBUTES | 24 |
| BONUS INTELLECT | 24 |
| BONUS STRENGTH | 24 |
| DURATION | 4.0 |
| DURATION ALLY | 4.0 |
| ETHEREAL DAMAGE BONUS | -30% |
| PROJECTILE SPEED | 1400 |

[gamefile:items/item_ethereal_blade#attribs]

## Components

| Component | Gold cost |
|---|---:|
| Ultimate Orb | 2800 gold |
| Ghost Scepter | 1500 gold |
| Recipe | 900 gold |

[gamefile:items/item_ethereal_blade#components]

## Ether Blast

Ether Blast converts the target unit to ethereal form, making it immune to physical damage but unable to attack and more vulnerable to magic damage. Enemy targets are additionally slowed and take magical damage based on the sum of the caster’s attributes plus base damage. [loc:DOTA_Tooltip_ability_item_ethereal_blade_Description]

The ability is Unit Target, uses `DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK`, and is dispellable. [gamefile:items/item_ethereal_blade#mechanics]

| Mechanic | Value |
|---|---:|
| Cast range | 800 |
| Mana cost | 100 |
| Cooldown | 22.0 |

[gamefile:items/item_ethereal_blade#mechanics]

*A flickering blade of a ghastly nature, capable of dealing damage in both magical and physical planes.* [loc:DOTA_Tooltip_ability_item_ethereal_blade_Lore]