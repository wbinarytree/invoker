---
title: Critical Strike
kind: concept
patch: 7.41d
card:
  entity: critical_strike
  sentences:
  - text: Critical strike is a passive ability that gives a successful attack a chance
      to amplify its total damage by a source multiplier, defined as Critical Strike
      Multiplier = 1 + MAX Ci.
    marks:
    - corpus:liquipedia_dota2/critical_strike@2353356
    - corpus:liquipedia_dota2/critical_strike@2353356#Multiplier
  - text: The proc is determined when the attack begins, not when it launches or lands.
    marks:
    - corpus:liquipedia_dota2/critical_strike@2353356#Mechanics
  - text: A critical strike is an attack-damage amplifier, not a separate bonus-damage
      instance.
    marks:
    - corpus:liquipedia_dota2/critical_strike@2353356#Multiplier
  - text: Its multiplier is applied before reductions or amplifications on the attacker
      or target.
    marks:
    - corpus:liquipedia_dota2/critical_strike@2353356#Multiplier
  - text: It includes main attack damage and percentage or flat bonus attack damage
      but excludes separate damage instances such as conditional attack-damage bonuses.
    marks:
    - corpus:liquipedia_dota2/critical_strike@2353356#Multiplier
  - text: All chance-based critical-strike sources use pseudo-random distribution.
    marks:
    - corpus:liquipedia_dota2/critical_strike@2353356#Multiplier
  - text: Multiple procs roll from strongest to weakest multiplier and stop at the
      first proc, so two critical strikes cannot occur on the same attack.
    marks:
    - corpus:liquipedia_dota2/critical_strike@2353356#Stacking
  - text: If a stronger source procs, weaker sources do not roll, and their current
      pseudo-random proc chances are neither increased nor reset for that attack.
    marks:
    - corpus:liquipedia_dota2/critical_strike@2353356#Stacking
  - text: Critical strike fully stacks with attack modifiers, whose attack-damage
      increases and reductions are included in its multiplier.
    marks:
    - corpus:liquipedia_dota2/critical_strike@2353356#Attack_Modifier_Interactions
  - text: Lifesteal and cleave or splash are calculated after the critical strike,
      increasing their values during a proc.
    marks:
    - corpus:liquipedia_dota2/critical_strike@2353356#Attack_Modifier_Interactions
  - text: The displayed red number with a lightning-bolt icon reports multiplied damage
      before reductions or amplifications, not the damage actually taken.
    marks:
    - corpus:liquipedia_dota2/critical_strike@2353356#Visual_Feedback
  - text: Critical Attack Damage = %Critical / %Proc.
    marks:
    - corpus:liquipedia_dota2/critical_strike@2353356#Critical_Strike_Sources
---

# Critical Strike

Critical strike is a passive ability that gives a successful attack a chance to deal bonus damage. [corpus:liquipedia_dota2/critical_strike@2353356]

## Mechanics

