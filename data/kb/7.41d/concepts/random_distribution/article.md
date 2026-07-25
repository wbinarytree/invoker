# Random Distribution

Randomness is sometimes rejected from competitive gaming since it can decide over loss and defeat without reflecting the actual skill level, though coping with the unexpected is itself an aspect of skill. A number of random events exist within Dota 2 to keep the game less predictable and static. To limit the influence of huge streaks, pseudo-random distribution replaces the true random distribution where it made sense for the developers. [corpus:liquipedia_dota2/random_distribution@2376760]

## Definition

The geometric distribution, or true random distribution, describes the probability of the number of events that occur before a successful event; this memoryless property means every "coin flip" in a sequence operates independently. The pseudo-random distribution (PRD) is a statistical mechanic governing how certain probability-based items and abilities work. Under this conditional distribution, the event's chance increases every time the event does not occur, but is lower in the first place as compensation. The result is lower variance — the proc chance occurs in a narrow band — and a concave distribution, meaning the proc chance has a highest point.

The probability of an effect proccing on the N-th test since the last successful proc is given by **P(N) = C · N**. For each instance which could trigger the effect but does not, PRD augments the probability for the next instance by a constant C. This constant, which is also the initial probability, is lower than the listed probability of the effect it is shadowing; once the effect occurs, the counter resets. When C · N ≥ 1 — which occurs on the first trial N where N ≥ 1/C — the event is guaranteed if it has not already happened. [corpus:liquipedia_dota2/random_distribution@2376760#Definition]

## Example

On melee heroes, Skull Basher's Bash has a 25% chance to stun the target, but on the first attack it only has an ~8.5% probability to bash. Each subsequent attack without a bash increases the probability by ~8.5%, so the second attack has ~17%, the third ~25.5%, and so on; after a bash occurs the probability resets to ~8.5%. These probabilities average out so that, over a moderate period of time, Bash procs nearly 25% of the time. For a nominal 25% chance, C = 8.47% and the 12th attempt is the ensured (100%) proc.

Effects based on PRD rarely proc many times in a row, or go a long time without happening, which adds consistency to probability-based abilities. PRD is difficult to exploit: it is theoretically possible to raise the next attack's bash or critical strike chance by attacking creeps without proccing, but in practice this is nearly impossible. Instances that would not trigger the effect do not increase the counter — a hero with critical strike attacking buildings does not increase its crit chance, since critical strike does not work against buildings — and the chance is neither reset nor increased while the ability is on cooldown. [corpus:liquipedia_dota2/random_distribution@2376760#Example]

## C values

| Nominal chance | Approximate C | Nominal chance | Approximate C |
| --- | --- | --- | --- |
| 5% | 0.38% | 50% | 30% |
| 10% | 1.5% | 55% | 36% |
| 15% | 3.2% | 60% | 42% |
| 20% | 5.6% | 65% | 48% |
| 25% | 8.5% | 70% | 57% |
| 30% | 12% | 75% | 67% |
| 35% | 16% | 80% | 75% |
| 40% | 20% | 85% | 82% |
| 45% | 25% | 90% | 89% |
| | | 95% | 95% |

[corpus:liquipedia_dota2/random_distribution@2376760#C_Values]

## Pseudo-random events

Along with the listed abilities, all evasion sources and the drop chance of neutral items use pseudo-random distribution. [corpus:liquipedia_dota2/random_distribution@2376760#Pseudo_random_events]

Evasion sources include Brewmaster's Drunken Brawler (Storm Stance), Storm's Drunken Brawler, Mirana's Moonlight Shadow, Naga Siren's Eelskin, Phantom Assassin's Immaterial, Phantom Lancer's Phantom Rush, the Evasion attribute, and the 25% uphill miss chance for ranged attacks. [corpus:liquipedia_dota2/random_distribution@2376760#Evasion_Sources]

Other PRD-based hero, unit and item effects include Chaos Knight's Chaos Strike, Faceless Void's Time Lock and Backtrack, Juggernaut's Blade Dance, Legion Commander's Moment of Courage, Pangolier's Lucky Shot, Phantom Assassin's Coup de Grace, Phantom Lancer's Juxtapose, Razor's Storm Surge, Sniper's Headshot, Spirit Breaker's Greater Bash, Roshan's Bash, Crystalys and Daedalus critical strikes, Javelin and Monkey King Bar pierce, the Chain Lightning of Gleipnir, Maelstrom and Mjollnir, Radiance's Burn, Skull Basher's Bash, and the damage block of Vanguard, Crimson Guard and Abyssal Blade. [corpus:liquipedia_dota2/random_distribution@2376760#Hero_and_Unit_Abilities]

## True random events

**Flat distribution.** Some mechanics roll a random value between 0 and 1 and scale it along a minimum/maximum gradient. This includes unit attack damage where a min–max range exists, last hit gold bounty where a range is given, Roshan's respawn timer, Chaos Knight's Chaos Bolt (damage and stun duration are correlated inversely), Phantom Lancer's Doppelganger with its 325 reappear radius, and Crystal Maiden's Freezing Field between its 195 minimum and 785 maximum explosion distance. [corpus:liquipedia_dota2/random_distribution@2376760#Flat_distribution]

**Discrete distribution.** Other random events have discrete states of similar probability: powerup runes clamped over 6 types and 2 locations, neutral camp creep spawns for small, medium, hard and ancient camps, illusion formation positions for Chaos Knight's Phantasm and for Manta Style and Naga Siren's Mirror Image, and target selection for effects such as Clockwerk's Battery Assault, Dazzle's Shadow Wave, Death Prophet's Exorcism, Ember Spirit's Sleight of Fist, Enchantress's Nature's Attendants, Gyrocopter's Rocket Barrage, Lich's Chain Frost, Luna's Eclipse, Ogre Magi's Ignite and Bloodlust multicast, Riki's Tricks of the Trade and Witch Doctor's Paralyzing Cask. [corpus:liquipedia_dota2/random_distribution@2376760#Discrete_distribution]

Ogre Magi's Multicast is listed separately, with a 75%/75%/75% chance of 2x multicast, 0%/30%/30% for 3x and 0%/0%/15% for 4x. [corpus:liquipedia_dota2/random_distribution@2376760#Other]

## Legacy data

The following legacy table is cited from the website of the original WC3 DotA. P(T) is the theoretical probability and P(A) the actual probability; Max N is the minimum number of attacks at which C · N exceeds 1 (guaranteed proc), Average N is the expected value of N, and SD is the population standard deviation of N. SDt gives the standard deviation of N under true random distribution (sample formula, N = 1 to 264) for comparison; these are higher than those of PRD, hence not as consistent.

| P(T) | P(A) | C | Max N | Most probable N | Average N | SD | SDt |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5% | 5.0% | 0.00380 | 264 | 16 | 20.00 | 10.30 | 19.53 |
| 10% | 10.0% | 0.01475 | 68 | 8 | 10.00 | 5.06 | 9.50 |
| 15% | 15.0% | 0.03221 | 32 | 6 | 6.67 | 3.31 | 6.16 |
| 20% | 20.0% | 0.05570 | 18 | 4 | 5.00 | 2.43 | 4.48 |
| 25% | 24.9% | 0.08475 | 12 | 3 | 4.02 | 1.90 | 3.49 |
| 30% | 29.9% | 0.11895 | 9 | 3 | 3.34 | 1.54 | 2.81 |
| 40% | 37.7% | 0.18128 | 6 | 2 | 2.65 | 1.17 | 2.10 |
| 50% | 45.7% | 0.25701 | 4 | 2 | 2.19 | 0.91 | 1.62 |
| 60% | 53.0% | 0.33324 | 4 | 2 | 1.89 | 0.74 | 1.30 |
| 70% | 60.1% | 0.42448 | 3 | 2 | 1.66 | 0.63 | 1.05 |
| 80% | 66.7% | 0.50276 | 2 | 1 | 1.50 | 0.50 | 0.87 |

[corpus:liquipedia_dota2/random_distribution@2376760#Legacy_data]

## Version history

- **7.22e (2019-07-14):** Blind now uses pseudo-random distribution (uphill miss chance, Incapacitating Bite, Blinding Light, Burn, Sand Storm, Smoke Screen, Whirling Axes (Melee)). Cinder Brew's self-attack chance and Shapeshift's critical strike also moved to PRD.
- **7.22 (2019-05-24):** Walrus PUNCH! passive trigger talent now uses PRD.
- **7.00 (2016-12-12):** Juxtapose, Craggy Exterior, Alpha Wolf's Critical Strike and Giant Wolf's Critical Strike now use PRD.
- **6.87c (2016-05-07):** Essence Aura now uses PRD.
- **6.87 (2016-04-25):** Evasion and Entangling Claws now use PRD.
- **6.85 (2015-09-24):** Greater Bash now uses PRD.
- **6.81 (2014-04-29):** Counter Helix and Moment of Courage now use PRD. [corpus:liquipedia_dota2/random_distribution@2376760#Version_history]