---
title: Disperser
kind: item
patch: 7.41d
card:
  entity: disperser
  sentences:
  - text: Disperser is a 6100-gold artifact item granting 40 Agility and 10 Intelligence;
      Suppress applies a basic dispel to the wearer and target, slows enemies for
      4.0 seconds, and grants allies bonus movement speed and 40% slow resistance
      for 4.0 seconds, while Manabreak burns 40 mana per attack for 1.0 physical damage
      per mana burned.
    marks:
    - gamefile:items/item_disperser#cost
    - gamefile:items/item_disperser#attribs
    - loc:DOTA_Tooltip_ability_item_disperser_Description
  - text: Suppress has Unit Target, AOE behavior.
    marks:
    - gamefile:items/item_disperser#mechanics
  - text: Suppress has a cast range of 600.
    marks:
    - gamefile:items/item_disperser#mechanics
  - text: Suppress costs 75 mana.
    marks:
    - gamefile:items/item_disperser#mechanics
  - text: Suppress has a 15.0-second cooldown.
    marks:
    - gamefile:items/item_disperser#mechanics
  - text: Suppress applies a basic dispel to both the wearer and the target.
    marks:
    - loc:DOTA_Tooltip_ability_item_disperser_Description
  - text: An enemy target's movement-speed reduction decreases from 100% to 0% over
      4.0 seconds.
    marks:
    - gamefile:items/item_disperser#attribs
    - loc:DOTA_Tooltip_ability_item_disperser_Description
  - text: An allied target gains 40% slow resistance while its movement-speed increase
      decreases from 100% to 0% over 4.0 seconds.
    marks:
    - gamefile:items/item_disperser#attribs
    - loc:DOTA_Tooltip_ability_item_disperser_Description
  - text: The caster always receives the allied benefit from Suppress.
    marks:
    - loc:DOTA_Tooltip_ability_item_disperser_Description
  - text: Melee and ranged illusions burn 0 mana with Manabreak.
    marks:
    - gamefile:items/item_disperser#attribs
  - text: Disperser is built from Diffusal Blade (2500 gold), Eaglesong (2800 gold),
      and Recipe (800 gold).
    marks:
    - gamefile:items/item_disperser#components
  - text: “Once entrusted to an Apostle General of the Rumusque Faithful's expeditionary
      force.”
    marks:
    - loc:DOTA_Tooltip_ability_item_disperser_Lore
---

# Disperser

Disperser is an artifact item that grants Agility and Intelligence and provides the active Suppress and passive Manabreak. [gamefile:items/item_disperser#cost] [gamefile:items/item_disperser#attribs] [loc:DOTA_Tooltip_ability_item_disperser_Description]

## Stats

| Stat | Value |
|---|---:|
| ALLY EFFECT DURATION — allied bonus movespeed and slow resistance | 4.0 seconds |
| AGILITY | 40 |
| INTELLIGENCE | 10 |
| DAMAGE PER BURN — physical damage per burned mana | 1.0 |
| ENEMY EFFECT DURATION — slow | 4.0 seconds |
| FEEDBACK MANA BURN — per attack | 40 mana |
| FEEDBACK MANA BURN ILLUSION MELEE | 0 |
| FEEDBACK MANA BURN ILLUSION RANGED | 0 |
| MOVEMENT SPEED BUFF RATE | 4 |
| PHASE MOVEMENT SPEED — initial movement speed reduction and increase | 100% |
| Movement speed reduction and increase at buff end | 0% |
| PURGE RATE | 5 |
| PURGE ROOT DURATION | 3.0 |
| SLOW RESIST | 40% |
[gamefile:items/item_disperser#attribs] [loc:DOTA_Tooltip_ability_item_disperser_Description]

| Ability property | Value |
|---|---:|
| Behavior | Unit Target, AOE |
| Dispellable | Yes |
| Cast range | 600 |
| Mana cost | 75 |
| Cooldown | 15.0 |
[gamefile:items/item_disperser#mechanics]

## Components

| Component | Gold cost |
|---|---:|
| Diffusal Blade | 2500 gold |
| Eaglesong | 2800 gold |
| Recipe | 800 gold |
| **Disperser** | **6100 gold** |
[gamefile:items/item_disperser#components] [gamefile:items/item_disperser#cost]

## Abilities

**Active — Suppress.** Dispels both the wearer and the target with a basic dispel. Enemy targets are slowed, while allied targets gain bonus movespeed and slow resistance; the caster always receives the allied benefit. Both the movement speed reduction and increase gradually decrease from their listed initial amounts to their ending amounts over the buff duration. [loc:DOTA_Tooltip_ability_item_disperser_Description]

**Passive — Manabreak.** Each attack burns mana from the target and deals physical damage per mana burned. Illusions do not burn mana. [loc:DOTA_Tooltip_ability_item_disperser_Description]

*Once entrusted to an Apostle General of the Rumusque Faithful's expeditionary force.* [loc:DOTA_Tooltip_ability_item_disperser_Lore]