---
title: Root
kind: concept
patch: 7.41d
card:
  entity: root
  sentences:
  - text: Root, formerly Ensnare, is a status effect that prevents movement and most
      mobility abilities without preventing turning, other abilities, or most items;
      a Root that also disarms is called a Bind, formerly Entangle.
    marks:
    - corpus:liquipedia_dota2/root@2383465
  - text: Root is invoked by `MODIFIER_STATE_ROOTED` and does not change actual movement
      speed, so movement-speed-based effects are unaffected.
    marks:
    - corpus:liquipedia_dota2/root@2383465#Mechanics
  - text: Move orders remain valid while rooted, but movement waits until the Root
      source expires.
    marks:
    - corpus:liquipedia_dota2/root@2383465#Mechanics
  - text: Abilities with `DOTA_ABILITY_BEHAVIOR_ROOT_DISABLES` cannot be cast while
      rooted, and pending orders to cast them are canceled when Root is applied.
    marks:
    - corpus:liquipedia_dota2/root@2383465#Mechanics
  - text: Applying Root interrupts an already-started cast animation and cancels the
      ability if it is channeling, although Root does not cancel channeling abilities
      by default.
    marks:
    - corpus:liquipedia_dota2/root@2383465#Mechanics
  - text: Root does not prevent Forced Movement, but abilities may separately use
      an `IsRooted` check to withhold movement.
    marks:
    - corpus:liquipedia_dota2/root@2383465#Mechanics
  - text: Some Root sources separately revoke `MODIFIER_STATE_INVISIBLE` to provide
      True Sight, but True Sight is not inherent to Root.
    marks:
    - corpus:liquipedia_dota2/root@2383465#True_Sight
  - text: Bind has no separate state and additionally invokes `MODIFIER_STATE_DISARMED`,
      so both Root and Disarm notes apply.
    marks:
    - corpus:liquipedia_dota2/root@2383465#Disarm
  - text: Most Root-source abilities can be dispelled by Basic Dispel.
    marks:
    - corpus:liquipedia_dota2/root@2383465#Root_Sources
  - text: All Bind sources apply True Sight and Disarm and can be dispelled by Basic
      Dispel.
    marks:
    - corpus:liquipedia_dota2/root@2383465#Bind_Sources
  - text: Some abilities Root their caster or an allied target while active, preventing
      orders such as moving or attacking, and some also disarm the caster.
    marks:
    - corpus:liquipedia_dota2/root@2383465#Ally-Rooting_Abilities
  - text: Version 7.39, dated 2025-05-21, classified Root sources that also Disarm
      their target as Bind Effects.
    marks:
    - corpus:liquipedia_dota2/root@2383465#Recent_Changes
---

# Root

Root, formerly **Ensnare**, is a status effect that prevents affected units from moving and casting most mobility abilities. It does not prevent turning, casting other abilities, or using most items. A Root that also disarms is called a **Bind**, formerly **Entangle**. [corpus:liquipedia_dota2/root@2383465]

## Definition

| Root type | Disabled aspects and definition | Example |
|---|---|---|
| Root | Prevents movement and disables certain mobility spells. May apply True Sight, depending on the source. | Ensnare |
| Bind | Prevents movement and disables certain mobility spells; disarms. May apply True Sight, depending on the source. | Frostbite |

