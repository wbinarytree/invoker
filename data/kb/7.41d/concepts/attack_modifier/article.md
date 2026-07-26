---
title: Attack Modifier
kind: concept
patch: 7.41d
card:
  entity: attack_modifier
  sentences:
  - text: Attack modifiers are effects applied to a unit’s basic attacks that provide
      healing, damage, or disables and may activate manually, passively, on every
      attack, or by chance.
    marks:
    - corpus:liquipedia_dota2/attack_modifier@2383995
  - text: 'There is no universal stacking rule: different modifier types generally
      stack, while same-type interactions follow each modifier’s mechanics.'
    marks:
    - corpus:liquipedia_dota2/attack_modifier@2383995#Mechanics
  - text: Attack modifiers are calculated when an attack begins, so changes made while
      a projectile is airborne generally do not affect it.
    marks:
    - corpus:liquipedia_dota2/attack_modifier@2383995#Attack_Modifiers
  - text: An attack modifier is not applied when its attack misses.
    marks:
    - corpus:liquipedia_dota2/attack_modifier@2383995#Attack_Modifiers
  - text: Multishot abilities generally apply all attack modifiers but not on-hit
      effects.
    marks:
    - corpus:liquipedia_dota2/attack_modifier@2383995#Attack_Modifiers
  - text: On-hit effects apply only when an attack reaches its target, allowing airborne
      value changes to affect them.
    marks:
    - corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects
  - text: Effects that only change attack speed or attack damage are not attack modifiers.
    marks:
    - corpus:liquipedia_dota2/attack_modifier@2383995#Common_Attack_Modifiers
  - text: Active attack modifiers require manual use on each attack or Autocast, which
      applies them whenever their costs can be paid.
    marks:
    - corpus:liquipedia_dota2/attack_modifier@2383995#Active_Attack_Modifiers
  - text: Manual use employs the ability’s cast range, whereas Autocast employs the
      hero’s attack range.
    marks:
    - corpus:liquipedia_dota2/attack_modifier@2383995#Active_Attack_Modifiers
  - text: Manually casting an active attack modifier draws aggro from neither lane
      creeps nor towers.
    marks:
    - corpus:liquipedia_dota2/attack_modifier@2383995#Active_Attack_Modifiers
  - text: When multiple critical-strike sources proc, only the highest multiplier
      applies.
    marks:
    - corpus:liquipedia_dota2/attack_modifier@2383995#Critical_Strike
  - text: Lifesteal heals only from physical attack damage dealt to the attacked unit.
    marks:
    - corpus:liquipedia_dota2/attack_modifier@2383995#Lifesteal
---

# Attack Modifier

## Overview

Attack modifiers apply effects to a unit’s basic attacks. Effects range from healing to damage and disables, and each modifier may have its own rules: it may not stack, may fully stack, or may work only for melee units, ranged units, or both. Attack modifiers may be active and manually used—usually with an Autocast option—or passive, guaranteed to proc, or chance-based on each attack. [corpus:liquipedia_dota2/attack_modifier@2383995]

## Mechanics

