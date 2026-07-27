---
title: Damage Barrier
kind: concept
patch: 7.41d
card:
  entity: damage_barrier
  sentences:
  - text: 'A Damage Barrier is a unit protection mechanic that absorbs matching incoming
      damage up to its maximum capacity through 3 independently operating types: physical,
      magical, and all damage.'
    marks:
    - corpus:liquipedia_dota2/damage_barrier@2357651
    - corpus:liquipedia_dota2/damage_barrier@2357651#Definition
    - corpus:liquipedia_dota2/damage_barrier@2357651#Stacking
  - text: '`MODIFIER_PROPERTY_INCOMING_PHYSICAL_DAMAGE_CONSTANT` absorbs physical
      attack damage and physical spell damage.'
    marks:
    - corpus:liquipedia_dota2/damage_barrier@2357651#Physical_Damage_Barrier
  - text: '`MODIFIER_PROPERTY_INCOMING_PHYSICAL_DAMAGE_CONSTANT_BLOCK_SPECIAL` absorbs
      only physical attack damage.'
    marks:
    - corpus:liquipedia_dota2/damage_barrier@2357651#Physical_Damage_Barrier
  - text: Magical Damage Barriers absorb magical attack damage and spell damage, including
      magical damage with the HP Removal flag.
    marks:
    - corpus:liquipedia_dota2/damage_barrier@2357651#Magical_Damage_Barrier
  - text: All Damage Barriers absorb every type of attack and spell damage, including
      damage with the HP Removal flag.
    marks:
    - corpus:liquipedia_dota2/damage_barrier@2357651#All_Damage_Barrier
  - text: Multiple barrier sources of the same type stack additively, while the 3
      types work independently.
    marks:
    - corpus:liquipedia_dota2/damage_barrier@2357651#Stacking
  - text: All Damage Barriers have the lowest priority and are depleted after physical
      or magical barriers.
    marks:
    - corpus:liquipedia_dota2/damage_barrier@2357651#Stacking
  - text: Damage Barriers apply after armor and magic resistance but before generic
      incoming damage manipulation.
    marks:
    - corpus:liquipedia_dota2/damage_barrier@2357651#Mechanics
  - text: Blocked damage is completely negated, preventing most on-damage effects,
      but the hit still registers a 0-damage instance.
    marks:
    - corpus:liquipedia_dota2/damage_barrier@2357651#Mechanics
  - text: Among barrier sources, the earliest-applied source is depleted first.
    marks:
    - corpus:liquipedia_dota2/damage_barrier@2357651#Definition
  - text: Higher-priority damage-negating sources such as Borrowed Time prevent barriers
      from absorbing damage until they expire.
    marks:
    - corpus:liquipedia_dota2/damage_barrier@2357651#Definition
  - text: False Promise is the only damage-negation source calculated after Damage
      Barriers.
    marks:
    - corpus:liquipedia_dota2/damage_barrier@2357651#After_Barrier_Absorption
---

# Damage Barrier

A Damage Barrier surrounds a unit and protects it from incoming damage according to its maximum capacity. [corpus:liquipedia_dota2/damage_barrier@2357651]

## Definition

Damage Barrier directly reduces damage upon hit according to its barrier type.

| Type | Definition | Example |
|---|---|---|
| Physical | Only absorbs physical damage from attacks. | Resonant Pulse |
| Physical | Absorbs all physical damage from abilities and attacks. | Protect |
| Magical | Absorbs all magical damage coming from abilities and attacks. | Flame Guard |
| All Damage | Absorbs all damage coming from abilities and attacks. | Aphotic Shield |

All Damage has the lowest priority among damage barriers; its capacity is depleted last when combined with other damage-type barriers.

Damage Barrier absorption occurs after Damage Block, other generic damage reductions such as armor and magic resistance, and damage-negating sources. The earliest-applied damage barrier source is depleted first. When combined with higher-priority damage-negating sources such as Borrowed Time, barriers absorb no damage until those sources expire.

