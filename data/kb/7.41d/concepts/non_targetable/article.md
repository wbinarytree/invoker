---
title: Non-targetable
kind: concept
patch: 7.41d
card:
  entity: non_targetable
  sentences:
  - text: Non-targetable, or untargetability, is a mechanic whose standard form excludes
      Hide sources, grants Attack Immunity and Phased, makes a unit unselectable,
      removes its Selection Box, and prevents allies and enemies from targeting it.
    marks:
    - corpus:liquipedia_dota2/non_targetable@2382188
    - corpus:liquipedia_dota2/non_targetable@2382188#Definition
  - text: Misc Non-targetable units may remain selectable and retain their Selection
      Boxes, but neither allies nor enemies can target them.
    marks:
    - corpus:liquipedia_dota2/non_targetable@2382188#Definition
  - text: Unselectability prevents a unit from being selected except in a few cases.
    marks:
    - corpus:liquipedia_dota2/non_targetable@2382188#Unselectability
  - text: Most abilities and items treat unselectable units as invisible, with exceptions.
    marks:
    - corpus:liquipedia_dota2/non_targetable@2382188#Unselectability
  - text: Hide sources also cause unselectability and non-targetability, but Hide
      is a different mechanic.
    marks:
    - corpus:liquipedia_dota2/non_targetable@2382188#Unselectability
  - text: Gaining unselectability cancels attacks and abilities already in their animations
      when performed by a faction that can no longer target the unit.
    marks:
    - corpus:liquipedia_dota2/non_targetable@2382188#Sources
  - text: Most target-unit abilities cannot target unselectable units, and their exceptions
      fail against effects that prevent both factions from targeting the unit.
    marks:
    - corpus:liquipedia_dota2/non_targetable@2382188#Directly_Unit-Targeting
  - text: Spell Reflection sources and some instant, no-facing abilities can fully
      target units made unselectable by Shadow Realm or Smoke Screen.
    marks:
    - corpus:liquipedia_dota2/non_targetable@2382188#Directly_Unit-Targeting
  - text: Friendly Shadow can target an allied hero affected by Smoke Screen or Shadow
      Realm.
    marks:
    - corpus:liquipedia_dota2/non_targetable@2382188#Directly_Unit-Targeting
  - text: Secondary effects generally affect or exclude unselectable units according
      to whether they affect or exclude invisible units.
    marks:
    - corpus:liquipedia_dota2/non_targetable@2382188#Secondary_Targets
  - text: The Swarm’s beetles latch onto unselectable units, apply their first damage
      instance, and die after 0.13 seconds, while ignoring invisible units.
    marks:
    - corpus:liquipedia_dota2/non_targetable@2382188#Secondary_Targets
  - text: Solar Guardian, Poof, and Toss consider allied non-selectable units valid
      targets.
    marks:
    - corpus:liquipedia_dota2/non_targetable@2382188#Other_Cases
---

# Non-targetable

Untargetability is a mechanic that makes a unit untargetable. [corpus:liquipedia_dota2/non_targetable@2382188]

## Definition

