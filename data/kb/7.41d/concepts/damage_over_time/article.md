---
title: Damage Over Time
kind: concept
patch: 7.41d
card:
  entity: Damage Over Time
  sentences:
  - text: Damage Over Time (DoT) is an ability debuff that damages an affected unit
      at the end of each individually specified, hard-coded interval over an extended
      period.
    marks:
    - corpus:liquipedia_dota2/damage_over_time@2377716
  - text: The first interval begins when the ability affects the unit.
    marks:
    - corpus:liquipedia_dota2/damage_over_time@2377716
  - text: Some DoT abilities also deal initial damage, which may differ from their
      periodic damage.
    marks:
    - corpus:liquipedia_dota2/damage_over_time@2377716
  - text: Damage duration runs from the initial damage to the last damage instance.
    marks:
    - corpus:liquipedia_dota2/damage_over_time@2377716#Definition
  - text: Maximum total damage equals initial damage plus damage per instance multiplied
      by its instances.
    marks:
    - corpus:liquipedia_dota2/damage_over_time@2377716#Definition
  - text: Firefly deals 10/20/30/40 damage per interval, starting 0.1 seconds after
      cast.
    marks:
    - corpus:liquipedia_dota2/damage_over_time@2377716#Misc.
  - text: Firefly’s first interval is 0.4 seconds and its remaining intervals are
      0.5 seconds, resulting in 31 damage instances.
    marks:
    - corpus:liquipedia_dota2/damage_over_time@2377716#Misc.
  - text: Firefly can deal up to 310/620/930/1240 damage before reductions to one
      unit that remains in range for the full duration.
    marks:
    - corpus:liquipedia_dota2/damage_over_time@2377716#Misc.
  - text: Fire trails from successive Firefly casts fully stack.
    marks:
    - corpus:liquipedia_dota2/damage_over_time@2377716#Misc.
  - text: If Batrider dies during Firefly, existing ground fire remains for the remaining
      duration.
    marks:
    - corpus:liquipedia_dota2/damage_over_time@2377716#Misc.
  - text: The source table marks Berserker’s Call and Black Hole as requiring Aghanim’s
      Scepter.
    marks:
    - corpus:liquipedia_dota2/damage_over_time@2377716#Damage_Over_Time_Sources
  - text: Instant attacks and fixed-interval attacks ignore base attack time, attack
      speed, and attack rate and are not considered DoT abilities.
    marks:
    - corpus:liquipedia_dota2/damage_over_time@2377716#Fixed_Attack_Interval
---

# Damage Over Time

## Overview

Damage Over Time (DoT) is an ability debuff that damages the affected unit over an extended period. Damage is dealt at the end of each interval; the first interval begins when the ability affects the unit. Some abilities also deal initial damage, which may or may not equal their periodic damage. Every DoT ability has individually specified, hard-coded intervals. [corpus:liquipedia_dota2/damage_over_time@2377716]

## Definition

A DoT ability comprises several components that can produce different in-game interactions.

