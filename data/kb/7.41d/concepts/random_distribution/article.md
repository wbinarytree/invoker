---
title: Random Distribution
kind: concept
patch: 7.41d
card:
  entity: random_distribution
  sentences:
  - text: 'Random Distribution covers Dota 2''s random events, where pseudo-random
      distribution (PRD) replaces true random distribution for many proc effects:
      the chance on the N-th test since the last proc is P(N) = C·N, the counter resets
      on a proc, and C is lower than the effect''s listed chance (25% nominal gives
      C = 8.47% and a guaranteed proc on attempt 12).'
    marks:
    - corpus:liquipedia_dota2/random_distribution@2376760
    - corpus:liquipedia_dota2/random_distribution@2376760#Definition
    - corpus:liquipedia_dota2/random_distribution@2376760#Example
  - text: True random distribution is the geometric distribution, whose memoryless
      property makes every coin flip in a sequence independent.
    marks:
    - corpus:liquipedia_dota2/random_distribution@2376760#Definition
  - text: PRD produces lower variance under a concave distribution, so the proc chance
      occurs in a narrow band with a highest point.
    marks:
    - corpus:liquipedia_dota2/random_distribution@2376760#Definition
  - text: The event is guaranteed when C·N ≥ 1, which first occurs at N ≥ 1/C.
    marks:
    - corpus:liquipedia_dota2/random_distribution@2376760#Definition
  - text: The resulting distribution is P(X_k) = (1-C)(1-2C)...(1-(k-1)C)·kC.
    marks:
    - corpus:liquipedia_dota2/random_distribution@2376760#Definition
  - text: Skull Basher's Bash on melee heroes lists 25% but has ~8.5% on the first
      attack, ~17% on the second and ~25.5% on the third, resetting to ~8.5% after
      a bash.
    marks:
    - corpus:liquipedia_dota2/random_distribution@2376760#Example
  - text: Instances that could not trigger the effect do not increase the counter,
      such as critical strike attacking buildings, and the chance is neither reset
      nor increased while the ability is on cooldown.
    marks:
    - corpus:liquipedia_dota2/random_distribution@2376760#Example
  - text: C by nominal chance includes 0.38% for 5%, 5.6% for 20%, 30% for 50%, 75%
      for 80% and 95% for 95%.
    marks:
    - corpus:liquipedia_dota2/random_distribution@2376760#C_Values
  - text: Flat true-random distribution rolls a value between 0 and 1 along a min/max
      gradient for unit attack damage, last hit gold bounty and Roshan's respawn timer.
    marks:
    - corpus:liquipedia_dota2/random_distribution@2376760#Flat_distribution
  - text: Discrete true-random events include Powerup Runes, clamped over 6 types
      and 2 locations, and neutral camp creep spawns for the small, medium, hard and
      ancient camps.
    marks:
    - corpus:liquipedia_dota2/random_distribution@2376760#Discrete_distribution
  - text: Ogre Magi's Multicast has 2x chance 75%/75%/75%, 3x chance 0%/30%/30% and
      4x chance 0%/0%/15%.
    marks:
    - corpus:liquipedia_dota2/random_distribution@2376760#Other
  - text: All Evasion sources and the drop chance of neutral items also use pseudo-random
      distribution.
    marks:
    - corpus:liquipedia_dota2/random_distribution@2376760#Pseudo_random_events
---

# Random Distribution

Randomness is sometimes rejected in competitive gaming because it can decide victory and defeat without reflecting actual skill level — though coping with the unexpected is itself an aspect of skill. Dota 2 contains a number of random events that keep the game less predictable and static. To limit the influence of huge streaks, pseudo-random distribution replaces true random distribution where the developers deemed it sensible. [corpus:liquipedia_dota2/random_distribution@2376760]

## Definition

