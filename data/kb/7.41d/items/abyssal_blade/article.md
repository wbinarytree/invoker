---
title: Abyssal Blade
kind: item
patch: 7.41d
card:
  entity: abyssal_blade
  sentences:
  - text: Abyssal Blade is an epic item costing 6250 gold that grants 35 Damage, 26
      Strength, 16% Health Restoration, and 30 Slow Resistance; its active Overwhelm
      costs 75 mana, has 35 Cooldown and 150 Cast range, and stuns a target enemy
      for 1.6 while piercing Debuff Immunity, while its passive Bash has a 25% melee
      or 10% ranged chance to stun for 1.2 and deal 120 bonus physical damage, with
      2.3 Cooldown.
    marks:
    - gamefile:items/item_abyssal_blade#cost
    - gamefile:items/item_abyssal_blade#attribs
    - gamefile:items/item_abyssal_blade#mechanics
    - loc:DOTA_Tooltip_ability_item_abyssal_blade_Description
  - text: Abyssal Blade is built from Skull Basher for 2875 gold, Sange for 2100 gold,
      and a Recipe costing 1275 gold.
    marks:
    - gamefile:items/item_abyssal_blade#components
  - text: Overwhelm has Unit Target behavior.
    marks:
    - gamefile:items/item_abyssal_blade#mechanics
  - text: Overwhelm is dispellable by Strong Dispels Only.
    marks:
    - gamefile:items/item_abyssal_blade#mechanics
  - text: Bash can trigger when melee or ranged heroes hit.
    marks:
    - loc:DOTA_Tooltip_ability_item_abyssal_blade_Description
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