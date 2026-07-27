---
title: Nullifier
kind: item
patch: 7.41d
card:
  entity: nullifier
  sentences:
  - text: Nullifier is an epic item costing 4350 gold that grants 10 armor, 75 damage,
      and 0 health regeneration; its Nullify active dispels the target and applies
      a continuously dispelling and slowing debuff with a Basic Dispel, 4.0 mute duration,
      10% slow, and 0.5-second slow intervals.
    marks:
    - gamefile:items/item_nullifier#cost
    - gamefile:items/item_nullifier#attribs
    - loc:DOTA_Tooltip_ability_item_nullifier_Description
  - text: Nullify is Unit Target with 900 cast range, 0 mana cost, and a 10.0-second
      cooldown.
    marks:
    - gamefile:items/item_nullifier#mechanics
  - text: Nullify has 1800 projectile speed.
    marks:
    - gamefile:items/item_nullifier#attribs
  - text: Nullifier is built from Sacred Relic (3400 gold) and Splintmail (950 gold).
    marks:
    - gamefile:items/item_nullifier#components
---

# Nullifier

Nullifier is an epic item with Armor, Damage, and Health Regeneration attributes and the Nullify active. [gamefile:items/item_nullifier#cost] [gamefile:items/item_nullifier#attribs] [loc:DOTA_Tooltip_ability_item_nullifier_Description]

## Stats

| Stat | Value |
|---|---:|
| Cost | 4350 gold |
[gamefile:items/item_nullifier#cost]

| Attribute | Value |
|---|---:|
| ARMOR | 10 |
| DAMAGE | 75 |
| HEALTH REGENERATION | 0 |
| MUTE DURATION | 4.0 |
| PROJECTILE SPEED | 1800 |
| SLOW INTERVAL DURATION | 0.5 |
| SLOW PCT | 10 |
[gamefile:items/item_nullifier#attribs]

## Components

| Component | Cost |
|---|---:|
| Sacred Relic | 3400 gold |
| Splintmail | 950 gold |
[gamefile:items/item_nullifier#components]

## Nullify

| Property | Value |
|---|---:|
| Behavior | Unit Target |
| Cast range | 900 |
| Mana cost | 0 |
| Cooldown | 10.0 |
[gamefile:items/item_nullifier#mechanics]

Nullify dispels its target and applies a debuff. The debuff continuously dispels and slows the target and uses a Basic Dispel. [loc:DOTA_Tooltip_ability_item_nullifier_Description]