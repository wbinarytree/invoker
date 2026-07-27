---
title: Orchid Malevolence
kind: item
patch: 7.41d
card:
  entity: orchid
  sentences:
  - text: Orchid Malevolence is a rare 3275-gold item that grants Soul Burn, a 5-second
      silence that inflicts 30% of the damage received during the silence as bonus
      magical damage when it ends.
    marks:
    - gamefile:items/item_orchid#cost
    - gamefile:items/item_orchid#attribs
    - loc:DOTA_Tooltip_ability_item_orchid_Description
  - text: It provides 35 Attack Speed, 20 Damage, 0.0 Health Regeneration, 12 Intelligence,
      and 2.5 Mana Regeneration.
    marks:
    - gamefile:items/item_orchid#attribs
  - text: Its build formula is Oblivion Staff for 1625 gold, Claymore for 1350 gold,
      and a Recipe for 300 gold; it builds into Bloodthorn.
    marks:
    - gamefile:items/item_orchid#components
  - text: Soul Burn has Unit Target behavior.
    marks:
    - gamefile:items/item_orchid#mechanics
  - text: Soul Burn is dispellable.
    marks:
    - gamefile:items/item_orchid#mechanics
  - text: Its cast range is 900.
    marks:
    - gamefile:items/item_orchid#mechanics
  - text: Its mana cost is 125.
    marks:
    - gamefile:items/item_orchid#mechanics
  - text: Its cooldown is 18.0.
    marks:
    - gamefile:items/item_orchid#mechanics
  - text: “A garnet rod constructed from the essence of a fire demon.”
    marks:
    - loc:DOTA_Tooltip_ability_item_orchid_Lore
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