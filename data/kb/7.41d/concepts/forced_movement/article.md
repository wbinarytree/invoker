---
title: Forced Movement
kind: concept
patch: 7.41d
card:
  entity: forced_movement
  sentences:
  - text: Forced Movement is a status effect with two types—non-disabling and fully
      disabling—that changes a unit’s position independently of movement speed and
      continues while the unit is disabled.
    marks:
    - corpus:liquipedia_dota2/forced_movement@2357980
    - corpus:liquipedia_dota2/forced_movement@2357980#Mechanics
  - text: Fully disabling movement behaves like a stun, while non-disabling movement
      prevents moving but permits actions such as turning, attacking, and casting
      abilities or items.
    marks:
    - corpus:liquipedia_dota2/forced_movement@2357980#Definition
  - text: Movement orders issued during forced movement are not canceled, so the unit
      moves toward the ordered destination after the effect expires.
    marks:
    - corpus:liquipedia_dota2/forced_movement@2357980#Mechanics
  - text: Forced movement generally passes straight through terrain and obstacles,
      although some abilities impose custom restrictions.
    marks:
    - corpus:liquipedia_dota2/forced_movement@2357980#Mechanics
  - text: Effects on the same plane do not stack, and new horizontal forced movement
      completely cancels existing horizontal forced movement.
    marks:
    - corpus:liquipedia_dota2/forced_movement@2357980#Mechanics
  - text: Horizontal and vertical forced movement can affect a unit simultaneously,
      producing parabolic motion.
    marks:
    - corpus:liquipedia_dota2/forced_movement@2357980#Mechanics
  - text: Forced movement is bound to its ability modifier, so dispelling a dispellable
      modifier stops the movement.
    marks:
    - corpus:liquipedia_dota2/forced_movement@2357980
  - text: Forced movement overrides pulling regardless of the source abilities’ cast
      order.
    marks:
    - corpus:liquipedia_dota2/forced_movement@2357980#Pulling
  - text: A unit’s Z-position affects projectile travel time because projectiles fly
      toward the unit’s center.
    marks:
    - corpus:liquipedia_dota2/forced_movement@2357980#Upward_Movement
  - text: A lane creep killed by a player-controlled unit is knocked up to 200 range
      from the damage source in an arc reaching up to 50 range upward.
    marks:
    - corpus:liquipedia_dota2/forced_movement@2357980#Lane_Creeps
  - text: Lane-creep death knockback lasts between 0.4 and 0.6 seconds.
    marks:
    - corpus:liquipedia_dota2/forced_movement@2357980#Lane_Creeps
  - text: Knockback Resistance reduces the distance heroes are pushed by many enemy
      status debuffs, and every unit has a base value of 0.
    marks:
    - corpus:liquipedia_dota2/forced_movement@2357980#Knockback_Resistance
---

# Forced Movement

Forced Movement is a status effect that changes a unit’s position independently of movement speed and continues while the unit is disabled. Most forced-movement abilities prevent the affected unit from acting, although some permit attacking, turning, and casting abilities or items. Almost all forced-movement effects override one another: the later effect nullifies the previous effect, with a few exceptions. Forced movement is bound to the ability’s buff or debuff, so dispelling a dispellable modifier also stops its forced movement. [corpus:liquipedia_dota2/forced_movement@2357980]

## Definition

| Type | Definition | Example |
|---|---|---|
| Fully Disabling | Behaves like a stun, preventing the unit from performing any action but allowing actions to continue once the effect expires. | Meat Hook affecting enemies |
| Non-disabling | Prevents moving but permits other actions, including turning, attacking depending on the situation, and casting abilities or items. | Meat Hook affecting allies |
| Upward Movement | Moves a unit upward, changing its Z-position. | Cyclone Sources |
| Pulling | Allows normal movement but affects its speed depending on the movement direction. | Gale Force |

