---
title: Hex
kind: concept
patch: 7.41d
card:
  entity: Hex
  sentences:
  - text: Hex, also called Sheep, Voodoo, or Polymorph, is a status effect that transforms
      a unit into a harmless critter and applies silence, mute, and disarm, preventing
      attacks, ability casts, and active-item use.
    marks:
    - corpus:liquipedia_dota2/hex@2383903
    - corpus:liquipedia_dota2/hex@2383903#Mechanics
  - text: All Hex sources instantly destroy illusions except strong illusions.
    marks:
    - corpus:liquipedia_dota2/hex@2383903#Mechanics
  - text: Abilities continue to treat hexed heroes as heroes.
    marks:
    - corpus:liquipedia_dota2/hex@2383903#Mechanics
  - text: Hex’s regular silence does not toggle off active toggles or stop ongoing
      abilities, except channeling abilities.
    marks:
    - corpus:liquipedia_dota2/hex@2383903#Mechanics
  - text: Hex does not dispel status effects.
    marks:
    - corpus:liquipedia_dota2/hex@2383903#Mechanics
  - text: Unless stated otherwise, Hex does not apply break, so passive abilities
      and current passive effects such as armor and magic resistance remain active.
    marks:
    - corpus:liquipedia_dota2/hex@2383903#Mechanics
  - text: 'The transformation is visual: collision size and other unit properties
      remain unchanged, although the hit box and selection box change.'
    marks:
    - corpus:liquipedia_dota2/hex@2383903#Mechanics
  - text: Strong dispels can remove Hex.
    marks:
    - corpus:liquipedia_dota2/hex@2383903#Mechanics
  - text: Hex directly sets the target’s movement speed to a fixed value for its duration.
    marks:
    - corpus:liquipedia_dota2/hex@2383903#Set_Movement_Speed
  - text: Flat and percentage-based movement-speed changes still fully affect a hexed
      unit.
    marks:
    - corpus:liquipedia_dota2/hex@2383903#Set_Movement_Speed
  - text: Shadow Shaman’s Hex changes Sand King’s base movement speed from 290 to
      2/2.3/2.6/2.9 for the duration.
    marks:
    - corpus:liquipedia_dota2/hex@2383903#Set_Movement_Speed
  - text: Listed Hex sources are Dazzle’s Poison Touch, Lion’s Hex, Scythe of Vyse’s
      Hex, and Shadow Shaman’s Hex.
    marks:
    - corpus:liquipedia_dota2/hex@2383903#Sources_of_Hex
---

# Hex

Hex, also called **Sheep**, **Voodoo**, or **Polymorph**, is a status effect that transforms an affected unit into a harmless critter and disables many of its fighting capabilities. [corpus:liquipedia_dota2/hex@2383903]

## Mechanics

All hex sources instantly destroy illusions except strong illusions. Hexed heroes remain treated as heroes by abilities. [corpus:liquipedia_dota2/hex@2383903#Mechanics]

Hex applies silence, mute, and disarm, preventing the target from attacking, casting abilities, or using active item abilities. Because the silence is regular, toggled-on abilities are not toggled off and ongoing abilities are not stopped, except channeling abilities. Hex does not dispel status effects. [corpus:liquipedia_dota2/hex@2383903#Mechanics]

Hex does not apply break unless stated, so passive abilities continue working. It does not affect armor, magic resistance, or other current passive effects. [corpus:liquipedia_dota2/hex@2383903#Mechanics]

The critter transformation is visual: the unit retains all properties, including collision size, although its hit box and selection box change. A hexed Windranger’s collision size stays unchanged, while the selection boxes change according to the Hex model. Hex can be removed by strong dispels. [corpus:liquipedia_dota2/hex@2383903#Mechanics]

### Set Movement Speed

Hex directly sets the target’s movement speed to a fixed value for its duration. Flat and percentage-based movement-speed changes still fully affect the unit, and other movement-speed notes fully apply. [corpus:liquipedia_dota2/hex@2383903#Set_Movement_Speed]

For example, Sand King has a base movement speed of 290. While affected by Shadow Shaman’s Hex, his base movement speed is set to 2/2.3/2.6/2.9 for the duration. [corpus:liquipedia_dota2/hex@2383903#Set_Movement_Speed]

## Sources

| Hero or item | Hex source |
|---|---|
| Dazzle | Poison Touch4 |
| Lion | Hex |
| Scythe of Vyse | Hex |
| Shadow Shaman | Hex |

| Marker | Requirement |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |

[corpus:liquipedia_dota2/hex@2383903#Sources_of_Hex]

## Modifying Hex Models

| Cosmetic item | Effect |
|---|---|
| Fin King's Charm | Changes Lion’s Hex model into a fish. |
| Fin King's Charm of Eminent Revival | Changes Lion’s Hex model into a fish. |
| Lamb to the Slaughter | Changes Shadow Shaman’s Hex model into a sheep. |
| Golden Lamb to the Slaughter | Changes Shadow Shaman’s Hex model into a sheep. |

[corpus:liquipedia_dota2/hex@2383903#Modifying_Hex_Models]

## Models

| Model | Usage |
|---|---|
| Chicken model | Used by Shadow Shaman’s Hex |
| Frog mode | Used by Lion’s Hex |
| Pig model | Used by Scythe of Vyse, Pig Pole, and Poison Touch |
| Fish model | Used by Lion with Fin King's Charm equipped |
| Green fish model | Used by Lion with Fin King's Charm of Eminent Revival equipped |
| Lamb model | Used by Shadow Shaman with Lamb to the Slaughter equipped |
| Lamb model | Used by Shadow Shaman with Golden Lamb to the Slaughter equipped |

[corpus:liquipedia_dota2/hex@2383903#Gallery]

## Version History

| Version | Date | Description |
|---|---|---|
| 7.20 | 2018-11-19 | Hex state can now be removed by strong dispels. |
| 7.07 | 2017-10-31 | Hex can no longer be dispelled. |
| 6.84 | 2015-04-30 | Hex no longer disables certain passive abilities. |
| 5.31 | 2026-07-25 | Created Scythe of Vyse. |

[corpus:liquipedia_dota2/hex@2383903#Version_History]

## Patch History

| Patch | Description |
|---|---|
| 20 Aug 2021 | Fixed generic hex debuff modifiers missing descriptions. |
| 02 Oct 2015 | Improved hexed unit hitboxes. |
| 29 Apr 2014 | Fixed Hex disabling Bristleback. |
| 18 Nov 2013 | Roshan is now uninterrupted by Hex sources. |
| 28 Mar 2012 | Fixed heroes drawing parts of their models in portraits when Hexed. |
| 01 Jul 2011 | Hex-sources now disable the following mechanics:<br>• Auras<br>• Bash<br>• Critical Strike<br>• Damage Block<br>• Evasion<br>• Lifesteal<br>• True Sight |
| 12 Mar 2011 | Fixed ability interactions between Elder Dragon Form and Hex sources, not changing Dragon Knight to the new Hex model. |
| 04 Feb 2011 | Fixed being able to use items while Hexed. |

[corpus:liquipedia_dota2/hex@2383903#Patch_History]