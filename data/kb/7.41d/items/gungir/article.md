---
title: Gleipnir
kind: item
patch: 7.41d
card:
  entity: gungir
  sentences:
  - text: Gleipnir is an artifact item costing 4650 gold that grants 450 Health, 12
      Intelligence, and 200 Mana; Eternal Chains roots all enemies within a 400 radius
      for 2.0 seconds.
    marks:
    - gamefile:items/item_gungir#cost
    - gamefile:items/item_gungir#attribs
    - loc:DOTA_Tooltip_ability_item_gungir_Description
  - text: Eternal Chains has Point Target and AOE behavior.
    marks:
    - gamefile:items/item_gungir#mechanics
  - text: Eternal Chains is dispellable.
    marks:
    - gamefile:items/item_gungir#mechanics
  - text: Its cast range is 1100.
    marks:
    - gamefile:items/item_gungir#mechanics
  - text: Its Mana cost is 150.
    marks:
    - gamefile:items/item_gungir#mechanics
  - text: Its cooldown is 18.
    marks:
    - gamefile:items/item_gungir#mechanics
  - text: Gleipnir is built from Rod of Atos for 2250 gold, Point Booster for 1200
      gold, Chasm Stone for 800 gold, and a Recipe for 400 gold.
    marks:
    - gamefile:items/item_gungir#components
  - text: “Bindings forged by impossible means to leash an ancient evil.”
    marks:
    - loc:DOTA_Tooltip_ability_item_gungir_Lore
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