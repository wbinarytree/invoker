---
title: Buildings
kind: concept
patch: 7.41d
card:
  entity: Buildings
  sentences:
  - text: 'Buildings are non-player-controlled Dota 2 map units: each faction has
      26 fixed base structures that defend the base and include the Ancient whose
      destruction wins the match, while neutral buildings may be conquered or used
      by either team.'
    marks:
    - corpus:liquipedia_dota2/buildings@2376134
    - corpus:liquipedia_dota2/buildings@2376134#Faction_Buildings
    - corpus:liquipedia_dota2/buildings@2376134#Ancients
  - text: Except Ancients, faction buildings may be denied below 10% maximum health
      to reduce or prevent enemy Gold bounties.
    marks:
    - corpus:liquipedia_dota2/buildings@2376134#Faction_Buildings
  - text: Buildings use the Reinforced classification; damage factors are 0.5 for
      heroes, 0.6 for illusions, 0.9 for summoned units, 0.7 for Runty attacks, 0.35
      for Piercing attacks, and 2.5 for Reinforced damage against Reinforced units.
    marks:
    - corpus:liquipedia_dota2/buildings@2376134#General_Information
  - text: Active Backdoor Protection reduces incoming damage by 50%, reduces damage
      from illusions and summoned units by 75%, and heals 180 health per second.
    marks:
    - corpus:liquipedia_dota2/buildings@2376134#Backdoor_Protection
  - text: Glyph of Fortification gives allied buildings 100% incoming-damage reduction
      for 7 seconds on a team-shared 300-second cooldown.
    marks:
    - corpus:liquipedia_dota2/buildings@2376134#Glyph_of_Fortification
  - text: 'Each faction has 11 Towers: three in each lane and two guarding its Ancient.'
    marks:
    - corpus:liquipedia_dota2/buildings@2376134#Towers
  - text: Tier 1–4 Towers have 1800/2500/2500/2600 health and 12/16/16/21 armor.
    marks:
    - corpus:liquipedia_dota2/buildings@2376134#Tier_Difference_(Towers)
  - text: A Tower remains invulnerable until its lane’s preceding lower-tier Tower
      is destroyed.
    marks:
    - corpus:liquipedia_dota2/buildings@2376134#Towers
  - text: Each faction has 6 Barracks, comprising 3 melee and 3 ranged buildings with
      2200 and 1300 health, respectively.
    marks:
    - corpus:liquipedia_dota2/buildings@2376134#Barracks
  - text: Destroying either enemy Barracks in a lane replaces its corresponding regular
      creeps with super creeps; destroying all enemy Barracks produces mega creeps
      in every lane.
    marks:
    - corpus:liquipedia_dota2/buildings@2376134#Lane_Creep_Upgrades
  - text: Each Ancient has 4500 health and 23 armor and remains invulnerable until
      both guarding Tier 4 Towers are destroyed.
    marks:
    - corpus:liquipedia_dota2/buildings@2376134#Ancients
  - text: Fountain Rejuvenation Aura has 1200 radius and grants health regeneration
      equal to 5% of maximum health and mana regeneration equal to 6% of maximum mana.
    marks:
    - corpus:liquipedia_dota2/buildings@2376134#Fountain_Ability
---

# Buildings

## Overview

Buildings are units not controlled by players. A fixed set spawns at set locations in each team’s base when a match begins. Both factions have the same buildings, differing only in appearance. Buildings primarily serve defensive roles and constitute the game’s main objective. Neutral buildings are also scattered across the map and may be conquered or otherwise used by both teams. [corpus:liquipedia_dota2/buildings@2376134]

### Neutral buildings

Neutral buildings do not directly belong to either faction. They are permanently invulnerable, cannot be destroyed, and are immune to every ability. They remain visible through the Fog of War to both teams at all times.

| Type | Rules |
|---|---|
| Capturable buildings | Players can conquer them for their faction; the opposing faction can recapture them. |
| True neutral buildings | Never belong to either faction but can be used by both. |

