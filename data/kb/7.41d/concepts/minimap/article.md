---
title: Minimap
kind: concept
patch: 7.41d
card:
  entity: minimap
  sentences:
  - text: The minimap is a HUD element that shows the game map at a smaller scale,
      with real-time locations and statuses of buildings, heroes, creeps, couriers,
      and wards subject to team vision and fog of war.
    marks:
    - corpus:liquipedia_dota2/minimap@2402552
  - text: Options control its interface side, team colors, background, and use of
      hero icons or names.
    marks:
    - corpus:liquipedia_dota2/minimap@2402552#Settings
  - text: Players see their personal courier with Radiant-style icons, allied couriers
      as green dots, and enemy couriers as white dots.
    marks:
    - corpus:liquipedia_dota2/minimap@2402552#Couriers
  - text: Friendly wards are green, or blue in colorblind mode, while enemy wards
      are red.
    marks:
    - corpus:liquipedia_dota2/minimap@2402552#Wards
  - text: Available Bounty Runes are always displayed, while other runes require vision.
    marks:
    - corpus:liquipedia_dota2/minimap@2402552#Runes
  - text: Scan detects enemy heroes in a targeted area and reports their presence
      through a minimap indicator and audio cues.
    marks:
    - corpus:liquipedia_dota2/minimap@2402552#Scanning
  - text: Scan has global cast range, 900 radius, 1 scan interval, 8 duration, and
      1 initial charge.
    marks:
    - corpus:liquipedia_dota2/minimap@2402552#Scanning
  - text: Right-clicking commands the hero to move to the selected location, but clicks
      are ignored for 0.2 seconds after the cursor enters the minimap.
    marks:
    - corpus:liquipedia_dota2/minimap@2402552#Controls
  - text: Ground-targeted abilities can be cast by clicking the minimap.
    marks:
    - corpus:liquipedia_dota2/minimap@2402552#Controls
  - text: Pings can notify teammates about locations, buildings, enemy heroes, or
      danger.
    marks:
    - corpus:liquipedia_dota2/minimap@2402552#Pinging
  - text: Holding Ctrl and Left Click while moving the cursor draws fading, player-colored
      lines visible to all allies.
    marks:
    - corpus:liquipedia_dota2/minimap@2402552#Drawing
---

# Minimap

The minimap is a HUD element representing the game map at a smaller scale. It shows the real-time location and status of buildings, heroes, creeps, couriers, and wards. Team vision applies: unseen areas are covered by the fog of war. Certain events and Terrain items can change its appearance. [corpus:liquipedia_dota2/minimap@2402552]

## Settings

These settings can be changed in the game options.

