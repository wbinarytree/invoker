---
title: Echo Sabre
kind: item
patch: 7.41d
card:
  entity: echo_sabre
  sentences:
  - text: Echo Sabre is a 2700-gold artifact item that grants 20 Damage, 1.75 Mana
      Regeneration, and 15 Strength; Echo Strike causes melee attacks to attack twice
      in quick succession and applies 100% Movement Slow for 0.8 seconds on the first
      strike.
    marks:
    - gamefile:items/item_echo_sabre#cost
    - gamefile:items/item_echo_sabre#attribs
    - loc:DOTA_Tooltip_Ability_item_echo_sabre_Description
  - text: Echo Strike is passive.
    marks:
    - gamefile:items/item_echo_sabre#mechanics
  - text: Echo Strike is dispellable.
    marks:
    - gamefile:items/item_echo_sabre#mechanics
  - text: Echo Strike costs 0 mana.
    marks:
    - gamefile:items/item_echo_sabre#mechanics
  - text: Echo Strike has a 5-second cooldown.
    marks:
    - gamefile:items/item_echo_sabre#mechanics
  - text: Echo Sabre's build formula is Ogre Axe (1000 gold), Broadsword (1000 gold),
      and Void Stone (700 gold); it builds into Harpoon.
    marks:
    - gamefile:items/item_echo_sabre#components
---

# Echo Sabre

Echo Sabre is an artifact item that grants Damage, Mana Regeneration, and Strength, and provides Echo Strike, which causes melee attacks to attack twice in quick succession and applies Movement Slow on the first strike. [gamefile:items/item_echo_sabre#cost] [gamefile:items/item_echo_sabre#attribs] [loc:DOTA_Tooltip_Ability_item_echo_sabre_Description]

## Cost

| Stat | Value |
|---|---:|
| Cost | 2700 gold |

[gamefile:items/item_echo_sabre#cost]

## Attributes

| Stat | Value |
|---|---:|
| Damage | 20 |
| Mana Regeneration | 1.75 |
| Strength | 15 |
| Movement Slow | 100% |
| Slow Duration | 0.8 |

[gamefile:items/item_echo_sabre#attribs]

## Mechanics

| Property | Value |
|---|---:|
| Behavior | Passive |
| Dispellable | Yes |
| Mana cost | 0 |
| Cooldown | 5 |

[gamefile:items/item_echo_sabre#mechanics]

## Components

| Type | Item | Gold cost |
|---|---|---:|
| Component | Ogre Axe | 1000 gold |
| Component | Broadsword | 1000 gold |
| Component | Void Stone | 700 gold |
| Builds into | Harpoon | 4700 gold |

[gamefile:items/item_echo_sabre#components]

*A deceptively swift blade imbued with resonant magic.* [loc:DOTA_Tooltip_Ability_item_echo_sabre_Lore]