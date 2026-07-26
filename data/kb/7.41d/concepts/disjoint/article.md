---
title: Disjoint
kind: concept
patch: 7.41d
card:
  entity: disjoint
  sentences:
  - text: Disjointing is a secondary effect of certain abilities that makes a projectile
      completely lose track of its target, recognized when it stops tracking a moving
      unit.
    marks:
    - corpus:liquipedia_dota2/disjoint@2360423
  - text: A projectile that expires before reaching its target was outrun rather than
      disjointed.
    marks:
    - corpus:liquipedia_dota2/disjoint@2360423
  - text: Blinking and becoming invisible are the most common forms of disjointing.
    marks:
    - corpus:liquipedia_dota2/disjoint@2360423
  - text: Not every projectile is disjointable, and not every repositioning ability
      disjoints.
    marks:
    - corpus:liquipedia_dota2/disjoint@2360423
  - text: Some abilities disjoint projectiles once upon cast.
    marks:
    - corpus:liquipedia_dota2/disjoint@2360423#Disjointing_Abilities
  - text: Every blink-based ability disjoints, but not every teleporting ability does.
    marks:
    - corpus:liquipedia_dota2/disjoint@2360423#Teleporting
  - text: Blink or teleport distance is irrelevant, and the disjoint occurs when the
      ability moves the unit.
    marks:
    - corpus:liquipedia_dota2/disjoint@2360423#Teleporting
  - text: Every invisibility-granting ability can disjoint unless an enemy has True
      Sight over the unit.
    marks:
    - corpus:liquipedia_dota2/disjoint@2360423#Invisibility
  - text: Momentary invisibility during the projectile’s flight is sufficient to disjoint
      it.
    marks:
    - corpus:liquipedia_dota2/disjoint@2360423#Invisibility
  - text: Entering the Fog of War or leaving vision range does not count as invisibility
      for disjointing.
    marks:
    - corpus:liquipedia_dota2/disjoint@2360423#Invisibility
  - text: Becoming hidden does not itself disjoint projectiles.
    marks:
    - corpus:liquipedia_dota2/disjoint@2360423#Hiding
  - text: Every physical attack projectile from each unit and hero can be disjointed.
    marks:
    - corpus:liquipedia_dota2/disjoint@2360423#Disjointable_projectiles
---

# Disjoint

## Overview

Disjointing causes a projectile to lose track of its target completely and is recognized when the projectile stops tracking a moving unit. A projectile that expires before reaching its target has instead been avoided by “outrunning” it. Disjointing is not granted explicitly by effects or spells; it occurs as a secondary effect of other abilities.

Blinking and becoming invisible are the most common forms. Invulnerability and hiding can prevent a projectile from affecting its target but do not disjoint it, because the projectile continues homing and technically hits. Not every projectile is disjointable, and not every repositioning ability disjoints. An example is Shadow Fiend using a Blink Dagger to dodge Phantom Assassin’s Stifling Dagger. [corpus:liquipedia_dota2/disjoint@2360423]

## Disjointing abilities

### Upon cast

These abilities disjoint projectiles once upon cast. For abilities involving Forced Movement, the disjoint belongs to the spell rather than the movement; other Forced Movement spells do not therefore disjoint.

| Source | Ability | Note |
|---|---|---|
| Alchemist | Chemical Rage |  |
| Chaos Knight | Phantasm |  |
| Dark Willow | Shadow Realm |  |
| Enchantress | Sproink |  |
| Runes | Illusion |  |
| Lifestealer | Infest |  |
| Manta Style | Mirror Image |  |
| Morphling | Waveform |  |
| Muerta | Pierce the Veil |  |
| Naga Siren | Mirror Image |  |
| Phoenix | Supernova | 2a, 3 |
| Puck | Phase Shift |  |
| Pudge | Dismember | 2b |
| Riki | Tricks of the Trade |  |
| Snapfire | Gobble Up | 2a |
| Storm Spirit | Ball Lightning |  |