| Setting | Effect |
|---|---|
| Location | Displays the minimap at the bottom left or bottom right of the interface. |
| Simple Colors | Uses a single color for all heroes on the same team. |
| Hide Background | Hides the graphical background and displays only essential elements such as heroes, couriers, buildings, wards, and creeps. |
| Simple Background | Replaces the graphical background with a simple background. Turned on by default. |
| Draw Hero Icons | While holding `ALT`, displays hero icons instead of hero names. |
| Always Use Icons/Names | Permanently displays hero icons and names instead of arrows and Os. [corpus:liquipedia_dota2/minimap@2402552#Settings] |

## Icons

### Heroes

The minimap icon collection includes a **Heroes** category. [corpus:liquipedia_dota2/minimap@2402552#Heroes]

#### Other Units

The Heroes collection includes an **Other Units** category. [corpus:liquipedia_dota2/minimap@2402552#Other_Units]

#### Custom Icons

Some cosmetic items alter a hero’s minimap icon.

| Cosmetic category |
|---|
| Arcanas |
| Personas [corpus:liquipedia_dota2/minimap@2402552#Custom_Icons] |

### Shops

The black background shown with shop icons provides contrast and is not part of the icons.

| Shop | Status |
|---|---|
| Main Shop | |
| Side Lane Shop | (Removed) |
| Secret Shop | [corpus:liquipedia_dota2/minimap@2402552#Shops] |

### Couriers

Dire-side icons are used only while observing a game. For players, the personal courier uses Radiant-style icons; allied couriers appear as green dots and enemy couriers as white dots. Courier icons are organized into Radiant and Dire styles.

| Courier |
|---|
| Animal Courier |
| Flying Courier [corpus:liquipedia_dota2/minimap@2402552#Couriers] |

### Wards

Friendly wards are green, or blue in colorblind mode, while enemy wards are red. When spectating, Radiant wards are green or blue and Dire wards are red.

| Ward |
|---|
| Observer Ward |
| Sentry Ward [corpus:liquipedia_dota2/minimap@2402552#Wards] |

### Runes

Bounty Runes are always shown when available. Other runes are shown only when they are within vision.

| Rune |
|---|
| Arcane |
| Bounty |
| Amplify Damage |
| Haste |
| Illusion |
| Invisibility |
| Regeneration |
| Shield |
| Water |
| Wisdom [corpus:liquipedia_dota2/minimap@2402552#Runes] |

### Neutral Creep Camps

Camp icons are yellow in-game. Roshan’s icon is colored like Roshan.

| Element |
|---|
| Small camps |
| Medium camps |
| Large camps |
| Ancient camps |
| Roshan [corpus:liquipedia_dota2/minimap@2402552#Neutral_creep_camps] |

### Other Icons

| Element |
|---|
| Ancient |
| Attack Building |
| Defend Building |
| Eyes In The Forest |
| Fiend's Gate |
| Mango Tree [corpus:liquipedia_dota2/minimap@2402552#Others] |

#### Event Icons

| Event | Element |
|---|---|
| Frostivus 2012 | Greevil Hero |
| Frostivus 2012 | Thyg the Giftsnatch |
| Diretide | Pumpkin Bucket |
| New Bloom Festival | Year Beast |
| Wrath of the Mo'rokai | Mo'rokai |
| Aghanim's Labyrinth | Miniboss |
| Aghanim's Labyrinth | Aghanim [corpus:liquipedia_dota2/minimap@2402552#Events] |

## Scanning

Scan is an ability usable by any player. It scans a targeted area of the map and detects all enemy heroes within it. It is a point ability affecting self. The area is scanned for a few seconds, with a minimap indicator and audio cues reporting whether enemy heroes are present.

| Property | Value |
|---|---|
| Cast Animation | 0 + 0 |
| Cast Range | Global |
| Radius | 900 |
| Scan Interval | 1 |
| Duration | 8 |
| Initial Charges | 1 |

Scan does not begin a match with maximum charges.

| Listed value |
|---|
| 210 |
| 2 |
| 0 |
| 0 [corpus:liquipedia_dota2/minimap@2402552#Scanning] |

## Controls

- **Right Click:** Clicking anywhere on the minimap commands the hero to move there. Clicks are not registered for `0.2` seconds after entering the minimap, preventing miss-clicks.
- **Left Click while using Town Portal Scroll or Boots of Travel:** Teleports the hero to the allied building nearest the specified location.
- **Ground-targeted abilities:** Abilities such as Wrath of Nature can be cast by clicking the minimap. [corpus:liquipedia_dota2/minimap@2402552#Controls]

### Pinging

Pings send notifications to teammates.

| Input | Target | Result |
|---|---|---|
| `Alt` + `Left Click` | Minimap | Plays a sound and displays a ‼ Ping exclamation mark on teammates’ minimaps. |
| `Alt` + `Left Click` | Building | Plays a different sound according to the building’s alliance and generally requests its defense or attack. |
| `Alt` + `Left Click` | Enemy hero | Plays the same sound used for enemy buildings, typically announcing a desire to attack. |
| `Ctrl` + `Alt` + `Left Click` | Minimap | Plays a different sound and displays an ✖ Ping (Danger), generally indicating danger. [corpus:liquipedia_dota2/minimap@2402552#Pinging] |

### Drawing

Holding `Ctrl` + `Left Click` while moving the cursor over the minimap draws lines. All allied players can see them, and their color corresponds to the player’s color. The lines fade after a few seconds. [corpus:liquipedia_dota2/minimap@2402552#Drawing]

## Console Commands

Console commands can modify the minimap to suit individual preferences.

| Command | Default | Help text |
|---|---:|---|
| `dota_hud_extra_large_minimap 0` | `0` | Use extra large minimap. |
| `dota_minimap_hero_size` | `600` | Changes the hero minimap icon size. |
| `dota_minimap_misclick_time` | `0.2` | Minimum time after the mouse enters the minimap before accepting a move command. Can be increased slightly to prevent accidental misclicks. |
| `dota_minimap_ping_duration` | `3` | Adjust how long pings are displayed on the minimap. |
| `dota_minimap_disable_rightclick` | `0` | Disables right clicks on the minimap. |
| `dota_minimap_creep_scale` | `1` | Increase the size of creeps/neutrals/roshan icons on the minimap. [corpus:liquipedia_dota2/minimap@2402552#Console_Commands] |

## Gallery

### Current

| Style |
|---|
| Graphical |
| Simple [corpus:liquipedia_dota2/minimap@2402552#Current] |

### Pre-7.41

| Style |
|---|
| Graphical |
| Simple [corpus:liquipedia_dota2/minimap@2402552#Pre-7.41] |

### Pre-7.40

| Style |
|---|
| Graphical |
| Simple [corpus:liquipedia_dota2/minimap@2402552#Pre-7.40] |

### Pre-7.39

| Style |
|---|
| Graphical |
| Simple [corpus:liquipedia_dota2/minimap@2402552#Pre-7.39] |

### Pre-7.38

| Style |
|---|
| Graphical |
| Simple [corpus:liquipedia_dota2/minimap@2402552#Pre-7.38] |

### Pre-7.37

| Style |
|---|
| Graphical |
| Simple [corpus:liquipedia_dota2/minimap@2402552#Pre-7.37] |

### Pre-7.29

| Style |
|---|
| Graphical |
| Simple [corpus:liquipedia_dota2/minimap@2402552#Pre-7.29] |

### Pre-7.23

| Style |
|---|
| Graphical |
| Simple [corpus:liquipedia_dota2/minimap@2402552#Pre-7.23] |

### Pre-7.20

| Style |
|---|
| Graphical |
| Simple [corpus:liquipedia_dota2/minimap@2402552#Pre-7.20] |

### Pre-7.07

| Style |
|---|
| Graphical |
| Simple [corpus:liquipedia_dota2/minimap@2402552#Pre-7.07] |

### Pre-7.00

| Style |
|---|
| Default |
| Simple |
| Desert Terrain |
| Seasonal Terrain - Winter |
| Seasonal Terrain - Autumn [corpus:liquipedia_dota2/minimap@2402552#Pre-7.00] |

### Pre-6.86

| Style |
|---|
| Default |
| Simple |
| Winter (Frostivus) [corpus:liquipedia_dota2/minimap@2402552#Pre-6.86] |

### Pre-6.82

| Style |
|---|
| Default |
| Autumn (Diretide) |
| Winter (Frostivus) [corpus:liquipedia_dota2/minimap@2402552#Pre-6.82] |

### Tutorial

| Entry |
|---|
| Mechanics II [corpus:liquipedia_dota2/minimap@2402552#Tutorial] |

### Events

| Entry |
|---|
| Frostivus 2013 |
| Frostivus 2018 |
| New Bloom Festival 2014 |
| Dark Moon 2017 |
| Diretide 2020 [corpus:liquipedia_dota2/minimap@2402552#Events_2] |

#### Aghanim's Labyrinth

| Area | Status |
|---|---|
| Boss Island | (Unused) |
| Fodder Arena | (Unused) |
| Kerblam | (Unused) [corpus:liquipedia_dota2/minimap@2402552#Aghanim's_Labyrinth] |

### Artifact Hero Icons

This archive contains hero icons that appear in Artifact Card Game.

| Entry |
|---|
| Hero Icons [corpus:liquipedia_dota2/minimap@2402552#Artifact_Hero_Icons] |

### Monster Hunter Icons

The Dota 2 X Monster Hunter event created icons for palicos and poogies in the style of Dota 2’s heroes.

| Entry |
|---|
| Monster Hunter [corpus:liquipedia_dota2/minimap@2402552#Monster_Hunter_Icons] |

## Patch History

| Date | Description |
|---|---|
| 05 Aug 2025 | Updated attack ping particle effects. |
| 09 Jun 2025 | Adjusted ping volumes. |
| 21 May 2025 | Updated pinging and the pingwheel |
| 21 May 2025 | Updated attack and defense ping sound effects. |
| 21 May 2025 | Added "enemy ward here" ping, with a unique sound effect. |
| 21 May 2025 | Added "need ward here" ping, with a unique sound effect. |
| 21 May 2025 | Added "heart" ping, with a unique sound. |
| 21 May 2025 | Pinging an enemy hero as missing now uses the warning sound effect. |
| 21 May 2025 | Using the "on my way" ping now draws an estimation of the travel path on the minimap. |
| 21 May 2025 | Updated ping particle effects to be more informative, and added a lot more ping particle variants. |
| 21 May 2025 | Fixed the minimap teleport indicator not updating its position when teleporting to a unit and that unit is moving. |
| 25 Feb 2025 | Minor adjustments to the 7.38 maps. |
| 25 Feb 2025 | Simple map: zoomed in abit, and added Roshan Pits. |
| 25 Feb 2025 | Realistic map: added missing ramps above the Roshan Pits. |
| 19 Feb 2025 | Updated to match 7.38 map changes. |
| 20 Apr 2023 | Updated to match 7.33 map changes. |
| 09 Apr 2021 | Updated to match 7.29 map changes. |
| 29 Nov 2019 | Updated to match 7.23 map changes. |
| 19 Nov 2018 | Updated to match 7.20 map changes. |
| 01 Feb 2018 | Runes can now be ‼ Ping via the minimap. |
| 15 Feb 2017 | Fixed a bug with minimap rendering on some systems. |
| 14 Feb 2017 | Reduced minimap large version size has been from 296px x 296px to 280px x 280px. |
| 10 Feb 2017 | Reduced minimap size from 260px x 260px to 244px x 244px. |
| 12 Dec 2016 | Updated to match 7.00 map changes. |
| 25 Apr 2016 | Added Scan ability. |
| 24 Mar 2016 | Changed X's to arrows. |
| 16 Dec 2015 | Updated to match 6.86 map changes. |
| 16 Dec 2015 | Added Desert Terrain minimap. |
| 12 Feb 2015 | Left Click inputs on the minimap no longer ignores input for the first 0.2 seconds. |
| 25 Sep 2014 | Updated to match 6.82 map changes. [corpus:liquipedia_dota2/minimap@2402552#Patch_History] |