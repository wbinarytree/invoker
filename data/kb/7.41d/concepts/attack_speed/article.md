---
title: Attack Speed
kind: concept
patch: 7.41d
card:
  entity: attack_speed
  sentences:
  - text: Attack speed is a unit statistic measuring how frequently a unit attacks;
      items, agility, flat-bonus abilities, and auras modify it, while most heroes
      have 100 base attack speed and 1.7 BAT and the default total range is 20–700.
    marks:
    - corpus:liquipedia_dota2/attack_speed@2383425
    - corpus:liquipedia_dota2/attack_speed@2383425#Mechanics
  - text: Total attack speed is `(Base Attack Speed + Σ Current + Σ Flat Attack Speed
      Bonuses) × (1 + Attack Speed Multiplier)`.
    marks:
    - corpus:liquipedia_dota2/attack_speed@2383425#Mechanics
  - text: Attack rate in attacks per second is total attack speed divided by `100
      × BAT`.
    marks:
    - corpus:liquipedia_dota2/attack_speed@2383425#Mechanics
  - text: Time per attack is the reciprocal of attack rate.
    marks:
    - corpus:liquipedia_dota2/attack_speed@2383425#Mechanics
  - text: BAT is the default interval between a unit’s attacks before agility and
      attack-speed bonuses are considered.
    marks:
    - corpus:liquipedia_dota2/attack_speed@2383425#Base_Attack_Time
  - text: Most heroes’ attack rate is `0.588` attacks per second.
    marks:
    - corpus:liquipedia_dota2/attack_speed@2383425#Benchmark
  - text: Each point from an increased attack speed source adds `1` attack-speed point.
    marks:
    - corpus:liquipedia_dota2/attack_speed@2383425#Benchmark
  - text: Percentage attack-speed changes apply after flat bonuses and reductions
      and stack additively with one another.
    marks:
    - corpus:liquipedia_dota2/attack_speed@2383425#Percentage_Bonus
  - text: A hero’s nonstandard base attack speed shifts its minimum from `20` by the
      same difference from `100`; Tiny’s `85` gives `5`, while Sven’s `110` gives
      `30`.
    marks:
    - corpus:liquipedia_dota2/attack_speed@2383425#Attack_Speed_Limits
  - text: Every hero’s maximum attack speed remains `700` regardless of base attack
      speed.
    marks:
    - corpus:liquipedia_dota2/attack_speed@2383425#Attack_Speed_Limits
  - text: Marci’s Unleash and Troll Warlord’s Battle Trance can raise the maximum
      above `700`, with the higher maximum taking priority.
    marks:
    - corpus:liquipedia_dota2/attack_speed@2383425#Maximum_Attack_Speed
  - text: Instant attacks and fixed-interval attacks ignore BAT, attack speed, and
      attack rate.
    marks:
    - corpus:liquipedia_dota2/attack_speed@2383425#Fixed_Attack_Interval
---

# Attack Speed

Attack speed measures how frequently units attack. It can be modified by items, each point of agility, abilities that provide flat bonuses, and auras. [corpus:liquipedia_dota2/attack_speed@2383425]

## Mechanics

Most heroes have `100` base attack speed and `1.7` base attack time (BAT). Total attack speed is:

\[
\Sigma\text{ Attack Speed}
=
(\text{Base Attack Speed}+\Sigma\text{ Current}+\Sigma\text{ Flat Attack Speed Bonuses})
\times(1+\text{Attack Speed Multiplier})
\]

with:

\[
20 \leq \Sigma\text{ Attack Speed} \leq 700
\]

Attack-speed bonuses and reductions stack additively as flat values and/or percentages. By default, total attack speed has a minimum of `20` and a maximum of `700`; most units cannot be reduced or increased beyond these values.

Attack rate—the attacks a unit can launch within a second—is:

\[
r=\frac{\Sigma\text{ Attack Speed}}{100\times BAT}
\]

The time needed per attack is:

\[
T=\frac{1}{r}
\]

