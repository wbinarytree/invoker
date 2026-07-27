---
title: Bloodthorn
kind: item
patch: 7.41d
card:
  entity: bloodthorn
  sentences:
  - text: Bloodthorn is an epic 6400-gold item granting 70 Attack Speed, 20 Damage,
      0 Health Regeneration, 25 Intelligence, and 4 Mana Regeneration; Soul Rend silences
      for 5 seconds and repeats 60% of damage taken, while Pierce has a 40% chance
      to deal 60 bonus magical damage.
    marks:
    - gamefile:items/item_bloodthorn#cost
    - gamefile:items/item_bloodthorn#attribs
    - loc:DOTA_Tooltip_ability_item_bloodthorn_Description
  - text: It is built from Orchid Malevolence (3275 gold), Oblivion Staff (1625 gold),
      Javelin (900 gold), and a Recipe (600 gold).
    marks:
    - gamefile:items/item_bloodthorn#components
  - text: Soul Rend has 900 cast range.
    marks:
    - gamefile:items/item_bloodthorn#mechanics
  - text: Soul Rend costs 150 mana.
    marks:
    - gamefile:items/item_bloodthorn#mechanics
  - text: Soul Rend has a 15.0-second cooldown.
    marks:
    - gamefile:items/item_bloodthorn#mechanics
  - text: Soul Rend is dispellable.
    marks:
    - gamefile:items/item_bloodthorn#mechanics
  - text: When the silence ends, Soul Rend deals 60% of all damage taken during it
      again as magical damage.
    marks:
    - gamefile:items/item_bloodthorn#attribs
    - loc:DOTA_Tooltip_ability_item_bloodthorn_Description
  - text: During Soul Rend, hero attacks deal 50 additional damage and creep attacks
      deal 25 additional damage.
    marks:
    - gamefile:items/item_bloodthorn#attribs
    - loc:DOTA_Tooltip_ability_item_bloodthorn_Description
  - text: The wielder and its controlled units gain True Strike against the silenced
      target.
    marks:
    - loc:DOTA_Tooltip_ability_item_bloodthorn_Description
  - text: Pierce gives each attack a 40% chance to pierce evasion and deal 60 bonus
      magical damage.
    marks:
    - gamefile:items/item_bloodthorn#attribs
    - loc:DOTA_Tooltip_ability_item_bloodthorn_Description
  - text: Its Spell Amp Debuff value is 35.
    marks:
    - gamefile:items/item_bloodthorn#attribs
---

# Bloodthorn

Bloodthorn is an epic item with Attack Speed, Damage, Health Regeneration, Intelligence, and Mana Regeneration attributes, the active Soul Rend, and the passive Pierce. [gamefile:items/item_bloodthorn#cost] [gamefile:items/item_bloodthorn#attribs] [loc:DOTA_Tooltip_ability_item_bloodthorn_Description]

## Cost

| Item | Cost |
|---|---:|
| Bloodthorn | 6400 gold |

[gamefile:items/item_bloodthorn#cost]

## Components

| Component | Cost |
|---|---:|
| Orchid Malevolence | 3275 gold |
| Oblivion Staff | 1625 gold |
| Javelin | 900 gold |
| Recipe | 600 gold |

[gamefile:items/item_bloodthorn#components]

## Stats

| Attribute | Value |
|---|---:|
| Attack Speed | 70 |
| Damage | 20 |
| Health Regeneration | 0 |
| Intelligence | 25 |
| Mana Regeneration | 4 |
| Duration | 6 |
| Passive Proc Damage | 60 |
| Proc Chance | 40% |
| Proc Damage Creeps | 25 |
| Proc Damage Heroes | 50 |
| Silence Damage Percent | 60% |
| Silence Duration | 5 |
| Spell Amp Debuff | 35 |

[gamefile:items/item_bloodthorn#attribs]

## Mechanics

| Property | Value |
|---|---:|
| Behavior | Unit Target |
| Damage Type | Magical |
| Dispellable | Yes |
| Cast Range | 900 |
| Mana Cost | 150 |
| Cooldown | 15.0 |

[gamefile:items/item_bloodthorn#mechanics]

Soul Rend silences the target. When the silence ends, a portion of all damage taken during it is dealt again as magical damage. Attacks against the silenced target deal additional damage based on whether the attacker is a hero or creep, while attacks from the wielder and their controlled units gain True Strike against that target. Pierce gives each attack a chance to pierce evasion and deal bonus magical damage. [loc:DOTA_Tooltip_ability_item_bloodthorn_Description]

*A reviled blade that bites deeper with each wriggle of its victim's final throes.* [loc:DOTA_Tooltip_ability_item_bloodthorn_Lore]