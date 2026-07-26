---
title: Scan
kind: concept
patch: 7.41d
card:
  entity: scan
  sentences:
  - text: Scan is a team-shared, global point-targeted ability usable by any player
      that checks a 900-radius map area for enemy heroes at 1-second intervals for
      8 seconds.
    marks:
    - corpus:liquipedia_dota2/scan@2346506
    - corpus:liquipedia_dota2/scan@2346506#Scan
  - text: Its checks begin immediately, producing 9 checks in total.
    marks:
    - corpus:liquipedia_dota2/scan@2346506#Scan
  - text: Scan has 2 charges, a 210-second replenish time, and starts each match with
      1 charge.
    marks:
    - corpus:liquipedia_dota2/scan@2346506#Version_History
  - text: Charges and their restore time are shared by the team, so one use puts Scan
      on cooldown for every teammate.
    marks:
    - corpus:liquipedia_dota2/scan@2346506
  - text: Enemies receive no indication that Scan is detecting them.
    marks:
    - corpus:liquipedia_dota2/scan@2346506
  - text: Detection changes the minimap indicator from green to red, or from blue
      in color-blind mode, and produces audio cues.
    marks:
    - corpus:liquipedia_dota2/scan@2346506#Scan
  - text: Scan reports only whether enemies are present, not their number, and grants
      no vision or revelation.
    marks:
    - corpus:liquipedia_dota2/scan@2346506#Scan
  - text: It detects invisible heroes and heroes affected by Smoke of Deceit.
    marks:
    - corpus:liquipedia_dota2/scan@2346506#Scan
  - text: Illusions and the Spirit Bear count as heroes for Scan.
    marks:
    - corpus:liquipedia_dota2/scan@2346506#Scan
  - text: Invulnerable units, hidden units, and creep-heroes do not trigger Scan.
    marks:
    - corpus:liquipedia_dota2/scan@2346506#Scan
  - text: Alt+Left Click reports Scan’s cooldown state, while Alt+Ctrl+Left Click
      advises teammates not to use it yet.
    marks:
    - corpus:liquipedia_dota2/scan@2346506#Scan
---

# Scan

## Overview

Scan is an ability usable by any player to scan a targeted map area and detect all enemy heroes within it. It can defensively check whether an area is safe, including revealing an enemy gank attempt, or offensively locate enemies in the Fog of War for a gank. Enemies receive absolutely no indication that Scan is detecting them. [corpus:liquipedia_dota2/scan@2346506]

Any player can activate Scan through a button to the right of the minimap or a hotkey defined in the settings. Its charges and charge restore time are shared by the entire team, so one player’s use puts it on cooldown for every teammate. For spectators, the button is split to show both teams’ cooldowns simultaneously. [corpus:liquipedia_dota2/scan@2346506]

