---
title: Orchid Malevolence
kind: item
patch: 7.41d
card:
  entity: orchid
  sentences:
  - text: Orchid Malevolence is a rare 3275-gold item whose Soul Burn active silences
      a target for a duration of 5, then inflicts 30% of the damage received during
      the silence as bonus magical damage.
    marks:
    - gamefile:items/item_orchid#cost
    - gamefile:items/item_orchid#attribs
    - loc:DOTA_Tooltip_ability_item_orchid_Description
  - text: It provides 35 Attack Speed.
    marks:
    - gamefile:items/item_orchid#attribs
  - text: It provides 20 Damage.
    marks:
    - gamefile:items/item_orchid#attribs
  - text: It provides 0.0 Health Regeneration.
    marks:
    - gamefile:items/item_orchid#attribs
  - text: It provides 12 Intelligence.
    marks:
    - gamefile:items/item_orchid#attribs
  - text: It provides 2.5 Mana Regeneration.
    marks:
    - gamefile:items/item_orchid#attribs
  - text: Its build formula is Oblivion Staff (1625 gold) + Claymore (1350 gold) +
      Recipe (300 gold), and it builds into Bloodthorn.
    marks:
    - gamefile:items/item_orchid#components
  - text: Soul Burn has Unit Target behavior.
    marks:
    - gamefile:items/item_orchid#mechanics
  - text: Soul Burn is dispellable.
    marks:
    - gamefile:items/item_orchid#mechanics
  - text: Soul Burn has 900 cast range.
    marks:
    - gamefile:items/item_orchid#mechanics
  - text: Soul Burn costs 125 mana.
    marks:
    - gamefile:items/item_orchid#mechanics
  - text: Soul Burn has an 18.0 cooldown.
    marks:
    - gamefile:items/item_orchid#mechanics
---

# Orchid Malevolence

Orchid Malevolence is a rare item that provides Attack Speed, Damage, Health Regeneration, Intelligence, and Mana Regeneration and grants the Soul Burn active, governed by Silence Damage Percent and Silence Duration. [gamefile:items/item_orchid#cost] [gamefile:items/item_orchid#attribs] [loc:DOTA_Tooltip_ability_item_orchid_Description]

## Stats

| Stat | Value |
|---|---:|
| Cost | 3275 gold |
| Attack Speed | 35 |
| Damage | 20 |
| Health Regeneration | 0.0 |
| Intelligence | 12 |
| Mana Regeneration | 2.5 |
| Silence Damage Percent | 30% |
| Silence Duration | 5 |

[gamefile:items/item_orchid#cost] [gamefile:items/item_orchid#attribs]

## Components

| Type | Item | Gold cost |
|---|---|---:|
| Component | Oblivion Staff | 1625 gold |
| Component | Claymore | 1350 gold |
| Recipe | Recipe | 300 gold |
| Builds into | Bloodthorn | 6400 gold |

[gamefile:items/item_orchid#components]

## Soul Burn

| Property | Value |
|---|---:|
| Behavior | Unit Target |
| Dispellable | Yes |
| Cast range | 900 |
| Mana cost | 125 |
| Cooldown | 18.0 |

[gamefile:items/item_orchid#mechanics]

Soul Burn silences the target unit. When the silence ends, a portion of the damage received while silenced is inflicted as bonus magical damage. [loc:DOTA_Tooltip_ability_item_orchid_Description]

*A garnet rod constructed from the essence of a fire demon.* [loc:DOTA_Tooltip_ability_item_orchid_Lore]