| Note | Requirement or effect |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim’s Scepter. |
| 2b | Requires Aghanim’s Shard. |
| 3 | Disjoints projectiles for the allied hero with Aghanim’s Scepter. [corpus:liquipedia_dota2/disjoint@2360423#Disjointing_Abilities] |

### Teleporting

Every blink-based ability disjoints, but not every teleporting ability does. Blink or teleport distance is irrelevant, and the disjoint occurs when the ability moves the unit. Unlisted teleporting abilities, including Reverse Polarity, do not disjoint projectiles.

| Source | Ability | Note |
|---|---|---|
| Anti-Mage | Blink |  |
| Blink Dagger | Blink |  |
| Chen | Holy Persuasion |  |
| Fallen Sky | Fallen Sky |  |
| Io | Relocate | 1 |
| Keeper of the Light | Recall | 3 |
| Nature’s Prophet | Teleportation |  |
| Phantom Lancer | Doppelganger | 2 |
| Puck | Ethereal Jaunt |  |
| Queen of Pain | Blink |  |
| Spirit Bear | Return |  |
| Town Portal Scroll | Teleport |  |
| Weaver | Time Lapse |  |

| Note | Condition |
|---|---|
| 1 | Relocate disjoints only for Io when teleporting to the targeted point, not for allies or when teleporting back. |
| 2 | Doppelganger disjoints for Phantom Lancer and all gathered illusions. |
| 3 | Requires facet. [corpus:liquipedia_dota2/disjoint@2360423#Teleporting] |

### Invisibility

Every ability that grants invisibility can disjoint projectiles unless an enemy has True Sight over the unit. Under True Sight, the projectile continues tracking until the unit is no longer affected by True Sight. If True Sight cannot pierce the invisibility source, the projectile is still disjointed.

Momentary invisibility during the projectile’s flight is sufficient; the unit need not remain invisible until the projectile arrives. If the unit becomes visible again, the projectile resumes visually tracking it. Entering the Fog of War or otherwise leaving vision range does not count as invisibility for disjointing.

Fade time does not disjoint. Shadow Amulet and Glimmer Cape can disjoint, but must be applied sufficiently in advance. [corpus:liquipedia_dota2/disjoint@2360423#Invisibility]

### Hiding

Becoming temporarily hidden does not disjoint projectiles. The disjointing attribute belongs to particular spells rather than to the act of becoming hidden, so hiding spells do not necessarily disjoint. With proper timing, however, hiding can prevent projectiles or spells generally from hitting the caster or target. [corpus:liquipedia_dota2/disjoint@2360423#Hiding]

### Invulnerability

Becoming invulnerable does not disjoint projectiles; it instead reduces or eliminates their effects on impact. Attack damage and spell damage are ignored, though a few spells affect invulnerable units. [corpus:liquipedia_dota2/disjoint@2360423#Invulnerability]

## Disjointable projectiles

Every physical attack projectile of each unit and hero can be disjointed, including the following categories:

| Category | Included examples |
|---|---|
| Attack modifiers | Frost Arrows; Liquid Fire |
| Enhanced attacks | Meld; attacks with True Strike |
| Secondary attack projectiles from instant attacks | Flak Cannon; Geminate Attack |

For both bouncing projectiles below, disjointing a bounce does not stop it from continuing to bounce. It can immediately jump to the disjointing unit again if the disjoint was not caused by invisibility and the unit remains within bounce range, because the disjoint is not considered a hit and the unit remains a valid bounce target. A disjointed bounce still counts toward the bounce count.

| Ability |
|---|
| Moon Glaives |
| Death Ward |

| Note | Projectile interaction |
|---|---|
| 1 | Mist Coil and Ether Blast can also be disjointed by targeted allies. |
| 2 | Disjointing Shuriken Toss or an Aghanim’s Scepter-upgraded Spirit Lance causes it to stop bouncing. |
| 3 | Dragon Tail is normally instant, but while in Elder Dragon Form it uses a disjointable projectile. |
| 4 | Disjointing a projectile that applies an area effect also prevents that area effect. |
| 5 | Assassinate grants True Sight over the target when Sniper begins casting. It lasts for 4 seconds, until the projectile lands, or until the cast is canceled. Assassinate therefore usually cannot be disjointed with invisibility except through Shadow Dance or Smoke of Deceit. |
| 6 | Splinter Blast’s secondary projectiles can be disjointed, but its initial projectile cannot. |
| 7 | Cinder Brew launches invisible, disjointable projectiles on enemies upon cast. |
| 8 | The ability applies a modifier to the hero’s normal attack and can therefore be disjointed like a regular attack. [corpus:liquipedia_dota2/disjoint@2360423#Disjointable_projectiles] |

## Undisjointable projectiles

Attempting to disjoint these abilities does not cause their projectiles to lose track of the target. Turning invisible does not prevent the target from being fully affected.

| Source | Ability | Note |
|---|---|---|
| Earthshaker | Echo Slam |  |
| Lich | Chain Frost |  |
| Tiny | Toss | 4 |
| Spectre | Spectral Dagger |  |
| Mirana | Starstorm |  |
| Venomancer | Noxious Plague |  |
| Beastmaster | Summon Raptors |  |
| Necrophos | Death Pulse |  |
| Alchemist | Berserk Potion |  |
| Alchemist | Unstable Concoction Throw |  |
| Queen of Pain | Scream of Pain |  |
| Ember Spirit | Activate Fire Remnant |  |
| Ember Spirit | Searing Chains |  |
| Rubick | Spell Steal |  |
| Arc Warden | Spark Wraith |  |
| Medusa | Cold Blooded |  |
| Medusa | Mystic Snake | 3 |
| Witch Doctor | Maledict |  |
| Witch Doctor | Paralyzing Cask |  |
| Grimstroke | Phantom’s Embrace | 1 |

| Note | Interaction |
|---|---|
| 1 | Phantom’s Embrace cannot be disjointed by its targets. It can be disjointed while returning to Grimstroke, causing its cooldown not to be reset. |
| 2 | Huskar acts as a projectile. Although he cannot be disjointed, the spell is immediately canceled when the distance between Huskar and the target gets greater than . |
| 3 | Although Mystic Snake is not disjointable, it does not affect a target that becomes invisible before being hit. |
| 4 | The tossed unit can be avoided by blinking or moving rapidly but cannot technically be disjointed. Upon casting Toss, the minimum distance required to avoid the tossed unit is 4000, decreasing by 307.69 for each 0.1 seconds of Toss’ duration. |
| 5 | Snowball can be avoided by moving far enough because it travels for a maximum of 3 seconds. [corpus:liquipedia_dota2/disjoint@2360423#Undisjointable_projectiles] |

## Balance changelog

### 7.00 — 2016-12-12

| Change | Ability or projectile |
|---|---|
| No longer disjoints projectiles | Borrowed Time |
| No longer disjoints projectiles | True Form |
| No longer disjoints projectiles | Pounce |
| No longer disjoints projectiles | Metamorphosis |
| No longer disjoints projectiles | Leap |
| Now disjoints projectiles | Test of Faith (Teleport) |
| Now disjoints projectiles | Recall |
| Now disjoints projectiles | Morph Replicate |
| Now disjointable | Splinter Blast secondary hit |
| Now disjointable | Soul Assumption [corpus:liquipedia_dota2/disjoint@2360423#Balance_changelog] |