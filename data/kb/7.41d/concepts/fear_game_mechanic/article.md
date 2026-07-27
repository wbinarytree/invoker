---
title: Fear (Game Mechanic)
kind: concept
patch: 7.41d
card:
  entity: fear_game_mechanic
  sentences:
  - text: Fear and Hypnosis are hard disables that reject orders, fully disable affected
      units, and issue involuntary move orders every 0.1 seconds toward or away from
      designated units or points.
    marks:
    - corpus:liquipedia_dota2/fear_game_mechanic@2353559
    - corpus:liquipedia_dota2/fear_game_mechanic@2353559#Definition
    - corpus:liquipedia_dota2/fear_game_mechanic@2353559#Mechanics
  - text: Fountain Fear moves units toward a fixed point in front of their team fountain,
      while Neutral Creeps move toward their original spawn location.
    marks:
    - corpus:liquipedia_dota2/fear_game_mechanic@2353559#Mechanics
  - text: Caster Fear repeatedly targets a point 400 range from the affected unit,
      directly away from the source.
    marks:
    - corpus:liquipedia_dota2/fear_game_mechanic@2353559#Mechanics
  - text: Hypnosis forces units to approach a designated unit or point.
    marks:
    - corpus:liquipedia_dota2/fear_game_mechanic@2353559#Definition
  - text: Both effects cancel the current order, clear the order queue, and block
      new player or status-effect orders until expiration.
    marks:
    - corpus:liquipedia_dota2/fear_game_mechanic@2353559#Mechanics
  - text: Both effects always interrupt channeling, silence the unit, and disarm it.
    marks:
    - corpus:liquipedia_dota2/fear_game_mechanic@2353559#Mechanics
  - text: Expiration gives the unit a stop order, after which it remains still or
      auto-attacks according to player settings.
    marks:
    - corpus:liquipedia_dota2/fear_game_mechanic@2353559#Mechanics
  - text: Their regular move orders fully respect pathing, movement restrictions,
      and other disables.
    marks:
    - corpus:liquipedia_dota2/fear_game_mechanic@2353559#Mechanics
  - text: Affected units use no abilities or items to flee, and movement-speed increases
      and hastes apply unless the source fixes their speed.
    marks:
    - corpus:liquipedia_dota2/fear_game_mechanic@2353559#Mechanics
  - text: Concurrent Fear or Hypnosis instances compete equally, making the resulting
      movement direction random.
    marks:
    - corpus:liquipedia_dota2/fear_game_mechanic@2353559#Stacking
  - text: Hypnosis determines movement speed during stacking, with the slowest source
      used when multiple Hypnosis effects apply.
    marks:
    - corpus:liquipedia_dota2/fear_game_mechanic@2353559#Stacking
  - text: Taunt takes priority over Fear and Hypnosis, causing the disarmed unit to
      follow the Taunt source until the higher-priority effect ends.
    marks:
    - corpus:liquipedia_dota2/fear_game_mechanic@2353559#Stacking
---

# Fear and Hypnosis

Fear and Hypnosis are hard disables that fully disable affected units and force involuntary movement toward specific points. [corpus:liquipedia_dota2/fear_game_mechanic@2353559]

## Definition

Both effects reject every order given to affected units and force them to move involuntarily toward or away from a unit or point. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Definition]

| Subtype | Definition | Example |
|---|---|---|
| Fountain Fear | Forces units to flee toward their own fountain. | Terrorize [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Definition] |
| Caster Fear | Forces units to flee from the source of the fear debuff. | Requiem of Souls [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Definition] |
| Hypnosis | Forces units to approach a particular point or unit, usually—but not necessarily—the caster. | Wheel of Wonder [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Definition] |

## Mechanics

Fear and Hypnosis work almost identically. Both cancel the affected unit’s current order, clear its entire order queue, and prevent the player from issuing new orders until the effect expires. Forced orders from other status effects, including Taunt, are also prevented. Both effects therefore always interrupt channeling abilities, silence the unit, and disarm it. When the effect expires, the unit receives a stop order and either remains still until commanded or auto-attacks nearby enemies, depending on the player’s settings. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Mechanics]

The affected unit is forced to move toward a point determined by the source ability. This uses a regular move order rather than Forced Movement, so it fully respects pathing and movement restrictions, including other disables. Units do not cast abilities or use items to flee faster and rely solely on their movement speed. Movement-speed increases and hastes are not ignored unless the source ability fixes the unit’s movement at a particular value. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Mechanics]

### Fountain Fear

Fountain Fear issues move orders in 0.1 second intervals toward a fixed point directly in front of the affected unit’s team fountain. Neutral Creeps instead move toward their original spawn location. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Mechanics]

### Caster Fear

Caster Fear issues move orders in 0.1-second intervals directly away from a particular unit or point. Each order targets a point 400 range from the affected unit’s current location, at an angle based on that location and the unit or point being fled from. If a source unit suddenly teleports in front of the fleeing unit, subsequent orders make the affected unit flee in the other direction. Because the order uses a distance of 400, more distant pathing blockers are ignored until they come within 400 range. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Mechanics]

### Hypnosis

Hypnosis instead issues move orders toward a particular unit or point. It has the same restrictions as Fear and issues orders in 0.1-second intervals. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Mechanics]

## Stacking

When multiple instances of Fear and/or Hypnosis affect a target, every instance attempts to apply its effect equally, making the unit try to move in multiple directions simultaneously. The unit may stutter back and forth while effectively moving toward a middle ground, or it may move toward one source. The outcome is random and cannot be predetermined. Regardless of the outcome, the unit moves at the speed determined by Hypnosis; with multiple Hypnosis sources, it uses the slowest source. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Stacking]