The button is specifically located at the bottom-right corner of the minimap border, above the Glyph of Fortification button. [corpus:liquipedia_dota2/scan@2346506#Scan]

## Ability

Scan is a point-targeted ability that affects self. It scans an area for a few seconds and indicates the presence of enemy heroes through a minimap indicator and audio cues. [corpus:liquipedia_dota2/scan@2346506#Scan]

| Property | Value |
|---|---:|
| Ability | Point [corpus:liquipedia_dota2/scan@2346506#Scan] |
| Affects | Self [corpus:liquipedia_dota2/scan@2346506#Scan] |
| Cast Animation | 0 + 0 [corpus:liquipedia_dota2/scan@2346506#Scan] |
| Cast Range | Global [corpus:liquipedia_dota2/scan@2346506#Scan] |
| Radius | 900 [corpus:liquipedia_dota2/scan@2346506#Scan] |
| Scan Interval | 1 [corpus:liquipedia_dota2/scan@2346506#Scan] |
| Duration | 8 [corpus:liquipedia_dota2/scan@2346506#Scan] |
| Initial Charges | 1 [corpus:liquipedia_dota2/scan@2346506#Scan] |
| Other displayed values, in order | 210; 2; 0; 0 [corpus:liquipedia_dota2/scan@2346506#Scan] |

Scan does not begin a match with its maximum charges. [corpus:liquipedia_dota2/scan@2346506#Scan]

## Detection mechanics

Scan checks for enemy presence at 1-second intervals, beginning immediately when used and resulting in 9 checks. When a hero is detected, the green minimap indicator—blue in color-blind mode—turns red. Scan reports only whether any enemy heroes are present, not how many there are, and grants no vision or revelation beyond their presence. [corpus:liquipedia_dota2/scan@2346506#Scan]

Scan detects invisible enemies and enemy heroes affected by Smoke of Deceit. It treats illusions and the Spirit Bear as heroes, but does not consider invulnerable units, hidden units, or creep-heroes. [corpus:liquipedia_dota2/scan@2346506#Scan]

## Team controls

Alt+Left Click informs the team of Scan’s cooldown state. Alt+Ctrl+Left Click advises the team not to use it yet. [corpus:liquipedia_dota2/scan@2346506#Scan]

## Status effect

| Modifier | Application |
|---|---|
| `modifier_radar_thinker` | On hidden entity [corpus:liquipedia_dota2/scan@2346506#Scan] |

## Version history

| Version | Date | Changes |
|---|---|---|
| 7.39e | 2025-10-02 | Scan no longer triggers on creep-heroes. [corpus:liquipedia_dota2/scan@2346506#Version_History] |
| 7.38 | 2025-02-19 | Removed Telescope. [corpus:liquipedia_dota2/scan@2346506#Version_History] |
| 7.34 | 2023-08-08 | Scan now has 2 charges with a 210-second replenish time and starts with 1 charge when the match begins. [corpus:liquipedia_dota2/scan@2346506#Version_History] |
| 7.23 | 2019-11-26 | Created Telescope. Added Prescient Aura. Radius: 1200. Scan cooldown reduction: 50%. [corpus:liquipedia_dota2/scan@2346506#Version_History] |
| 7.20 | 2018-11-19 | Scan no longer ignores heroes inside Roshan’s pit. [corpus:liquipedia_dota2/scan@2346506#Version_History] |
| 7.03 | 2017-03-15 | Reduced cooldown from 270 to 210. [corpus:liquipedia_dota2/scan@2346506#Version_History] |
| 6.87 | 2016-04-25 | Created. [corpus:liquipedia_dota2/scan@2346506#Version_History] |

## Patch history

| Patch date | Changes |
|---|---|
| 21 May 2025 | Scan particle effects now also appear within the world rather than only on the minimap. Fixed the Scan icon sometimes being greyed out when charges were available. Fixed interfering multiple casts failing to draw their visual effects separately. [corpus:liquipedia_dota2/scan@2346506#Patch_History] |
| 06 Oct 2023 | Updated the Scan ability icon and backend strings. [corpus:liquipedia_dota2/scan@2346506#Patch_History] |
| 05 Oct 2023 — UPDATE 2 | Fixed Scan not showing its remaining charges when the charges were not full. [corpus:liquipedia_dota2/scan@2346506#Patch_History] |
| 24 Oct 2022 | Removed `dota_silent_scan`. [corpus:liquipedia_dota2/scan@2346506#Patch_History] |
| 22 Oct 2022 | Added `dota_silent_scan`. When set to 1 (true), it silences sound effects when Scan is initiated and when Scan detects enemy heroes. [corpus:liquipedia_dota2/scan@2346506#Patch_History] |
| 08 Aug 2019 | Scan could be Alt+Right Clicked to inform the team of its cooldown state. Ctrl+Right Click advised the team not to use it yet. [corpus:liquipedia_dota2/scan@2346506#Patch_History] |
| 01 Aug 2017 | The announcer received response rules for Scan usage. [corpus:liquipedia_dota2/scan@2346506#Patch_History] |
| 08 Jun 2017 | Added response rules for the right and wrong usage of Scan. [corpus:liquipedia_dota2/scan@2346506#Patch_History] |
| 01 Feb 2018 | Added the spectating view for Scan. [corpus:liquipedia_dota2/scan@2346506#Patch_History] |
| 12 Dec 2016 — UPDATE 5 | Updated Scan’s ability tooltips and hotkeys. [corpus:liquipedia_dota2/scan@2346506#Patch_History] |
| 02 Jul 2016 | Fixed Scan not working on spell-immune heroes. [corpus:liquipedia_dota2/scan@2346506#Patch_History] |
| 09 May 2016 | Adjusted Scan’s blue color in color-blind mode. [corpus:liquipedia_dota2/scan@2346506#Patch_History] |
| 06 May 2016 | Scan now supports color-blind mode. [corpus:liquipedia_dota2/scan@2346506#Patch_History] |
| 26 Apr 2016 — UPDATE 2 | Added a hotkey to activate Scan. [corpus:liquipedia_dota2/scan@2346506#Patch_History] |