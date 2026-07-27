---
title: Diffusal Blade
kind: item
patch: 7.41d
card:
  entity: diffusal_blade
  sentences:
  - text: Diffusal Blade is a 2500-gold artifact item that grants 15 Agility and 10
      Intelligence; Inhibit slows an enemy, while Manabreak burns 40 mana per attack
      and deals 1 physical damage per mana burned, with illusions burning 0 mana.
    marks:
    - gamefile:items/item_diffusal_blade#cost
    - gamefile:items/item_diffusal_blade#attribs
    - loc:DOTA_Tooltip_ability_item_diffusal_blade_Description
  - text: Inhibit has Unit Target behavior.
    marks:
    - gamefile:items/item_diffusal_blade#mechanics
  - text: Its cast range is 600.
    marks:
    - gamefile:items/item_diffusal_blade#mechanics
  - text: It is dispellable.
    marks:
    - gamefile:items/item_diffusal_blade#mechanics
  - text: Its mana cost is 25.
    marks:
    - gamefile:items/item_diffusal_blade#mechanics
  - text: Its cooldown is 15.0.
    marks:
    - gamefile:items/item_diffusal_blade#mechanics
  - text: Its purge rate is 5.
    marks:
    - gamefile:items/item_diffusal_blade#attribs
  - text: Its purge root duration is 3.0.
    marks:
    - gamefile:items/item_diffusal_blade#attribs
  - text: Its purge slow duration is 4.0.
    marks:
    - gamefile:items/item_diffusal_blade#attribs
  - text: Its build formula is Blade of Alacrity for 1000 gold, Robe of the Magi for
      450 gold, and a Recipe for 1050 gold.
    marks:
    - gamefile:items/item_diffusal_blade#cost
    - gamefile:items/item_diffusal_blade#components
  - text: It builds into Disperser.
    marks:
    - gamefile:items/item_diffusal_blade#components
  - text: “An enchanted blade that allows the user to cut straight into the enemy's
      soul.”
    marks:
    - loc:DOTA_Tooltip_ability_item_diffusal_blade_Lore
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