Taunt always takes priority over Fear and Hypnosis. A unit affected by both does not move through the Fear or Hypnosis effect, but tries to attack the Taunt source. Its attacks remain disabled, effectively causing it to follow that source. If Fear or Hypnosis remains when Taunt expires, its movement effect resumes. If Taunt remains when Fear or Hypnosis expires, the unit begins attacking. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Stacking]

### Castable while feared

| Unit or system | Ability |
|---|---|
| Buildings | Glyph of Fortification [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Stacking] |
| Lifestealer | Consume [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Stacking] |
| Elder Titan | Move Astral Spirit [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Stacking] |
| Elder Titan | Return Astral Spirit [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Stacking] |
| Scan | Scan [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Stacking] |

## Sources

### Fountain Fear

| Unit | Ability | Requirement |
|---|---|---|
| Brewmaster | Cinder Brew | Requires talent.<sup>1</sup> [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Fountain_Fear] |
| Dark Willow | Terrorize | — [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Fountain_Fear] |
| Lone Druid | Savage Roar | — [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Fountain_Fear] |
| Spirit Bear | Savage Roar | — [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Fountain_Fear] |

| Marker | Requirement |
|---|---|
| 1 | Requires talent. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Fountain_Fear] |
| 2a | Requires Aghanim’s Scepter. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Fountain_Fear] |

### Caster Fear

| Unit | Ability | Requirement |
|---|---|---|
| Death Prophet | Spirit Siphon<sup>2b</sup> | Requires Aghanim’s Shard. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Caster_Fear] |
| Muerta | Dead Shot | — [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Caster_Fear] |
| Ringmaster | Tame the Beasts | — [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Caster_Fear] |
| Shadow Fiend | Requiem of Souls | — [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Caster_Fear] |
| Spectre | Reality<sup>2a</sup> | Requires Aghanim’s Scepter. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Caster_Fear] |
| Terrorblade | Terror Wave | — [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Caster_Fear] |

| Marker | Requirement |
|---|---|
| 2a | Requires Aghanim’s Scepter. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Caster_Fear] |
| 2b | Requires Aghanim’s Shard. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Caster_Fear] |

### Hypnosis

| Unit | Ability | Special behavior |
|---|---|---|
| Keeper of the Light | Will-O-Wisp<sup>4</sup> | Unlike other sources, permits attacking and using abilities and items while hypnotized, but locks turning. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Hypnosis] |
| Lich | Sinister Gaze | — [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Hypnosis] |
| Ringmaster | Wheel of Wonder | — [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Hypnosis] |
| Void Spirit | Aether Remnant | — [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Hypnosis] |

## Version history

| Version | Date | Change |
|---|---|---|
| 7.28 | 2020-12-17 | Scream of Pain no longer uses the Fear mechanic. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Version_History] |
| 7.28 | 2020-12-17 | Nether Swap no longer uses the Fear mechanic. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Version_History] |
| 7.27b | 2020-07-15 | Will-O-Wisp no longer applies hypnosis and instead applies a stun. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Version_History] |
| 7.25 | 2020-03-17 | Metamorphosis no longer applies fear to affected units within its radius upon transforming. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Version_History] |
| 7.25 | 2020-03-17 | Added the new Terror Wave ability, which uses the Fear mechanic. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Version_History] |
| 7.23 | 2019-11-26 | Added the new Aether Remnant ability, which uses the hypnosis mechanic. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Version_History] |
| 7.23 | 2019-11-26 | Requiem of Souls now uses the Fear mechanic. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Version_History] |
| 7.23 | 2019-11-26 | Nether Swap now uses the Fear mechanic. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Version_History] |
| 7.22 | 2019-05-24 | Metamorphosis now applies fear to affected units within its radius upon transforming. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Version_History] |
| 7.20 | 2018-11-19 | Added a new subtype to the Fear mechanic. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Version_History] |
| 7.20 | 2018-11-19 | Will-O-Wisp now uses the hypnosis mechanic. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Version_History] |
| 7.20 | 2018-11-19 | Sinister Gaze now uses the hypnosis mechanic. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Version_History] |
| 7.07 | 2017-10-31 | Terrorize now uses the Fear mechanic. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Version_History] |
| 7.07 | 2017-10-31 | Scream of Pain now uses the Fear mechanic. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Version_History] |
| 6.86 | 2015-12-16 | Added the Fear mechanic. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Version_History] |
| 6.86 | 2015-12-16 | Savage Roar now applies fear to affected units within its radius. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Version_History] |

## Patch history

| Patch | Change |
|---|---|
| 05 Aug 2025 | Hypnotized became an official overhead status effect. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Patch_History] |
| 05 Aug 2025 | Aether Remnant now uses the Hypnotized status effect. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Patch_History] |
| 05 Aug 2025 | Sinister Gaze now uses the Hypnotized status effect. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Patch_History] |
| 05 Aug 2025 | Wheel of Wonder now uses the Hypnotized status effect. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Patch_History] |
| 05 Aug 2025 | Will-O-Wisp now uses the Hypnotized status effect. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Patch_History] |
| 01 Feb 2018 | Fixed Fear not reliably forcing non-hero units to flee toward their fountain. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Patch_History] |
| 01 Feb 2018 | Fixed Fear making units stand still when their last command was stop/halt. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Patch_History] |
| 14 Nov 2017, Update 2 | Fear now interrupts Charge of Darkness. [corpus:liquipedia_dota2/fear_game_mechanic@2353559#Patch_History] |