[corpus:liquipedia_dota2/root@2383465#Definition]

## Mechanics

Root is invoked by `MODIFIER_STATE_ROOTED`. It disables movement without changing actual movement speed, so effects based on movement speed are unaffected.

Move orders can still be issued, and the unit attempts to execute them; movement proceeds when the Root source expires. Root does not prevent turning or generally interrupt the unit. Orders issued before or during Root still execute, although orders requiring movement wait until the source expires.

An ability with `DOTA_ABILITY_BEHAVIOR_ROOT_DISABLES` cannot be cast while rooted. An order to cast such an ability is canceled if issued before Root is applied. Applying Root interrupts an already-started cast animation and cancels the ability if it is channeling; Root does not cancel channeling abilities by default.

Root does not prevent Forced Movement. However, some abilities use an `IsRooted` check and are coded not to move units in this state. [corpus:liquipedia_dota2/root@2383465#Mechanics]

### True Sight

Some Root sources also revoke `MODIFIER_STATE_INVISIBLE`, providing True Sight over the unit. This is a separate mechanic applied alongside Root rather than an effect of Root itself, so not every Root source applies True Sight. [corpus:liquipedia_dota2/root@2383465#True_Sight]

### Disarm

Bind has no separate state; it additionally invokes `MODIFIER_STATE_DISARMED`. All Root notes and all Disarm notes therefore apply. [corpus:liquipedia_dota2/root@2383465#Disarm]

## Sources

### Root sources

Most Root-source abilities can be dispelled by Basic Dispel.

| True Sight | Source | Ability | Notes |
|---|---|---|---|
| Yes | Ancient Prowler Shaman | Petrify | — |
| Yes | Broodmother | Spinner's Snare | — |
| Yes | Ember Spirit | Searing Chains | — |
| Yes | Enchantress | Little Friends | 5 |
| Yes | Gleipnir | Eternal Chains | — |
| Yes | Hill Troll | Ensnare | — |
| Yes | Invoker | Ice Wall | 2a |
| Yes | Lone Druid | Entangle | — |
| Yes | Meepo | Earthbind | 3 |
| Yes | Medusa | Gorgon's Grasp | 4 |
| Yes | Naga Siren | Ensnare | — |
| Yes | Oracle | Fortune's End | — |
| Yes | Rod of Atos | Cripple | — |
| Yes | Spirit Bear | Entangling Claws | — |
| Yes | Troll Warlord | Berserker's Rage | — |
| Yes | Underlord | Fiend's Gate | 2a |
| Yes | Underlord | Pit of Malice | 3 |
| No | Dark Willow | Bramble Maze | 3 |
| No | Dark Willow | Cursed Crown | 2b, 3 |
| No | Raptor | Dive Bomb | 2b |
| No | Naga Siren | Song of the Siren | 5 |
| No | Tinker | Warp Flare | — |
| No | Void Spirit | Dissimilate | 1 |

| Note | Meaning |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |
| 3 | Can affect unrevealed invisible units. |
| 4 | Also disables turning of rooted unit. |
| 5 | Can't be dispelled by Basic and Strong Dispel. |

[corpus:liquipedia_dota2/root@2383465#Root_Sources]

### Bind sources

All Bind sources apply True Sight and Disarm and can be dispelled by Basic Dispel.

| Source | Ability | Notes |
|---|---|---|
| Crystal Maiden | Crystal Clone | — |
| Crystal Maiden | Freezing Field | 2a |
| Crystal Maiden | Frostbite | — |
| Nature's Prophet | Wrath of Nature | 2a |
| Treant Protector | Nature's Guise | 2b |
| Treant Protector | Overgrowth | — |

| Note | Meaning |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |

[corpus:liquipedia_dota2/root@2383465#Bind_Sources]

## Ally-rooting abilities

Some abilities Root the caster or an allied target while active, preventing certain orders such as moving or attacking. Some also disarm the caster.

| Source | Ability | Notes |
|---|---|---|
| Centaur Warrunner | Hitch A Ride | — |
| Earth Spirit | Rolling Boulder | — |
| Familiar | Stone Form | — |
| Juggernaut | Omnislash | — |
| Juggernaut | Swiftslash | — |
| Nyx Assassin | Burrow | — |
| Phoenix | Supernova | — |
| Tusk | Snowball | — |
| Tombstone | Grab Ally | — |
| Visage | Gravekeeper's Cloak | 2b |
| Void Spirit | Dissimilate | — |

| Note | Meaning |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |

[corpus:liquipedia_dota2/root@2383465#Ally-Rooting_Abilities]

## Fully disabled by Root

| Source | Ability |
|---|---|
| Fallen Sky | Fallen Sky |
| Tumbler's Toy | Vault |
| Sven | Storm Hammer |
| Earthshaker | Enchant Totem |
| Tidehunter | Anchor Smash |
| Morphling | Waveform |
| Spectre | Reality |
| Mirana | Leap |
| Nature's Prophet | Teleportation |
| Storm Spirit | Ball Lightning |
| Puck | Ethereal Jaunt |
| Sand King | Burrowstrike |
| Ringmaster | Whoopee Cushion |
| Earth Spirit | Rolling Boulder |
| Queen of Pain | Blink |
| Magnus | Skewer |
| Riki | Blink Strike |
| Elder Titan | Echo Stomp |
| Elder Titan | Natural Order |
| Anti-Mage | Blink |
| Marci | Rebound |
| Ember Spirit | Activate Fire Remnant |
| Ember Spirit | Sleight of Fist |
| Void Spirit | Astral Step |
| Void Spirit | Dissimilate |
| Enchantress | Little Friends |
| Meepo | Dig |
| Meepo | Poof |
| Faceless Void | Reverse Time Walk |
| Faceless Void | Time Walk |
| Monkey King | Boundless Strike |
| Monkey King | Primal Spring |
| Monkey King | Tree Dance |
| Zeus | Heavenly Jump |
| Slark | Pounce |
| Sniper | Concussive Grenade |
| Spirit Breaker | Nether Strike |
| Techies | Blast Off! |
| Chaos Knight | Reality Rift |
| Pangolier | Rolling Thunder |
| Pangolier | Swashbuckle |
| Phantom Assassin | Phantom Strike |
| Phantom Lancer | Doppelganger |
| Timbersaw | Timber Chain |
| Phoenix | Icarus Dive |
| Phoenix | Toggle Movement |
| Tinker | Keen Conveyance |
| Primal Beast | Onslaught |
| Dawnbreaker | Converge |
| Tusk | Drinking Buddies |
| Tusk | Snowball |
| Town Portal Scroll | Teleport |
| Kez | Grappling Claw |
| Spirit Bear | Return |

[corpus:liquipedia_dota2/root@2383465#Fully_Disabled_by_Root]

## Partially disabled by Root

| Source | Ability |
|---|---|
| Viper | Nosedive |
| Puck | Waning Rift |
| Ursa | Earthshock |
| Riki | Tricks of the Trade |
| Hoodwink | Sharpshooter |
| Templar Assassin | Psionic Projection |
| Pangolier | Shield Crash |
| Io | Relocate |
| Phantom Lancer | Phantom Rush |
| Primal Beast | Trample |
| Dawnbreaker | Starbreaker |
| Fiend's Gate | Warp |
| Twin Gate | Warp |
| Kez | Echo Slash |
| Spirit Bear (Pre 7.40) | Return |

[corpus:liquipedia_dota2/root@2383465#Partially_disabled_by_Root]

## Recent changes

| Version | Date | Change |
|---|---|---|
| 7.39 | 2025-05-21 | Root sources that also Disarm the target are now considered Bind Effects. |
| 7.22g | 2019-09-06 | Ethereal Jaunt can no longer be cast while rooted. Phase Shift can now be cast while rooted. |
| 7.22e | 2019-07-14 | Sleight of Fist can no longer be cast while rooted. |

[corpus:liquipedia_dota2/root@2383465#Recent_Changes]