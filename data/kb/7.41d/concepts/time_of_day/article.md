---
title: Time of Day
kind: concept
patch: 7.41d
card:
  entity: time_of_day
  sentences:
  - text: Time of day is a Dota 2 game-clock system whose 10-minute day is divided
      evenly between daytime and nighttime, changing vision, neutral-creep behavior,
      and abilities; heroes normally have 1800 daytime vision and 800 nighttime vision.
    marks:
    - corpus:liquipedia_dota2/time_of_day@2360236
    - corpus:liquipedia_dota2/time_of_day@2360236#Day-Night_Cycle
    - corpus:liquipedia_dota2/time_of_day@2360236#Neutral_Creeps
    - corpus:liquipedia_dota2/time_of_day@2360236#Vision
  - text: The clock starts after both factions’ heroes are shown, at -90 in regular
      matches and New_Player_Mode, -75 in Play vs Bots, -60 in Turbo, and 0 in Demo
      Hero.
    marks:
    - corpus:liquipedia_dota2/time_of_day@2360236
  - text: A match begins at night during pre-horn preparation; dawn starts at 0:00,
      night at 5:00, and the second day at 10:00.
    marks:
    - corpus:liquipedia_dota2/time_of_day@2360236#Day-Night_Cycle
  - text: Alt+Left Click on the clock prints the time in allied chat and indicates
      whether Bounty or Powerup runes are spawning soon.
    marks:
    - corpus:liquipedia_dota2/time_of_day@2360236#Day-Night_Cycle
  - text: Phoenix’s Supernova turns night into day for its duration and overrides
      nighttime caused by Eclipse or Dark Ascension.
    marks:
    - corpus:liquipedia_dota2/time_of_day@2360236#Game_Clock_Modifying_Abilities
  - text: Luna’s Eclipse and Night Stalker’s Dark Ascension each turn day into night
      for their duration.
    marks:
    - corpus:liquipedia_dota2/time_of_day@2360236#Game_Clock_Modifying_Abilities
  - text: Affected abilities include Lunar Blessing, Shapeshift, Tree Dance, Consume,
      Shade Sight, Void, Crippling Fear, and Hunter in the Night.
    marks:
    - corpus:liquipedia_dota2/time_of_day@2360236#Affected_Abilities
  - text: At night, every neutral creep except Roshan sleeps with aggro range 0 and
      must be damaged or targeted by a single-targeted ability to draw aggro.
    marks:
    - corpus:liquipedia_dota2/time_of_day@2360236#Neutral_Creeps
  - text: Vision talents can grant +500 Night Vision.
    marks:
    - corpus:liquipedia_dota2/time_of_day@2360236#Talents
  - text: No talent currently increases daytime vision.
    marks:
    - corpus:liquipedia_dota2/time_of_day@2360236#Talents
  - text: The server ticks every 0.033 seconds, and 1 server tick is the minimum ability
      duration.
    marks:
    - corpus:liquipedia_dota2/time_of_day@2360236#Server_Ticks
  - text: Version 7.38, dated 2025-02-19, removed the 15 movement speed units had
      gained at night.
    marks:
    - corpus:liquipedia_dota2/time_of_day@2360236#Version_History
---

# Time of Day

Time of day operates alongside the game clock, and certain mechanics behave differently according to the time of day. The clock starts after both factions’ heroes have been shown. [corpus:liquipedia_dota2/time_of_day@2360236]

| Game mode | Starting clock value |
|---|---:|
| Regular match | -90 [corpus:liquipedia_dota2/time_of_day@2360236] |
| Play vs Bots | -75 [corpus:liquipedia_dota2/time_of_day@2360236] |
| Turbo | -60 [corpus:liquipedia_dota2/time_of_day@2360236] |
| New_Player_Mode | -90 [corpus:liquipedia_dota2/time_of_day@2360236] |
| Demo Hero | 0 [corpus:liquipedia_dota2/time_of_day@2360236] |

New_Player_Mode starts at -90 despite using the Turbo ruleset. Item availability is not adjusted, so the additional preparation time makes items such as Aghanim's Shard available in the shop 30 seconds “earlier.” [corpus:liquipedia_dota2/time_of_day@2360236]

## Day-Night Cycle

