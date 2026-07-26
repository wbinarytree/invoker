---
title: Hero Animations
kind: concept
patch: 7.41d
card:
  entity: hero_animations
  sentences:
  - text: Hero animations determine how a Hero moves in-game and may differ within
      the same scenario; Injured animations apply below 25% max health, and Overkill
      plays when fatal damage exceeds 33% of max health.
    marks:
    - corpus:liquipedia_dota2/hero_animations@2317981
    - corpus:liquipedia_dota2/hero_animations@2317981#Injured
    - corpus:liquipedia_dota2/hero_animations@2317981#Overkill
  - text: Aggressive Idle and Walk/Jog/Run animations require vision over an enemy
      Hero and proximity within the trigger range.
    marks:
    - corpus:liquipedia_dota2/hero_animations@2317981#Aggressive
  - text: Most melee Heroes trigger aggressive animations at 600 range, while ranged
      Heroes use ranges of 800, 850, or 900.
    marks:
    - corpus:liquipedia_dota2/hero_animations@2317981#Melee
    - corpus:liquipedia_dota2/hero_animations@2317981#Ranged
  - text: Enemy aggressive animations can indicate vision; invisible Heroes trigger
      them after exposure by True Sight or enemy high-ground vision.
    marks:
    - corpus:liquipedia_dota2/hero_animations@2317981#Ranged
  - text: Attack animations may vary with the Hero’s max health, current attack speed,
      or enemy proximity.
    marks:
    - corpus:liquipedia_dota2/hero_animations@2317981#Attack
  - text: Attack-speed-tagged Heroes may progress through Base < Fast < Faster < Fastest
      < Super Fast < Mega Fast Animation.
    marks:
    - corpus:liquipedia_dota2/hero_animations@2317981#Attack
  - text: Attack-range-tagged Heroes may progress through Closest < Close/Short <
      Medium/Normal < Long.
    marks:
    - corpus:liquipedia_dota2/hero_animations@2317981#Attack
  - text: Channel animations play while a Hero channels an ability lacking a specialized
      animation.
    marks:
    - corpus:liquipedia_dota2/hero_animations@2317981#Channel
  - text: Chase animations play when pursuing a low-health enemy unit, neutral unit,
      or allied unit in deny range.
    marks:
    - corpus:liquipedia_dota2/hero_animations@2317981#Chase
  - text: 'Not every stun source triggers Stun/Disable: some trigger Flail, while
      listed exceptions freeze the Hero in place.'
    marks:
    - corpus:liquipedia_dota2/hero_animations@2317981#Stun/Disable
  - text: When a unit is hasted, its Run animation is replaced by its Haste animation.
    marks:
    - corpus:liquipedia_dota2/hero_animations@2317981#Haste
  - text: Movement-speed-tagged Heroes may progress through Walk < Run < Run Fast/Sprint
      < Haste.
    marks:
    - corpus:liquipedia_dota2/hero_animations@2317981#Walk/Jog/Run
---

# Hero Animations

Hero animations determine how a Hero moves in game. They vary by situation, and a Hero can have different animations for the same scenario. [corpus:liquipedia_dota2/hero_animations@2317981]

## Aggressive

