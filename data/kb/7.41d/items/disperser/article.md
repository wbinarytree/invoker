---
title: Disperser
kind: item
patch: 7.41d
card:
  entity: disperser
  sentences:
  - text: Disperser is a 6100-gold artifact item granting 40 Agility and 10 Intelligence;
      its active Suppress basic-dispels the wearer and target, slows enemies, and
      gives allied recipients 100% phase movement speed and 40% slow resistance for
      4.0 seconds, while its passive Manabreak burns 40 mana per attack and deals
      1.0 physical damage per mana burned.
    marks:
    - gamefile:items/item_disperser#cost
    - gamefile:items/item_disperser#attribs
    - loc:DOTA_Tooltip_ability_item_disperser_Description
  - text: It is built from Diffusal Blade (2500 gold), Eaglesong (2800 gold), and
      a Recipe (800 gold).
    marks:
    - gamefile:items/item_disperser#components
    - gamefile:items/item_disperser#cost
  - text: Suppress has Unit Target, AOE behavior.
    marks:
    - gamefile:items/item_disperser#mechanics
  - text: Suppress has 600 cast range.
    marks:
    - gamefile:items/item_disperser#mechanics
  - text: Suppress costs 75 mana.
    marks:
    - gamefile:items/item_disperser#mechanics
  - text: Suppress has a cooldown of 15.0.
    marks:
    - gamefile:items/item_disperser#mechanics
  - text: Suppress is dispellable.
    marks:
    - gamefile:items/item_disperser#mechanics
  - text: The caster always receives the allied benefit.
    marks:
    - loc:DOTA_Tooltip_ability_item_disperser_Description
  - text: Suppress's movement-speed reduction and increase gradually fall to no effect
      over the buff duration.
    marks:
    - loc:DOTA_Tooltip_ability_item_disperser_Description
  - text: Suppress has a purge rate of 5.
    marks:
    - gamefile:items/item_disperser#attribs
  - text: Suppress has a purge root duration of 3.0.
    marks:
    - gamefile:items/item_disperser#attribs
  - text: Manabreak's feedback mana burn is 0 for melee illusions and 0 for ranged
      illusions.
    marks:
    - gamefile:items/item_disperser#attribs
---

# Disperser

Disperser is an artifact item that provides Agility and Intelligence and grants the active Suppress and passive Manabreak. [gamefile:items/item_disperser#cost] [gamefile:items/item_disperser#attribs] [loc:DOTA_Tooltip_ability_item_disperser_Description]

## Components

| Component | Gold cost |
|---|---:|
| Diffusal Blade | 2500 gold |
| Eaglesong | 2800 gold |
| Recipe | 800 gold |
| **Disperser** | **6100 gold** |

[gamefile:items/item_disperser#components] [gamefile:items/item_disperser#cost]

## Stats

| Stat | Value |
|---|---:|
| Ally effect duration | 4.0 |
| Agility | 40 |
| Intelligence | 10 |
| Damage per burn | 1.0 |
| Enemy effect duration | 4.0 |
| Feedback mana burn | 40 |
| Feedback mana burn illusion melee | 0 |
| Feedback mana burn illusion ranged | 0 |
| Movement speed buff rate | 4 |
| Phase movement speed | 100% |
| Purge rate | 5 |
| Purge root duration | 3.0 |
| Slow resistance | 40% |

[gamefile:items/item_disperser#attribs]

## Mechanics

| Property | Value |
|---|---:|
| Behavior | Unit Target, AOE |
| Dispellable | Yes |
| Cast range | 600 |
| Mana cost | 75 |
| Cooldown | 15.0 |

[gamefile:items/item_disperser#mechanics]

Suppress applies a basic dispel to both the wearer and the target. Enemy targets are slowed, while allied targets gain bonus movement speed and slow resistance; the caster always receives the allied benefit. Both the movement-speed reduction and increase gradually fall to no effect over the buff duration. [loc:DOTA_Tooltip_ability_item_disperser_Description]

Manabreak causes attacks to burn the target’s mana and deal physical damage per mana burned. Illusions do not burn mana. [loc:DOTA_Tooltip_ability_item_disperser_Description]

*Once entrusted to an Apostle General of the Rumusque Faithful's expeditionary force.* [loc:DOTA_Tooltip_ability_item_disperser_Lore]