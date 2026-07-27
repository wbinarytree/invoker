---
title: Heaven's Halberd
kind: item
patch: 7.41d
card:
  entity: heavens_halberd
  sentences:
  - text: Heaven's Halberd is a 3400-gold artifact item granting 9 Armor, 25% Evasion,
      and 6.5 Health Regeneration, with Disarm preventing its target from attacking
      for 3.5 seconds.
    marks:
    - gamefile:items/item_heavens_halberd#cost
    - gamefile:items/item_heavens_halberd#attribs
    - loc:DOTA_Tooltip_ability_item_heavens_halberd_Description
  - text: It is built from Talisman of Evasion (1300 gold), Splintmail (950 gold),
      Ring of Health (700 gold), and a Recipe (450 gold).
    marks:
    - gamefile:items/item_heavens_halberd#components
  - text: Disarm has Unit Target behavior.
    marks:
    - gamefile:items/item_heavens_halberd#mechanics
  - text: Disarm is removable by Strong Dispels Only.
    marks:
    - gamefile:items/item_heavens_halberd#mechanics
  - text: Disarm has 750 cast range.
    marks:
    - gamefile:items/item_heavens_halberd#mechanics
  - text: Disarm costs 25 mana.
    marks:
    - gamefile:items/item_heavens_halberd#mechanics
  - text: Disarm has a 16-second cooldown.
    marks:
    - gamefile:items/item_heavens_halberd#mechanics
---

# Heaven's Halberd

Heaven's Halberd is an artifact item that grants Armor, Evasion, and Health Regeneration and provides the Disarm active. [gamefile:items/item_heavens_halberd#cost] [gamefile:items/item_heavens_halberd#attribs] [loc:DOTA_Tooltip_ability_item_heavens_halberd_Description]

## Cost

| Item | Gold cost |
|---|---:|
| Heaven's Halberd | 3400 gold |

[gamefile:items/item_heavens_halberd#cost]

## Components

| Component | Gold cost |
|---|---:|
| Talisman of Evasion | 1300 gold |
| Splintmail | 950 gold |
| Ring of Health | 700 gold |
| Recipe | 450 gold |

[gamefile:items/item_heavens_halberd#components]

## Stats

| Stat | Value |
|---|---:|
| Armor | 9 |
| Evasion | 25% |
| Health Regeneration | 6.5 |
| Disarm Melee | 3.5 |
| Disarm Range | 3.5 |

[gamefile:items/item_heavens_halberd#attribs]

## Disarm

| Property | Value |
|---|---:|
| Duration | 3.5 seconds |

[loc:DOTA_Tooltip_ability_item_heavens_halberd_Description]

Disarm prevents the target from attacking. [loc:DOTA_Tooltip_ability_item_heavens_halberd_Description]

| Property | Value |
|---|---:|
| Behavior | Unit Target |
| Dispellable | Strong Dispels Only |
| Cast range | 750 |
| Mana cost | 25 |
| Cooldown | 16 |

[gamefile:items/item_heavens_halberd#mechanics]

*This halberd moves with the speed of a smaller weapon, allowing the bearer to win duels that a heavy edge would not.* [loc:DOTA_Tooltip_ability_item_heavens_halberd_Lore]