The geometric distribution, or **true random distribution**, describes the probability of the number of events that occur before a successful event. Its memoryless property means every "coin flip" in a sequence operates independently. [corpus:liquipedia_dota2/random_distribution@2376760#Definition]

The **pseudo-random distribution** (PRD) is a statistical mechanic governing how certain probability-based items and abilities work. Under a conditional distribution, the event's chance increases every time the event does not occur, but is lower in the first place as compensation. This produces effects with lower variance — the proc chance occurs in a narrow band — operating under a concave distribution, meaning the proc chance has a highest point. [corpus:liquipedia_dota2/random_distribution@2376760#Definition]

The probability of an effect to proc on the N-th test since the last successful proc is `P(N) = C · N`. For each instance which could trigger the effect but does not, PRD augments the probability for the next instance by a constant C. This constant — which is also the initial probability — is lower than the listed probability of the effect it shadows. Once the effect occurs, the counter resets. [corpus:liquipedia_dota2/random_distribution@2376760#Definition]

Formally, if `X_i` is the event occurring on trial `i` and `¬X_i` its inverse, PRD enforces `P(X_N | ¬X_i for all i < N) = C · N`. When `C · N ≥ 1` — which occurs on the first trial N where `N ≥ 1/C` — the event is guaranteed if it has not already happened. The resulting distribution is: [corpus:liquipedia_dota2/random_distribution@2376760#Definition]

```
P(X_k) = (1-C)(1-2C)...(1-(k-1)C) · kC = k! · C · ∏_{i=1}^{k-1}(1/i - C)
```

[corpus:liquipedia_dota2/random_distribution@2376760#Definition]

### Example

On melee heroes, Skull Basher's Bash has a 25% chance to stun the target, but on the first attack it only has an ~8.5% probability to bash. Each subsequent attack without a bash increases the probability by ~8.5%: ~17% on the second attack, ~25.5% on the third, and so on. After a bash occurs, the probability resets to ~8.5%. These probabilities average out so that, over a moderate period of time, Bash procs nearly 25% of the time. [corpus:liquipedia_dota2/random_distribution@2376760#Example]

| Quantity | Value |
|---|---|
| C | 8.47% (probability increase per failed attempt) |
| N | 12 (the attempt with ensured 100% proc chance) |

[corpus:liquipedia_dota2/random_distribution@2376760#Example]

PRD effects rarely proc many times in a row, or go a long time without happening, making the game less luck-based and adding consistency to probability-based abilities. PRD is difficult to exploit in practice: it is theoretically possible to increase your chance to bash or critical strike on the next attack by attacking creeps repeatedly without the effect happening, but in practice this is nearly impossible. For instances that would not trigger the effect, the probability counter does not increase — a hero with critical strike attacking buildings does not increase its chance to crit on the next attack, since critical strike does not work against buildings. The chance is likewise not reset or increased while the ability is on cooldown (e.g. Bash). [corpus:liquipedia_dota2/random_distribution@2376760#Example]

### C Values

C as a function of nominal chance: [corpus:liquipedia_dota2/random_distribution@2376760#C_Values]

| Nominal Chance | C | Approximate C |
|---|---|---|
| 5% | 0.003801658303553139101756466 | 0.38% |
| 10% | 0.014745844781072675877050816 | 1.5% |
| 15% | 0.032220914373087674975117359 | 3.2% |
| 20% | 0.055704042949781851858398652 | 5.6% |
| 25% | 0.084744091852316990275274806 | 8.5% |
| 30% | 0.118949192725403987583755553 | 12% |
| 35% | 0.157983098125747077557540462 | 16% |
| 40% | 0.201547413607754017070679639 | 20% |
| 45% | 0.249306998440163189714677100 | 25% |
| 50% | 0.302103025348741965169160432 | 30% |
| 55% | 0.360397850933168697104686803 | 36% |
| 60% | 0.422649730810374235490851220 | 42% |
| 65% | 0.481125478337229174401911323 | 48% |
| 70% | 0.571428571428571428571428572 | 57% |
| 75% | 0.666666666666666666666666667 | 67% |
| 80% | 0.750000000000000000000000000 | 75% |
| 85% | 0.823529411764705882352941177 | 82% |
| 90% | 0.888888888888888888888888889 | 89% |
| 95% | 0.947368421052631578947368421 | 95% |

[corpus:liquipedia_dota2/random_distribution@2376760#C_Values]

## True Random Events

### Flat distribution

Some mechanics roll a random value between 0 and 1 and scale it along a minimum/maximum gradient: [corpus:liquipedia_dota2/random_distribution@2376760#Flat_distribution]

- Attack damage of units, if they have a minimum and maximum attack damage range.
- Last hit gold bounty, if a minimum and maximum range is given.
- Roshan's respawn timer.

[corpus:liquipedia_dota2/random_distribution@2376760#Flat_distribution]

| Ability | Parameters |
|---|---|
| Chaos Knight – Chaos Bolt | Min Damage: 90/110/130/150; Max Damage: 180/220/260/300; Min Stun Duration: 1.25/1.5/1.75/2 (2.25/2.5/2.75/3); Max Stun Duration: 2.2/2.8/3.4/4 (3.2/3.8/4.4/5). Damage and stun duration are correlated inversely. |
| Phantom Lancer – Doppelganger | Reappear Radius: 325. Random positions within the target area; calculation might be in polar coordinates with 0–360° angle and 0–325 distance units as min/max gradients. |
| Crystal Maiden – Freezing Field | Minimum Explosion Distance: 195; Maximum Explosion Distance: 785. Angle within the four 90° sectors (0°–90°, 90°–180°, 180°–270°, 270°–360°) may be random. |

[corpus:liquipedia_dota2/random_distribution@2376760#Flat_distribution]

### Discrete distribution

A number of random events have discrete states of similar probability: Powerup Runes, with a discrete clamping over the 6 types and 2 locations; and neutral camps, which can spawn different creeps for each of the small, medium, hard and ancient camps. [corpus:liquipedia_dota2/random_distribution@2376760#Discrete_distribution]

| Ability | Parameters and notes |
|---|---|
| Chaos Knight – Phantasm | The position of the caster and the illusions within the formation is random. |
| Clockwerk – Battery Assault | Number of Shrapnels: 16 (24); Search Radius: 275; Interval: 0.7 sec (0.45 sec) |
| Dark Willow – Bedlam | Attack Radius: 300; Attack Interval: 0.25 sec |
| Dazzle – Shadow Wave | Number of Bounces: 3/4/5/6; Bounce Distance: 475. Although prioritizing heroes over units, and injured allies over non-injured ones, if multiple units meet the criteria it chooses between them randomly. |
| Death Prophet – Exorcism | Search Radius: 700. Spirits choose targets randomly; once chosen they stick with that target until they can't attack it anymore. Spirits prioritise units the caster attacks. |
| Ember Spirit – Searing Chains | Max Targets: 2; Search Radius: 400 |
| Ember Spirit – Sleight of Fist | Effect Radius: 250/350/450/550; Attack Interval: 0.2 sec. Targets are determined upon cast; the order of attacks is random. |
| Enchantress – Nature's Attendants | Number of Wisps: 4/6/8/10 (12/14/16/18); Search Radius: 275; Interval: 1 sec; Duration: 10 sec. Every second, each wisp chooses a random allied unit to heal, so it is possible to heal up to as many allies as the number of wisps at a time. |
| Gyrocopter – Rocket Barrage | Rockets per Second: 10; Search Radius: 400; Interval: 0.1; Duration: 3 |
| Harpy Stormcrafter – Chain Lightning | Number of Bounces: 4; Bounce Distance: 500; Interval: 0.25 sec |
| Juggernaut – Omnislash | Attack Rate Divisor: 1.7; Search Radius: 425. Slashes enemies based on Juggernaut's attack rate. |
| Leshrac – Diabolic Edict | Number of Explosions: 40 (80); Search Radius: 500; Interval: 0.25 sec (0.13 sec) |
| Lich – Chain Frost | Number of Bounces: 10 (Infinite); Bounce Distance: 575; Interval: 0.2 sec |
| Lion – Mana Drain | Max Targets: 1 (3); Search Radius: 0 (400) |
| Luna – Eclipse | Number of Beams: 6/9/12 (6/12/18); Search Radius: 675; Interval: 0.6 sec (0.3 sec) |
| Manta Style – Mirror Image | The position of the caster and the illusions within the formation is random. |
| Morphling – Adaptive Strike (Agility) | Max Targets: 1 (4); Search Radius: 900/1000/1100/1200. Requires a talent; when upgraded, releases three extra projectiles hitting a second, third and fourth random enemy within the search radius. |
| Morphling – Adaptive Strike (Strength) | Max Targets: 1 (4); Search Radius: 900/1000/1100/1200. Requires a talent; when upgraded, releases three extra projectiles hitting a second, third and fourth random enemy within the search radius. |
| Naga Siren – Mirror Image | The position of the caster and the illusions within the formation is random. |
| Ogre Magi – Ignite | Multicast Amount: 1/2/3; Multicast Range: 1400; Interval: 0.4 sec |
| Ogre Magi – Bloodlust | Multicast Amount: 1/2/3; Search Radius: 700 |
| Phantom Assassin – Stifling Dagger | Max Targets: 1 (3); Search Radius: 825/1050/1275/1500. Requires a talent; when upgraded, releases two extra projectiles hitting a second and third random enemy within the search radius. |
| Razor – Eye of the Storm | Search Radius: 500. When multiple enemies have the same amount of health, or if multiple heroes are linked with Static Link, chooses between them randomly. |
| Riki – Tricks of the Trade | Search Radius: 450; Attack Count: 4 (5); Max Channel Time: 2 |
| Shadow Shaman – Mass Serpent Ward | Max Targets: 1 (2); Search Radius: 0 (875). Requires Aghanim's Scepter; when upgraded, releases a second attack on each attack, hitting a second random enemy within the search radius. |
| Skywrath Mage – Arcane Bolt | Max Targets: 1 (2) (2, 3); Search Radius: 0 (700) (700). Requires a talent or Aghanim's Scepter; when upgraded, releases a second/third projectile hitting a second/third random enemy within the search radius. |
| Skywrath Mage – Concussive Shot | Max Targets: 1 (2); Search Radius: 0 (700, Global). Requires Aghanim's Scepter; when upgraded, releases a second projectile hitting a second random enemy within the search radius. |
| Skywrath Mage – Ancient Seal | Max Targets: 1 (2); Search Radius: 0 (700). Requires Aghanim's Scepter; when upgraded, targets a second random enemy within the search radius. |
| Skywrath Mage – Mystic Flare | Number of Flares: 1 (2); Search Radius: 0 (700). Requires Aghanim's Scepter; when upgraded, creates a second flare on a random enemy within the search radius. |
| Visage – Soul Assumption | Max Targets: 1 (2); Search Radius: 1200 (1325). Requires a talent; when upgraded, releases a second projectile hitting a second random enemy within the search radius. |
| Witch Doctor – Paralyzing Cask | Number of Bounces: 2/4/6/8 (4/6/8/10); Bounce Distance: 575; Interval: 0.3 sec |

[corpus:liquipedia_dota2/random_distribution@2376760#Discrete_distribution]

### Other

Ogre Magi – Multicast: [corpus:liquipedia_dota2/random_distribution@2376760#Other]

| Multicast | Chance |
|---|---|
| 2x Multicast Chance | 75%/75%/75% |
| 3x Multicast Chance | 0%/30%/30% |
| 4x Multicast Chance | 0%/0%/15% |

[corpus:liquipedia_dota2/random_distribution@2376760#Other]

## Pseudo Random Events

Along with the listed abilities, all Evasion sources and the drop chance of neutral items use pseudo-random distribution as well. [corpus:liquipedia_dota2/random_distribution@2376760#Pseudo_random_events]

### Evasion Sources

| Source | Note |
|---|---|
| Brewmaster – Drunken Brawler (Storm Stance) | |
| Storm – Drunken Brawler | Requires talent |
| Mirana – Moonlight Shadow | Requires talent |
| Naga Siren – Eelskin | |
| Phantom Assassin – Immaterial | |
| Phantom Lancer – Phantom Rush | |
| Evasion – 25% Uphill Miss Chance (Ranged Attacks) | |

[corpus:liquipedia_dota2/random_distribution@2376760#Evasion_Sources]

### Other Hero and Unit Abilities

| Source | Note |
|---|---|
| Alpha Wolf – Critical Strike | |
| Brewmaster – Drunken Brawler (Fire Stance) | |
| Chaos Knight – Chaos Strike | |
| Faceless Void – Time Lock | |
| Faceless Void – Backtrack | Requires talent |
| Juggernaut – Blade Dance | |
| Keeper of the Light – Blinding Light | |
| Legion Commander – Moment of Courage | |
| Lycan – Wolf Bite | |
| Lycan – Shapeshift | |
| Lycan Wolf – Cripple | |
| Ogre Magi – Fireblast | Requires talent |
| Pangolier – Lucky Shot | |
| Phantom Assassin – Coup de Grace | |
| Phantom Lancer – Juxtapose | |
| Razor – Storm Surge | |
| Riki – Smoke Screen | |
| Roshan – Bash | |
| Sand King – Sand Storm | |
| Sniper – Headshot | |
| Spirit Breaker – Greater Bash | |
| Troll Warlord – Berserker's Rage | |
| Troll Warlord – Whirling Axes (Melee) | |
| Tusk – Walrus PUNCH! | Requires talent |
| Abyssal Blade – Bash | |
| Abyssal Blade – Damage Block | |
| Crimson Guard – Damage Block | |
| Crystalys – Critical Strike | |
| Daedalus – Critical Strike | |
| Javelin – Pierce | |
| Gleipnir – Chain Lightning | |
| Maelstrom – Chain Lightning | |
| Mjollnir – Chain Lightning | |
| Mjollnir – Static Charge | |
| Monkey King Bar – Pierce | |
| Radiance – Burn | |
| Skull Basher – Bash | |
| Vanguard – Damage Block | |

[corpus:liquipedia_dota2/random_distribution@2376760#Hero_and_Unit_Abilities]

## Legacy Data

Legacy data cited from the website of the original WC3 DotA. P(T) is the theoretical probability, P(A) the actual probability, C the PRD constant. Max N is the minimum number of attacks that would result in `C · N` becoming greater than 1 (guaranteed proc). Average N is the expected value of N: the sum of the products of N and probabilities. SD is the standard deviation of N, a measure of how spread the data is, using the population formula — the lower the deviation, the more consistent the procs. SDt is the standard deviation of N in true random distribution for comparison, using the sample formula from N = 1 to N = 264; these are higher than those of PRD, hence not as consistent. [corpus:liquipedia_dota2/random_distribution@2376760#Legacy_data]

| P(T) | P(A) | C | Max N | Most Probable N | Average N | SD | SDt |
|---|---|---|---|---|---|---|---|
| 5% | 5.0% | 0.00380 | 264 | 16 | 20.00 | 10.30 | 19.53 |
| 10% | 10.0% | 0.01475 | 68 | 8 | 10.00 | 5.06 | 9.50 |
| 15% | 15.0% | 0.03221 | 32 | 6 | 6.67 | 3.31 | 6.16 |
| 20% | 20.0% | 0.05570 | 18 | 4 | 5.00 | 2.43 | 4.48 |
| 25% | 24.9% | 0.08475 | 12 | 3 | 4.02 | 1.90 | 3.49 |
| 30% | 29.9% | 0.11895 | 9 | 3 | 3.34 | 1.54 | 2.81 |
| 35% | 33.6% | 0.14628 | 7 | 3 | 2.98 | 1.35 | 2.43 |
| 40% | 37.7% | 0.18128 | 6 | 2 | 2.65 | 1.17 | 2.10 |
| 45% | 41.8% | 0.21867 | 5 | 2 | 2.39 | 1.03 | 1.83 |
| 50% | 45.7% | 0.25701 | 4 | 2 | 2.19 | 0.91 | 1.62 |
| 55% | 49.3% | 0.29509 | 4 | 2 | 2.03 | 0.83 | 1.45 |
| 60% | 53.0% | 0.33324 | 4 | 2 | 1.89 | 0.74 | 1.30 |
| 65% | 56.6% | 0.38109 | 3 | 2 | 1.77 | 0.69 | 1.17 |
| 70% | 60.1% | 0.42448 | 3 | 2 | 1.66 | 0.63 | 1.05 |
| 75% | 63.2% | 0.46134 | 3 | 2 | 1.58 | 0.57 | 0.96 |
| 80% | 66.7% | 0.50276 | 2 | 1 | 1.50 | 0.50 | 0.87 |

[corpus:liquipedia_dota2/random_distribution@2376760#Legacy_data]

## Version History

| Version | Changes |
|---|---|
| 7.22e (2019-07-14) | Blind now uses pseudo-random distribution (Uphill miss chance, Incapacitating Bite, Blinding Light, Burn, Sand Storm, Smoke Screen, Whirling Axes (Melee)). Cinder Brew's self-attack chance now uses pseudo-random distribution. Shapeshift's critical strike now uses pseudo-random distribution. |
| 7.22 (2019-05-24) | Walrus PUNCH! passive trigger talent now uses pseudo-random distribution. |
| 7.00 (2016-12-12) | Juxtapose now uses pseudo-random distribution. Craggy Exterior now uses pseudo-random distribution. Alpha Wolf's Critical Strike now uses pseudo-random distribution. Giant Wolf's Critical Strike now uses pseudo-random distribution. |
| 6.87c (2016-05-07) | Essence Aura now uses pseudo-random distribution. |
| 6.87 (2016-04-25) | Evasion now uses pseudo-random distribution. Entangling Claws now uses pseudo-random distribution. |
| 6.85 (2015-09-24) | Greater Bash now uses pseudo-random distribution. |
| 6.81 (2014-04-29) | Counter Helix now uses pseudo-random distribution. Moment of Courage now uses pseudo-random distribution. |

[corpus:liquipedia_dota2/random_distribution@2376760#Version_history]