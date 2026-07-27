---
title: Elixir
kind: item
patch: 7.41d
card:
  entity: elixer
  sentences:
  - text: Elixir is a 0-gold consumable that restores 500 health and 250 mana over
      a duration of 6.
    marks:
    - loc:DOTA_Tooltip_ability_item_elixer_Description
    - gamefile:items/item_elixer#attribs
    - gamefile:items/item_elixer#cost
  - text: Its build formula is Elixir (0 gold).
    marks:
    - gamefile:items/item_elixer#cost
  - text: Its cast range is 250.
    marks:
    - gamefile:items/item_elixer#mechanics
  - text: It is dispellable.
    marks:
    - gamefile:items/item_elixer#mechanics
  - text: Elixir is unit-targeted.
    marks:
    - gamefile:items/item_elixer#mechanics
  - text: Its use is immediate.
    marks:
    - gamefile:items/item_elixer#mechanics
  - text: Using it does not resume attacks.
    marks:
    - gamefile:items/item_elixer#mechanics
  - text: Using it suppresses the associated consumable.
    marks:
    - gamefile:items/item_elixer#mechanics
  - text: The restoration effect is lost if the target is attacked by an enemy hero
      or Roshan.
    marks:
    - loc:DOTA_Tooltip_ability_item_elixer_Description
---

# Elixir

Elixir is a consumable item that restores health and mana over a duration. [loc:DOTA_Tooltip_ability_item_elixer_Description]

## Stats

| Stat | Value |
|---|---:|
| Duration | 6 |
| Health | 500 |
| Mana | 250 |

[gamefile:items/item_elixer#attribs]

## Components

| Component | Gold cost |
|---|---:|
| Elixir | 0 gold |

[gamefile:items/item_elixer#cost]

## Mechanics

| Property | Value |
|---|---:|
| Cast range | 250 |
| Dispellable | Yes |

[gamefile:items/item_elixer#mechanics]

Elixir is unit-targeted and immediate. Using it does not resume attacks and suppresses the associated consumable. [gamefile:items/item_elixer#mechanics]

The restoration effect is lost if the target is attacked by an enemy hero or Roshan. [loc:DOTA_Tooltip_ability_item_elixer_Description]