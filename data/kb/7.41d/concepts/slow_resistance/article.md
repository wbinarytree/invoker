---
title: Slow Resistance
kind: concept
patch: 7.41d
card:
  entity: slow_resistance
  sentences:
  - text: Slow resistance is a hero mechanic that reduces the impact of slows by a
      percentage, increases minimum movement speed by a percentage, and is distinct
      from status resistance.
    marks:
    - corpus:liquipedia_dota2/slow_resistance@2365304
  - text: Total percentage-based move-speed reductions equal current percentage-based
      reductions multiplied by ∏(1 − Slow Resistanceᵢ).
    marks:
    - corpus:liquipedia_dota2/slow_resistance@2365304#Equation
  - text: All slow-resistance sources stack multiplicatively, preventing stacked sources
      from reaching 100% slow resistance.
    marks:
    - corpus:liquipedia_dota2/slow_resistance@2365304#Stacking
  - text: In the Sange example, 25% slow resistance reduces Frost Blast’s 25% movement-speed
      slow to 18.75%.
    marks:
    - corpus:liquipedia_dota2/slow_resistance@2365304#Stacking
  - text: Level 3 God’s Strength at 40% and Sange at 25% combine to 55% slow resistance.
    marks:
    - corpus:liquipedia_dota2/slow_resistance@2365304#Stacking
  - text: That 55% resistance reduces a 25% movement-speed slow to 11.25%.
    marks:
    - corpus:liquipedia_dota2/slow_resistance@2365304#Stacking
  - text: Listed item bonuses include Abyssal Blade at +25%, Brawny Enchantment at
      +0/0/0/25%, Sange at +20%, Kaya and Sange at +25%, and Sange and Yasha at +25%.
    marks:
    - corpus:liquipedia_dota2/slow_resistance@2365304#Sources
  - text: Ability sources include Earth Element, Falcon Rush, Solid Core, Dead Shot,
      Guardian Sprint, God’s Strength, Insurmountable, and Overpower.
    marks:
    - corpus:liquipedia_dota2/slow_resistance@2365304#Sources
  - text: The listed innate sources are Roshan’s Strength of the Immortal and Warlock’s
      Chaotic Offering.
    marks:
    - corpus:liquipedia_dota2/slow_resistance@2365304#Sources
  - text: Affected slows include Flux, Battle Hunger, Poison Touch, Rot, Viper Strike,
      Arctic Burn, Poison Attack from Orb of Venom, and Freezing Aura from Shiva’s
      Guard.
    marks:
    - corpus:liquipedia_dota2/slow_resistance@2365304#Affected_by_Slow_Resistance
  - text: Version 7.34 on 2023-08-08 added slow resistance, multiplicative stacking,
      and the separation of movement-speed slows from status resistance.
    marks:
    - corpus:liquipedia_dota2/slow_resistance@2365304#Recent_Changes
  - text: Version 7.38 on 2025-02-19 made slow resistance also increase minimum movement
      speed by its percentage.
    marks:
    - corpus:liquipedia_dota2/slow_resistance@2365304#Recent_Changes
---

# Slow Resistance

Slow resistance reduces the impact of slows on a hero by a percentage and increases minimum movement speed by a percentage. It is distinct from status resistance. [corpus:liquipedia_dota2/slow_resistance@2365304]

## Equation

**Total Percentage-based Move Speed Reductions**  
= Current Percentage-based Move Speed Reductions × Slow Resistance Multiplier

