---
title: Diffusal Blade
kind: item
patch: 7.41d
card:
  entity: diffusal_blade
  sentences:
  - text: Diffusal Blade is a 2500-gold artifact item granting 15 Agility and 10 Intelligence;
      Inhibit slows an enemy with purge rate 5, purge root duration 3.0, and purge
      slow duration 4.0, while Manabreak burns 40 mana per attack and deals 1 physical
      damage per mana burned.
    marks:
    - gamefile:items/item_diffusal_blade#cost
    - gamefile:items/item_diffusal_blade#attribs
    - loc:DOTA_Tooltip_ability_item_diffusal_blade_Description
  - text: Inhibit is dispellable and unit-targeted, with 600 cast range, 25 mana cost,
      and 15.0 cooldown.
    marks:
    - gamefile:items/item_diffusal_blade#mechanics
  - text: Melee and ranged illusions each have 0 feedback mana burn.
    marks:
    - gamefile:items/item_diffusal_blade#attribs
  - text: The build formula is Blade of Alacrity (1000 gold), Robe of the Magi (450
      gold), and Recipe (1050 gold); it builds into Disperser.
    marks:
    - gamefile:items/item_diffusal_blade#cost
    - gamefile:items/item_diffusal_blade#components
---

# Diffusal Blade

Diffusal Blade is an artifact item that grants Agility and Intelligence, provides the enemy slow Inhibit, and provides the mana-burning, physical-damage passive Manabreak. [gamefile:items/item_diffusal_blade#cost] [gamefile:items/item_diffusal_blade#attribs] [loc:DOTA_Tooltip_ability_item_diffusal_blade_Description]

## Attributes

| Stat | Value |
|---|---:|
| Agility | 15 |
| Intelligence | 10 |
| Damage per burn | 1 |
| Feedback mana burn | 40 |
| Feedback mana burn illusion melee | 0 |
| Feedback mana burn illusion ranged | 0 |
| Purge rate | 5 |
| Purge root duration | 3.0 |
| Purge slow duration | 4.0 |

[gamefile:items/item_diffusal_blade#attribs]

## Mechanics

| Property | Value |
|---|---:|
| Behavior | Unit Target |
| Dispellable | Yes |
| Cast range | 600 |
| Mana cost | 25 |
| Cooldown | 15.0 |

[gamefile:items/item_diffusal_blade#mechanics]

Inhibit targets and slows an enemy. Manabreak burns mana from the target with each attack and deals physical damage per mana burned; illusions do not burn mana. [loc:DOTA_Tooltip_ability_item_diffusal_blade_Description]

## Components

| Build formula | Gold cost |
|---|---:|
| Diffusal Blade | 2500 gold |
| Blade of Alacrity | 1000 gold |
| Robe of the Magi | 450 gold |
| Recipe | 1050 gold |
| Builds into: Disperser | 6100 gold |

[gamefile:items/item_diffusal_blade#cost] [gamefile:items/item_diffusal_blade#components]

*An enchanted blade that allows the user to cut straight into the enemy's soul.* [loc:DOTA_Tooltip_ability_item_diffusal_blade_Lore]