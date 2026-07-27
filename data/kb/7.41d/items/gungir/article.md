---
title: Gleipnir
kind: item
patch: 7.41d
card:
  entity: gungir
  sentences:
  - text: Gleipnir is a 4650-gold artifact item that grants 450 Health, 12 Intelligence,
      and 200 Mana; its Eternal Chains active roots all enemies within a 400 radius
      for 2.0 seconds.
    marks:
    - gamefile:items/item_gungir#cost
    - gamefile:items/item_gungir#attribs
    - loc:DOTA_Tooltip_ability_item_gungir_Description
  - text: Eternal Chains has Point Target, AOE behavior.
    marks:
    - gamefile:items/item_gungir#mechanics
  - text: Eternal Chains is dispellable.
    marks:
    - gamefile:items/item_gungir#mechanics
  - text: Eternal Chains has 1100 cast range.
    marks:
    - gamefile:items/item_gungir#mechanics
  - text: Eternal Chains has a Mana cost of 150.
    marks:
    - gamefile:items/item_gungir#mechanics
  - text: Eternal Chains has a cooldown of 18.
    marks:
    - gamefile:items/item_gungir#mechanics
  - text: 'Build formula: Rod of Atos (2250 gold), Point Booster (1200 gold), Chasm
      Stone (800 gold), and Recipe (400 gold).'
    marks:
    - gamefile:items/item_gungir#components
---

# Gleipnir

Gleipnir is an artifact item that grants Health, Intelligence, and Mana and provides the Eternal Chains active, which roots all enemies in its area. [gamefile:items/item_gungir#cost] [gamefile:items/item_gungir#attribs] [loc:DOTA_Tooltip_ability_item_gungir_Description]

## Stats

| Stat | Value |
|---|---:|
| AREA OF EFFECT | 75 |
| HEALTH | 450 |
| INTELLIGENCE | 12 |
| MANA | 200 |
| DURATION | 2.0 |
| RADIUS | 325 |
| RADIUS TOOLTIP | 400 |

[gamefile:items/item_gungir#attribs]

## Eternal Chains

Eternal Chains is point-targeted with an area of effect and can be dispelled. [gamefile:items/item_gungir#mechanics]

| Effect | Value |
|---|---:|
| Root radius | 400 |
| Root duration | 2.0 seconds |

[loc:DOTA_Tooltip_ability_item_gungir_Description]

| Mechanic | Value |
|---|---:|
| Behavior | Point Target, AOE |
| Dispellable | Yes |
| Cast range | 1100 |
| Mana cost | 150 |
| Cooldown | 18 |

[gamefile:items/item_gungir#mechanics]

## Components

| Component | Gold cost |
|---|---:|
| Rod of Atos | 2250 gold |
| Point Booster | 1200 gold |
| Chasm Stone | 800 gold |
| Recipe | 400 gold |
| **Gleipnir** | **4650 gold** |

[gamefile:items/item_gungir#components] [gamefile:items/item_gungir#cost]

*Bindings forged by impossible means to leash an ancient evil.* [loc:DOTA_Tooltip_ability_item_gungir_Lore]