There is no universal stacking rule. Different types generally stack with each other, while interactions between modifiers of the same type depend on their individual mechanics. General descriptions may not cover additional rules or hard-coded exceptions belonging to specific abilities. Many heroes, units, and items also possess unique attack modifiers; on-hit effects have a separate definition that helps distinguish and predict these interactions. [corpus:liquipedia_dota2/attack_modifier@2383995#Mechanics]

### Attack Modifiers

Attack modifiers are applied when an attack begins. This may be visible on a ranged attack’s projectile, as with Corruption or Cold Attack, but not every modifier has a visual effect. Because the modifications are calculated at the start, changes made while a projectile is airborne—such as picking up an item—generally do not affect attacks launched earlier. [corpus:liquipedia_dota2/attack_modifier@2383995#Attack_Modifiers]

Attack modifiers are not applied when the attack misses: the modifier is carried by the attack and fails when the attack does. [corpus:liquipedia_dota2/attack_modifier@2383995#Attack_Modifiers]

Multishot abilities that apply modifiers, including Marksmanship and Split Shot, generally apply all attack modifiers but not on-hit effects. Most on-hit effects specify the “first” or “next” attack, a condition met only by the attack landing on the primary target; the other attacks check for on-hit effects as separate instances. [corpus:liquipedia_dota2/attack_modifier@2383995#Attack_Modifiers]

### On-hit Effects

On-hit effects are applied only when an attack reaches its target. They have no visual effect while a projectile is airborne, and value changes during that time can influence them. An on-hit effect is tied to an ability or item rather than to a particular attack. It can act before evasion, although its implementation may still account for evasion. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects]

The attack that breaks Shadow Walk invisibility and disables passive abilities cannot miss, whereas Overload explicitly does nothing when its attack is evaded. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects]

## Common Attack Modifiers

Common attack modifiers are non-unique modifiers found on many heroes and items. They differ only in their values and in how they are activated or acquired; some apply on every attack and others are chance-based. [corpus:liquipedia_dota2/attack_modifier@2383995#Common_Attack_Modifiers]

Abilities that merely grant or reduce attack speed, such as Focus Fire or Overpower, or attack damage, such as Alacrity, are not attack modifiers: they enhance the attack directly rather than modifying it. [corpus:liquipedia_dota2/attack_modifier@2383995#Common_Attack_Modifiers]

### Corruption

Armor Corruption is an attack modifier with an on-hit effect that reduces the target’s armor. Successive attacks refresh the debuff’s duration rather than stacking it. Each attack applies the armor-reduction debuff before dealing its own damage. It works against wards, buildings, and allied units, and fully stacks with other items or sources of Armor Corruption. [corpus:liquipedia_dota2/attack_modifier@2383995#Corruption]

### Critical Strike

When an attack procs multiple critical-strike sources, only the highest multiplier applies. The red number shown for a critical strike represents the resulting physical damage before reductions. [corpus:liquipedia_dota2/attack_modifier@2383995#Critical_Strike]

### Cleave and Splash

Cleave and Splash are common attack-modifier topics. [corpus:liquipedia_dota2/attack_modifier@2383995#Cleave_and_Splash]

### Lifesteal

Percentage-based lifesteal from items, abilities, and talents stacks independently and additively after each source’s respective creep-lifesteal multiplier. All lifesteal sources are summed before lifesteal amplification is applied as a multiplier to the unit’s lifesteal value. All lifesteal-manipulation sources stack multiplicatively with each other. [corpus:liquipedia_dota2/attack_modifier@2383995#Lifesteal]

Lifesteal healing is a percentage of the total physical attack damage the attacker deals to the attacked unit. If an attack’s damage exceeds the target’s current health and kills it, healing uses the damage the target would have received had it survived. Lifesteal heals more from critical-strike procs and works conditionally with certain attack modifiers. [corpus:liquipedia_dota2/attack_modifier@2383995#Lifesteal]

Lifesteal heals from neither magical attack-damage sources, such as Monkey King Bar procs, nor spell-damage sources of any damage type; it heals only from physical attack damage. Instant attacks against secondary targets can provide lifesteal when attack modifiers work with that instant-attack source. [corpus:liquipedia_dota2/attack_modifier@2383995#Lifesteal]

Most damage-manipulation effects on the attacked target, such as Flesh Golem or Aeon Disk, do not affect lifesteal healing. An illusion’s lifesteal healing is based on its outgoing damage-manipulation values—its total attack damage—but lifesteal gained by attacking illusions is unaffected by their incoming damage-manipulation values. There is no limit to how much a unit can heal through lifesteal. [corpus:liquipedia_dota2/attack_modifier@2383995#Lifesteal]

### Bash

Bash is a passive ability that gives a unit a chance to stun its attack target. Most bashes also deal extra damage when they proc, usually by adding it directly to the attacker’s attack damage. When directly added, this damage can provide lifesteal and is affected by attack-damage reduction. It cannot critically strike or cleave and is unaffected by attack-damage increases, damage block, or magical damage barriers. Multiple bash sources do not stack at all. [corpus:liquipedia_dota2/attack_modifier@2383995#Bash]

## Attack Modifier Sources

### Active Abilities

| Source | Effect |
|---|---|
| Abaddon — Mist Coil | Applies one stack of Curse of Avernus, based on its current level, to affected enemy units. [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Abilities] |
| Clinkz — Burning Barrage | Channels and fires multiple arrows in the target direction, hitting all enemy units for a percentage of Clinkz’ attack damage and applying attack modifiers. [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Abilities] |
| Dragon Knight — Elder Dragon Form | Applies Corrosive Breath, Splash Attack, or Freezing Breath depending on its current level. [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Abilities] |
| Gyrocopter — Flak Cannon | Uses instant attacks against every enemy within the radius; other attack modifiers apply only to the primary target. [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Abilities] |
| Medusa — Split Shot | A toggleable active ability that uses instant attacks against every enemy within attack range; other attack modifiers apply only to the primary target. Aghanim’s Scepter removes this restriction. [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Abilities] |
| Riki — Tricks of the Trade | Deals extra damage to affected targets within the radius based on the current level of Cloak and Dagger. [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Abilities] |
| Tiny — Tree Grab | Makes attacks deal more damage to buildings and grants area damage similar to cleave. [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Abilities] |
| Winter Wyvern — Arctic Burn | Slows movement speed and deals damage over time based on the target’s current health. It can debuff each enemy only once per cast; Aghanim’s Scepter removes this restriction. [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Abilities] |
| Witch Doctor — Death Ward | Death Ward’s attacks bounce between enemies. [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Abilities] |

### Passive Abilities

| Unit | Ability |
|---|---|
| Abaddon | Curse of Avernus [corpus:liquipedia_dota2/attack_modifier@2383995#Passive_Abilities] |
| Drow Ranger | Marksmanship [corpus:liquipedia_dota2/attack_modifier@2383995#Passive_Abilities] |
| Spirit Bear | Demolish [corpus:liquipedia_dota2/attack_modifier@2383995#Passive_Abilities] |
| Spirit Bear | Entangling Claws [corpus:liquipedia_dota2/attack_modifier@2383995#Passive_Abilities] |
| Lone Druid | Entangle [corpus:liquipedia_dota2/attack_modifier@2383995#Passive_Abilities] |
| Luna | Moon Glaives [corpus:liquipedia_dota2/attack_modifier@2383995#Passive_Abilities] |
| Riki | Backstab [corpus:liquipedia_dota2/attack_modifier@2383995#Passive_Abilities] |
| Sniper | Headshot [corpus:liquipedia_dota2/attack_modifier@2383995#Passive_Abilities] |

### Active Attack Modifiers

Active attack modifiers must be actively used on each attack to apply their effects. They can also be set to Autocast, causing every attack to apply the effect when the hero can pay its costs. They typically use different attack-range values when their cast range differs from the hero’s attack range. [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Attack_Modifiers]

Manual use through the designated hotkey uses the ability’s cast range, while Autocast uses the hero’s attack range. Their cast range can be increased by attack-range bonuses appropriate to the hero’s range type, but not by cast-range bonuses. All active attack modifiers are affected by attack-range increases and not by cast-range increases. [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Attack_Modifiers]

On Autocast they count as regular attacks; manually cast, they partly count as ability casts. Manual casting—Orb Walking—therefore draws aggro from neither lane creeps nor towers. In other circumstances they do not count as abilities: they cannot be used when attacking is restricted, such as by disarm, and they neither proc nor trigger on-cast effects. Unless stated otherwise, they use the hero’s attack speed and the ability’s projectile speed. [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Attack_Modifiers]

Spell Steal cannot acquire active attack modifiers except Walrus PUNCH!. [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Attack_Modifiers]

| Unit | Active attack modifier | Notes |
|---|---|---|
| Ancient Apparition | Chilling Touch | 5 [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Attack_Modifiers] |
| Bounty Hunter | Jinada | 4, 5 [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Attack_Modifiers] |
| Clinkz | Searing Arrows | 5 [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Attack_Modifiers] |
| Doom | Infernal Blade | 7 [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Attack_Modifiers] |
| Drow Ranger | Frost Arrows | — [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Attack_Modifiers] |
| Enchantress | Impetus | — [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Attack_Modifiers] |
| Huskar | Burning Spear | — [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Attack_Modifiers] |
| Jakiro | Liquid Fire | 5 [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Attack_Modifiers] |
| Jakiro | Liquid Frost | — [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Attack_Modifiers] |
| Kunkka | Tidebringer | 4, 7 [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Attack_Modifiers] |
| Omniknight | Hammer of Purity | 4, 5 [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Attack_Modifiers] |
| Outworld Destroyer | Arcane Orb | — [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Attack_Modifiers] |
| Silencer | Glaives of Wisdom | — [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Attack_Modifiers] |
| Slark | Saltwater Shiv | 7 [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Attack_Modifiers] |
| Tusk | Walrus PUNCH! | 5, 6 [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Attack_Modifiers] |
| Treant Protector | Leech Seed | 4, 5 [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Attack_Modifiers] |
| Viper | Poison Attack | — [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Attack_Modifiers] |
| Weaver | Geminate Attack | 4 [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Attack_Modifiers] |

| Note | Meaning |
|---|---|
| 4 | Breakable. Ignores Silence. [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Attack_Modifiers] |
| 5 | Can be triggered by Instant Attack. [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Attack_Modifiers] |
| 6 | Rubick can Spell Steal this ability. [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Attack_Modifiers] |
| 7 | Can be triggered by another source of instant attack only if the other source can proc attack modifiers and is triggered during the normal attack animation. [corpus:liquipedia_dota2/attack_modifier@2383995#Active_Attack_Modifiers] |

### Unit Abilities

Most attack modifiers belonging to units are passive abilities, with some exceptions. [corpus:liquipedia_dota2/attack_modifier@2383995#Units_Abilities]

| Unit | Attack modifier |
|---|---|
| Razorback | Poison [corpus:liquipedia_dota2/attack_modifier@2383995#Units_Abilities] |
| Earth | Demolish [corpus:liquipedia_dota2/attack_modifier@2383995#Units_Abilities] |
| Ghost | Frost Attack [corpus:liquipedia_dota2/attack_modifier@2383995#Units_Abilities] |
| Forged Spirit | Melting Strike [corpus:liquipedia_dota2/attack_modifier@2383995#Units_Abilities] |
| Spiderling | Poison Sting [corpus:liquipedia_dota2/attack_modifier@2383995#Units_Abilities] |
| Spiderling | Spawn Spiderling [corpus:liquipedia_dota2/attack_modifier@2383995#Units_Abilities] |
| Spirit Bear | Entangling Claws [corpus:liquipedia_dota2/attack_modifier@2383995#Units_Abilities] |
| Spirit Bear | Demolish [corpus:liquipedia_dota2/attack_modifier@2383995#Units_Abilities] |
| Undying Zombie | Deathlust [corpus:liquipedia_dota2/attack_modifier@2383995#Units_Abilities] |
| Vhoul Assassin | Envenomed Weapon [corpus:liquipedia_dota2/attack_modifier@2383995#Units_Abilities] |
| Warlock Golem | Flaming Fists [corpus:liquipedia_dota2/attack_modifier@2383995#Units_Abilities] |

| Note | Requirement |
|---|---|
| 1 | Requires a talent. [corpus:liquipedia_dota2/attack_modifier@2383995#Units_Abilities] |
| 2 | Requires Aghanim’s Scepter. [corpus:liquipedia_dota2/attack_modifier@2383995#Units_Abilities] |
| 3 | Requires Aghanim’s Shard. [corpus:liquipedia_dota2/attack_modifier@2383995#Units_Abilities] |

### Instant Attacks

The following instant attacks cannot proc attack modifiers and do not interact with them. [corpus:liquipedia_dota2/attack_modifier@2383995#Instant_Attack]

| Source | Ability |
|---|---|
| Defiant Shell | Reciprocity [corpus:liquipedia_dota2/attack_modifier@2383995#Instant_Attack] |
| Gyrocopter | Flak Cannon [corpus:liquipedia_dota2/attack_modifier@2383995#Instant_Attack] |
| Luna | Lunar Orbit [corpus:liquipedia_dota2/attack_modifier@2383995#Instant_Attack] |
| Medusa | Split Shot [corpus:liquipedia_dota2/attack_modifier@2383995#Instant_Attack] |
| Specialist’s Array | Splitshot [corpus:liquipedia_dota2/attack_modifier@2383995#Instant_Attack] |

## On-hit Effect Sources

| Source | Effect and interactions |
|---|---|
| Phantom Lancer — Juxtapose | Has a chance to create an illusion of Phantom Lancer on each attack. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Sand King — Burrowstrike | Applies Caustic Finale at its current level to affected units. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Sand King — Caustic Finale | Applies a debuff that slows movement speed and makes the affected unit explode upon death, dealing area damage based on its max health plus a flat bonus. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Silencer — Glaives of Wisdom | Steals intelligence from attacked targets for an amount of time. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Slark — Essence Shift | Steals one of every attribute from attacked targets and converts them into 3 agility for Slark. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Spectre — Desolate | Deals extra pure damage to enemies without allies nearby. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Storm Spirit — Overload | Slows and deals magical damage in an area around the attack target. Its buff is granted whenever Storm Spirit casts an ability. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Templar Assassin — Psi Blades | Deals damage in a line behind the attack target. Its distance is based on Templar Assassin’s attack range and its damage on her attack damage. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Troll Warlord — Fervor | Increases attack speed with every continuous attack against the same target; the bonus is lost when switching targets. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Ursa — Fury Swipes | Places a debuff that gains a stack with every continuous attack and deals extra physical damage based on its number of stacks. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Venomancer — Poison Sting | Slows movement speed and deals damage over time to attack targets. Plague Ward also has this ability. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Quelling Blade — Quell | Deals extra attack damage against non-hero units. It fully stacks with everything except itself. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Battle Fury — Quell | Deals extra attack damage against non-hero units. Quell fully stacks with everything except itself. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Battle Fury — Cleave | Deals cleave damage around the initial target. Multiple instances fully stack but are applied as separate instances. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Orb of Blight — Lesser Corruption | An attack modifier with an on-hit effect that reduces armor. It does not stack with Desolator, Stygian Desolator, or Orb of Corrosion. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Desolator — Corruption | An attack modifier with an on-hit effect that reduces armor. It fully stacks with Stygian Desolator, partially stacks with Orb of Corrosion, and does not stack with Orb of Blight. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Stygian Desolator — Greater Corruption | An attack modifier with an on-hit effect that reduces armor. It fully stacks with Desolator, partially stacks with Orb of Corrosion, and does not stack with Orb of Blight. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Orb of Corrosion — Corrosion | Reduces armor, slows, and applies Health Restoration reduction. It partially stacks with Desolator, Stygian Desolator, or Eye of Skadi, and does not stack with Orb of Blight or Orb of Frost. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Orb of Frost — Frost | Slows and applies Health Restoration reduction. It does not stack with Orb of Corrosion or Skadi. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Eye of Skadi — Cold Attack | Slows and applies Health Restoration reduction. It partially stacks with Orb of Corrosion and does not stack with Orb of Frost. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Javelin — Pierce | Deals extra magical damage when it procs. It fully stacks with everything, including multiple instances of itself. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Bloodthorn — Pierce | Deals extra magical damage when it procs. It fully stacks with everything, including multiple instances of itself. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Monkey King Bar — Pierce | Deals extra magical damage when it procs. It fully stacks with everything except multiple instances of itself. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Maelstrom — Chain Lightning | Launches a Chain Lightning when it procs. It does not stack with Maelstrom-based items. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Mjollnir — Chain Lightning | Launches a Chain Lightning when it procs. It does not stack with Maelstrom-based items. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Orb of Venom — Poison Attack | Gives the proccing attack true strike and damage over time. It does not stack with Witch Blade or Parasma. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Witch Blade — Witch Blade | Gives the proccing attack true strike, slows enemies, and deals damage over time. It does not stack with Orb of Venom or Parasma. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Parasma — Witch Blade | Gives the proccing attack true strike, slows enemies, and deals damage over time. It does not stack with Orb of Venom or Witch Blade. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Skull Basher — Bash | Stuns the target when it procs. It does not stack with Skull Basher-based items. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Abyssal Blade — Bash | Stuns the target when it procs. It does not stack with Skull Basher-based items. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Shadow Blade — Shadow Walk | An on-hit effect that grants bonus damage on the first attack out of invisibility. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Silver Edge — Shadow Walk | An on-hit effect that grants bonus damage, break, and True Strike on the first attack out of invisibility. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Echo Sabre — Echo Strike | Slows movement and attack speed on the proccing attack and the following attack, and drastically increases attack speed for the next attack. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |
| Mage Slayer — Mage Slayer | Reduces the enemy’s spell damage and deals damage over time. [corpus:liquipedia_dota2/attack_modifier@2383995#On-hit_Effects_Sources] |

## Trivia

### Unique Attack Modifiers

Unique Attack Modifiers—UAMs, formerly Orb Effects—were attack modifiers that could not be used simultaneously: one always took priority, and multiple UAMs did not stack. They could work simultaneously with non-unique attack modifiers under this priority order. [corpus:liquipedia_dota2/attack_modifier@2383995#Trivia]

| Priority | Modifier |
|---|---|
| 1st | Active attack modifiers cast manually. [corpus:liquipedia_dota2/attack_modifier@2383995#Trivia] |
| 2nd | Active attack modifiers set to Autocast. [corpus:liquipedia_dota2/attack_modifier@2383995#Trivia] |
| 3rd | Item-based unique attack modifiers. [corpus:liquipedia_dota2/attack_modifier@2383995#Trivia] |

In Ability Draft, the first drafted unique attack-modifier ability always overrode later ones. With multiple items carrying unique attack modifiers, only the item continuously present in the inventory for the longest time would proc or trigger its modifier. Illusions instead prioritized them by inventory-slot reading order. [corpus:liquipedia_dota2/attack_modifier@2383995#Trivia]

When an Autocast modifier’s target was invalid for it, such as a spell-immune unit or building, another unique attack modifier to which the target was vulnerable could be used despite having lower priority. For example, Arcane Orb could not affect a spell-immune hero, but a carried Morbid Mask would proc instead. This exception did not apply to non-Autocastable unique attack modifiers such as Mana Break, which retained the priority order regardless of the target’s spell immunity. [corpus:liquipedia_dota2/attack_modifier@2383995#Trivia]

### Orb Walking

Warcraft III calls unique attack modifiers “orb effects” because items granting them were commonly orbs, such as Orb of Venom and Orb of Corruption, and their effects did not stack. The orb imagery also served as a metaphor for the difficulty of stacking real sphere-shaped objects. [corpus:liquipedia_dota2/attack_modifier@2383995#Orb_Walking]

As a Warcraft III custom map, DotA used the abilities of these orb items and adopted “orb” for item-based attack modifiers that did not stack; its unique attack modifiers were consequently called Orb Effects. Dota2 later replaced Orb Effects with the term Unique Attack Modifiers, although many players coming from DotA continued to call them orb effects. “Orb Walking” likewise originated in Warcraft III and denotes the technique described for active attack modifiers. [corpus:liquipedia_dota2/attack_modifier@2383995#Orb_Walking]

### Stutter Stepping

Stutter stepping originated in Starcraft, carried over into various MOBAs, and was commonly combined with the active-attack-modifier technique of orb walking. [corpus:liquipedia_dota2/attack_modifier@2383995#Stutter_Stepping]

During the cast time of a manually cast active attack modifier, the player can repeatedly issue move commands without cancelling the cast. The first move command after the cast point cancels the backswing, allowing the hero to move almost immediately after launching the attack. Issuing a move command during a regular attack instead cancels that attack and moves the unit immediately, so the player must time the command after the attack launches. Manual active attack modifiers therefore made stutter stepping easier and more effective because the move command required no timing. [corpus:liquipedia_dota2/attack_modifier@2383995#Stutter_Stepping]

Orb walking and stutter stepping were combined so commonly that the combination became known simply as orb walking, even though stutter stepping also works with regular attacks. Consequently, “stutter stepping” became less familiar terminology in Dota, although the technique is still called stutter stepping outside Dota. [corpus:liquipedia_dota2/attack_modifier@2383995#Stutter_Stepping]

## Recent Changes

| Version | Date | Description |
|---|---|---|
| 7.31 | 2022-02-23 | Mana Break now stacks with Manabreak. [corpus:liquipedia_dota2/attack_modifier@2383995#Recent_Changes] |
| 7.07 | 2017-10-31 | Mana Break and Arcane Orb are no longer unique attack modifiers. Morbid Mask, Mask of Madness, and Satanic are no longer unique attack modifiers. [corpus:liquipedia_dota2/attack_modifier@2383995#Recent_Changes] |
| 7.06 | 2017-05-15 | Frost Arrows, Caustic Finale, Lesser Corruption, and Corruption are no longer unique attack modifiers. [corpus:liquipedia_dota2/attack_modifier@2383995#Recent_Changes] |