---
title: Turn Rate
kind: concept
patch: 7.41d
card:
  entity: turn_rate
  sentences:
  - text: Turn rate is a unit’s turning speed, measured in radians per 0.03 seconds;
      most heroes have a base value of 0.5–0.6 and are stated to require 0.15–0.19
      seconds to turn 180°.
    marks:
    - corpus:liquipedia_dota2/turn_rate@2394976
    - corpus:liquipedia_dota2/turn_rate@2394976#Mechanics
  - text: Before moving to a location, attacking another unit, or casting a spell
      on one, a unit turns to face its destination or target.
    marks:
    - corpus:liquipedia_dota2/turn_rate@2394976
  - text: Movement and targeted area- or point-casts begin only when the target is
      within 11.5° of the unit’s facing direction.
    marks:
    - corpus:liquipedia_dota2/turn_rate@2394976
  - text: Maximum time to turn 180° is t = 0.03π/T, where T is turn rate.
    marks:
    - corpus:liquipedia_dota2/turn_rate@2394976#Mechanics
  - text: Turn-rate slows modify base turn rate directly, and all slow sources stack
      multiplicatively.
    marks:
    - corpus:liquipedia_dota2/turn_rate@2394976#Mechanics
  - text: Turn rate ramps up after turning starts, but both the ramp duration and
      ramp rate are unknown.
    marks:
    - corpus:liquipedia_dota2/turn_rate@2394976#Mechanics
  - text: The bilateral 11.5° allowance creates a 23° instant-action arc, so an action
      requires at most 168.5° of turning.
    marks:
    - corpus:liquipedia_dota2/turn_rate@2394976#Mechanics
  - text: Turning for an out-of-angle point-, area-, or unit-target cast cannot be
      canceled by move, attack, or another spell-cast order.
    marks:
    - corpus:liquipedia_dota2/turn_rate@2394976#Mechanics
  - text: Turn-rate increases stack multiplicatively, but the resulting value cannot
      exceed 1.
    marks:
    - corpus:liquipedia_dota2/turn_rate@2394976#Turn_Rate_Improving_Abilities
  - text: A set turn rate fixes the value for its duration and prevents other effects
      from changing it.
    marks:
    - corpus:liquipedia_dota2/turn_rate@2394976#Turn_Rate_Setting_Abilities
  - text: Will-O-Wisp, Bulwark, and Gorgon’s Grasp completely prevent affected units
      from turning.
    marks:
    - corpus:liquipedia_dota2/turn_rate@2394976#Turn_Rate_Lock
  - text: Patch 7.29 improved turn rate’s effect on required turning time by 20%.
    marks:
    - corpus:liquipedia_dota2/turn_rate@2394976#Recent_Changes
---

# Turn Rate

Turn rate is the speed at which a unit turns. Before moving to a location, the unit turns to face it; before attacking or casting a spell on another unit, it turns toward the target. Movement and targeted area- or point-casts begin only when the target lies within an 11.5° angle in front of the ordered unit. This turning time makes kiting harder because the hero must repeatedly turn toward and away from the target.

Every unit has a base turn rate that some abilities can reduce. Most heroes have a turn rate between 0.6 and 0.5, requiring between 0.15 and 0.19 seconds to turn 180°. No talents currently improve turn rate. [corpus:liquipedia_dota2/turn_rate@2394976]

## Mechanics

Turn-rate speed was improved by 20% in 7.29. Turn rate is measured in radians per 0.03 seconds. Because 180° equals \(\pi\), or 3.1416, radians, the time required to turn 180° is:

\[
t=\frac{0.03\pi}{T}
\]

Here, \(t\) is the time required to turn around and \(T\) is the turn rate.

Turn-rate slows directly affect base turn rate, and all slow sources stack multiplicatively:

\[
\sum T=
\begin{cases}
T_{\text{Set}} & \text{if }T_{\text{Set}}=\top\\
T_b\times\displaystyle\prod_{i=1}^{n}(1-r_i)(1+a_i) & \text{otherwise}
\end{cases}
\]