| Property |
|---|
| Does not interact with negative damage during damage calculations. |
| Only absorbs flat incoming damage matching its barrier damage type and has a lower limit of 0. |
| Although absorption negates damage and prevents most on-damage effects, the damage instance still deals a 0-damage instance. |
| Barrier capacity is displayed on the HUD with a Physical, Magical, or All Damage icon. |
| Sources of the same damage-type barrier stack additively; different damage-type barriers stack independently. [corpus:liquipedia_dota2/damage_barrier@2357651#Definition] |

## Physical Damage Barrier

`MODIFIER_PROPERTY_INCOMING_PHYSICAL_DAMAGE_CONSTANT` absorbs only physical attack damage and physical spell damage.

### Physical Damage (Attack and Spell) Barrier Sources

| Source | Ability |
|---|---|
| Ash Legion Shield | Shield Wall |
| Pavise | Protect |
| Solar Crest | Shine |

`MODIFIER_PROPERTY_INCOMING_PHYSICAL_DAMAGE_CONSTANT_BLOCK_SPECIAL` absorbs only physical attack damage.

### Physical Damage (Attack Only) Barrier Sources

| Source | Ability |
|---|---|
| Void Spirit | Resonant Pulse (Call of the Void) [corpus:liquipedia_dota2/damage_barrier@2357651#Physical_Damage_Barrier] |

## Magical Damage Barrier

Magical Damage Barriers have `MODIFIER_PROPERTY_INCOMING_SPELL_DAMAGE_CONSTANT`, which absorbs magical attack damage and spell damage, including magical damage with the HP Removal flag.

### Sources

| Source | Ability |
|---|---|
| Ember Spirit | Flame Guard |
| Glimmer Cape | Glimmer |
| Pipe of Insight | Barrier |

| Marker | Requirement |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. [corpus:liquipedia_dota2/damage_barrier@2357651#Magical_Damage_Barrier] |

## All Damage Barrier

All Damage Barriers have `MODIFIER_PROPERTY_INCOMING_DAMAGE_CONSTANT`, which absorbs all types of attack damage and spell damage, including damage with the HP Removal flag.

### Sources

| Source | Ability |
|---|---|
| Abaddon | Aphotic Shield |
| Block of Cheese | Scrumptious |
| Lina | Laguna Blade<sup>2b</sup> |
| Outworld Destroyer | Essence Flux<sup>2a</sup> |
| Pangolier | Shield Crash |
| Safety Bubble | Bubbled Up |
| Tinker | Defense Matrix |
| Tormentor | Unyielding Shield |
| Runes | Shield |
| Spirit Breaker | Bulldoze<sup>1</sup> |
| Templar Assassin | Refraction |
| Timbersaw | Reactive Armor<sup>2a</sup> |
| Vengeful Spirit | Nether Swap |
| Void Spirit | Resonant Pulse<sup>3</sup> |

| Marker | Requirement |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |
| 3 | Requires selecting the corresponding facet. [corpus:liquipedia_dota2/damage_barrier@2357651#All_Damage_Barrier] |

## Mechanics

Damage Barriers completely negate blocked incoming damage, preventing most on-damage effects from triggering, although a 0 damage instance is still registered. They block damage after magic resistance and armor but before generic incoming damage manipulation. Because barriers interact with incoming damage, outgoing damage manipulation is always applied first.

### Example 1

Anti-Mage has a 200 health damage barrier and is hit by 500 magical damage. His base magic resistance is 0.25.

```text
Magical Damage Taken
= 500 × (1 - 0.25) - 200
= 175
```

Anti-Mage takes 175 magical damage.

### Example 2

Anti-Mage additionally has 45% generic incoming damage reduction.

```text
= (500 × (1 - 0.25)- 200) * (1- 0.45)
= 96.25
```

The excess 175 magical damage is not absorbed; generic incoming damage reduction reduces it to 96.25 magical damage. Anti-Mage takes 96.25 magic damage, making the barrier less effective when combined with generic incoming damage reduction. [corpus:liquipedia_dota2/damage_barrier@2357651#Mechanics]

### Before Barrier Absorption

The following sources may manipulate damage before Damage Barriers absorb it.

#### Incoming Damage Reduction Sources

| Source | Ability or scope |
|---|---|
| Armor | All Sources |
| Magic Resistance | All Sources |
| Abaddon | Borrowed Time |
| Faceless Void | Backtrack |
| Medusa | Mana Shield |
| Monkey King | Mischief |
| Nyx Assassin | Spiked Carapace |
| Omniknight | Guardian Angel |
| Winter Wyvern | Cold Embrace |

#### Constant Magical Damage Block Sources

| Source | Ability |
|---|---|
| Dandelion Amulet | Magical Damage Block |
| Infused Raindrops | Magical Damage Block |

| Marker | Requirement |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. [corpus:liquipedia_dota2/damage_barrier@2357651#Before_Barrier_Absorption] |

### After Barrier Absorption

The following sources manipulate damage after Damage Barriers absorb it.

| Source or category | Rule |
|---|---|
| Incoming damage manipulation sources | Manipulate damage after barrier absorption. |
| Illusion incoming damage amplification | Manipulates damage after barrier absorption. |
| Terminal Damage Block sources | Manipulate damage after barrier absorption. |
| False Promise | The only damage-negation source calculated after Damage Barriers. [corpus:liquipedia_dota2/damage_barrier@2357651#After_Barrier_Absorption] |

### Stacking

A unit can simultaneously have all 3 types of Damage Barriers, with each type working independently. Multiple sources of the same type stack additively. All Damage Barriers have the lowest priority and are depleted last when combined with other types. If a unit has an All Damage Barrier and a magical/bonus db-phy barrier, then takes magical/physical damage, the All Damage Barrier absorbs the damage last.

#### Example 1

Clockwerk is affected by Level 4 Power Cogs and Barrier of Pipe of Insight, then takes 1000 magical damage without accounting for magic resistance damage reduction.

```text
Barrier capacity:
+ 425 = 425

Magical damage taken:
= 1000 - 425
= 575
```

Since incoming magical damage is less than all individual barriers. Both Power Cogs and Barrier will now have and remaining bonus db-mag capacity respectively in this example.

#### Example 2

The same Clockwerk is also affected by a Level 4 Aphotic Shield, then takes 800 magical damage.

```text
Barrier Capacities:
Power Cogs + Barrier: 425 magical barrier
Aphotic Shield: all damage barrier
```

The magical barrier absorbs the magical damage first according to Damage Barrier priorities.

```text
= 425 - 800
= -375
```

The magical barrier is depleted, and the remaining 375 damage is absorbed by the All Damage Barrier.

```text
= - 375
= -375
```

The damage instance is completely negated, and Clockwerk retains an All Damage Damage Barrier with a remaining capacity of -375. [corpus:liquipedia_dota2/damage_barrier@2357651#Stacking]