[corpus:liquipedia_dota2/forced_movement@2357980#Definition]

## Mechanics

Forced movement has two types: non-disabling and fully disabling. Movement orders can still be issued, but the forced movement completely negates attempts to move. These orders are not canceled, so the unit moves toward the ordered destination once the effect expires.

Forced movement generally ignores terrain and other obstacles, moving the unit straight through them similarly to unobstructed movement. Some abilities have custom restrictions, such as Rolling Thunder bouncing off cliffs.

Forced-movement effects on the same planes do not stack: the X- and Y-axis form the horizontal plane, while the Z-axis is the vertical plane. Applying new horizontal forced movement to a unit already moving horizontally cancels the previous effect completely. A unit can be affected by two sources when one applies vertical movement and the other horizontal movement, producing parabolic motion.

Some abilities that do not themselves apply forced movement can interrupt it. [corpus:liquipedia_dota2/forced_movement@2357980#Mechanics]

| Ability able to cancel forced movement |
|---|
| Faceless Void – Chronosphere |
| Faceless Void – Time Zone |
| Grimstroke – Soulbind<sup>2</sup> |
| Pudge – Dismember |
| Slark – Pounce<sup>2</sup> |

| Marker | Condition |
|---|---|
| 1 | Requires talent. |
| 2 | Soulbind and Pounce cancel forced movement upon expiring, not upon being applied. |

[corpus:liquipedia_dota2/forced_movement@2357980#Mechanics]

## Lane Creeps

When a lane creep dies to a player-controlled unit, it is knocked up to 200 range away from the damage source in an arc reaching up to 50 range upward. Distance and height increase with the killing damage instance, capped at 500, but remain randomized so equal damage instances do not always produce equal distances. Knockback lasts between 0.4 and 0.6 seconds, while damage below 100 causes no knockback.

This knockback is mainly aesthetic but can affect abilities. Thunder Strike and Leech Seed, for example, follow the unit’s corpse with their effects. [corpus:liquipedia_dota2/forced_movement@2357980#Lane_Creeps]

## Fully Disabling Forced Movement

The following abilities disable units while moving them. [corpus:liquipedia_dota2/forced_movement@2357980#Fully_Disabling_Forced_Movement]

| Disabled aspect and target | Ability |
|---|---|
| Stun [Enemy] | Batrider – Flaming Lasso |
| Stun [Enemy] | Beastmaster – Primal Roar |
| Stun [Enemy] | Clockwerk – Power Cogs |
| Stun [Enemy] | Dark Seer – Vacuum |
| Stun [Enemy] | Enigma – Black Hole |
| Stun [Enemy] | Kunkka – Torrent |
| Stun [Enemy] | Lion – Earth Spike |
| Stun [Enemy] | Magnus – Skewer (Skewered Hero) |
| Stun [Enemy] | Magnus – Horn Toss |
| Stun [Enemy] | Marci – Dispose |
| Stun [Enemy] | Mars – Spear of Mars (Skewered Hero) |
| Stun [Enemy] | Morphling – Adaptive Strike |
| Stun [Enemy] | Nyx Assassin – Impale |
| Stun [Enemy] | Pangolier – Rolling Thunder |
| Stun [Enemy] | Pudge – Dismember |
| Stun [Enemy] | Pudge – Meat Hook<sup>4</sup> |
| Stun [Enemy] | Primal Beast – Onslaught |
| Stun [Enemy] | Primal Beast – Pulverize |
| Stun [Enemy] | Rubick – Telekinesis |
| Stun [Enemy] | Sand King – Burrowstrike |
| Stun [Enemy] | Snapfire – Firesnap Cookie |
| Stun [Enemy] | Snapfire – Spit Out |
| Stun [Enemy] | Spirit Breaker – Greater Bash |
| Stun [Enemy] | Storm Spirit – Electric Vortex |
| Stun [Enemy] | Tidehunter – Ravage |
| Stun [Enemy] | Tiny – Toss |
| Stun [Enemy] | Tusk – Walrus Kick |
| Stun [Enemy] | Tusk – Walrus PUNCH! |
| Stun [Enemy] | Eul's Scepter of Divinity – Cyclone |
| Stun [Enemy] | Wind Waker – Cyclone |
| Stun [Enemy] | Invoker – Tornado |
| Stun [Enemy] | Storm – Cyclone |
| Can't Act [Enemy] | Lich – Sinister Gaze |
| Can't Act [Enemy] | Ringmaster – Wheel of Wonder |
| Can't Act [Enemy] | Void Spirit – Aether Remnant |
| Silence [Enemy] | Snapfire – Gobble Up |
| Stun [Ally/Self] | Brewmaster – Primal Split |
| Stun [Ally/Self] | Earthshaker – Enchant Totem<sup>2a</sup> |
| Stun [Ally/Self] | Faceless Void – Time Walk |
| Stun [Ally/Self] | Faceless Void – Reverse Time Walk |
| Stun [Ally/Self] | Kez – Grappling Claw |
| Stun [Ally/Self] | Marci – Rebound |
| Stun [Ally/Self] | Marci – Rebound (Alt-Cast) |
| Stun [Ally/Self] | Monkey King – Tree Dance |
| Stun [Ally/Self] | Monkey King – Boundless Strike (Alt-Cast) |
| Stun [Ally/Self] | Monkey King – Primal Spring |
| Stun [Ally/Self] | Pangolier – Swashbuckle |
| Stun [Ally/Self] | Pangolier – Shield Crash |
| Stun [Ally/Self] | Rubick – Telekinesis<sup>2b</sup> |
| Stun [Ally/Self] | Sand King – Burrowstrike |
| Stun [Ally/Self] | Snapfire – Firesnap Cookie |
| Stun [Ally/Self] | Snapfire – Spit Out |
| Stun [Ally/Self] | Sven – Storm Hammer (Alt-Cast) |
| Stun [Ally/Self] | Techies – Blast Off! |
| Stun [Ally/Self] | Tiny – Toss |
| Stun [Ally/Self] | Viper – Nosedive |
| Stun [Ally/Self] | Eul's Scepter of Divinity – Cyclone |
| Stun [Ally/Self] | Wind Waker – Cyclone |
| Can't Act [Ally/Self] | Lifestealer – Infest |
| Can't Act [Ally/Self] | Magnus – Skewer |
| Can't Act [Ally/Self] | Tusk – Snowball |
| Silence [Ally] | Snapfire – Gobble Up |

| Marker | Condition |
|---|---|
| 4 | If interrupted, the unit is forcefully teleported to the ability’s cast location after the hook returns. |

[corpus:liquipedia_dota2/forced_movement@2357980#Fully_Disabling_Forced_Movement]

## Non-disabling Forced Movement

These abilities do not fully disable units while moving them. Some do not disable at all, while others disable only partially. [corpus:liquipedia_dota2/forced_movement@2357980#Non-disabling_Forced_Movement]

| Target | Non-disabling forced-movement source |
|---|---|
| Enemy | Batrider – Flamebreak |
| Enemy | Beastmaster – Primal Roar |
| Enemy | Bloodseeker – Rupture<sup>3</sup> |
| Enemy | Drow Ranger – Gust |
| Enemy | Earth Spirit – Boulder Smash |
| Enemy | Enigma – Black Hole<sup>2a</sup> |
| Enemy | Force Staff – Force |
| Enemy | Hurricane Pike – Hurricane Thrust |
| Enemy | Huskar – Inner Fire |
| Enemy | Invoker – Deafening Blast |
| Enemy | Keeper of the Light – Blinding Light |
| Enemy | Keeper of the Light – Will-O-Wisp |
| Enemy | Kunkka – Tidal Wave |
| Enemy | Magnus – Shockwave |
| Enemy | Mars – Arena of Blood |
| Enemy | Mars – God's Rebuke |
| Enemy | Mars – Spear of Mars |
| Enemy | Puck – Waning Rift<sup>3</sup> |
| Enemy | Queen of Pain – Sonic Wave |
| Enemy | Sniper – Headshot |
| Enemy | Wildwing Ripper – Hurricane |
| Ally/Self | Bloodseeker – Rupture<sup>3</sup> |
| Ally/Self | Clockwerk – Hookshot |
| Ally/Self | Crystal Maiden – Crystal Clone |
| Ally/Self | Dawnbreaker – Converge |
| Ally/Self | Earth Spirit – Boulder Smash |
| Ally/Self | Earth Spirit – Rolling Boulder |
| Ally/Self | Ember Spirit – Activate Fire Remnant |
| Ally/Self | Enchantress – Sproink |
| Ally/Self | Force Staff – Force |
| Ally/Self | Hurricane Pike – Hurricane Thrust |
| Ally/Self | Huskar – Life Break |
| Ally/Self | Io – Tether |
| Ally/Self | Mirana – Leap |
| Ally/Self | Morphling – Waveform |
| Ally/Self | Pangolier – Shield Crash |
| Ally/Self | Pangolier – Rolling Thunder |
| Ally/Self | Phoenix – Icarus Dive |
| Ally/Self | Phoenix – Toggle Movement |
| Ally/Self | Pudge – Meat Hook<sup>4</sup> |
| Ally/Self | Primal Beast – Onslaught |
| Ally/Self | Ringmaster – Whoopee Cushion |
| Ally/Self | Slark – Pounce |
| Ally/Self | Spirit Breaker – Charge of Darkness |
| Ally/Self | Storm Spirit – Ball Lightning |
| Ally/Self | Timbersaw – Timber Chain |
| Ally/Self | Ursa – Earthshock |
| Ally/Self | Wildwing Ripper – Hurricane |
| Ally/Self | Zeus – Heavenly Jump |

| Marker | Condition |
|---|---|
| 4 | If interrupted, the unit is forcefully teleported to the ability’s cast location after the hook returns. |

[corpus:liquipedia_dota2/forced_movement@2357980#Non-disabling_Forced_Movement]

## Pulling

Forced-movement sources generally ignore terrain and other obstacles, moving units through everything toward the intended direction. Certain pulling sources can move affected targets through impassable terrain but do not grant unobstructed movement.

A unit’s movement speed can affect pulling. If the pulling direction matches the movement direction, the unit may be pulled faster. Forced movement has higher priority than pulling and overrides pulling regardless of the source abilities’ cast order. [corpus:liquipedia_dota2/forced_movement@2357980#Pulling]

| Pulling source |
|---|
| Enigma – Black Hole<sup>2a</sup> |
| Invoker – E.M.P.<sup>2b 3</sup> |
| Naga Siren – Reel In |
| Windranger – Gale Force |

| Marker | Condition |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |

[corpus:liquipedia_dota2/forced_movement@2357980#Pulling]

## Upward Movement

Several abilities move units upward by changing their Z-position. A unit’s Z-position affects projectile travel time because projectiles always fly toward the unit’s center. It also affects the unit’s ability to block other units’ pathing because one unit can block another only when both have roughly the same Z-position.

Height does not affect abilities that affect or search for units within an area. A unit thrown into the air by Torrent remains fully affected by area abilities such as Impale. Attacks also disregard the target’s height. Although attack projectiles must travel farther to reach an elevated target, a unit with 600 range can begin attacking an airborne unit from 600 range away.

The following list includes only abilities that move units upward. [corpus:liquipedia_dota2/forced_movement@2357980#Upward_Movement]

| Upward Movement (Z-axis) source |
|---|
| Batrider – Flamebreak |
| Earthshaker – Enchant Totem<sup>2a</sup> |
| Enchantress – Sproink |
| Kunkka – Torrent |
| Lion – Earth Spike |
| Magnus – Horn Toss |
| Mirana – Leap |
| Monkey King – Tree Dance |
| Monkey King – Primal Spring |
| Nyx Assassin – Impale |
| Pangolier – Shield Crash |
| Pangolier – Rolling Thunder |
| Rubick – Telekinesis |
| Sand King – Burrowstrike |
| Slark – Pounce |
| Snapfire – Firesnap Cookie |
| Snapfire – Spit Out |
| Spirit Breaker – Greater Bash |
| Techies – Blast Off! |
| Tidehunter – Ravage |
| Tiny – Toss |
| Tusk – Walrus Kick |
| Tusk – Walrus PUNCH! |
| Ursa – Earthshock |
| Eul's Scepter of Divinity – Cyclone |
| Wind Waker – Cyclone |
| Invoker – Tornado |
| Storm – Cyclone |

| Marker | Condition |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |

[corpus:liquipedia_dota2/forced_movement@2357980#Upward_Movement]

## Knockback Resistance

Knockback Resistance is a hero attribute that reduces the distance the hero is pushed by many enemy status debuffs. Every unit has a base knockback resistance of 0 by default. Knockback Resistance is currently granted only by the tier 4 Tough Enchantment and Solid Core. [corpus:liquipedia_dota2/forced_movement@2357980#Knockback_Resistance]

| Ability affected by Knockback Resistance |
|---|
| Batrider – Flamebreak |
| Beastmaster – Primal Roar |
| Bloodseeker – Bloodrage<sup>1</sup> (Arterial Spray) |
| Clockwerk – Power Cogs |
| Disruptor – Electromagnetic Repulsion |
| Drow Ranger – Gust |
| Earth Spirit – Boulder Smash |
| Keeper of the Light – Blinding Light |
| Invoker – Deafening Blast |
| Kunkka – Tidal Wave |
| Magnus – Shockwave |
| Mars – Arena of Blood |
| Mars – God's Rebuke |
| Morphling – Adaptive Strike |
| Primal Beast – Pulverize |
| Puck – Waning Rift<sup>1</sup> (Jostling Rift) |
| Queen of Pain – Sonic Wave |
| Sniper – Concussive Grenade |
| Sniper – Headshot |
| Spirit Breaker – Greater Bash |
| Tusk – Walrus Kick |
| Force Staff – Force |
| Hurricane Pike – Hurricane Thrust |

| Marker | Condition |
|---|---|
| 1 | Requires facet. |

[corpus:liquipedia_dota2/forced_movement@2357980#Knockback_Resistance]