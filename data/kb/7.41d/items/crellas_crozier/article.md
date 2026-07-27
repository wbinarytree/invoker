---
title: Crella's Crozier
kind: item
patch: 7.41d
card:
  entity: crellas_crozier
  sentences:
  - text: Crella's Crozier is an epic 4800-gold item granting 6 All Attributes, 450
      Health, and 450 Mana; Rite of Rumusque grants 4.0 seconds of ghost form and
      75% Active Health Steal, while Putrefaction Aura provides 30% Health Steal within
      900.
    marks:
    - gamefile:items/item_crellas_crozier#cost
    - gamefile:items/item_crellas_crozier#attribs
    - loc:DOTA_Tooltip_ability_item_crellas_crozier_Description
  - text: Ghost Scepter (1500 gold) + Soul Booster (3000 gold) + Recipe (300 gold)
      builds Crella's Crozier.
    marks:
    - gamefile:items/item_crellas_crozier#components
  - text: Rite of Rumusque is an immediate, no-target active with a 20.0 cooldown.
    marks:
    - gamefile:items/item_crellas_crozier#mechanics
  - text: Rite of Rumusque is dispellable.
    marks:
    - gamefile:items/item_crellas_crozier#mechanics
  - text: Ghost form grants physical-damage immunity, prevents attacks, and increases
      vulnerability to magic damage with -30% Extra Spell Damage Percent.
    marks:
    - loc:DOTA_Tooltip_ability_item_crellas_crozier_Description
    - gamefile:items/item_crellas_crozier#attribs
  - text: Every 1.0 seconds, Rite of Rumusque steals 6% movement speed from enemy
      heroes within 900, with each steal lasting 1.5.
    marks:
    - loc:DOTA_Tooltip_ability_item_crellas_crozier_Description
    - gamefile:items/item_crellas_crozier#attribs
  - text: During Rite of Rumusque, Putrefaction Aura redirects all lost Health Restoration
      to the user every 1.0 seconds.
    marks:
    - loc:DOTA_Tooltip_ability_item_crellas_crozier_Description
    - gamefile:items/item_crellas_crozier#attribs
  - text: Putrefaction Aura passively reduces the Health Restoration of enemy heroes
      within 900 according to its 30% Health Steal.
    marks:
    - loc:DOTA_Tooltip_ability_item_crellas_crozier_Description
    - gamefile:items/item_crellas_crozier#attribs
---

# Crella's Crozier

Crella's Crozier is an epic item that grants All Attributes, Health, and Mana and provides Rite of Rumusque and Putrefaction Aura. [gamefile:items/item_crellas_crozier#cost] [gamefile:items/item_crellas_crozier#attribs] [loc:DOTA_Tooltip_ability_item_crellas_crozier_Description]

## Components

| Component | Gold cost |
|---|---:|
| Ghost Scepter | 1500 gold |
| Soul Booster | 3000 gold |
| Recipe | 300 gold |
| **Crella's Crozier** | **4800 gold** |

[gamefile:items/item_crellas_crozier#components] [gamefile:items/item_crellas_crozier#cost]

## Stats

| Stat | Value |
|---|---:|
| Active Health Steal | 75% |
| Active Radius | 900 |
| All Attributes | 6 |
| Health | 450 |
| Mana | 450 |
| Duration | 4.0 |
| Extra Spell Damage Percent | -30% |
| Health Steal | 30% |
| Interval | 1.0 |
| Movespeed Steal Pct | 6% |
| Radius | 900 |
| Stack Duration | 1.5 |

[gamefile:items/item_crellas_crozier#attribs]

| Mechanic | Value |
|---|---|
| Behavior | No Target, Immediate |
| Dispellable | Yes |
| Cooldown | 20.0 |

[gamefile:items/item_crellas_crozier#mechanics]

## Abilities

**Rite of Rumusque** is an immediate, no-target active and is dispellable. [gamefile:items/item_crellas_crozier#mechanics] It places the user in ghost form for the listed Duration, granting immunity to physical damage while preventing attacks and increasing vulnerability to magic damage. It steals movement speed from enemy heroes within the Active Radius at each Interval, with each steal lasting for the Stack Duration. During the active, Putrefaction Aura uses Active Health Steal, and all lost Health Restoration is redirected to the user at each Interval. [loc:DOTA_Tooltip_ability_item_crellas_crozier_Description] [gamefile:items/item_crellas_crozier#attribs]

**Putrefaction Aura** is passive and reduces the Health Restoration of enemy heroes within its Radius according to Health Steal. [loc:DOTA_Tooltip_ability_item_crellas_crozier_Description] [gamefile:items/item_crellas_crozier#attribs]