[corpus:liquipedia_dota2/buildings@2376134#Neutral_Buildings]

### Faction buildings

All faction buildings share the same base properties and are immune to most abilities, with only a few abilities able to affect them. Some destroyed buildings grant a team Gold bounty, while others grant a bounty to the player making the last hit. A building below 10% of its maximum health may be denied to reduce or prevent enemy Gold bounties, but Ancients cannot be denied. Buildings grant no experience; once destroyed, they are permanently lost and do not respawn. Each faction has a total of 26 buildings. [corpus:liquipedia_dota2/buildings@2376134#Faction_Buildings]

## General properties

All buildings use the Reinforced attack classification.

| Interaction | Effect or factor |
|---|---:|
| Damage from heroes | Hero Factor: 0.5 |
| Damage from illusions | Illusion Factor: 0.6 |
| Damage from summoned units | Summoned Unit Factor: 0.9 |
| Damage from Runty attacks | Runty Factor: 0.7 |
| Damage from Piercing attacks | Piercing Final Factor: 0.35 |
| Reinforced-class damage dealt to Reinforced units | Reinforced Factor: 2.5 |

[corpus:liquipedia_dota2/buildings@2376134#General_Information]

### Backdoor Protection

Backdoor Protection is a passive ability possessed by most destroyable buildings. While active, it reduces incoming damage and rapidly heals damage dealt by enemies, making buildings difficult to damage or destroy without lane creeps. An enemy lane creep entering the deactivation radius disables it; Dominated creeps do not. Reactivation occurs after a delay.

Four areas currently deactivate Backdoor Protection and operate independently. Base buildings display the ability individually but are controlled collectively by the Ancient’s Backdoor Protection: enemy creeps within its detection radius remove protection from every base building simultaneously. Each Tier 2 Tower instead has its own independent protection and deactivation radius, independent both from other Tier 2 Towers and from the Ancient. Tier 1 Towers are always unprotected.

Backdoor Protection does not create building invulnerability. A building whose corresponding prerequisite towers remain standing therefore stays invulnerable even if Backdoor Protection is disabled.

| Property | Value |
|---|---:|
| Incoming Damage Reduction | 50% |
| Heal per Second | 180 |
| Backdoor Disable Duration | 15 |
| Aura Linger Duration | 0.5 |
| Ancient-centered base Detection Radius | 4000 |
| Tier 2 Tower Detection Radius | 900 |
| Incoming Damage Reduction against illusions and all other summoned units | 75% |

Detection is aura-based. The aura’s 0.5-second linger makes the effective reactivation delay 15.5 seconds. While active, the building self-heals 18 health at 0.1-second intervals, beginning immediately when it takes damage. Only damage from enemies is healed; allied damage is not.

The generic incoming-damage reduction affects all damage types not flagged as HP removal. It stacks additively with other generic incoming-damage manipulation and multiplicatively with Reinforced-class reduction.

| Source | Expression |
|---|---|
| Illusion attack damage | `IllusionDamageDealt × 0.1` |
| Illusion spell damage | `SpellDamageDealt × 0.25` |
| Summons and Dominated creeps | `AttackDamageDealt × 0.025` |

Associated modifiers are `modifier_backdoor_protection`, `modifier_backdoor_protection_in_base`, and `modifier_backdoor_protection_active`. The visible status indicates that the structure takes reduced damage and rapidly regenerates damage while no enemy creeps are nearby. [corpus:liquipedia_dota2/buildings@2376134#Backdoor_Protection]

### Glyph of Fortification

Glyph of Fortification is a team ability usable by any player through the button to the right of the minimap or a configured hotkey. Its cooldown is shared by the team: one player’s use places it on cooldown for every teammate. The spectator button is split to display both teams’ cooldowns simultaneously.

Glyph temporarily makes all allied buildings and lane creeps impervious to damage through incoming-damage reduction. It also gives Tier 2 and higher Towers multishot attacks. Its short duration and high cooldown allow defensive use against pushes, offensive use to protect pushing creep waves, and use of Tower multishots against enemies.

| Property | Value |
|---|---:|
| Damage | Instant Attack, Physical |
| Building Incoming Damage Reduction | 100% |
| Building Duration | 7 |
| Lane-creep Duration | 3 |
| Bonus Attack Targets for Tier 2 and higher Towers | 5 |
| Cooldown Reset Delay | 1 |
| Initial Downtime | 180 |
| Cooldown | 300 |

Tier 1 Towers do not gain multishot. Losing the first Tier 1 Tower, first Tier 2 Tower, or first Melee Barracks resets Glyph’s cooldown after the listed delay.

The effect applies generic 100% incoming-damage reduction rather than invulnerability, so instant-kill sources can still kill affected units. Whenever an affected Tower launches an attack projectile, it performs instant attacks against the closest valid enemies. All extra projectiles launch simultaneously with the main attack, even if the primary attack misses, and travel at the leading projectile’s speed.

Multishot does not target wards, other buildings, invisible units, attack-immune units, untargetable units, or units inside the Fog of War. Attacking a ward or building can nevertheless cause secondary projectiles to hit valid targets within the radius.

The effect applies to:

| Structures |
|---|
| Towers |
| Ranged Barracks and Melee Barracks |
| Effigy Buildings |
| Ancients |
| Fountains |
| Fiend’s Gate |

Associated modifiers are `modifier_fountain_glyph`, whose status states that the structure is briefly impervious to damage, and the hidden `modifier_glyph_reset`. [corpus:liquipedia_dota2/buildings@2376134#Glyph_of_Fortification]

## Towers

Towers attack any non-neutral enemy unit entering their range and form both factions’ main line of defense. Each of the three lanes has three Towers, while each Ancient has two more, for a total of 11 Towers per faction.

| Tier | Location |
|---|---|
| Tower (Tier 1) | At the end of each lane |
| Tower (Tier 2) | Halfway through each lane |
| Tower (Tier 3) | On the three ramps at each base |
| Tower (Tier 4) | In pairs in front of each Ancient |

A Tower is innately invulnerable until the preceding lower-tier Tower in its lane is destroyed. Tier 1 Towers are invulnerable before the game begins. Barracks need not be destroyed to make Tier 4 Towers vulnerable. Both Tier 4 Towers must be destroyed to remove the Ancient’s invulnerability. [corpus:liquipedia_dota2/buildings@2376134#Towers]

### Tier attributes

| Building | Health (Deny Health) | Armor | Attack Damage | Backdoor Protection | Vision Range |
|---|---:|---:|---:|---:|---:|
| Tower (Tier 1) | 1800 (180) | 12 | 88‒92 (100 DPS) | 0 | 1900 600 |
| Tower (Tier 2) | 2500 (250) | 16 | 170‒174 (191.11 DPS) | 1 | 1900 1100 |
| Tower (Tier 3) | 2500 (250) | 16 | 170‒174 (191.11 DPS) | 1 | 1900 1100 |
| Tower (Tier 4) | 2600 (260) | 21 | 170‒174 (191.11 DPS) | 1 | 1900 1100 |

[corpus:liquipedia_dota2/buildings@2376134#Tier_Difference_(Towers)]

### Attack priority

When selecting a new target, Towers apply three criteria in order.

#### 1. Unit type

| Priority order |
|---|
| Heroes and non-hero units alike |
| Siege Creeps |
| Buildings |
| Ward-type units |

Unit types within attack range are checked continuously. If a Tower is attacking a lower-priority unit and a higher-priority unit enters range, it immediately switches to the higher-priority unit.

#### 2. Threat level

| Priority order |
|---|
| Units directly attacking the Tower |
| Units attacking an ally of the Tower |
| Units that are idle or casting abilities |

Threat checks apply only within 700 range and occur once when the Tower chooses its next target. A later change in the chosen unit’s action does not normally make the Tower switch.

#### 3. Distance

If several units meet the preceding criteria, the closest is selected.

#### Manual de-aggro

A unit being attacked by a Tower can issue an attack order against another allied unit to make the Tower immediately choose a new target. This works only if another allied hero is closer to the Tower than the current target. The order alone is sufficient; the attack need not begin, and immediately canceling the order does not prevent de-aggro.

Unit-type priority still applies, so aggro cannot be transferred from a higher-priority unit to a lower-priority one. This de-aggro can occur only once every 2.5 seconds. It also applies to Fountains and lane creeps.

#### Protective Towers

Towers protect heroes from other heroes. If a hero within 500 range of a Tower attacks another hero, the Tower immediately switches to the attacker. Regular manual and automatic attacks trigger this behavior; instant attacks do not. Manually casting an active attack modifier does not trigger it, but using that modifier through autocast does.

Protected heroes include illusions, clones, and the Spirit Bear. Valid attackers include heroes, illusions, clones, and creep-heroes. The factions of the attacker and target do not matter, so an enemy Tower can be aggroed by actively denying an allied hero or by being forced through a taunt to attack allies.

This behavior counteracts manual de-aggro. Manual de-aggro occurs on the attack order, whereas protection triggers on the order and attack beginning. When denying an ally, the Tower therefore initially de-aggros when the order is issued and re-aggros when the attack begins. This protective behavior applies to lane creeps but not Fountains. [corpus:liquipedia_dota2/buildings@2376134#Attack_Priority]

### Visual indicators

When a player approaches a Tower, part of its attack range begins fading into view at about 600 range. It becomes more visible as the player approaches and resembles a bending wall when viewed from the front. It is yellow if the Tower is already attacking.

Crossing the wall reveals the full attack-range circle. If the Tower starts attacking the player, a red line from the Tower and an audio cue warn that the player is targeted. If the Tower switches away, the effects become yellow and the targeting effect plays again on the new target. These effects are client-sided and appear differently to each player. [corpus:liquipedia_dota2/buildings@2376134#Visual_Indicators]

### Tower bounties

All three Tower bounty types grant unreliable Gold. Turbo Mode applies a building Gold-bounty multiplier of 2.

| Bounty type | Definition |
|---|---|
| Last Hit Bounty | Granted to the player who makes the Tower’s last hit. |
| Team Bounty | Granted to the team when the Tower is destroyed. If nobody can receive last-hit credit, such as when lane creeps destroy it, the Team Bounty is granted. |
| Denied Bounty | Both factions receive `0.5 × TeamBounty` when a Tower is denied. |

#### Default

| Building | Team Bounty / Hero | Last Hit Bounty (Avg) | Last Hit (Σ) | Without Last Hit (Σ) | Deny Bounty / Hero | Deny Bounty (Σ) |
|---|---:|---:|---:|---:|---:|---:|
| Tower (Tier 1) | 90 | 120 | 570 | 450 | 45 | 225 |
| Tower (Tier 2) | 110 | 140 | 690 | 550 | 55 | 275 |
| Tower (Tier 3) | 125 | 160 | 785 | 625 | 62 | 310 |
| Tower (Tier 4) | 145 | 180 | 905 | 725 | 72 | 360 |

#### Turbo Mode

| Building | Team Bounty / Hero | Last Hit Bounty (Avg) | Last Hit (Σ) | Without Last Hit (Σ) | Deny Bounty / Hero | Deny Bounty (Σ) |
|---|---:|---:|---:|---:|---:|---:|
| Tower (Tier 1) | 180 | 240 | 1140 | 900 | 90 | 450 |
| Tower (Tier 2) | 220 | 280 | 1380 | 1100 | 110 | 550 |
| Tower (Tier 3) | 250 | 320 | 1570 | 1250 | 125 | 625 |
| Tower (Tier 4) | 290 | 360 | 1810 | 1450 | 145 | 725 |

[corpus:liquipedia_dota2/buildings@2376134#Tower_Bounty]

### Tower Protection

Tower Protection is a passive aura affecting allied heroes.

| Property | Value |
|---|---:|
| Radius | 900 |
| Armor Bonus | 3/5/5/5 |
| Health Regen Bonus | 1/3/3/3 |
| Aura Linger Duration | 0.5 |
| Maximum health regenerated in one minute | 60/180/180/180 |

It affects heroes, including illusions, clones, and creep-heroes, and works on invulnerable heroes but not hidden heroes. Multiple Tower Protection auras do not stack. When teleporting between Towers, the bonuses immediately update to those of the Tower.

Associated modifiers are `modifier_tower_aura` and `modifier_tower_aura_bonus`; their statuses indicate increased armor and increased armor plus health regeneration, respectively. [corpus:liquipedia_dota2/buildings@2376134#Tower_Protection]

### True Sight

Tower True Sight is a passive enemy-affecting aura that reveals nearby invisible enemy units and wards.

| Property | Value |
|---|---:|
| Reveal Radius | 700 |
| Aura Linger Duration | 0.5 |

The aura is unobstructed and its debuff lingers for 0.5 seconds. It does not affect enemies with True Sight Immunity. Holding Alt displays the True Sight radii of allied Sentry Wards and Towers as green rings. Its hidden modifier is `modifier_truesight`. [corpus:liquipedia_dota2/buildings@2376134#True_Sight]

### Barracks Reinforcement

Barracks Reinforcement is a passive self-affecting ability exclusive to Tier 4 Towers. Each standing Barracks in the base grants 4 armor.

| Standing Barracks | Total armor |
|---|---|
| 0/1/2/3/4/5/6 | 0/4/8/12/16/20/24 |

There are 6 Barracks total. The associated modifier is `modifier_armor_per_barracks`, whose status indicates that each standing Barracks reinforces the Tower and increases its armor. [corpus:liquipedia_dota2/buildings@2376134#Barracks_Reinforcement]

## Barracks

Barracks, commonly shortened to Rax or Racks, stand behind the Tier 3 Tower in each respective lane. Their destruction is not required to make Tier 4 Towers vulnerable.

Each faction has two Barracks per lane and 6 total, comprising 3 of each type. Melee Barracks correspond to Melee Creeps and Flagbearer Creeps; Ranged Barracks correspond to Ranged Creeps and Siege Creeps. In every lane and for both factions, the Ranged Barracks is to the left of the Melee Barracks.

| Property | Melee Barracks | Ranged Barracks |
|---|---:|---:|
| Health | 2200 | 1300 |
| Deny Health | 220 | 130 |
| Health Regen | 5 | 0 |
| Armor | 15 | 9 |
| Daytime and nighttime Vision Range | 900 and 600 | 900 and 600 |
| Attacks | None | None |
| True Sight | None | None |
| Backdoor Protection | Yes | Yes |

[corpus:liquipedia_dota2/buildings@2376134#Barracks]

### Lane-creep upgrades

Barracks remain invulnerable until their corresponding defending Tier 3 Tower is destroyed. Losing Barracks does not stop lane creeps from spawning; it upgrades them.

Destroying an enemy Melee or Ranged Barracks makes the corresponding lane of the destroying team spawn super creeps instead of regular creeps. Super creeps are stronger and grant the enemy less Gold and experience when killed. Destroying all enemy Barracks causes mega creeps to spawn in every lane and grants siege creeps additional damage. Flagbearer creeps are not upgraded. [corpus:liquipedia_dota2/buildings@2376134#Lane_Creep_Upgrades]

### Barracks bounties

All three Barracks bounty types grant unreliable Gold. Turbo Mode applies a building Gold-bounty multiplier of 2.

| Bounty type | Definition |
|---|---|
| Last Hit Bounty | Granted to the player making the last hit. That player does not receive the Team Bounty, and vice versa. |
| Team Bounty | Granted to the team when a Barracks is destroyed. If nobody can receive last-hit credit, such as when lane creeps destroy it, the Team Bounty is granted. |
| Denied Bounty | Does not reduce the Team Bounty and grants the same amount as the Team Bounty. |

#### Default

| Building | Team Bounty / Hero | Last Hit Bounty (Avg) | Last Hit (Σ) | Without Last Hit (Σ) | Deny Bounty / Hero |
|---|---:|---:|---:|---:|---|
| Melee Barracks | 155 | 112 | 887 | 775 | Same as Team Bounty |
| Ranged Barracks | 90 | 112 | 562 | 450 | Same as Team Bounty |

#### Turbo Mode

| Building | Team Bounty / Hero | Last Hit Bounty (Avg) | Last Hit (Σ) | Without Last Hit (Σ) | Deny Bounty / Hero |
|---|---:|---:|---:|---:|---|
| Melee Barracks | 310 | 224 | 1774 | 1550 | Same as Team Bounty |
| Ranged Barracks | 180 | 224 | 1124 | 900 | Same as Team Bounty |

[corpus:liquipedia_dota2/buildings@2376134#Barracks_Bounty]

## Ancients

Ancients are massive structures inside each faction’s base and the game’s main objective: victory requires destroying the enemy Ancient while keeping the allied Ancient alive. They are also called Thrones; legacy DotA names include Tree for the Radiant Ancient and Throne for the Dire Ancient.

Each Ancient is guarded by two Tier 4 Towers, both of which must be destroyed to remove its invulnerability.

| Property | Value |
|---|---:|
| Health | 4500 |
| Health Regen | 12 |
| Health Regen in Turbo Mode | 0 |
| Armor | 23 |
| Daytime and nighttime Vision Range | 2600 and 2600 |
| Attacks | None |
| Backdoor Protection | Yes |

[corpus:liquipedia_dota2/buildings@2376134#Ancients]

### Ancient True Sight

The Ancient has a passive enemy-affecting True Sight aura that reveals nearby invisible enemy units and wards.

| Property | Value |
|---|---:|
| Reveal Radius | 900 |
| Aura Linger Duration | 0.5 |

[corpus:liquipedia_dota2/buildings@2376134#Ancients_Ability]

## Fountains

Fountains occupy the respawn areas of both bases and provide maximum-health- and maximum-mana-based regeneration to allied units through Rejuvenation Aura.

| Property | Value |
|---|---:|
| Invulnerability | Permanent |
| Daytime and nighttime Vision Range | 1800 and 1800 |
| Attack Range | 1200 |
| Projectile Speed | 1400 |
| Attack Damage | 290‒310 |
| Attacks per Second | 6.67 |
| DPS | 2000 |
| Splash Radius | 250 |
| Splash Damage | 25% |

Fountain Damage counts as player-based damage and dispels consumables and other abilities normally disabled by player-based damage. Fountains use Tower attack priority except that attacking an enemy hero cannot immediately aggro them. [corpus:liquipedia_dota2/buildings@2376134#Fountains]

### Fountain abilities

#### Rejuvenation Aura

Rejuvenation Aura is a passive aura affecting allied units.

| Property | Value |
|---|---:|
| Radius | 1200 |
| Max Health as Health Regen Bonus | 5% |
| Max Mana as Mana Regen Bonus | 6% |
| Aura Linger Duration | 3 |
| Bottle Refill Interval | 1 |

Heroes respawn at the Fountain and are invulnerable and untargetable until given an order. Allied bottles are fully refilled while their carrier is within range; this is not tied to the aura buff itself. Couriers become invulnerable while affected by the buff.

#### Fountain Damage

Fountain Damage is a passive enemy-affecting Attack/Physical ability. Consecutive attacks against the same target deal increasing damage.

| Property | Value |
|---|---:|
| Attack Damage Bonus per Stack | 3 |
| Debuff Duration | 12 |
| Splash Radius | 250 |
| Splash Damage | 25% |
| Accuracy | 25% |

Every attack splashes on impact around the primary target. The Fountain also has passive accuracy that occasionally ignores evasion.

#### True Sight

The Fountain’s passive enemy-affecting True Sight aura reveals nearby invisible enemy units and wards.

| Property | Value |
|---|---:|
| Reveal Radius | 1200 |
| Aura Linger Duration | 0.5 |

[corpus:liquipedia_dota2/buildings@2376134#Fountain_Ability]

## Effigy Buildings

Effigy Buildings, also called Filler Buildings, are base structures that delay lane creeps from reaching the Tier 4 Towers. Each base contains 7, spread around the Ancient.

Five form a half-circle around the Ancient and can be customized with Effigy Blocks. Customization changes their appearance and makes them display a text notification when destroyed, but is purely cosmetic. Each player can customize one of these five buildings in their base. The Radiant has two Effigy Building models, while the Dire uses one model for all of them.

| Property | Value |
|---|---:|
| Health | 1000 |
| Deny Health | 100 |
| Health Regen | 0 |
| Armor | 10 |
| Daytime and nighttime Vision Range | 900 and 600 |
| Gold Bounty | 68 |
| Gold Bounty in Turbo Mode | 136 |
| Bounty reliability | Unreliable |
| Attacks | None |
| True Sight | None |
| Backdoor Protection | Yes |

[corpus:liquipedia_dota2/buildings@2376134#Effigy_Buildings]

## Defender’s Gates

Defender’s Gates are force fields in the walls of each faction’s main base. Allies can path through them, while enemies are completely blocked. Each faction has 2, positioned at the furthest edges of the base walls behind the top and bottom Tier 3 Towers. They connect to paths leading directly toward the Tormentors and are separated from the main lane by cliffs. [corpus:liquipedia_dota2/buildings@2376134#Defender's_Gate]

### Ability

Defender’s Gate is a permanent passive force field affecting enemies. It grants vision, permits allied pathing, and fully blocks enemies.

| Property | Value |
|---|---:|
| Segments | 15 |
| Pathing Block Radius | 24 |
| Vision Radius | 700 |

[corpus:liquipedia_dota2/buildings@2376134#Defender's_Gate_2]

### Mechanics

Defender’s Gate cannot interact with abilities or be selected. Its 15 segments are tightly aligned. Each has a collision size of 24 and is placed every 12 distance from the preceding segment, causing overlap that forms a tight line. The gate has a width of 24 and length of 192.

A non-selectable `npc_dota_base_blocker` unit occupies the gate’s center. The aura gives allies unobstructed movement but not phased movement. Flying units can also pass freely. Holding Alt reveals the gate’s vision radius in the world and on the minimap. [corpus:liquipedia_dota2/buildings@2376134#Details]

## Abilities affecting buildings

The following abilities can target or damage buildings. Hero abilities dealing physical attack damage are reduced by Reinforced and by standard armor-value reductions.

| Category | Source | Ability or effect |
|---|---|---|
| Bonus damage vs buildings | Attack Damage | Reinforced |
| Bonus damage vs buildings | Earth | Demolish |
| Bonus damage vs buildings | Spirit Bear | Demolish |
| Physical damage | Bounty Hunter | Jinada |
| Physical damage | Centaur Warrunner | Retaliate⁴ |
| Physical damage | Clinkz | Searing Arrows |
| Physical damage | Gyrocopter | Flak Cannon²ᵃ |
| Physical damage | Roshan | Bash |
| Physical damage | Snapfire | Lil’ Shredder |
| Physical damage | Tiny | Tree Attack |
| Physical damage | Troll Warlord | Fervor²ᵇ |
| Physical damage | Weaver | Geminate Attack |
| Physical damage | Windranger | Focus Fire |
| Physical damage to multiple buildings | Clinkz | Searing Arrows¹ |
| Physical damage to multiple buildings | Death Prophet | Exorcism⁴ |
| Physical damage to multiple buildings | Gyrocopter | Flak Cannon (activated)²ᵃ |
| Physical damage to multiple buildings | Luna | Moon Glaives |
| Physical damage to multiple buildings | Muerta | Gunslinger |
| Physical damage to multiple buildings | Mars | Bulwark²ᵃ |
| Physical damage to multiple buildings | Razor | Eye of the Storm²ᵃ |
| Physical damage to multiple buildings | Tidehunter | Anchor Smash¹ |
| Magical damage | Ancient Ice Shaman | Icefire Bomb⁴ |
| Magical damage | Leshrac | Diabolic Edict |
| Magical damage | Lycan Lane Wolf | Cripple²ᵇ |
| Magical damage | Viper | Poison Attack²ᵇ ⁴ |
| Magical damage to multiple buildings | Batrider | Smoldering Resin |
| Magical damage to multiple buildings | Batrider | Sticky Napalm³ ⁴ |
| Magical damage to multiple buildings | Jakiro | Liquid Fire⁴ |
| Magical damage to multiple buildings | Pugna | Nether Blast⁴ |
| Magical damage to multiple buildings | Techies | Proximity Mines⁴ |
| Magical damage to multiple buildings | Timbersaw | Flamethrower⁴ |
| Magical damage to multiple buildings | Tiny | Toss⁴ |
| Magical damage to multiple buildings | Fallen Sky | Fallen Sky⁴ |
| Magical damage to multiple buildings | Meteor Hammer | Meteor Hammer⁴ |
| Armor Reduction | Assault Cuirass | Assault Aura |
| Armor Reduction | Desolator | Corruption |
| Armor Reduction | Dragon Knight | Wyrm’s Wrath³ |
| Armor Reduction | Orb of Blight | Lesser Corruption |
| Armor Reduction | Orb of Corrosion | Corrosion |
| Armor Reduction | Orb of Destruction | Impeding Corruption |
| Armor Reduction | Snapfire | Lil’ Shredder |
| Armor Reduction | Stygian Desolator | Greater Corruption |
| Armor Reduction | Viper | Poison Attack²ᵇ |
| Armor Reduction | Hoodwink | Armor Corruption¹ |
| Armor Reduction | Visage | Armor Corruption¹ |
| Health Restoration Reduction | Orb of Corrosion | Corrosion |
| Health Restoration Reduction | Orb of Frost | Frost |
| Other Debuffs | Abaddon | Curse of Avernus⁴ |
| Other Debuffs | Faceless Void | Chronosphere³ |
| Other Debuffs | Faceless Void | Time Zone³ |
| Other Debuffs | Jakiro | Liquid Fire |
| Other Debuffs | Hill Troll Berserker | Break |
| Other Debuffs | Kobold Soldier | Steal Weapon |
| Other Debuffs | Lycan Lane Wolf | Cripple²ᵇ |
| Other Debuffs | Naga Siren | Song of the Siren |
| Other Debuffs | Roshan | Bash |
| Other Debuffs | Viper | Poison Attack |
| Armor Increase | Assault Cuirass | Assault Aura |
| Protect | Buildings | Glyph of Fortification |
| Protect | Buildings | Backdoor Protection |
| Protect | Crimson Guard | Guard |
| Protect | Lich | Frost Shield |
| Protect | Ogre Magi | Fire Shield |
| Protect | Omniknight | Guardian Angel²ᵃ |
| Protect | Pipe of Insight | Barrier |
| Protect | Treant Protector | Living Armor |
| Damage Reduction vs | Attack Damage | Runty |
| Damage Reduction vs | Attack Damage | Piercing |
| Damage Reduction vs | Clinkz | Skeleton Walk |
| Damage Reduction vs | Wraith King | Bone Guard |
| Damage Reduction vs | Underlord | Abyssal Horde |
| Restore (Heal/Regen) | Buildings | Backdoor Protection |
| Restore (Heal/Regen) | Lich | Frost Shield¹ |
| Restore (Heal/Regen) | Omniknight | Guardian Angel²ᵃ ⁵ |
| Restore (Heal/Regen) | Treant Protector | Living Armor |
| Other Buffs | Ogre Magi | Bloodlust |

| Marker | Requirement or effect |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim’s Scepter. |
| 2b | Requires Aghanim’s Shard. |
| 4 | Less effective on Buildings. |
| 5 | Provides Heal Amp and Health Regen Amp. |

### Conditional interactions

| Source | Interaction |
|---|---|
| Centaur Warrunner — Retaliate | Affects enemy buildings but not allied buildings. Damage is reduced only by armor value. |
| Death Prophet — Exorcism | Damage is reduced by armor value and type. |
| Dragon Knight — Elder Dragon Form | Corrosive Breath deals full damage to buildings. |
| Fallen Sky — Fallen Sky | Fully affects buildings but uses different damage values than against other units. |
| Gyrocopter — Side Gunner | Passive Side Gunner attacks can target buildings. |
| Meteor Hammer — Meteor Hammer | Fully affects buildings but uses different damage values than against other units. |
| Naga Siren — Song of the Siren | Fully affects enemy buildings but not allied buildings. |
| Razor — Eye of the Storm | Can attack buildings but does not reduce their armor. Damage is reduced only by armor value. |
| Tiny — Toss | Deals reduced damage to buildings within the damage radius. Buildings cannot be tossed or directly targeted. |
| Tiny — Tree Grab | Tiny’s attacks deal increased building damage while he wields a tree. |
| Town Portal Scroll — Teleport | Can teleport only to buildings. |
| Viper — Poison Attack | Deals reduced building damage and reduces the affected target’s armor based on current stacks. |
| Windranger — Focus Fire | Can target buildings. |

[corpus:liquipedia_dota2/buildings@2376134#Abilities_Affecting_Buildings]

## Ward interactions

| Interaction | Ability |
|---|---|
| Tower attacks count as hero attacks | Clinkz — Skeleton Archer |
| Tower attacks count as hero attacks | Juggernaut — Healing Ward |
| Tower attacks count as hero attacks | Shadow Shaman — Mass Serpent Ward |
| Tower attacks count as hero attacks | Shadow Shaman — Urnaconda |
| Buildings deal 0 damage | Keeper of the Light — Will-O-Wisp |
| Buildings deal 0 damage | Phoenix — Supernova |
| Ignored by buildings | Techies — Proximity Mines |

[corpus:liquipedia_dota2/buildings@2376134#Interactions_with_Wards]

## Trivia

### Glyph in DotA

Glyph of Fortification grants allied buildings magic immunity and 9999 armor instead of 100% incoming-damage reduction. Because damage values round upward, every attack still deals 1 damage. Magic immunity also prevents spells that normally affect buildings from affecting them. In earlier versions, Glyph did not grant spell immunity, allowing spells including Nether Blast to damage buildings through it. [corpus:liquipedia_dota2/buildings@2376134#Trivia]

### Radiant legacy structures

In DotA, the Radiant are called The Sentinel, the primary army of the Night Elves, and their structures use Night Elf buildings.

| Building | DotA model or name |
|---|---|
| Towers | Ancient Protectors |
| Melee Barracks | Ancients of War |
| Ranged Barracks | Ancients of Lore |
| Effigy Buildings | Moon Wells; there are 11 |
| Fountain | Fountain of Health model; named Well of Life |
| Ancient | The World Tree, using a custom World Tree model whose creator is unknown |

Additional filler structures comprise two Ancients of Wind behind the top and bottom Barracks, each with 900 health and 5 armor, and two Hunter’s Halls farther behind them, each with 1100 health and 5 armor. The Well of Life is not invulnerable: it has 50000 health and 0 armor and can be attacked and destroyed. [corpus:liquipedia_dota2/buildings@2376134#Trivia]

### Dire legacy structures

In DotA, the Dire are called The Scourge, one of the Warcraft universe’s three major Undead factions, and their structures use Undead buildings.

| Building | DotA model or name |
|---|---|
| Towers | Spirit Towers |
| Melee Barracks | Crypts |
| Ranged Barracks | Temples of the Damned |
| Effigy Buildings | Ziggurats; there are 11 |
| Fountain | Defiled Fountain of Health model; named Defiled Fountain of Life |
| Ancient | The Frozen Throne, using the campaign’s Frozen Throne model |

Additional filler structures comprise two Sacrificial Pits behind the top and bottom Barracks, each with 900 health and 5 armor, and two Boneyards farther behind the Ancients of Wind, each with 1100 health and 5 armor. The Defiled Fountain of Life is not invulnerable: it has 50000 health and 0 armor and can be attacked and destroyed. [corpus:liquipedia_dota2/buildings@2376134#Trivia]

### Gallery

The gallery contains a placeholder Glyph icon and Dire Barracks concept art. [corpus:liquipedia_dota2/buildings@2376134#Gallery]

## Recent changes

| Version | Date | Changes |
|---|---|---|
| 7.40 | 2025-12-15 | Added Barracks Reinforcement to Tier 4 Towers, granting 4 armor per standing Barracks up to 24 bonus armor for 6 standing Barracks. Added a second alternative path to both lanes near the safelane Tier 3 Towers; like the offlane paths, these are sealed with Defender’s Gates. Increased Defender’s Gate vision range from 525 to 700. |
| 7.39c | 2025-06-24 | Moved the Watchers at the Shrines of Wisdom farther from the camps. Reduced capture distance from 300 to 200. |
| 7.38 | 2025-02-19 | Removed the Outposts behind the safe lanes. Moved the Twin Gates from near the ends of the safe lanes to the map corners near the Tormentor spawn locations. Lotus Pools ceased being targetable buildings and became part of the map. Each became a hollow ring with a central fountain and 3 walkable openings, and stopped providing both teams with permanent 500-radius ground vision. At 35:00, pools begin spawning Great Healing Lotuses and round up and combine existing regular Healing Lotuses into Great Healing Lotuses. At 60:00, they begin spawning Greater Healing Lotuses and round up and combine existing Great Healing Lotuses into Greater Healing Lotuses. Heroes automatically gather Healing Lotuses while inside the ring’s 350 radius; gathering pauses if an enemy hero is present. The first Healing Lotus takes 1.5 seconds, and consecutive Lotuses take 30% less time than the preceding one. If several allied heroes are present, one receives the Lotus at random. Shrine of Wisdom replaced Wisdom Rune at the same locations. Shrines begin dormant and activate every 7 minutes. Heroes gather the experience by remaining within 300 range for 3 seconds; gathering pauses if an enemy hero is present. If several allied heroes are present, one receives the experience at random, as does the allied hero with the team’s lowest experience. Both receive 280 by default, plus an additional 280 for every 7 minutes of elapsed game time. |

[corpus:liquipedia_dota2/buildings@2376134#Recent_Changes]