The default HUD includes a Day/Night indicator. Each day is 10 minutes long and is divided evenly between daytime and nighttime. A match begins at nighttime during the pre-horn preparation phase. When the Radiant/Dire horn sounds and game time reaches 0:00, the first dawn begins; the first night begins at 5:00, the second day starts at 10:00, and the cycle continues. [corpus:liquipedia_dota2/time_of_day@2360236#Day-Night_Cycle]

Transitions have audio cues: nighttime is announced by a wolf’s howl, while daytime is announced by a bird’s tweet and a rooster’s crow. Custom maps may use their own versions of these cues. [corpus:liquipedia_dota2/time_of_day@2360236#Day-Night_Cycle]

At night, the map is darker and most units have reduced vision. Some heroes’ abilities are also modified according to the time of day, with Night Stalker being the most notable example. [corpus:liquipedia_dota2/time_of_day@2360236#Day-Night_Cycle]

Alt+Left Click on the clock prints the time in allied chat and indicates whether Bounty Rune and/or Powerup runes are spawning soon. [corpus:liquipedia_dota2/time_of_day@2360236#Day-Night_Cycle]

## Game Clock Modifying Abilities

The following abilities change the current time of day without pausing the day-night cycle. [corpus:liquipedia_dota2/time_of_day@2360236#Game_Clock_Modifying_Abilities]

| Hero | Ability | Effect and priority |
|---|---|---|
| Phoenix | Supernova | Turns night into day for its duration. It has higher priority than the nighttime caused by Eclipse and Dark Ascension. [corpus:liquipedia_dota2/time_of_day@2360236#Game_Clock_Modifying_Abilities] |
| Luna | Eclipse | Turns day into night for its duration. [corpus:liquipedia_dota2/time_of_day@2360236#Game_Clock_Modifying_Abilities] |
| Night Stalker | Dark Ascension | Turns day into night for its duration. [corpus:liquipedia_dota2/time_of_day@2360236#Game_Clock_Modifying_Abilities] |

### Affected Abilities

| Source | Ability |
|---|---|
| Luna | Lunar Blessing [corpus:liquipedia_dota2/time_of_day@2360236#Affected_Abilities] |
| Lycan | Shapeshift [corpus:liquipedia_dota2/time_of_day@2360236#Affected_Abilities] |
| Monkey King | Tree Dance [corpus:liquipedia_dota2/time_of_day@2360236#Affected_Abilities] |
| Moon Shard | Consume [corpus:liquipedia_dota2/time_of_day@2360236#Affected_Abilities] |
| Moon Shard | Shade Sight [corpus:liquipedia_dota2/time_of_day@2360236#Affected_Abilities] |
| Night Stalker | Void [corpus:liquipedia_dota2/time_of_day@2360236#Affected_Abilities] |
| Night Stalker | Crippling Fear [corpus:liquipedia_dota2/time_of_day@2360236#Affected_Abilities] |
| Night Stalker | Hunter in the Night [corpus:liquipedia_dota2/time_of_day@2360236#Affected_Abilities] |

## Neutral Creeps

At nighttime, every neutral creep except Roshan sleeps. Sleeping neutral creeps have an aggro range of 0 and therefore do not attack enemies merely for approaching them. They must be damaged or targeted by a single-targeted ability to draw their aggro. Apart from not drawing aggro automatically, they behave as they do during daytime. After de-aggroing, they return to sleep as soon as they reach their original camp position. Floating Zs identify sleeping creeps. [corpus:liquipedia_dota2/time_of_day@2360236#Neutral_Creeps]

## Vision

Heroes normally have 1800 daytime vision and 800 nighttime vision, except for the entries in the following supplied table. [corpus:liquipedia_dota2/time_of_day@2360236#Vision]

| Unit | Day | Night |
|---|---:|---:|
|  | 800 | 1800 [corpus:liquipedia_dota2/time_of_day@2360236#Vision] |
|  | 1800 | 1200 [corpus:liquipedia_dota2/time_of_day@2360236#Vision] |
|  | 1800 | 1200 [corpus:liquipedia_dota2/time_of_day@2360236#Vision] |
|  | 1800 | 1000 [corpus:liquipedia_dota2/time_of_day@2360236#Vision] |
|  | 1800 | 1000 [corpus:liquipedia_dota2/time_of_day@2360236#Vision] |
|  | 1800 | 1800 [corpus:liquipedia_dota2/time_of_day@2360236#Vision] |
|  | 1800 | 1400 [corpus:liquipedia_dota2/time_of_day@2360236#Vision] |

### Talents

Heroes can have a talent granting bonus vision. The talent table contains Left and Right positions at each listed level. [corpus:liquipedia_dota2/time_of_day@2360236#Talents]

| Level | Positions |
|---|---|
| Level 10 | Left; Right [corpus:liquipedia_dota2/time_of_day@2360236#Talents] |
| Level 15 | Left; Right [corpus:liquipedia_dota2/time_of_day@2360236#Talents] |
| Level 20 | Left; Right [corpus:liquipedia_dota2/time_of_day@2360236#Talents] |
| Level 25 | Left; Right [corpus:liquipedia_dota2/time_of_day@2360236#Talents] |

| Bonus | Value |
|---|---:|
| Night Vision | +500 [corpus:liquipedia_dota2/time_of_day@2360236#Talents] |

There are currently no talents that increase daytime vision. [corpus:liquipedia_dota2/time_of_day@2360236#Talents]

## Server Ticks

The game server ticks at 0.033-seconds, which is how often Dota2 sends data between the server and client. The minimum duration for an ability’s duration is 1-server tick. [corpus:liquipedia_dota2/time_of_day@2360236#Server_Ticks]

## Version History

| Version | Date | Description |
|---|---|---|
| 7.38 | 2025-02-19 | Units no longer gain 15 movement speed during the night. [corpus:liquipedia_dota2/time_of_day@2360236#Version_History] |
| 7.33 | 2023-04-20 | All units now gain 15 movement speed during the night. The effect is doubled for heroes, but it can be broken for 5 seconds upon attacking or taking damage from player-controlled sources, similar to Tranquil Boots. [corpus:liquipedia_dota2/time_of_day@2360236#Version_History] |
| 7.28 | 2020-12-17 | Matches now start at nighttime during the preparation phase and turn to day when the timer reaches 0:00. [corpus:liquipedia_dota2/time_of_day@2360236#Version_History] |
| 7.20 | 2018-11-19 | Increased daytime/nighttime length from 240 to 300. [corpus:liquipedia_dota2/time_of_day@2360236#Version_History] |
| 7.12 | 2018-03-29 | Supernova now turns night into day for its duration. It has higher priority than Darkness and Eclipse. [corpus:liquipedia_dota2/time_of_day@2360236#Version_History] |
| 6.83 | 2014-12-17 | Darkness no longer stops the day/night cycle anymore. [corpus:liquipedia_dota2/time_of_day@2360236#Version_History] |
| 6.79 | 2013-10-21 | Reduced daytime/nighttime length from 360 to 240. [corpus:liquipedia_dota2/time_of_day@2360236#Version_History] |
| 6.68 | 2026-07-25 | Reduced daytime/nighttime length from 480 to 360. [?] Eclipse now turns day into night for 10 seconds. [corpus:liquipedia_dota2/time_of_day@2360236#Version_History] |
| 6.63 | 2026-07-25 | Time of Day is now synchronized across all game modes. [corpus:liquipedia_dota2/time_of_day@2360236#Version_History] |
| 6.19b | 2026-07-25 | Fixed a rare bug with Darkness that caused permanent nighttime. [corpus:liquipedia_dota2/time_of_day@2360236#Version_History] |

## Patch History

| Patch | Description |
|---|---|
| 08 Aug 2019 | Alt+Left Click on the clock to print the time now also prints whether Bounty Rune and/or Powerup runes are spawning soon. [corpus:liquipedia_dota2/time_of_day@2360236#Patch_History] |
| 01 Feb 2018 | Added Alt+Left Click on the clock to print the time, indicating how much time is left on day or night. [corpus:liquipedia_dota2/time_of_day@2360236#Patch_History] |
| 13 Dec 2016 | Alt now displays the time pre-horn instead of only showing either daytime or nighttime. [corpus:liquipedia_dota2/time_of_day@2360236#Patch_History] |
| 13 Sep 2016 | U — Fixed rune spawn times and day-night-cycle offset in longer matches. [corpus:liquipedia_dota2/time_of_day@2360236#Patch_History] |
| 17 Dec 2014, Update 4 | Fixed Eclipse not turning day into night properly. [corpus:liquipedia_dota2/time_of_day@2360236#Patch_History] |
| 25 Sep 2014 | Alt+Left Click on the clock now prints the current game time. [corpus:liquipedia_dota2/time_of_day@2360236#Patch_History] |
| 07 Feb 2013 | Fixed day-night-cycle duration and the initial state being a bit off. [corpus:liquipedia_dota2/time_of_day@2360236#Patch_History] |
| 29 Sep 2011 | Updated and added a new day-night-cycle display. Added new sounds indicating daytime and nighttime. [corpus:liquipedia_dota2/time_of_day@2360236#Patch_History] |
| 20 May 2011 | Updated and cleaned up the visual transition between the day-night cycle. [corpus:liquipedia_dota2/time_of_day@2360236#Patch_History] |
| 16 Feb 2012 | Updated the day-night-cycle indicator. [corpus:liquipedia_dota2/time_of_day@2360236#Patch_History] |
| 14 Apr 2011 | Added the day-night-cycle indicator. [corpus:liquipedia_dota2/time_of_day@2360236#Patch_History] |