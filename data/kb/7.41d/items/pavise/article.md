---
title: Pavise
kind: item
patch: 7.41d
card:
  entity: pavise
  sentences:
  - text: Pavise is a rare item costing 1350 gold that grants 3 Armor, 175 Health,
      and 175 Mana; its Protect active grants an allied target a 250-point physical
      damage barrier for 7 seconds.
    marks:
    - gamefile:items/item_pavise#cost
    - gamefile:items/item_pavise#attribs
    - loc:DOTA_Tooltip_ability_item_pavise_Description
  - text: Protect has Unit Target and Immediate behavior.
    marks:
    - gamefile:items/item_pavise#mechanics
  - text: Protect is dispellable.
    marks:
    - gamefile:items/item_pavise#mechanics
  - text: Protect has a cast range of 1000.
    marks:
    - gamefile:items/item_pavise#mechanics
  - text: Protect costs 60 Mana.
    marks:
    - gamefile:items/item_pavise#mechanics
  - text: Protect has a 16.0-second cooldown.
    marks:
    - gamefile:items/item_pavise#mechanics
  - text: Pavise requires Wizard Hat for 250 gold, Fluffy Hat for 250 gold, Ring of
      Protection for 175 gold, and a Recipe for 675 gold; it builds into Solar Crest.
    marks:
    - gamefile:items/item_pavise#components
---

# Pavise

Pavise is a rare item that grants Armor, Health, and Mana, while its active, Protect, grants an allied target a physical damage barrier. [gamefile:items/item_pavise#cost] [gamefile:items/item_pavise#attribs] [loc:DOTA_Tooltip_ability_item_pavise_Description]

## Cost

| Property | Value |
|---|---:|
| Cost | 1350 gold |

[gamefile:items/item_pavise#cost]

## Components

| Role | Item | Gold cost |
|---|---|---:|
| Component | Wizard Hat | 250 gold |
| Component | Fluffy Hat | 250 gold |
| Component | Ring of Protection | 175 gold |
| Recipe | Recipe | 675 gold |
| Builds into | Solar Crest | 2575 gold |

[gamefile:items/item_pavise#components]

## Stats

| Stat | Value |
|---|---:|
| ABSORB AMOUNT | 250 |
| ARMOR | 3 |
| HEALTH | 175 |
| MANA | 175 |
| DURATION | 7 |

[gamefile:items/item_pavise#attribs]

## Protect

| Property | Value |
|---|---:|
| Behavior | Unit Target, Immediate |
| Dispellable | Yes |
| Cast range | 1000 |
| Mana cost | 60 |
| Cooldown | 16.0 |

[gamefile:items/item_pavise#mechanics]

Protect is cast on an ally and grants a physical damage barrier. [loc:DOTA_Tooltip_ability_item_pavise_Description]

*Devised by a wizard who made one too many enemies.* [loc:DOTA_Tooltip_ability_item_pavise_Lore]