A critical strike is determined when an attack begins, not when it launches or lands. If Crystalys procs when an attack starts, that attack retains Crystalys’ critical-strike value even if the item is upgraded during the attack animation. Likewise, an attack begun against an enemy affected by Soul Rend still applies the critical strike if the debuff expires during the animation. [corpus:liquipedia_dota2/critical_strike@2353356#Mechanics]

### Visual Feedback

A critical strike displays a red number on the victim with a lightning-bolt icon to its right. The number is the multiplied damage before reductions or amplifications, so it does not equal the damage actually taken. [corpus:liquipedia_dota2/critical_strike@2353356#Visual_Feedback]

### Multiplier

A critical strike multiplies the attack’s total damage by the source’s multiplier. It is an attack-damage amplifier rather than a separate instance of bonus damage:

`Critical Strike Multiplier = 1 + MAX Ci`

The multiplier is applied before reductions or amplifications on either the target or attacker. It counts main attack damage and percentage or flat bonus attack damage, but not separate damage instances such as conditional attack-damage bonuses. Damage added directly to attack damage by an ability may be included, although exceptions exist. All chance-based critical-strike sources use pseudo-random distribution. [corpus:liquipedia_dota2/critical_strike@2353356#Multiplier]

### Stacking

Multiple critical-strike procs are rolled from the strongest to the weakest multiplier, stopping when one procs; two critical strikes therefore cannot proc on the same attack, producing diminishing behavior. When a stronger source procs, weaker sources do not roll, so their pseudo-random states are preserved: their current proc chances are neither increased nor reset for that attack.

While Tusk casts Walrus PUNCH!, the attack will not proc Daedalus’ critical strike (225%) because Walrus PUNCH! has a higher critical-strike value of 1. If a stronger critical strike occurs ahead of a cooldown-based source such as Mortal Strike, the cooldown-based strike remains unused and does not enter cooldown for that attack. [corpus:liquipedia_dota2/critical_strike@2353356#Stacking]

### Attack Modifier Interactions

Critical strike fully stacks with and does not interfere with attack modifiers. Attack-damage increases and reductions from modifiers are included by its multiplier. Conditional attack-damage bonuses may or may not be included.

The following modifiers are calculated after the critical strike, increasing their value during a proc:

| Modifier | Interaction |
|---|---|
| Lifesteal | Increases the amount lifestealed; this is distinct from lifesteal manipulation. |
| Cleave / Splash | Deals increased damage to all units within the cleave radius. |

[corpus:liquipedia_dota2/critical_strike@2353356#Attack_Modifier_Interactions]

#### Sources Affected

| Conditional attack-damage bonus affected by Critical Strike |
|---|
| Battle Fury – Quell |
| Bounty Hunter – Jinada |
| Ember Spirit – Sleight of Fist |
| Kunkka – Tidebringer |
| Quelling Blade – Quell |
| Riki – Cloak and Dagger |
| Storm – Wind Walk |
| Tiny – Tree Grab |
| Tusk – Tag Team |
| Weaver – Geminate Attack |

[corpus:liquipedia_dota2/critical_strike@2353356#Sources_Affected]

#### Sources Not Affected

| Conditional attack-damage bonus not affected by Critical Strike |
|---|
| Abyssal Blade – Bash |
| Ancient Apparition – Chilling Touch |
| Clinkz – Burning Barrage Arrows<sup>3</sup> |
| Clinkz – Skeleton Arrows Multishot<sup>2b, 1</sup> |
| Clinkz – Burning Army Arrows<sup>2a, 3</sup> |
| Drow Ranger – Frost Arrows |
| Drow Ranger – Multishot Frost Arrows |
| Drow Ranger – Splinter Shot<sup>2a, 3</sup> |
| Enchanted Quiver – Certain Strike |
| Enchantress – Impetus |
| Enchantress – Sproink<sup>2a</sup> |
| Faceless Void – Time Walk<sup>2a, 3</sup> |
| Faceless Void – Time Lock<sup>3</sup> |
| Maelstrom – Chain Lightning |
| Mjollnir – Chain Lightning |
| Gleipnir – Chain Lightning |
| Javelin – Pierce |
| Monkey King Bar – Pierce |
| Outworld Destroyer – Arcane Orb |
| Roshan – Bash |
| Shadow Blade – Shadow Walk |
| Silencer – Glaives of Wisdom<sup>2a, 3</sup> |
| Silver Edge – Shadow Walk |
| Skull Basher – Bash |
| Slardar – Bash of the Deep |
| Sniper – Headshot |
| Spectre – Desolate |
| Storm Spirit – Overload<sup>1, 3</sup> |
| Templar Assassin – Meld |
| Ursa – Fury Swipes |
| Warlock Golem – Flaming Fists |
| Anti-Mage – Mana Break |
| Diffusal Blade – Manabreak |
| Disperser – Manabreak |
| Demonic Warrior (Book of the Dead) – Mana Break |
| Demonic Warrior (Underlord) – Mana Break |

| Marker | Condition |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |
| 3 | The ability’s multishot / bounces can proc critical strike. The bonus spell damage is not considered by critical damage. |

[corpus:liquipedia_dota2/critical_strike@2353356#Sources_Not_Affected]

## Critical Strike Sources

The amount of damage increase is defined as:

`Critical Attack Damage = %Critical / %Proc`

[corpus:liquipedia_dota2/critical_strike@2353356#Critical_Strike_Sources]

### Chance-Based Sources

| Chance-based critical-strike ability |
|---|
| Alpha Wolf – Critical Strike |
| Brewmaster – Drunken Brawler |
| Chaos Knight – Chaos Strike |
| Crystalys – Critical Strike |
| Daedalus – Critical Strike |
| Juggernaut – Blade Dance |
| Lycan – Shapeshift |
| Lycan – Wolf Bite |
| Phantom Assassin – Coup de Grace |
| Revenant's Brooch – Phantom Critical |
| Tusk – Walrus PUNCH! |

| Marker | Condition |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |

[corpus:liquipedia_dota2/critical_strike@2353356#Chance-based_Sources]

### Ensured Critical Strike Sources

| Ensured critical-strike source |
|---|
| Dawnbreaker – Luminosity |
| Mars – God's Rebuke |
| Monkey King – Boundless Strike |
| Tusk – Walrus PUNCH! |
| Void Spirit – Astral Step<sup>1</sup> |
| Wraith King – Mortal Strike |

| Marker | Condition |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |

[corpus:liquipedia_dota2/critical_strike@2353356#Ensured_Critical_Strike_Sources]

### Unique Critical Strike Sources

Sources with the `MODIFIER_PROPERTY_PREATTACK_TARGET_CRITICALSTRIKE` flag proc critical strike at the unit’s attack point against the affected target. [corpus:liquipedia_dota2/critical_strike@2353356#Unique_Critical_Strike_Sources]

### Instant Attacks

| Scope | Instant-attack source |
|---|---|
| Does not trigger Critical Strike | Morphling – Ebb |
| Does not trigger Critical Strike on secondary targets | Gyrocopter – Flak Cannon |
| Does not trigger Critical Strike on secondary targets | Medusa – Split Shot |
| Does not trigger Critical Strike on secondary targets | Storm Spirit – Overload<sup>1</sup> |

[corpus:liquipedia_dota2/critical_strike@2353356#Instant_Attack]

### Talents

| Property | Value |
|---|---|
| Ability | Critical Strike |
| Ability type | Passive |
| Affects | Enemies |
| Proc Chance | Varies |
| Critical Damage | Varies |

The ability grants the hero’s attacks a chance to deal critical damage.

| Value | Series |
|---|---|
| Proc chance | 24%/30%/20%/50% |
| Critical damage | 200%/200%/150%/400% |
| Average attack-damage increase | 24%/30%/10%/150% |

The proc chances of multiple critical-strike sources stack. If two sources proc simultaneously, the higher multiplier has priority. Critical Strike uses pseudo-random distribution and does not work against wards, buildings, or allied units.

For self-illusions, the displayed critical-strike values are before illusion outgoing damage and armor reduction. Heroes can have a talent that grants them critical strike. [corpus:liquipedia_dota2/critical_strike@2353356#Talents]

## Version History

| Version | Date | Change |
|---|---|---|
| 7.30 | 2021-08-18 | Multiple critical-strike procs are now rolled from the strongest to weakest multiplier and stop rolling once a proc occurs. |

[corpus:liquipedia_dota2/critical_strike@2353356#Version_History]