Aggressive animations are used near enemies and exist for the Idle and Walk/Jog/Run animation sets. Not every Hero has them. [corpus:liquipedia_dota2/hero_animations@2317981#Aggressive]

Both conditions are required:

| Condition |
|---|
| Have vision over the enemy |
| Be within a certain range of the enemy Hero |
[corpus:liquipedia_dota2/hero_animations@2317981#Aggressive]

### Melee

Most melee Heroes have an aggressive-animation trigger range of 600. [corpus:liquipedia_dota2/hero_animations@2317981#Melee]

| Hero type | Range |
|---|---:|
| Melee Heroes | 600 |
[corpus:liquipedia_dota2/hero_animations@2317981#Melee]

### Ranged

| Hero type | Range |
|---|---:|
| Ranged Heroes | 800 |
| Ranged Heroes | 850 |
| Ranged Heroes | 900 |
[corpus:liquipedia_dota2/hero_animations@2317981#Ranged]

Enemy aggressive animations can indicate whether that enemy has vision over the Hero. For invisible Heroes, the animations trigger once they are exposed by True Sight and/or when the enemy gains high-ground vision over them, such as through a high-ground Observer Ward. [corpus:liquipedia_dota2/hero_animations@2317981#Ranged]

## Attack

Heroes can have multiple attack animations when attacking a unit. The animation may change according to the following factors. [corpus:liquipedia_dota2/hero_animations@2317981#Attack]

| Factor |
|---|
| Hero’s max health |
| Current attack speed |
| Enemy proximity |
[corpus:liquipedia_dota2/hero_animations@2317981#Attack]

Heroes whose attack animations vary with attack speed are tagged with `AttackSpeedActivityModifiers` in their Hero attributes and may use this progression:

| Attack-speed animation progression |
|---|
| Base < Fast < Faster < Fastest < Super Fast < Mega Fast Animation |
[corpus:liquipedia_dota2/hero_animations@2317981#Attack]

| Attack-speed activity table entry |
|---|
| 180 |
| 300 |
| 170 |
| 275 |
| 375 |
| 170 |
| 200 |
| 150 |
| 190 |
| 220 |
| 300 |
| 420 |
| 200 |
| 300 |
| 140 |
| 180 |
| 250 |
| 350 |
| 150 |
| 240 |
| 330 |
| 150 |
| 170 |
| 275 |
| 350 |
| ( and ) |
| 150 |
| 250 |
| 170 |
| 250 |
| 300 |
| 140 |
| 180 |
| 230 |
| 300 |
| 180 |
| 250 |
| 145 |
| 195 |
| 350 |
| 190 |
| 300 |
| 200 |
| 350 |
| 175 |
| 275 |
| 360 |
| 170 |
| 320 |
| 266 |
| 376 |
| 487 |
| 130 |
| 200 |
| 200 |
| 320 |
| 430 |
| 142 |
| 275 |
| 350 |
| 150 |
| 200 |
| 155 |
| 205 |
| 300 |
| 175 |
| 250 |
| 350 |
[corpus:liquipedia_dota2/hero_animations@2317981#Attack]

Not every listed Hero has a unique animation for different attack speeds. [corpus:liquipedia_dota2/hero_animations@2317981#Attack]

Heroes whose animations vary with attack range are tagged with `AttackRangeActivityModifiers` in their Hero attributes and may use this progression:

| Attack-range animation progression |
|---|
| Closest < Close/Short < Medium/Normal < Long |
[corpus:liquipedia_dota2/hero_animations@2317981#Attack]

| Attack-range activity table entry |
|---|
| 0-79 |
| >80 |
| 0-199 |
| >200 |
| 0-89 |
| 90-149 |
| 150-249 |
| >250 |
[corpus:liquipedia_dota2/hero_animations@2317981#Attack]

Not every tagged Hero has a unique animation for different attack ranges; Heroes with unique animations are listed in the varying-attack-range category. [corpus:liquipedia_dota2/hero_animations@2317981#Attack]

## Channel

Channel animations play when a Hero is channeling an ability for which no specialized animation exists. [corpus:liquipedia_dota2/hero_animations@2317981#Channel]

### Teleport

The Teleport channel animation is used with these items:

| Item |
|---|
| Town Portal Scroll |
| Boots of Travel |
| Boots of Travel 2 |
[corpus:liquipedia_dota2/hero_animations@2317981#Teleport]

At the teleport destination, the Hero hovers in its Idle animation. [corpus:liquipedia_dota2/hero_animations@2317981#Teleport]

## Chase

Chase animations play when a Hero chases a low-health unit. [corpus:liquipedia_dota2/hero_animations@2317981#Chase]

| Possible target |
|---|
| Enemy unit |
| Neutral unit |
| Allied unit in deny range |
[corpus:liquipedia_dota2/hero_animations@2317981#Chase]

## Critical Strike

Certain Heroes use a different attack animation when they land a critical strike. This is usually true for Heroes with a built-in critical-strike ability. [corpus:liquipedia_dota2/hero_animations@2317981#Critical_Strike]

## Death

A death animation plays when a Hero dies, and Heroes can have multiple death animations. [corpus:liquipedia_dota2/hero_animations@2317981#Death]

### Overkill

The Overkill animation plays when a Hero dies to a damage instance greater than 33% of the Hero’s max health. [corpus:liquipedia_dota2/hero_animations@2317981#Overkill]

## Defeat

The Defeat animation plays at the end of a game lost by the player. [corpus:liquipedia_dota2/hero_animations@2317981#Defeat]

## Flail

The following sources trigger the Flail animation:

| Source | Trigger |
|---|---|
| Eul's Scepter of Divinity | Cyclone |
| Wind Waker | Cyclone |
| Invoker | Tornado |
| Storm | Cyclone |
| Force Staff | Force |
| Hurricane Pike | Hurricane Thrust |
| Force Boots | Force |
| Psychic Headband | Psychic Push |
| Bane | Nightmare |
| Bane | Fiend's Grip |
| Batrider | Flaming Lasso |
| Batrider | Flamebreak |
| Clockwerk | Power Cogs |
| Dark Seer | Vacuum |
| Dark Seer | Normal Punch |
| Drow Ranger | Gust |
| Enigma | Black Hole |
| Havoc Hammer | Havoc |
| Hoodwink | Bushwhack |
| Marci | Dispose |
| Magnus | Skewer |
| Magnus | Horn Toss |
| Primal Beast | Pulverize<sup>1</sup> |
| Pudge | Meat Hook |
| Pudge | Dismember |
| Snapfire | Spit Out |
| Storm Spirit | Electric Vortex |
| Keeper of the Light | Blinding Light |
| Kunkka | Torrent |
| Kunkka | Tidal Wave |
| Rubick | Telekinesis |
| Queen of Pain | Sonic Wave |
| Spirit Breaker | Greater Bash |
| Spirit Breaker | Nether Strike |
| Tiny | Toss |
| Underlord | Fiend's Gate |
[corpus:liquipedia_dota2/hero_animations@2317981#Flail]

<sup>1</sup> The affected Hero is upside down, as is the Flail animation. [corpus:liquipedia_dota2/hero_animations@2317981#Flail]

### Force Staff

This animation plays when a Hero is affected by ally-based forced movement from these items:

| Item |
|---|
| Force Staff |
| Hurricane Pike |
| Force Boots |
[corpus:liquipedia_dota2/hero_animations@2317981#Force_Staff]

Heroes can have a custom friendly ForceStaff animation. [corpus:liquipedia_dota2/hero_animations@2317981#Force_Staff]

## Stun/Disable

These animations trigger while a Hero is affected by sources listed on the stun mechanics page. Not every stun source triggers the Stun animation; some trigger Flail. [corpus:liquipedia_dota2/hero_animations@2317981#Stun/Disable]

The following sources trigger no animation and instead freeze the Hero in place:

| Source |
|---|
| Cold Feet |
| Enchant Remnant |
| Echo Stomp |
| Time Lock |
| Chronosphere |
| Cold Snap |
| Ice Path |
| Mystic Snake |
| Stone Gaze |
| Cold Embrace |
| Winter's Curse |
[corpus:liquipedia_dota2/hero_animations@2317981#Stun/Disable]

## Haste

Hastes increase a unit’s minimum and maximum movement speed to a specific value. When a unit is hasted, its Run animation is replaced by its Haste animation. [corpus:liquipedia_dota2/hero_animations@2317981#Haste]

## Idle

Idle animations play while a Hero is standing still. Heroes can have multiple Idle animations and different Idle animations based on enemy presence or low health. [corpus:liquipedia_dota2/hero_animations@2317981#Idle]

## Injured

Injured animations are used while a Hero is below 25% max health. Not every Hero has them. [corpus:liquipedia_dota2/hero_animations@2317981#Injured]

| Animation set with Injured animations |
|---|
| Attack |
| Idle |
| Walk/Jog/Run |
[corpus:liquipedia_dota2/hero_animations@2317981#Injured]

## Spawn

Spawn animations play when a Hero respawns from death or from Reincarnation sources. [corpus:liquipedia_dota2/hero_animations@2317981#Spawn]

## Victory

The Victory animation plays at the end of a game won by the player. [corpus:liquipedia_dota2/hero_animations@2317981#Victory]

## Walk/Jog/Run

Movement animations play while a Hero is moving. Heroes can have multiple movement animations, which may vary according to these factors. [corpus:liquipedia_dota2/hero_animations@2317981#Walk/Jog/Run]

| Factor |
|---|
| Hero’s movement speed |
| Health |
| Enemy presence |
| Chasing a low-health target |
[corpus:liquipedia_dota2/hero_animations@2317981#Walk/Jog/Run]

Heroes whose movement animations vary with movement speed are tagged with `MovementSpeedActivityModifiers` in their Hero attributes and may use this progression:

| Movement-animation progression |
|---|
| Walk < Run < Run Fast/Sprint < Haste |
[corpus:liquipedia_dota2/hero_animations@2317981#Walk/Jog/Run]

| Movement-speed activity table entry |
|---|
| 340 |
| 325 |
| 320 |
| 345 |
| - |
| 430 |
| 345 |
| 373 |
| 335 |
| - |
| 385 |
| - |
| 400 |
| 360 |
| 345 |
| 400 |
| 375 |
| 350 |
| 400 |
| 350 |
| 395 |
| 390 |
| 440 |
| 400 |
| 350 |
| 440 |
| 540 |
[corpus:liquipedia_dota2/hero_animations@2317981#Walk/Jog/Run]

Not every listed Hero has a unique animation for the different movement animations. [corpus:liquipedia_dota2/hero_animations@2317981#Walk/Jog/Run]

## Spell Steal

The related main article is **Spell Steal Interactions**. [corpus:liquipedia_dota2/hero_animations@2317981#Spell_Steal]