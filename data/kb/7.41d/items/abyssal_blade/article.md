---
title: Abyssal Blade
kind: item
patch: 7.41d
card:
  entity: abyssal_blade
  sentences:
  - text: Abyssal Blade is an epic item costing 6250 gold that grants 35 Damage, 26
      Strength, 16% Health Restoration, and 30 Slow Resistance, with active Overwhelm
      and passive Bash.
    marks:
    - gamefile:items/item_abyssal_blade#cost
    - gamefile:items/item_abyssal_blade#attribs
    - loc:DOTA_Tooltip_ability_item_abyssal_blade_Description
  - text: It is built from Skull Basher (2875 gold) and Sange (2100 gold), plus a
      Recipe (1275 gold).
    marks:
    - gamefile:items/item_abyssal_blade#components
    - gamefile:items/item_abyssal_blade#cost
  - text: Bash Chance is 25% for melee heroes and 10% for ranged heroes.
    marks:
    - gamefile:items/item_abyssal_blade#attribs
  - text: Bash has a 2.3 cooldown.
    marks:
    - gamefile:items/item_abyssal_blade#attribs
  - text: Bash can trigger when melee or ranged heroes hit, stunning the target for
      1.2 and dealing 120 bonus physical damage.
    marks:
    - gamefile:items/item_abyssal_blade#attribs
    - loc:DOTA_Tooltip_ability_item_abyssal_blade_Description
  - text: Overwhelm is Unit Target and has 150 cast range.
    marks:
    - gamefile:items/item_abyssal_blade#mechanics
  - text: Overwhelm has a 75 mana cost and a 35 cooldown.
    marks:
    - gamefile:items/item_abyssal_blade#mechanics
  - text: Overwhelm stuns a target enemy unit for 1.6 and pierces Debuff Immunity.
    marks:
    - gamefile:items/item_abyssal_blade#attribs
    - loc:DOTA_Tooltip_ability_item_abyssal_blade_Description
  - text: Overwhelm is dispellable by Strong Dispels Only.
    marks:
    - gamefile:items/item_abyssal_blade#mechanics
  - text: The lost blade of the Commander of the Abyss, this edge cuts into an enemy's
      soul.
    marks:
    - loc:DOTA_Tooltip_ability_item_abyssal_blade_Lore
---

# Abyssal Blade

Abyssal Blade is an epic item that grants Damage, Strength, Health Restoration, and Slow Resistance, with the active Overwhelm and passive Bash. [gamefile:items/item_abyssal_blade#cost] [gamefile:items/item_abyssal_blade#attribs] [loc:DOTA_Tooltip_ability_item_abyssal_blade_Description]

## Components

| Component | Gold cost |
|---|---:|
| Skull Basher | 2875 gold |
| Sange | 2100 gold |
| Recipe | 1275 gold |
| **Abyssal Blade** | **6250 gold** |

[gamefile:items/item_abyssal_blade#components] [gamefile:items/item_abyssal_blade#cost]

## Stats

| Stat | Value |
|---|---:|
| Bash Chance Melee | 25% |
| Bash Chance Ranged | 10% |
| Bash Cooldown | 2.3 |
| Bash Duration | 1.2 |
| Bonus Chance Damage | 120 |
| Damage | 35 |
| Strength | 26 |
| Health Restoration | 16% |
| Slow Resistance | 30 |
| Stun Duration | 1.6 |

[gamefile:items/item_abyssal_blade#attribs]

## Mechanics

| Property | Value |
|---|---:|
| Behavior | Unit Target |
| Dispellable | Strong Dispels Only |
| Cast range | 150 |
| Mana cost | 75 |
| Cooldown | 35 |

[gamefile:items/item_abyssal_blade#mechanics]

Overwhelm stuns a target enemy unit and pierces Debuff Immunity. Bash can trigger when melee or ranged heroes hit, stunning the target and dealing bonus physical damage. [loc:DOTA_Tooltip_ability_item_abyssal_blade_Description]

*The lost blade of the Commander of the Abyss, this edge cuts into an enemy's soul.* [loc:DOTA_Tooltip_ability_item_abyssal_blade_Lore]