**Slow Resistance Multiplier**  
= \(\prod_{i=1}^{n}(1-\text{Slow Resistance}_i)\) [corpus:liquipedia_dota2/slow_resistance@2365304#Equation]

## Stacking

All slow-resistance sources stack multiplicatively. A unit’s slow-resistance value therefore changes less when its slow resistance is higher and more when it is lower, preventing different stacked sources from reaching 100% slow resistance.

With Sange providing 25% slow resistance against Frost Blast’s 25% movement-speed slow:

\[
25\% \times (1-25\%)=18.75\%
\]

With level 3 God’s Strength providing 40% slow resistance, Sange providing 25%, and Frost Blast applying a 25% movement-speed slow:

\[
\text{Total Slow Resistance}
=1-(1-40\%)\times(1-25\%)
=55\%
\]

\[
\text{Actual Slow}
=25\%\times(1-55\%)
=11.25\%
\]

[corpus:liquipedia_dota2/slow_resistance@2365304#Stacking]

## Sources

### Ability sources

| Unit | Ability |
|---|---|
| Earth | Earth Element |
| Kez | Falcon Rush |
| Magnus | Solid Core |
| Muerta | Dead Shot |
| Roshan | On The Move |
| Ringmaster | Escape Act |
| Slardar | Guardian Sprint |
| Sven | God’s Strength |
| Tiny | Insurmountable |
| Ursa | Overpower |

[corpus:liquipedia_dota2/slow_resistance@2365304#Sources]

### Item sources

| Item | Slow resistance source |
|---|---|
| Abyssal Blade | +25% Slow Resistance |
| Boots of Bearing | Endurance |
| Brawny Enchantment | +0/0/0/25% Slow Resistance |
| Disperser | Suppress |
| Sange | +20% Slow Resistance |
| Kaya and Sange | +25% Slow Resistance |
| Sange and Yasha | +25% Slow Resistance |
| Unrelenting Eye | Relentless |

[corpus:liquipedia_dota2/slow_resistance@2365304#Sources]

### Innate sources

| Unit | Source |
|---|---|
| Roshan | Strength of the Immortal |
| Warlock | Chaotic Offering |

Source annotations may specify the following requirements:

| Annotation | Requirement |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim’s Scepter. |
| 2b | Requires Aghanim’s Shard. |

[corpus:liquipedia_dota2/slow_resistance@2365304#Sources]

## Affected slows

| Unit or item | Ability or effect |
|---|---|
| Arc Warden | Flux |
| Axe | Battle Hunger |
| Dazzle | Poison Touch |
| Death Prophet | Spirit Siphon |
| Enchantress | Untouchable |
| Invoker | Ghost Walk |
| Invoker | Ice Wall |
| Jakiro | Dual Breath |
| Jakiro | Liquid Fire |
| Lion | Mana Drain |
| Lycan Wolf | Cripple |
| Ogre Magi | Ignite |
| Omniknight | Degen Aura |
| Phoenix | Icarus Dive |
| Phoenix | Fire Spirits |
| Pudge | Rot |
| Queen of Pain | Shadow Strike |
| Silencer | Arcane Curse |
| Spiderling | Poison Sting |
| Templar Assassin | Psionic Trap |
| Tornado (Wildwing) | Tempest |
| Venomancer | Venomous Gale |
| Venomancer | Poison Sting |
| Viper | Poison Attack |
| Viper | Corrosive Skin |
| Viper | Viper Strike |
| Winter Wyvern | Arctic Burn |
| Wraith King | Wraithfire Blast |
| Orb of Venom | Poison Attack |
| Shiva’s Guard | Freezing Aura |

[corpus:liquipedia_dota2/slow_resistance@2365304#Affected_by_Slow_Resistance]

## Recent changes

| Version | Date | Description |
|---|---|---|
| 7.38 | 2025-02-19 | Now also increases min movement speed by the slow resistance percentage. `EXPR MinMS = MinMS * (1 + %SlowResist)` |
| 7.34 | 2023-08-08 | Added the Slow Resistance mechanic. The mechanic reduced the impact of movement-speed slow sources on a hero by a percentage and stacked multiplicatively. Status resistance no longer affected the impact of movement-speed slow sources. |

The following abilities were changed to grant a slow-resistance bonus in 7.34:

| Ability |
|---|
| Unholy Strength |
| Endurance |
| Rocket Barrage |
| Overcharge |
| God’s Strength |
| Grow |
| Overpower |
| Vindicator’s Axe |
| Warlock Golem |

[corpus:liquipedia_dota2/slow_resistance@2365304#Recent_Changes]