[corpus:liquipedia_dota2/attack_speed@2383425#Mechanics]

## Base Attack Time

Every unit has a BAT: the default interval between its attacks before considering agility and attack-speed bonuses. A Melee Creep has `1` BAT and therefore attacks once per second by default. A hero with `1.7` BAT, no agility, and no bonus attack speed attacks once every `1.7` seconds. Nearly every unit can have its attack speed modified, but only a few heroes can actively change their BAT. [corpus:liquipedia_dota2/attack_speed@2383425#Base_Attack_Time]

### Example

Marci has `1.7` BAT, `100` base attack speed, and `20` agility at level `1`:

```text
AttackRate = (100 + 20) / (100 x 1.7) = 0.706
Attack s^-1 = 1/r = 1.416
```

She attacks about `0.706` times per second and takes `1.416` seconds between attacks. [corpus:liquipedia_dota2/attack_speed@2383425#Examples]

### Benchmarks

Most heroes’ attack rate is `0.588` attacks per second. Attack speed is expressed as a percentage of base attack speed, whose base is `100`. Each point from an increased attack speed (IAS) source adds `1` point; attack speed and BAT together determine how often a unit attacks.

When hovering over a hero’s attributes in the HUD, the first field displays attack speed and, in parentheses, the time required per attack. The field defaults to `100`, then applies attack-speed bonuses or reductions, with a minimum of `20` and a maximum of `700`. [corpus:liquipedia_dota2/attack_speed@2383425#Benchmark]

| Default AS (`100`) | BAT | Normal speed |
|---:|---:|---:|
| 20 | 5x | 1/5x |
| 25 | 4x | 1/4x |
| 33 | 3x | 1/3x |
| 50 | 2x | 1/2x |
| 100 | 1x | 1x |
| 200 | 1/2x | 2x |
| 300 | 1/3x | 3x |
| 400 | 1/4x | 4x |
| 500 | 1/5x | 5x |
| 600 | 1/6x | 6x |
| 700 | 1/7x | 7x |

[corpus:liquipedia_dota2/attack_speed@2383425#Benchmark]

### Hero BAT exceptions

Most heroes have `1.7` BAT except for the following: [corpus:liquipedia_dota2/attack_speed@2383425#Exceptions]

| Hero | BAT | Base attack speed | Difference in attacks/sec | Range min, in `1.7` BAT representation | Range max, in `1.7` BAT representation |
|---|---:|---:|---:|---:|---:|
| Juggernaut | 1.4 | 110 | +21.4% | 36.4 | 850 |
| Anti-Mage | 1.4 | 100 | +21.4% | 24.3 | 850 |
| Abaddon | 1.5 | 100 | +13.3% | 22.7 | 793.3 |
| Dark Willow | 1.5 | 115 | +13.3% | 39.7 | 793.3 |
| Morphling | 1.5 | 100 | +13.3% | 22.7 | 793.3 |
| Bounty Hunter | 1.5 | 100 | +13.3% | 22.7 | 793.3 |
| Nature's Prophet | 1.5 | 100 | +13.3% | 22.7 | 793.3 |
| Queen of Pain | 1.5 | 100 | +13.3% | 22.7 | 793.3 |
| Terrorblade | 1.5 | 110 | +13.3% | 34 | 793.3 |
| Windranger | 1.5 | 90 | +13.3% | 11.3 | 793.3 |
| Spirit Bear | 1.5 | 110 | +13.3% | 34 | 793.3 |
| Dragon Knight | 1.6 | 100 | +6.3% | 21.3 | 743.8 |
| Huskar | 1.6 | 100 | +6.3% | 21.3 | 743.8 |
| Lina | 1.6 | 100 | +6.3% | 21.3 | 743.8 |
| Lone Druid | 1.6 | 100 | +6.3% | 21.3 | 743.8 |
| Shadow Fiend | 1.6 | 100 | +6.3% | 21.3 | 743.8 |
| Silencer | 1.6 | 110 | +6.3% | 31.9 | 743.8 |
| Storm Spirit | 1.6 | 110 | +6.3% | 31.9 | 743.8 |
| Bristleback | 1.8 | 100 | -5.6% | 18.9 | 661.1 |
| Magnus | 1.8 | 100 | -5.6% | 18.9 | 661.1 |
| Mars | 1.8 | 100 | -5.6% | 18.9 | 661.1 |
| Primal Beast | 1.8 | 100 | -5.6% | 18.9 | 661.1 |
| Snapfire | 1.8 | 100 | -5.6% | 18.9 | 661.1 |
| Weaver | 1.8 | 120 | -5.6% | 37.8 | 661.1 |
| Sven | 1.9 | 110 | -10.5% | 26.8 | 626.3 |
| Outworld Destroyer | 1.9 | 100 | -10.5% | 17.9 | 626.3 |
| Treant Protector | 1.9 | 100 | -10.5% | 17.9 | 626.3 |
| Spirit Breaker | 1.9 | 100 | -10.5% | 17.9 | 626.3 |
| Doom | 1.9 | 100 | -10.5% | 17.9 | 626.3 |
| Kez | 1.9 | 100 | -10.5% | 17.9 | 626.3 |
| Hoodwink | 2 | 100 | -15% | 17 | 595 |

[corpus:liquipedia_dota2/attack_speed@2383425#Exceptions]

### Other units

#### Summons

| Unit | BAT | Base attack speed | Difference in attacks/sec | Range min, in `1.7` BAT representation | Range max, in `1.7` BAT representation |
|---|---:|---:|---:|---:|---:|
| Fountain | 0.15 | 100 | +1033.3% | 226.7 | 7933.3 |
| Death Ward | 0.22 | 100 | +672.7% | 154.5 | 5409.1 |
| Familiar | 0.5 | 100 | +240% | 68 | 2380 |
| Necronomicon Warrior | 0.75 | 105 | +126.7% | 56.7 | 1586.7 |
| Void (Level 3) | 0.8 | 100 | +112.5% | 42.5 | 1487.5 |
| Lycan Wolf (Level 4) | 0.9 | 100 | +88.9% | 37.8 | 1322.2 |
| Melee Creep | 1 | 100 | +70% | 34 | 1190 |
| Necronomicon Archer | 1 | 105 | +70% | 42.5 | 1190 |
| Lycan Wolf (Level 3) | 1 | 100 | +70% | 34 | 1190 |
| Void (Level 2) | 1 | 100 | +70% | 34 | 1190 |
| Lycan Wolf (Level 2) | 1.1 | 100 | +54.5% | 30.9 | 1081.8 |
| Warlock Golem | 1.2 | 100 | +41.7% | 28.3 | 991.7 |
| Lycan Wolf (Level 1) | 1.2 | 100 | +41.7% | 28.3 | 991.7 |
| Void (Level 1) | 1.2 | 100 | +41.7% | 28.3 | 991.7 |
| Wraith King Skeleton | 1.2 | 100 | +41.7% | 28.3 | 991.7 |
| Razorback | 1.35 | 100 | +25.9% | 25.2 | 881.5 |
| Earth | 1.25 | 100 | +36% | 27.2 | 952 |
| Fire | 1.35 | 100 | +25.9% | 25.2 | 881.5 |
| Spiderite | 1.35 | 100 | +25.9% | 25.2 | 881.5 |
| Spiderling | 1.2 | 100 | +41.7% | 28.3 | 991.7 |
| Forged Spirit | 1.35 | 100 | +25.9% | 25.2 | 881.5 |
| Greater Treant | 1.6 | 100 | +6.3% | 21.3 | 743.8 |
| Plague Ward | 1.4 | 100 | +21.4% | 24.3 | 850 |
| Serpent Ward | 1.6 | 100 | +6.3% | 21.3 | 743.8 |
| Eidolon | 1.5 | 100 | +13.3% | 22.7 | 793.3 |
| Storm | 1.5 | 100 | +13.3% | 22.7 | 793.3 |
| Treant | 1.6 | 100 | +6.3% | 21.3 | 743.8 |
| Undying Zombie | 1.6 | 100 | +6.3% | 21.3 | 743.8 |
| Roshan | 2 | 200 | -15% | 102 | 595 |
| Siege Creep | 3 | 100 | -43.3% | 11.3 | 396.7 |

[corpus:liquipedia_dota2/attack_speed@2383425#Other_Units]

#### Neutral creeps

| Unit | BAT | Base attack speed | Difference in attacks/sec | Range min, in `1.7` BAT representation | Range max, in `1.7` BAT representation |
|---|---:|---:|---:|---:|---:|
| Ghost | 2 | 165 | -15% | 72.3 | 595 |
| Centaur Courser | 2 | 150 | -15% | 59.5 | 595 |
| Ancient Granite Golem | 2 | 150 | -15% | 59.5 | 595 |
| Ancient Rock Golem | 2 | 150 | -15% | 59.5 | 595 |
| Alpha Wolf | 2 | 150 | -15% | 59.5 | 595 |
| Dark Troll Summoner | 2 | 150 | -15% | 59.5 | 595 |
| Hill Troll | 2 | 150 | -15% | 59.5 | 595 |
| Kobold | 2 | 200 | -15% | 102 | 595 |
| Kobold Foreman | 2 | 200 | -15% | 102 | 595 |
| Kobold Soldier | 2 | 200 | -15% | 102 | 595 |
| Mud Golem | 2 | 150 | -15% | 59.5 | 595 |
| Ogre Bruiser | 2 | 150 | -15% | 59.5 | 595 |
| Ogre Frostmage | 2 | 150 | -15% | 59.5 | 595 |
| Satyr Mindstealer | 2 | 125 | -15% | 38.3 | 595 |
| Satyr Tormenter | 2 | 150 | -15% | 59.5 | 595 |
| Shard Golem | 2 | 150 | -15% | 59.5 | 595 |
| Wildwing | 2 | 150 | -15% | 59.5 | 595 |
| Wildwing Ripper | 2 | 150 | -15% | 59.5 | 595 |
| Warpine Raider | 2 | 150 | -15% | 59.5 | 595 |
| Ancient Frostbitten Golem | 2 | 150 | -15% | 59.5 | 595 |
| Ancient Ice Shaman | 2 | 135 | -15% | 46.8 | 595 |
| Ancient Black Dragon | 2 | 135 | -15% | 46.8 | 595 |
| Centaur Conqueror | 2 | 135 | -15% | 46.8 | 595 |
| Fell Spirit | 2 | 135 | -15% | 46.8 | 595 |
| Hellbear | 2 | 135 | -15% | 46.8 | 595 |
| Giant Wolf | 2 | 125 | -15% | 38.3 | 595 |
| Hellbear Smasher | 2 | 135 | -15% | 46.8 | 595 |
| Harpy Scout | 2 | 125 | -15% | 38.3 | 595 |
| Harpy Stormcrafter | 2 | 125 | -15% | 38.3 | 595 |
| Hill Troll Berserker | 2 | 125 | -15% | 38.3 | 595 |
| Vhoul Assassin | 2 | 125 | -15% | 38.3 | 595 |
| Ancient Black Drake | 2 | 120 | -15% | 34 | 595 |
| Ancient Rumblehide | 2 | 120 | -15% | 34 | 595 |
| Ancient Thunderhide | 2 | 120 | -15% | 34 | 595 |
| Hill Troll Priest | 2 | 125 | -15% | 38.3 | 595 |

[corpus:liquipedia_dota2/attack_speed@2383425#Other_Units]

### BAT manipulation

Abilities can alter BAT by setting it to a fixed value or reducing it by a specified amount.

BAT-setting abilities do not stack. The first cast or passively leveled setting ability has higher precedence, even if an ability with a lower BAT value is subsequently used. Metamorphosis and Switch Discipline are exceptions: both always override other BAT-setting abilities once cast or passively acquired, and Switch Discipline has the highest priority of all BAT-setting abilities.

BAT-reducing abilities fully stack with one another except for False Promise and Insatiable Hunger. They also stack with the highest-precedence BAT-setting ability. Application order does not matter: BAT reductions always reduce the unit’s current BAT after a setting ability fixes its value. [corpus:liquipedia_dota2/attack_speed@2383425#Base_Attack_Time_Manipulation]

#### BAT-setting sources

| Source |
|---|
| Alchemist – Chemical Rage |
| Lone Druid – Summon Spirit Bear |
| Kez – Switch Discipline |
| Lycan – Summon Wolves |
| Snapfire – Lil' Shredder |
| Terrorblade – Metamorphosis |
| Troll Warlord – Battle Stance |

[corpus:liquipedia_dota2/attack_speed@2383425#Base_Attack_Time_Manipulation]

#### BAT-reducing sources

| Source | Stated value |
|---|---|
| Crude Enchantment | Bonus Base Attack Time: `-12%/-18%` |
| Broodmother - Insatiable Hunger | Base Attack Time Reduction: |
| Oracle - False Promise | Base Attack Time Reduction: |

[corpus:liquipedia_dota2/attack_speed@2383425#Base_Attack_Time_Manipulation]

## Base Attack Speed

| Hero | Attack speed |
|---|---:|
|  | 85 |
|  | 90 |
|  | 95 |
|  | 100 |
|  | 110 |
|  | 115 |
|  | 120 |
|  | 125 |

[corpus:liquipedia_dota2/attack_speed@2383425#Base_Attack_Speed]

## Attack Speed Limits

Heroes with unique base attack speed also have a unique minimum attack speed equal to the difference between their base attack speed and the default `100` base attack speed. Tiny has `85` base attack speed, `15` less than the default `100`; his minimum is therefore `5`, which is `15` less than the default minimum of `20`.

Despite Tiny and Drow Ranger both having `1.7` BAT, their slowest attack rates are `34` and `8.5` seconds respectively. The mechanic works in reverse for higher base attack speeds: Sven has `110` base attack speed and a minimum of `30`.

This minimum-speed mechanic does not appear to apply to non-hero units. Roshan and Hoodwink both have `2` BAT and a minimum attack rate of `10` seconds, despite Roshan having `200` base attack speed.

Every hero’s maximum attack speed is `700`; it does not change with base attack speed. Tiny therefore has a greater range of `5 – 700`, Sven has a lesser range of `30 – 700`, and the average hero has `20 – 700`. [corpus:liquipedia_dota2/attack_speed@2383425#Attack_Speed_Limits]

### Maximum attack speed changes

The following abilities can change a unit’s maximum attack speed from `700`, allowing higher values. If multiple maximum-changing abilities affect a unit, the higher value takes priority. [corpus:liquipedia_dota2/attack_speed@2383425#Maximum_Attack_Speed]

| Ability |
|---|
| Marci – Unleash |
| Troll Warlord – Battle Trance3 |

[corpus:liquipedia_dota2/attack_speed@2383425#Maximum_Attack_Speed]

## Fixed Attack Intervals

The following abilities perform instant attacks or attacks at fixed intervals, completely ignoring the unit’s BAT, attack speed, and attack rate. [corpus:liquipedia_dota2/attack_speed@2383425#Fixed_Attack_Interval]

| Ability | Values and rules |
|---|---|
| Gyrocopter - Flak Cannon | Side Gunner Range:<br>Side Gunner Interval:<br>Prioritizes the furthest unit away within its range. |
| Io - Tether | Attacks are performed as soon as the ally launches its attack, including instant attacks. Whether the attack hits does not matter. |
| Lifestealer - Infest | Enemy Hero Attack Interval:<br>Enemy Hero Duration:<br>Can be cast on enemy heroes or creep-heroes. |
| Monkey King - Wukong's Command | Soldiers Attack Interval: `1.1` |
| Puck - Dream Coil | Instant Attack Radius: `375`<br>Performs instant attacks on all leashed enemies. The attack interval is set as the caster’s attack rate at cast time or reset on coil break. |
| Riki - Tricks of the Trade | Radius: `425`<br>Attack Count: `4 ( )`<br>Instant Attack Interval: `0.667 ( -2)`<br>Max Channel Time: `2` |
| Tiny - Tree Volley | Tree Throw Interval:<br>Max Channel Time: |
| Weaver - Geminate Attack | Instant Attack Interval: `0.25`<br>Number of Extra Attacks: `1 ( 2)` |

[corpus:liquipedia_dota2/attack_speed@2383425#Fixed_Attack_Interval]

## Modifying Attack Speed

The following modifiers increase or decrease attack speed by a constant value. Their bonuses and reductions cannot exceed the minimum and maximum attack-speed limits. [corpus:liquipedia_dota2/attack_speed@2383425#Modifying_Attack_Speed]

### Flat bonuses

| Source |
|---|
| Abaddon – Curse of Avernus |
| Alchemist – Berserk Potion |
| Ancient Rumblehide – War Drums Aura |
| Ancient Thunderhide – Frenzy |
| Arc Warden – Magnetic Field |
| Axe – Culling Blade |
| Beastmaster – Inner Beast |
| Bloodseeker – Bloodrage |
| Chen – Penitence |
| Clinkz – Strafe |
| Clockwerk – Overclocking |
| Drum of Endurance – Endurance |
| Boots of Bearing – Endurance |
| Disruptor – Thunder Strike2b |
| Echo Sabre – Echo Strike |
| Faceless Void – Chronosphere1 |
| Hellbear – Swiftness Aura |
| Hellbear – Death Throe: Rush |
| Hurricane Pike – Hurricane Thrust |
| Huskar – Berserker's Blood |
| Invoker – Alacrity |
| Invoker – Wex |
| Io – Overcharge |
| Juggernaut – Omnislash |
| Juggernaut – Swiftslash |
| Legion Commander – Overwhelming Odds |
| Lifestealer – Ghoul Frenzy |
| Lina – Fiery Soul |
| Lone Druid – Spirit Link |
| Lone Druid – Savage Roar2b |
| Mask of Madness – Berserk |
| Morphling – Morph2a |
| Spirit Bear – Savage Roar2b |
| Storm Spirit – Overload2b |
| Marci – Unleash |
| Mirana – Leap |
| Moon Shard – Consume |
| Night Stalker – Hunter in the Night |
| Ogre Magi – Bloodlust |
| Phantom Assassin – Phantom Strike |
| Slark – Shadow Dance1 |
| Slark – Depth Shroud1 |
| Solar Crest – Shine |
| Terrorblade – Demon Zeal |
| Troll Warlord – Fervor |
| Troll Warlord – Battle Trance |
| Ursa – Overpower |
| Undying Zombie – Deathlust |
| Visage – Grave Chill |
| Warlock – Upheaval1 |
| Windranger – Focus Fire |
| Winter Wyvern – Winter's Curse |
| Wraith King – Wraith Delay2a |

`1` Requires talent. `2a` Requires Aghanim's Scepter. `2b` Requires Aghanim's Shard. [corpus:liquipedia_dota2/attack_speed@2383425#Bonuses]

### Items

Items can increase their owner’s attack speed through agility or a flat bonus. The effects below are limited to the item’s owner, who must have the item equipped. [corpus:liquipedia_dota2/attack_speed@2383425#Items]

#### Flat-rate and agility attack speed

| Item | Value | Item cost | Cost/value point |
|---|---:|---:|---:|
| Manta Style | 41 | 4650 | 113.41 |
| Power Treads (Agility) | 35 | 1400 | 40 |
| Sange and Yasha | 36 | 4200 | 116.67 |
| Wraith Band | 11 | 505 | 45.91 |
| Yasha | 31 | 2100 | 67.74 |
| Yasha and Kaya | 36 | 4200 | 116.67 |

Values exclude portions from actives or auras. [corpus:liquipedia_dota2/attack_speed@2383425#Items]

#### Flat-rate attack speed

These items provide a flat attack-speed bonus to the hero who has them equipped. [corpus:liquipedia_dota2/attack_speed@2383425#Items]

| Item | Value | Item cost | Cost/value point |
|---|---:|---:|---:|
| Alert Enchantment | 0 | N/A | N/A |
| Armlet of Mordiggian | 25 | 2500 | 100 |
| Assault Cuirass | 30 | 5125 | 170.83 |
| Audacious Enchantment | 100 | N/A | N/A |
| Blitz Knuckles | 35 | 1000 | 28.57 |
| Bloodthorn | 70 | 6400 | 91.43 |
| Gloves of Haste | 20 | 450 | 22.5 |
| Hand of Midas | 35 | 2200 | 62.86 |
| Hulking Enchantment | Expression error: Unexpected < operator. | N/A | N/A |
| Hyperstone | 60 | 2000 | 33.33 |
| Maelstrom | 25 | 2950 | 118 |
| Mjollnir | 90 | 5500 | 61.11 |
| Monkey King Bar | 50 | 5000 | 100 |
| Moon Shard | 140 | 4000 | 28.57 |
| Oblivion Staff | 35 | 1625 | 46.43 |
| Orchid Malevolence | 35 | 3275 | 93.57 |
| Parasma | 40 | 5975 | 149.38 |
| Power Treads (Intelligence) | 25 | 1400 | 56 |
| Power Treads (Strength) | 25 | 1400 | 56 |
| Shadow Blade | 35 | 3250 | 92.86 |
| Silver Edge | 35 | 5700 | 162.86 |
| Titanic Enchantment | Expression error: Unexpected < operator. | N/A | N/A |
| Witch Blade | 40 | 2775 | 69.38 |

Values exclude portions from actives or auras. [corpus:liquipedia_dota2/attack_speed@2383425#Items]

#### Agility attack speed

These items increase the hero’s attack speed through the agility they provide. [corpus:liquipedia_dota2/attack_speed@2383425#Items]

| Item | Value | Item cost | Cost/value point |
|---|---:|---:|---:|
| Aghanim's Scepter | 10 | 4200 | 420 |
| Band of Elvenskin | 6 | 450 | 75 |
| Blade of Alacrity | 10 | 1000 | 100 |
| Bracer | 2 | 505 | 252.5 |
| Butterfly | 35 | 5450 | 155.71 |
| Circlet | 2 | 155 | 77.5 |
| Consecrated Wraps | 5 | 2600 | 520 |
| Crella's Crozier | 6 | 4800 | 800 |
| Crown | 4 | 450 | 112.5 |
| Diadem | 6 | 1000 | 166.67 |
| Diffusal Blade | 15 | 2500 | 166.67 |
| Disperser | 40 | 6100 | 152.5 |
| Dragon Lance | 15 | 1900 | 126.67 |
| Eaglesong | 25 | 2800 | 112 |
| Essence Distiller | 3 | 1775 | 591.67 |
| Ethereal Blade | 24 | 5200 | 216.67 |
| Eye of Skadi | 35 | 5900 | 168.57 |
| Ghost Scepter | 5 | 1500 | 300 |
| Harpoon | 10 | 4700 | 470 |
| Helm of the Dominator | 6 | 2550 | 425 |
| Helm of the Overlord | 21 | 5650 | 269.05 |
| Holy Locket | 7 | 2250 | 321.43 |
| Hurricane Pike | 20 | 4450 | 222.5 |
| Hydra's Breath | 30 | 5900 | 196.67 |
| Iron Branch | 1 | 55 | 55 |
| Khanda | 8 | 5600 | 700 |
| Linken's Sphere | 16 | 4800 | 300 |
| Magic Wand | 3 | 460 | 153.33 |
| Meteor Hammer | 6 | 2850 | 475 |
| Null Talisman | 2 | 505 | 252.5 |
| Orb of Corrosion | 7 | 1050 | 150 |
| Phylactery | 6 | 2600 | 433.33 |
| Slippers of Agility | 3 | 140 | 46.67 |
| Specialist's Array | 15 | 2550 | 170 |
| Spirit Vessel | 10 | 2725 | 272.5 |
| Swift Blink | 25 | 6800 | 272 |
| Ultimate Orb | 15 | 2800 | 186.67 |
| Urn of Shadows | 2 | 825 | 412.5 |

Values exclude portions from actives or auras. [corpus:liquipedia_dota2/attack_speed@2383425#Items]

### Talents

Attack Speed is a passive ability affecting self, with a varying attack-speed bonus. It grants a flat attack-speed bonus and uses a hidden modifier. [corpus:liquipedia_dota2/attack_speed@2383425#Talents]

| Existing bonus values |
|---:|
| 10 |
| 15 |
| 20 |
| 25 |
| 30 |
| 35 |
| 40 |
| 45 |
| 50 |
| 55 |
| 60 |
| 70 |
| 80 |
| 90 |
| 100 |
| 110 |
| 120 |
| 140 |
| 160 |
| 175 |
| 200 |
| 225 |
| 250 |

[corpus:liquipedia_dota2/attack_speed@2383425#Talents]

Heroes can have attack-speed talents in the Left or Right columns at Level `10`, Level `15`, Level `20`, or Level `25`. The stated bonuses are: [corpus:liquipedia_dota2/attack_speed@2383425#Talents]

| Bonus | Value |
|---|---:|
| Attack Speed | +20 |
| Attack Speed | +25 |
| Attack Speed | +50 |
| Attack Speed | +110 |
| Attack Speed | +55 |
| Attack Speed | +50 |

[corpus:liquipedia_dota2/attack_speed@2383425#Talents]

### Flat reductions

| Source |
|---|
| Ancient Thunderhide – Slam |
| Boar - Poison |
| Beastmaster – Primal Roar |
| Brewmaster – Thunder Clap |
| Crystal Maiden – Crystal Nova |
| Crystal Maiden – Freezing Field |
| Disruptor – Thunder Strike |
| Dragon Knight – Wyrm's Wrath (Frost Dragon) |
| Enchantress – Untouchable |
| Eye of Skadi – Cold Attack |
| Ghost – Frost Attack |
| Hellbear Smasher – Thunder Clap |
| Huskar – Life Break |
| Io – Tether |
| Jakiro – Dual Breath |
| Jakiro – Liquid Fire |
| Lich – Frost Blast |
| Lich – Chain Frost |
| Lycan Wolf – Cripple |
| Lycan Lane Wolf – Cripple |
| Magnus – Skewer |
| Magnus – Horn Toss |
| Marci – Unleash |
| Medusa – Stone Gaze |
| Morphling – Morph2a |
| Night Stalker – Void |
| Phoenix – Fire Spirits |
| Roshan – Slam |
| Sand King – Epicenter |
| Shiva's Guard – Freezing Aura |
| Slardar – Slithereen Crush |
| Snapfire – Scatterblast |
| Sniper – Headshot |
| Storm Spirit – Overload |
| Tiny – Tree Throw |
| Tiny – Tree Volley |
| Tiny – Grow |
| Troll Warlord – Berserker's Rage |
| Wildwing – Tornado |
| Venomancer – Poison Nova1 |
| Viper – Corrosive Skin |
| Viper – Viper Strike |
| Visage – Grave Chill |
| Wraith King – Reincarnation |
| Zeus – Heavenly Jump |

`1` Requires talent. `2a` Requires Aghanim's Scepter. `2b` Requires Aghanim's Shard. [corpus:liquipedia_dota2/attack_speed@2383425#Flat_Reductions]

### Percentage bonuses

Percentage attack-speed changes cannot exceed the minimum or maximum attack-speed limits and are applied after flat bonuses and reductions. Percentage changes stack additively with one another. [corpus:liquipedia_dota2/attack_speed@2383425#Percentage_Bonus]

| Source | Value and rules |
|---|---|
| Meepo - Divided We Stand (Codependent) | Attack Speed Bonus:<br>The bonus is a percentage applied to total attack speed and fully stacks with itself. |

[corpus:liquipedia_dota2/attack_speed@2383425#Percentage_Bonus]

### Percentage reductions

| Source | Value and rules |
|---|---|
| Tiny - Grow | Total Attack Speed Factor: `0.65`<br>Reduces all sources of attack speed on Tiny. |
| Giant's Maul - Crushing Blow | Attack Speed Slow: `15%`<br>The slow is a percentage applied to total attack speed. |

[corpus:liquipedia_dota2/attack_speed@2383425#Percentage_Reductions]

## Animations

Heroes whose attack animations vary with attack speed are tagged with `AttackSpeedActivityModifiers` in their hero attributes. Their possible animation progression is:

```text
Base < Fast < Faster < Fastest < Super Fast < Mega Fast Animation
```

[corpus:liquipedia_dota2/attack_speed@2383425#Animations]

The animation-threshold table uses the columns Fast, Faster, Fastest, Super Fast, and Mega Fast. Its stated threshold sequence is: [corpus:liquipedia_dota2/attack_speed@2383425#Animations]

| Stated threshold sequence |
|---:|
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

Not all listed heroes have a unique animation for different attack speeds. [corpus:liquipedia_dota2/attack_speed@2383425#Animations]

## Recent Changes

| Version | Date | Description |
|---|---|---|
| 7.22 | 2019-05-24 | Heroes can now have non-standard initial attack speed values; previously, all heroes had `100`. |
| 7.21 | 2019-01-29 | Agility heroes no longer gain `25%` more main armor/attack speed/movement speed bonus per agility. |
| 7.20 | 2018-11-19 | Increased the maximum attack-speed cap from `600` to `700`. |

[corpus:liquipedia_dota2/attack_speed@2383425#Recent_Changes]