| Component | Definition |
|---|---|
| Initial Damage | Some abilities have different initial damage. For abilities that start immediately upon impact, initial damage is the same as damage per instance. |
| Interval | The time between instances in seconds. This value is usually hard-coded in the ability. |
| Damage Duration | Duration from the initial damage to the last damage instance. |
| Damage per Instance | The total damage excluding initial damage over the interval. |
| Number of Intervals | The damage duration over the interval. |
| Max Total Damage | The total of the initial damage and the damage per instance multiplied by its instances. [corpus:liquipedia_dota2/damage_over_time@2377716#Definition] |

## Debuff duration and expiration

Some DoT abilities continuously damage their target through a debuff. Reapplying most debuffs refreshes their duration unless otherwise noted. Depending on its expiration condition, a DoT debuff may last until the effect expires, be dispelled, or stop affecting a target that moves out of range or a specified radius; these conditions are stated in the ability’s notes.

### Firefly

Batrider takes to the skies and leaves a trail of flames. The fire damages enemies it touches and destroys trees below Batrider.

| Property | Value |
|---|---|
| Ability | No |
| Affects | Enemy Units / Self |
| Damage | Spell / Magical |
| Cast Animation | 0 + 0 |
| Initial Delay | 0.1 |
| Damage per Second | 20/40/60/80 (50/70/90/110) |
| First Interval | 0.4 |
| Subsequent Intervals | 0.5 |
| Movement | Grants self unobstructed movement and gradually increases Batrider’s movement speed over the entire duration. |
| Max Move Speed Bonus | 12%/18%/24%/30% (17%/23%/29%/35%) |
| Roshan | Immune to the ability’s damage component. |
| Other displayed values | 48/42/36/30; 100 [corpus:liquipedia_dota2/damage_over_time@2377716#Example] |

### Firefly interactions

- Damage is dealt to every enemy unit that enters the fire trail’s radius.
- It deals 10/20/30/40 damage per interval, starting 0.1 seconds after cast. The first interval is 0.4 seconds and the remaining intervals are 0.5 seconds, resulting in 31 damage instances.
- It can deal up to 310/620/930/1240 damage to a single unit before reductions if that unit remains in range for the full duration.
- Fire trails from successive casts fully stack. Each cast creates its own buff and fire trail.
- If Batrider dies during Firefly, existing ground fire remains for the remaining duration.
- The buffs remain visible in the HUD and become responsible only for maintaining the existing fire.
- If Batrider respawns before the buffs expire, they do not make him fly again or resume leaving fire behind. [corpus:liquipedia_dota2/damage_over_time@2377716#Misc.]

## Damage-over-time sources

| Source | Ability or effect | Marker | Requirement |
|---|---|---:|---|
| Alchemist | Acid Spray |  |  |
| Ancient Apparition | Cold Feet |  |  |
| Ancient Apparition | Ice Blast |  |  |
| Armlet of Mordiggian | Unholy Strength |  |  |
| Axe | Berserker's Call | 2a | Requires Aghanim's Scepter. |
| Axe | Battle Hunger |  |  |
| Arc Warden | Flux |  |  |
| Bane | Enfeeble |  |  |
| Bane | Fiend's Grip |  |  |
| Batrider | Firefly |  |  |
| Batrider | Flamebreak |  |  |
| Batrider | Flaming Lasso |  |  |
| Brewmaster | Cinder Brew |  |  |
| Broodmother | Spinner's Snare |  |  |
| Fire | Permanent Immolation |  |  |
| Cloak of Flames | Immolate |  |  |
| Clockwerk | Battery Assault |  |  |
| Crystal Maiden | Frostbite |  |  |
| Crystal Maiden | Freezing Field |  |  |
| Dark Willow | Bramble Maze |  |  |
| Dark Willow | Cursed Crown | 2b | Requires Aghanim's Shard. |
| Dazzle | Poison Touch |  |  |
| Death Prophet | Spirit Siphon |  |  |
| Disruptor | Thunder Strike |  |  |
| Disruptor | Static Storm |  |  |
| Doom | Scorched Earth |  |  |
| Doom | Infernal Blade |  |  |
| Doom | Doom |  |  |
| Dragon Knight | Fireball |  |  |
| Dragon Knight | Elder Dragon Form |  |  |
| Dragon Scale | Afterburn |  |  |
| Earth Spirit | Magnetize |  |  |
| Ember Spirit | Searing Chains |  |  |
| Ember Spirit | Flame Guard |  |  |
| Ember Spirit | Fire Remnant | 2b | Requires Aghanim's Shard. |
| Enigma | Malefice |  |  |
| Enigma | Midnight Pulse |  |  |
| Enigma | Black Hole | 2a | Requires Aghanim's Scepter. |
| Faceless Void | Time Dilation |  |  |
| Fallen Sky | Fallen Sky |  |  |
| Giant's Ring | Giant's Foot |  |  |
| Grimstroke | Phantom's Embrace |  |  |
| Grimstroke | Ink Swell |  |  |
| Gyrocopter | Rocket Barrage |  |  |
| Gyrocopter | Homing Missile | 2b | Requires Aghanim's Shard. |
| Huskar | Burning Spear |  |  |
| Invoker | Ice Wall |  |  |
| Invoker | Chaos Meteor |  |  |
| Jakiro | Dual Breath |  |  |
| Jakiro | Liquid Fire |  |  |
| Jakiro | Liquid Frost |  |  |
| Jakiro | Macropyre |  |  |
| Juggernaut | Blade Fury |  |  |
| Kunkka | Torrent |  |  |
| Kunkka | Torrent Storm |  |  |
| Kunkka | Ghostship |  |  |
| Leshrac | Diabolic Edict |  |  |
| Leshrac | Pulse Nova |  |  |
| Lone Druid | Entangle |  |  |
| Spirit Bear | Entangling Claws |  |  |
| Luna | Eclipse |  |  |
| Meteor Hammer | Meteor Hammer |  |  |
| Necrophos | Heartstopper Aura |  |  |
| Ogre Magi | Ignite |  |  |
| Orb of Venom | Poison Attack |  |  |
| Orb of Corrosion | Corrosion |  |  |
| Phoenix | Icarus Dive |  |  |
| Phoenix | Fire Spirits |  |  |
| Phoenix | Sun Ray |  |  |
| Phoenix | Supernova |  |  |
| Pudge | Rot |  |  |
| Pudge | Dismember |  |  |
| Pugna | Life Drain |  |  |
| Queen of Pain | Shadow Strike |  |  |
| Radiance | Burn |  |  |
| Razor | Eye of the Storm |  |  |
| Sand King | Sand Storm |  |  |
| Sand King | Epicenter |  |  |
| Shadow Shaman | Shackles |  |  |
| Silencer | Arcane Curse |  |  |
| Skywrath Mage | Mystic Flare |  |  |
| Slark | Dark Pact |  |  |
| Sniper | Shrapnel |  |  |
| Spiderling | Poison Sting |  |  |
| Spirit Vessel | Soul Release |  |  |
| Urn of Shadows | Soul Release |  |  |
| Witch Blade | Witch Blade |  |  |
| Tornado (Wildwing Ripper) | Tempest |  |  |
| Timbersaw | Flamethrower |  |  |
| Timbersaw | Chakram |  |  |
| Timbersaw | Second Chakram |  |  |
| Tiny | Avalanche |  |  |
| Treant Protector | Leech Seed |  |  |
| Treant Protector | Eyes In The Forest |  |  |
| Treant Protector | Nature's Guise | 2b | Requires Aghanim's Shard. |
| Treant Protector | Overgrowth |  |  |
| Tusk | Ice Shards | 2b | Requires Aghanim's Shard. |
| Underlord | Firestorm |  |  |
| Venomancer | Venomous Gale |  |  |
| Venomancer | Poison Sting |  |  |
| Venomancer | Noxious Plague |  |  |
| Viper | Poison Attack |  |  |
| Viper | Nethertoxin |  |  |
| Viper | Corrosive Skin |  |  |
| Viper | Viper Strike |  |  |
| Vhoul Assassin | Envenomed Weapon |  |  |
| Warlock | Shadow Word |  |  |
| Warlock Golem | Permanent Immolation |  |  |
| Weaver | The Swarm |  |  |
| Winter Wyvern | Arctic Burn |  |  |
| Witch Doctor | Maledict |  |  |
| Wraith King | Wraithfire Blast |  |  |
| Wraith King | Reincarnation | 1 | Requires talent. [corpus:liquipedia_dota2/damage_over_time@2377716#Damage_Over_Time_Sources] |

## Fixed Attack Interval

Abilities that perform instant attacks or attacks at fixed intervals completely ignore the unit’s base attack time, attack speed, and attack rate. Although they deal damage between intervals, they are not considered DoT abilities. [corpus:liquipedia_dota2/damage_over_time@2377716#Fixed_Attack_Interval]