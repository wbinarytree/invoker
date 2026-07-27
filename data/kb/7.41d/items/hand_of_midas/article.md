---
title: Hand of Midas
kind: item
patch: 7.41d
card:
  entity: hand_of_midas
  sentences:
  - text: Hand of Midas is a common item costing 2200 gold that grants 35 attack speed;
      its active ability, Transmute, kills a non-hero target for 160 bonus gold.
    marks:
    - gamefile:items/item_hand_of_midas#cost
    - gamefile:items/item_hand_of_midas#attribs
    - loc:DOTA_Tooltip_ability_item_hand_of_midas_Description
  - text: Its build formula is Gloves of Haste (450 gold) and Recipe (1750 gold).
    marks:
    - gamefile:items/item_hand_of_midas#components
  - text: Transmute is Unit Target and has DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK
      behavior.
    marks:
    - gamefile:items/item_hand_of_midas#mechanics
  - text: Transmute has 600 cast range.
    marks:
    - gamefile:items/item_hand_of_midas#mechanics
  - text: Transmute costs 0 mana.
    marks:
    - gamefile:items/item_hand_of_midas#mechanics
  - text: Transmute has a 0 cooldown.
    marks:
    - gamefile:items/item_hand_of_midas#mechanics
  - text: Transmuting a neutral creep additionally grants a madstone bundle.
    marks:
    - loc:DOTA_Tooltip_ability_item_hand_of_midas_Description
  - text: Transmute cannot target Ancient creeps.
    marks:
    - loc:DOTA_Tooltip_ability_item_hand_of_midas_Description
---

# Hand of Midas

Hand of Midas is a common item that provides Attack Speed and has the active ability Transmute, which awards Bonus Gold. [gamefile:items/item_hand_of_midas#cost] [gamefile:items/item_hand_of_midas#attribs] [loc:DOTA_Tooltip_ability_item_hand_of_midas_Description]

## Stats

| Stat | Value |
|---|---:|
| Cost | 2200 gold |
| ATTACK SPEED | 35 |
| BONUS GOLD | 160 |

[gamefile:items/item_hand_of_midas#cost] [gamefile:items/item_hand_of_midas#attribs]

## Components

| Component | Gold cost |
|---|---:|
| Gloves of Haste | 450 gold |
| Recipe | 1750 gold |

[gamefile:items/item_hand_of_midas#components]

## Transmute

| Property | Value |
|---|---|
| Behavior | Unit Target, DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK |
| Cast range | 600 |
| Mana cost | 0 |
| Cooldown | 0 |

[gamefile:items/item_hand_of_midas#mechanics]

Transmute kills a non-hero target for the listed Bonus Gold. Killing a neutral creep additionally grants a madstone bundle. It cannot be used on Ancient creeps. [loc:DOTA_Tooltip_ability_item_hand_of_midas_Description]

*Preserved through unknown magical means, the Hand of Midas is a weapon of greed, sacrificing animals to line the owner's pockets.* [loc:DOTA_Tooltip_ability_item_hand_of_midas_Lore]