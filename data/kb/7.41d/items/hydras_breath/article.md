---
title: Hydra's Breath
kind: item
patch: 7.41d
card:
  entity: hydras_breath
  sentences:
  - text: Hydra's Breath is a rare 5900-gold item granting 30 Agility, 150 ranged-only
      Attack Range, and 15 Strength; Miasma deals Magical Damage equal to 2.5% of
      a target's Max HP per second for 3 seconds, while Polycephaly gives ranged attacks
      a 30% chance to fire 3 additional projectiles within a 120-degree forward angle
      and 150 bonus range.
    marks:
    - gamefile:items/item_hydras_breath#cost
    - gamefile:items/item_hydras_breath#attribs
    - loc:DOTA_Tooltip_Ability_item_hydras_breath_Description
  - text: Miasma has 0 Poison Base Damage.
    marks:
    - gamefile:items/item_hydras_breath#attribs
  - text: Polycephaly's additional projectiles have 20 Base Proc Damage and a 75%
      Proc Damage Percentage.
    marks:
    - gamefile:items/item_hydras_breath#attribs
    - loc:DOTA_Tooltip_Ability_item_hydras_breath_Description
  - text: The primary attack's modified normal-attack damage value is 100%.
    marks:
    - gamefile:items/item_hydras_breath#attribs
    - loc:DOTA_Tooltip_Ability_item_hydras_breath_Description
  - text: Additional projectiles do not trigger on-hit effects except Miasma.
    marks:
    - loc:DOTA_Tooltip_Ability_item_hydras_breath_Description
  - text: It is built from Specialist's Array (2550 gold), Dragon Lance (1900 gold),
      Orb of Venom (350 gold), and a Recipe (1100 gold).
    marks:
    - gamefile:items/item_hydras_breath#components
---

# Hydra's Breath

**Hydra's Breath** is a rare item that provides **Agility**, **Attack Range (Ranged Only)**, and **Strength**, and grants the passive effects **Miasma** and **Polycephaly**. [gamefile:items/item_hydras_breath#cost] [gamefile:items/item_hydras_breath#attribs] [loc:DOTA_Tooltip_Ability_item_hydras_breath_Description]

## Attributes

| Stat | Value |
|---|---:|
| AGILITY | 30 |
| ATTACK RANGE (RANGED ONLY) | 150 |
| BASE COUNT | 0 |
| BASE PROC DMG | 20 |
| COUNT | 3 |
| DAMAGE | 25 |
| POISON BASE DAMAGE | 0 |
| POISON DAMAGE PER SECOND | 2.5% |
| POISON DURATION | 3 |
| PROC CHANCE | 30% |
| PROC DMG PCT | 75% |
| PROC DMG PCT PRIMARY TOOLTIP | 100% |
| SECONDARY TARGET ANGLE | 120 |
| SECONDARY TARGET RANGE BONUS | 150 |
| STRENGTH | 15 |

[gamefile:items/item_hydras_breath#attribs]

## Mechanics

| Property | Value |
|---|---:|
| Behavior | Passive |
| Cast range | 0 |
| Mana cost | 0 |
| Cooldown | 0 |

[gamefile:items/item_hydras_breath#mechanics]

**Miasma** makes attacks poison enemies, dealing Magical Damage over time based on the target's Max HP. [loc:DOTA_Tooltip_Ability_item_hydras_breath_Description]

**Polycephaly** allows ranged attacks to sometimes fire additional projectiles at nearby enemies within a forward angle and with extra range. Additional projectiles deal modified normal-attack damage and do not trigger on-hit effects except Miasma; the primary attack has a separate modified normal-attack damage value. [loc:DOTA_Tooltip_Ability_item_hydras_breath_Description]

## Components

| Component | Gold cost |
|---|---:|
| Specialist's Array | 2550 gold |
| Dragon Lance | 1900 gold |
| Orb of Venom | 350 gold |
| Recipe | 1100 gold |
| **Total cost** | **5900 gold** |

[gamefile:items/item_hydras_breath#components] [gamefile:items/item_hydras_breath#cost]