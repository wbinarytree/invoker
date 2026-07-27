---
title: Veil of Discord
kind: item
patch: 7.41d
card:
  entity: veil_of_discord
  sentences:
  - text: Veil of Discord is a rare item costing 1700 gold that grants 175 Health,
      10 Intelligence, 10% Spell Amp, and 18% Spell Lifesteal, with an active Spell
      Weakness that increases spell damage taken by 10% for 16.0 seconds.
    marks:
    - gamefile:items/item_veil_of_discord#cost
    - gamefile:items/item_veil_of_discord#attribs
    - loc:DOTA_Tooltip_ability_item_veil_of_discord_Description
  - text: Its debuff radius is 900.
    marks:
    - gamefile:items/item_veil_of_discord#attribs
  - text: Its resist debuff duration is 16.0.
    marks:
    - gamefile:items/item_veil_of_discord#attribs
  - text: Spell Weakness has a cast range of 900.
    marks:
    - gamefile:items/item_veil_of_discord#mechanics
  - text: Spell Weakness costs 50 mana.
    marks:
    - gamefile:items/item_veil_of_discord#mechanics
  - text: Spell Weakness has a cooldown of 16.
    marks:
    - gamefile:items/item_veil_of_discord#mechanics
  - text: Spell Weakness is an AOE, no-target, immediate active that does not cancel
      movement, ignores channeling, and is dispellable.
    marks:
    - gamefile:items/item_veil_of_discord#mechanics
  - text: Its build formula is Voodoo Mask (650 gold), Robe of the Magi (450 gold),
      Fluffy Hat (250 gold), and Recipe (350 gold); it builds into Bloodstone.
    marks:
    - gamefile:items/item_veil_of_discord#components
  - text: “The headwear of corrupt magi.”
    marks:
    - loc:DOTA_Tooltip_ability_item_veil_of_discord_Lore
---

# Veil of Discord

Veil of Discord is a rare item that grants Health, Intelligence, Spell Amp, and Spell Lifesteal and provides the active Spell Weakness. [gamefile:items/item_veil_of_discord#cost] [gamefile:items/item_veil_of_discord#attribs] [loc:DOTA_Tooltip_ability_item_veil_of_discord_Description]

## Stats

| Property | Value |
|---|---:|
| Quality | rare |
| Cost | 1700 gold |

[gamefile:items/item_veil_of_discord#cost]

| Stat | Value |
|---|---:|
| HEALTH | 175 |
| INTELLIGENCE | 10 |
| DEBUFF RADIUS | 900 |
| RESIST DEBUFF DURATION | 16.0 |
| SPELL AMP | 10% |
| SPELL LIFESTEAL | 18% |

[gamefile:items/item_veil_of_discord#attribs]

| Active property | Value |
|---|---:|
| Increased spell damage taken | 10% |
| Duration | 16.0 seconds |

[loc:DOTA_Tooltip_ability_item_veil_of_discord_Description]

| Casting property | Value |
|---|---:|
| Cast range | 900 |
| Mana cost | 50 |
| Cooldown | 16 |

[gamefile:items/item_veil_of_discord#mechanics]

## Spell Weakness

Spell Weakness is an AOE, no-target, immediate active that does not cancel movement and ignores channeling. It is dispellable. [gamefile:items/item_veil_of_discord#mechanics]

The blast causes enemy heroes within its radius to take increased damage from spells and can be cast while channeling. [loc:DOTA_Tooltip_ability_item_veil_of_discord_Description]

## Components

| Formula role | Item | Cost |
|---|---|---:|
| Component | Voodoo Mask | 650 gold |
| Component | Robe of the Magi | 450 gold |
| Component | Fluffy Hat | 250 gold |
| Recipe | Recipe | 350 gold |
| Builds into | Bloodstone | 4700 gold |

[gamefile:items/item_veil_of_discord#components]

*The headwear of corrupt magi.* [loc:DOTA_Tooltip_ability_item_veil_of_discord_Lore]