| Mechanic | Definition | Example |
|---|---|---|
| Non-targetable | Excludes Hide sources. Grants Attack Immunity and Phased, makes the unit unselectable, removes its Selection Box, and prevents both allies and enemies from targeting it. | Hitch A Ride [corpus:liquipedia_dota2/non_targetable@2382188#Definition] |
| Misc Non-targetable | The unit can remain selectable and retain its Selection Box, but neither allies nor enemies can target it. | Smoke Screen [corpus:liquipedia_dota2/non_targetable@2382188#Definition] |

## Unselectability

Unselectability makes a unit not selectable except in a few cases. Most abilities and items treat unselectable units as invisible, with some exceptions. Some sources may also remove the unit’s Selection Box, grant Attack Immunity, and prevent allies, enemies, or both factions from targeting it. [corpus:liquipedia_dota2/non_targetable@2382188#Unselectability]

Hide sources also make units unselectable and non-targetable, but Hide is considered a different mechanic. [corpus:liquipedia_dota2/non_targetable@2382188#Unselectability]

### Sources

| Source | Effects and interactions |
|---|---|
| Crystal Maiden — Crystal Clone | The created illusion is unselectable by both factions, and its Selection Box is removed. It is not attack immune, and units can walk through it. Enemies can still attack the illusion with a ground-targeted attack on the nearest unit. [corpus:liquipedia_dota2/non_targetable@2382188#Sources] |
| Dark Willow — Shadow Realm | Dark Willow is unselectable by both factions, but her Selection Box is not removed. She is attack immune and phased and can choose herself as a target. [corpus:liquipedia_dota2/non_targetable@2382188#Sources] |
| Riki — Smoke Screen | Affected enemies within the radius are unselectable by their allies. Their Selection Boxes are not removed. They are neither phased nor attack immune, but their allies cannot attack them. [corpus:liquipedia_dota2/non_targetable@2382188#Sources] |
| Phantom Assassin — Blur | Phantom Assassin is unselectable by the enemy faction. Her Selection Box is not removed. She is attack immune but not phased. [corpus:liquipedia_dota2/non_targetable@2382188#Sources] |
| Ringmaster — Escape Act | The affected hero is unselectable by both factions, has its Selection Box removed, and is attack immune and phased. [corpus:liquipedia_dota2/non_targetable@2382188#Sources] |

#### Invulnerable sources

| Properties | Source |
|---|---|
| Unselectable by both factions; Invulnerable; Selection Box removed | Ember Spirit — Sleight of Fist [corpus:liquipedia_dota2/non_targetable@2382188#Sources] |
| Unselectable by both factions; Invulnerable; Selection Box removed | Juggernaut — Omnislash [corpus:liquipedia_dota2/non_targetable@2382188#Sources] |
| Unselectable by both factions; Invulnerable; Selection Box removed | Juggernaut — Swiftslash [corpus:liquipedia_dota2/non_targetable@2382188#Sources] |
| Unselectable by both factions; Invulnerable; Selection Box removed | Meepo — MegaMeepo Fling [corpus:liquipedia_dota2/non_targetable@2382188#Sources] |
| Unselectable by both factions; Invulnerable; Selection Box removed | Outworld Destroyer — Astral Imprisonment¹ [corpus:liquipedia_dota2/non_targetable@2382188#Sources] |
| Unselectable by both factions; Invulnerable; Selection Box removed; Phased | Centaur Warrunner — Hitch A Ride [corpus:liquipedia_dota2/non_targetable@2382188#Sources] |
| Unselectable by both factions; Invulnerable; Selection Box removed; Phased | Mars — Bulwark (Soldiers)² [corpus:liquipedia_dota2/non_targetable@2382188#Sources] |
| Unselectable by both factions; Invulnerable; Selection Box removed; Phased | Outworld Destroyer — Astral Imprisonment¹ [corpus:liquipedia_dota2/non_targetable@2382188#Sources] |

¹ Requires Aghanim’s Shard. [corpus:liquipedia_dota2/non_targetable@2382188#Sources]  
² Requires Aghanim’s Scepter. [corpus:liquipedia_dota2/non_targetable@2382188#Sources]

When a unit gains unselectability, attacks and abilities already in their attack or cast animations are canceled if performed by a faction that can no longer target the unit—for example, allies under Smoke Screen or all units under other sources. If an enemy is channeling Fiend’s Grip on a unit and an ally is channeling Life Drain on it, another ally casting Book of Shadows on that unit cancels Fiend’s Grip but not Life Drain. [corpus:liquipedia_dota2/non_targetable@2382188#Sources]

## Bypassing Unselectability

### Direct unit-targeting

Target-unit abilities require the caster to target a unit directly and cannot be used on the ground. Most cannot target unselectable units, but some exceptions exist. These exceptions do not work against abilities that prevent both factions from targeting the unit. [corpus:liquipedia_dota2/non_targetable@2382188#Directly_Unit-Targeting]

Spell Reflection sources and some abilities with an instant cast time that require no facing while casting can fully target units made unselectable by Shadow Realm or Smoke Screen. [corpus:liquipedia_dota2/non_targetable@2382188#Directly_Unit-Targeting]

| Target | Ability | Exception |
|---|---|---|
| Enemy | Pugna — Decrepify | Can target an enemy affected by Shadow Realm if Pugna is channeling with innate Oblivion Savant. [corpus:liquipedia_dota2/non_targetable@2382188#Directly_Unit-Targeting] |
| Ally | Bounty Hunter — Friendly Shadow | Can target an allied hero affected by Smoke Screen or Shadow Realm. [corpus:liquipedia_dota2/non_targetable@2382188#Directly_Unit-Targeting] |
| Ally | Lich — Frost Shield | Can target an allied unit affected by Smoke Screen or Shadow Realm if Lich is channeling Sinister Gaze. [corpus:liquipedia_dota2/non_targetable@2382188#Directly_Unit-Targeting] |
| Ally | Pugna — Decrepify | Can target an allied unit affected by Smoke Screen or Shadow Realm if Pugna is channeling with innate Oblivion Savant. [corpus:liquipedia_dota2/non_targetable@2382188#Directly_Unit-Targeting] |

### Secondary targets

Most abilities treat unselectable units as invisible: abilities that affect or exclude invisible units generally affect or exclude unselectable units respectively. Paralyzing Cask bounces to neither invisible nor unselectable units, while Thundergod’s Wrath strikes neither. [corpus:liquipedia_dota2/non_targetable@2382188#Secondary_Targets]

The following abilities behave differently:

| Source | Interaction |
|---|---|
| Abaddon — Mist Coil | Visually launches projectiles at both invisible and unselectable units, but projectiles against invisible units are instantly disjointed. It fully affects unselectable units. [corpus:liquipedia_dota2/non_targetable@2382188#Secondary_Targets] |
| Dust of Appearance — Reveal | Fully affects invisible units but does not damage or slow unselectable units. [corpus:liquipedia_dota2/non_targetable@2382188#Secondary_Targets] |
| Hoodwink — Bushwhack | Fully affects units made unselectable by Shadow Realm and Blur while not affecting invisible units. [corpus:liquipedia_dota2/non_targetable@2382188#Secondary_Targets] |
| Hoodwink — Decoy | Its lesser Bushwhack affects units made unselectable by Shadow Realm and Blur while not affecting invisible units. [corpus:liquipedia_dota2/non_targetable@2382188#Secondary_Targets] |
| Queen of Pain — Shadow Strike | Visually launches projectiles at both invisible and unselectable units, but projectiles against invisible units are instantly disjointed. It fully affects unselectable units. [corpus:liquipedia_dota2/non_targetable@2382188#Secondary_Targets] |
| Spirit Breaker — Charge of Darkness | When the current charge target dies, the ability can change targets to a nearby unit made unselectable by Shadow Realm or Blur, but not to an invisible unit. [corpus:liquipedia_dota2/non_targetable@2382188#Secondary_Targets] |
| Undying — Tombstone | Partially affects unselectable units. Tombstone does not spawn Undying Zombies to attack nearby unselectable or invisible units, but already-spawned zombies do not die when the unit they are attacking gains unselectability. [corpus:liquipedia_dota2/non_targetable@2382188#Secondary_Targets] |
| Weaver — The Swarm | Beetles fully latch onto unselectable units, apply their first damage instance, and then die after 0.13 seconds. Beetles ignore invisible units. [corpus:liquipedia_dota2/non_targetable@2382188#Secondary_Targets] |
| Wraith King — Reincarnation | Visually launches projectiles at both invisible and unselectable units, but projectiles against invisible units are instantly disjointed. It fully affects unselectable units. [corpus:liquipedia_dota2/non_targetable@2382188#Secondary_Targets] |

### Other cases

The following abilities consider allied non-selectable units valid targets:

| Ability |
|---|
| Dawnbreaker — Solar Guardian [corpus:liquipedia_dota2/non_targetable@2382188#Other_Cases] |
| Meepo — Poof [corpus:liquipedia_dota2/non_targetable@2382188#Other_Cases] |
| Tiny — Toss [corpus:liquipedia_dota2/non_targetable@2382188#Other_Cases] |