\(T_{\text{Set}}\) is the set turn-rate value, \(T_b\) is base turn rate, \(r\) is a turn-rate slow value, and \(a\) is a turn-rate improvement value.

A unit does not immediately turn at its maximum rate. Its turn rate ramps up after it starts turning, reaching its maximum after an unknown amount of time; the ramp rate is also unknown.

When an ability or item cast order targets a point, area, or unit outside the required 11.5° facing angle, the resulting turn cannot be canceled with a move, attack, or new spell-cast order. Because the 11.5° allowance extends in both directions, targets within a 23° angle directly ahead allow instant actions. Targets outside that angle require turning first. The formula calculates maximum turning time; the actual required turn before the action occurs is no more than 168.5°.

Commands issued while turning for a spell cast are queued and executed after the spell is cast. Canceling the cast requires a stop or halt command, as during the spell’s cast animation, preventing accidental cancellation through fast clicking. Pressing `S` after turning has begun does not stop the turn, but it stops the order that initiated it. Templar Assassin can therefore turn during Meld without canceling it, provided the move command is stopped before the targeted point enters the required angle. [corpus:liquipedia_dota2/turn_rate@2394976#Mechanics]

### Stacking examples

#### Example 1

Earthshaker is affected by a 70% turn-rate slow:

\[
T=\times(1-0.7)=\text{Expression error: Unexpected * operator.}
\]

\[
t=\frac{0.03\pi}{\text{Expression error: Unexpected * operator.}}
=\text{Expression error: Unexpected < operator.}
\]

His resulting turn rate is displayed as `Expression error: Unexpected * operator.`, and his approximate time to turn 180° is displayed as `Expression error: Unexpected < operator.s`.

#### Example 2

Earthshaker is affected by turn-rate slows of 70% and 50%:

\[
T=\times(1-0.7)\times(1-0.5)
=\text{Expression error: Unexpected * operator.}
\]

\[
t=\frac{0.03\pi}{\text{Expression error: Unexpected * operator.}}
=\text{Expression error: Unexpected < operator.}
\]

His resulting turn rate is displayed as `Expression error: Unexpected * operator.`, and his approximate time to turn 180° is displayed as `Expression error: Unexpected < operator.s`. [corpus:liquipedia_dota2/turn_rate@2394976#Stacking]

## Turn-rate comparison

| Hero | Turn rate |
|---|---:|
| — | 0.6 |
| — | 0.7 |
| — | 0.8 |
| — | 0.9 |
| — | 1 |

| Turn rate | Time to turn 180° |
|---:|---:|
| 0.4 | 0.262s |
| 0.5 | 0.209s |
| 0.6 | 0.175s |
| 0.7 | 0.15s |
| 0.8 | 0.131s |
| 0.9 | 0.116s |
| 1 | 0.105s |

[corpus:liquipedia_dota2/turn_rate@2394976#Turn_Rate_Comparison]

### Units

| Units | Turn rate |
|---|---:|
| Ofrenda, Minefield Sign, M.A.D., Fountain | 0 |
| Proximity Mine | 0.4 |
| Warlock Golem, Earth, Astral Spirit, Siege Creep, Undying Zombie, Tornado, Warpine Raider, Storm, Skeleton Archer, Minor Imp, Ancient Frostbitten Golem, Super Melee Creep, Mega Melee Creep, Super Ranged Creep, Mega Ranged Creep, Super Siege Creep, Mega Siege Creep, Flagbearer Creep, Super Flagbearer Creep, Mega Flagbearer Creep, Boglet, Ancient Croaker, Marshmage Apprentice, Ancient Marshmage, Demonic Archer, Demonic Warrior, Zealot, Fire, Melee Creep, Ranged Creep, Ancient Rock Golem, Ancient Granite Golem, Shard Golem, Treant, Spiderling, Plague Ward, Courier, Wraith King Skeleton, Death Ward, Healing Ward, Forged Spirit, Lycan Wolf, Ignis Fatuus | 0.5 |
| Keen Cannon | 0.55 |
| Raptor, Razorback | 0.6 |
| Ghost, Ancient Ice Shaman, Pollywog, Croaker, Marshmage, Kobold, Kobold Soldier, Kobold Foreman, Hill Troll Berserker, Hill Troll Priest, Vhoul Assassin, Fell Spirit, Harpy Scout, Harpy Stormcrafter, Centaur Courser, Centaur Conqueror, Giant Wolf, Alpha Wolf, Satyr Banisher, Satyr Mindstealer, Ogre Bruiser, Ogre Frostmage, Mud Golem, Satyr Tormenter, Hellbear, Hellbear Smasher, Wildwing, Wildwing Ripper, Hill Troll, Dark Troll Summoner, Skeleton Warrior, Ancient Black Drake, Ancient Black Dragon, Ancient Rumblehide, Ancient Thunderhide, Eidolon, Ancient Prowler Acolyte, Ancient Prowler Shaman, Familiar | 0.9 |
| Tower (Tier 1), Tower (Tier 2), Tower (Tier 3), Tower (Tier 4), Tormentor, Roshan, Anchor, Serpent Ward, Phantom | 1 |

[corpus:liquipedia_dota2/turn_rate@2394976#Units]

## Modifying turn rate

Several abilities and items slow or improve turn rate. For readability, some hero pages express turn rates in degrees per second rather than radians per 0.03 seconds. [corpus:liquipedia_dota2/turn_rate@2394976#Modifying_Turn_Rate]

### Turn-rate slowing abilities

The highest slowing value takes precedence.

| Hero | Ability |
|---|---|
| Batrider | Sticky Napalm |
| Medusa | Stone Gaze |

| Marker | Requirement |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |

[corpus:liquipedia_dota2/turn_rate@2394976#Turn_Rate_Slowing_Abilities]

### Turn-rate improving abilities

Multiple increasing sources stack multiplicatively, but the resulting turn-rate value cannot exceed 1.

| Source | Ability |
|---|---|
| Broodmother | Spin Web |
| Phase Boots | Phase |
| Faceless Void | Time Zone |

[corpus:liquipedia_dota2/turn_rate@2394976#Turn_Rate_Improving_Abilities]

### Turn-rate setting abilities

Set Turn Rate, \(T_{\text{Set}}\), fixes a unit’s turn rate for the duration and prevents other effects from altering it.

| Hero | Ability |
|---|---|
| Clockwerk | Jetpack |
| Hoodwink | Sharpshooter |
| Phoenix | Sun Ray |
| Pangolier | Rolling Thunder |
| Pangolier | Roll Up |

[corpus:liquipedia_dota2/turn_rate@2394976#Turn_Rate_Setting_Abilities]

## Turn-rate lock

The following abilities completely prevent the affected unit from turning:

| Hero | Ability |
|---|---|
| Keeper of the Light | Will-O-Wisp |
| Mars | Bulwark |
| Medusa | Gorgon's Grasp |

[corpus:liquipedia_dota2/turn_rate@2394976#Turn_Rate_Lock]

### Stunned

The unit cannot attack or use hero spells or items.

| Hero | Ability |
|---|---|
| Earthshaker | Enchant Totem 2a |
| Faceless Void | Time Walk |
| Faceless Void | Reverse Time Walk |
| Kez | Grappling Claw |
| Marci | Rebound |
| Marci | Rebound (Alt-Cast) |
| Monkey King | Boundless Strike (Alt-Cast) |
| Monkey King | Tree Dance |
| Pangolier | Swashbuckle |
| Pangolier | Shield Crash |
| Pudge | Meat Hook |
| Sand King | Burrowstrike |
| Snapfire | Firesnap Cookie |
| Snapfire | Spit Out |
| Techies | Blast Off! |
| Tiny | Toss |
| Viper | Nosedive |

[corpus:liquipedia_dota2/turn_rate@2394976#Stunned]

### Disarmed; spells do not require facing

The unit cannot attack manually but can cast spells without facing their targets.

| Hero | Ability |
|---|---|
| Bristleback | Bristleback |
| Clockwerk | Hookshot 4 |
| Juggernaut | Omnislash 5 |
| Juggernaut | Swiftslash 5 |
| Kez | Shodo Sai |
| Phoenix | Sun Ray |

| Marker | Effect |
|---|---|
| 1 | Applies self-silence and self-root. |
| 2 | Blade Fury is inactive. |

[corpus:liquipedia_dota2/turn_rate@2394976#Disarmed,_can_use_spells_without_facing_target]

### Disarmed; spells follow hero facing

The unit cannot attack but can use hero spells and items in its facing direction.

| Hero | Ability |
|---|---|
| Dawnbreaker | Converge |
| Dawnbreaker | Starbreaker |
| Drow Ranger | Multishot |
| Pudge | Meat Hook (Self) 4 |

| Marker | Effect |
|---|---|
| 4 | Muted. |

[corpus:liquipedia_dota2/turn_rate@2394976#Disarmed,_can_use_spells_following_hero_facing]

### All actions follow hero facing

The unit can attack and use hero spells and items in its facing direction.

| Hero | Ability |
|---|---|
| Ember Spirit | Activate Fire Remnant 4 |
| Mirana | Leap |
| Ringmaster | Whoopee Cushion |
| Zeus | Heavenly Jump |

| Marker | Effect |
|---|---|
| 4 | Can use hero spells in any direction. Can use items following his facing, on the forward and right side. |

[corpus:liquipedia_dota2/turn_rate@2394976#Allowes_anything_following_hero_facing]

## Abilities enabling other actions without turning

| Hero or source | Ability or state | Actions allowed without turning | Additional rules |
|---|---|---|---|
| Bristleback | Bristleback | Hero abilities or items | Applies self-disarm; locks turning. |
| Clockwerk | Jetpack | Hero abilities and items | Applies self-disarm. |
| Clockwerk | Hookshot | Items | Applies self-silence. |
| Drow Ranger | Multishot | Hero abilities and items | Applies self-disarm. |
| Ember Spirit | Activate Fire Remnant | Hero abilities | Objects can be used only in the direction of his gaze, which is shifted to the right; locks turning. |
| Juggernaut | Omnislash & Swiftslash | Hero abilities and items | Blade Fury is disabled; applies self-root; locks turning. |
| Kez | Shodo Sai | Hero abilities and items | Using any ability interrupts Shodo Sai; locks turning. |
| Lich | Sinister Gaze | Hero abilities while channeling | Locks turning. |
| Mars | Bulwark | Arena of Blood and items | Locks turning. |
| Nyx Assassin | Burrow | Hero abilities and items while underground | Applies self-disarm. |
| Ogre Seal Totem | Ogre Seal Flop | Attacks, hero abilities, and items while floping | This is an old ability. |
| Pugna | Oblivion Savant | Non-channeling hero abilities and items while channeling any ability | Locks turning. |
| Phoenix | Icarus Dive | Hero abilities and items | Sun Ray and Toggle Movement are disabled; locks turning. |
| Phoenix | Sun Ray | Hero abilities and items while active | Applies self-disarm. |
| Pangolier | Hero Model | Items generally | — |
| Primal Beast | Onslaught | A commanded hero ability or item while winding up for Charge | Primal Beast immediately begins charging forward and uses that ability without turning. |
| Riki | Tricks of the Trade | Smoke Screen while channeling | Locks turning. |
| Troll Warlord | Battle Trance | Hero abilities and items while in trance | — |

[corpus:liquipedia_dota2/turn_rate@2394976#Abilities_that_allow_you_to_use_other_abilities_without_turning]

## Actions that ignore turning

Items can be dropped and picked up without turning.

### Targeted to an area

| Source | Ability |
|---|---|
| Ancient Apparition | Release |
| Batrider | Sticky Napalm |
| Crystal Maiden | Crystal Clone |
| Kunkka | Torrent |
| Rubick | Telekinesis Land |

### Targeted to a hero

| Source | Ability or action |
|---|---|
| Bounty Hunter | Friendly Shadow |
| Bottle | Regenerate |
| Bottle | Store Rune |
| Clarity | Replenish |
| Enchanted Mango | Eat Mango |
| Healing Salve | Salve |
| Holy Locket | Energy Charge |
| Glimmer Cape | Glimmer |
| Moon Shard | Consume |
| Runes | Activate |
| Shadow Amulet | Fade |
| Tusk | Snowball (Grab Ally) |
| Tusk | Snowball (Enterance) |
| Undying | Tombstone (Enterance) |

[corpus:liquipedia_dota2/turn_rate@2394976#Abilities_Ignores_Turning]

## Recent changes

### 7.29 — 2021-04-09

The effect of turn rate on time required to turn was improved by 20%.

The following heroes had their turn rate increased from 0.5 to 0.6:

| Hero | Previous | New |
|---|---:|---:|
| Abaddon | 0.5 | 0.6 |
| Beastmaster | 0.5 | 0.6 |
| Bloodseeker | 0.5 | 0.6 |
| Broodmother | 0.5 | 0.6 |
| Centaur Warrunner | 0.5 | 0.6 |
| Chaos Knight | 0.5 | 0.6 |
| Disruptor | 0.5 | 0.6 |
| Doom | 0.5 | 0.6 |
| Elder Titan | 0.5 | 0.6 |
| Ember Spirit | 0.5 | 0.6 |
| Enigma | 0.5 | 0.6 |
| Huskar | 0.5 | 0.6 |
| Invoker | 0.5 | 0.6 |
| Jakiro | 0.5 | 0.6 |
| Keeper of the Light | 0.5 | 0.6 |
| Legion Commander | 0.5 | 0.6 |
| Leshrac | 0.5 | 0.6 |
| Lich | 0.5 | 0.6 |
| Lion | 0.5 | 0.6 |
| Lone Druid | 0.5 | 0.6 |
| Lycan | 0.5 | 0.6 |
| Mirana | 0.5 | 0.6 |
| Naga Siren | 0.5 | 0.6 |
| Necrophos | 0.5 | 0.6 |
| Night Stalker | 0.5 | 0.6 |
| Nyx Assassin | 0.5 | 0.6 |
| Outworld Destroyer | 0.5 | 0.6 |
| Pugna | 0.5 | 0.6 |
| Queen of Pain | 0.5 | 0.6 |
| Razor | 0.5 | 0.6 |
| Sand King | 0.5 | 0.6 |
| Shadow Shaman | 0.5 | 0.6 |
| Skywrath Mage | 0.5 | 0.6 |
| Slardar | 0.5 | 0.6 |
| Snapfire | 0.5 | 0.6 |
| Spectre | 0.5 | 0.6 |
| Spirit Breaker | 0.5 | 0.6 |
| Skywrath Mage | 0.5 | 0.6 |
| Techies | 0.5 | 0.6 |
| Terrorblade | 0.5 | 0.6 |
| Tidehunter | 0.5 | 0.6 |
| Tiny | 0.5 | 0.6 |
| Treant Protector | 0.5 | 0.6 |
| Troll Warlord | 0.5 | 0.6 |
| Ursa | 0.5 | 0.6 |
| Venomancer | 0.5 | 0.6 |
| Viper | 0.5 | 0.6 |
| Visage | 0.5 | 0.6 |
| Warlock | 0.5 | 0.6 |
| Weaver | 0.5 | 0.6 |
| Winter Wyvern | 0.5 | 0.6 |
| Witch Doctor | 0.5 | 0.6 |
| Wraith King | 0.5 | 0.6 |

The following heroes had their turn rate reduced from 1 to 0.9:

| Hero | Previous | New |
|---|---:|---:|
| Batrider | 1 | 0.9 |
| Bristleback | 1 | 0.9 |
| Faceless Void | 1 | 0.9 |
| Hoodwink | 1 | 0.9 |
| Lifestealer | 1 | 0.9 |
| Medusa | 1 | 0.9 |
| Pangolier | 1 | 0.9 |
| Phoenix | 1 | 0.9 |
| Shadow Fiend | 1 | 0.9 |

Dazzle’s turn rate increased from 0.6 to 0.7.

### 7.28 — 2020-12-17

Io now requires turning to perform any actions.

### 7.20 — 2018-11-19

The speed at which unit turn rates ramp up was reduced by 15%. [corpus:liquipedia_dota2/turn_rate@2394976#Recent_Changes]