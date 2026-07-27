---
title: Crella's Crozier
kind: item
patch: 7.41d
card:
  entity: crellas_crozier
  sentences:
  - text: Crella's Crozier is an epic 4800-gold item granting 6 All Attributes, 450
      Health, and 450 Mana; its 4.0-duration Rite of Rumusque grants ghost form and
      increases Putrefaction Aura's reduction of enemy Health Restoration from 30%
      to 75% in a 900 radius.
    marks:
    - gamefile:items/item_crellas_crozier#cost
    - gamefile:items/item_crellas_crozier#attribs
    - loc:DOTA_Tooltip_ability_item_crellas_crozier_Description
  - text: 'Build formula: Ghost Scepter (1500 gold) + Soul Booster (3000 gold) + Recipe
      (300 gold).'
    marks:
    - gamefile:items/item_crellas_crozier#components
  - text: Rite of Rumusque has No Target, Immediate behavior.
    marks:
    - gamefile:items/item_crellas_crozier#mechanics
  - text: Rite of Rumusque has a 20.0 cooldown.
    marks:
    - gamefile:items/item_crellas_crozier#mechanics
  - text: Rite of Rumusque is dispellable.
    marks:
    - gamefile:items/item_crellas_crozier#mechanics
  - text: Rite of Rumusque's ghost form grants immunity to physical damage.
    marks:
    - loc:DOTA_Tooltip_ability_item_crellas_crozier_Description
  - text: The ghost form prevents the user from attacking.
    marks:
    - loc:DOTA_Tooltip_ability_item_crellas_crozier_Description
  - text: While in ghost form, Extra Spell Damage Percent is -30%.
    marks:
    - gamefile:items/item_crellas_crozier#attribs
    - loc:DOTA_Tooltip_ability_item_crellas_crozier_Description
  - text: Rite of Rumusque steals 6% movement speed from enemy heroes every 1.0 within
      a 900 radius, with each stack lasting 1.5.
    marks:
    - gamefile:items/item_crellas_crozier#attribs
    - loc:DOTA_Tooltip_ability_item_crellas_crozier_Description
  - text: While Rite of Rumusque is active, all lost Health Restoration is redirected
      to the user.
    marks:
    - loc:DOTA_Tooltip_ability_item_crellas_crozier_Description
---

# Crella's Crozier

Crella's Crozier is an epic item that grants All Attributes, Health, and Mana and provides Rite of Rumusque and Putrefaction Aura. [gamefile:items/item_crellas_crozier#cost] [gamefile:items/item_crellas_crozier#attribs] [loc:DOTA_Tooltip_ability_item_crellas_crozier_Description]

## Components

| Entry | Cost |
|---|---:|
| Ghost Scepter | 1500 gold |
| Soul Booster | 3000 gold |
| Recipe | 300 gold |
| Crella's Crozier | 4800 gold |

[gamefile:items/item_crellas_crozier#components] [gamefile:items/item_crellas_crozier#cost]

## Stats

| Stat | Value |
|---|---:|
| ACTIVE HEALTH STEAL | 75% |
| ACTIVE RADIUS | 900 |
| ALL ATTRIBUTES | 6 |
| HEALTH | 450 |
| MANA | 450 |
| DURATION | 4.0 |
| EXTRA SPELL DAMAGE PERCENT | -30% |
| HEALTH STEAL | 30% |
| INTERVAL | 1.0 |
| MOVESPEED STEAL PCT | 6% |
| RADIUS | 900 |
| STACK DURATION | 1.5 |

[gamefile:items/item_crellas_crozier#attribs]

| Mechanic | Value |
|---|---:|
| Behavior | No Target, Immediate |
| Dispellable | Yes |
| Cooldown | 20.0 |

[gamefile:items/item_crellas_crozier#mechanics]

## Effects

Rite of Rumusque puts the user in ghost form, granting immunity to physical damage while preventing attacks and increasing vulnerability to magic damage. It periodically steals movement speed from enemy heroes in range, with each steal persisting briefly. During the active, Putrefaction Aura’s effect is increased and all lost Health Restoration is redirected to the user. [loc:DOTA_Tooltip_ability_item_crellas_crozier_Description]

Putrefaction Aura reduces the Health Restoration of nearby enemy heroes. [loc:DOTA_Tooltip_ability_item_crellas_crozier_Description]