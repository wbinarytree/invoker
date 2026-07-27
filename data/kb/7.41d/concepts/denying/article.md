---
title: Denying
kind: concept
patch: 7.41d
card:
  entity: denying
  sentences:
  - text: 'Denying is last-hitting a friendly unit to reduce enemy rewards: denied
      lane creeps grant enemies 50% experience, player-controlled units 0% experience,
      and allied creeps or non-heroes, heroes under special circumstances, and towers
      become deniable at 50%, 25%, and 10% health.'
    marks:
    - corpus:liquipedia_dota2/denying@2379552
  - text: A deny is performed with an attack command, or with Right Click when Right-Click
      Allies is not set to To Follow.
    marks:
    - corpus:liquipedia_dota2/denying@2379552
  - text: Illusions and couriers cannot be denied.
    marks:
    - corpus:liquipedia_dota2/denying@2379552
  - text: A denied allied lane creep not controlled by a player grants enemies within
      the 1500 experience range 50% of its experience bounty instead of 100%.
    marks:
    - corpus:liquipedia_dota2/denying@2379552#Denying_units
  - text: Denying allied lane creeps shifts creep equilibrium toward the denying side’s
      tower.
    marks:
    - corpus:liquipedia_dota2/denying@2379552#Denying_units
  - text: A lane creep killed by a neutral creep is not denied and grants enemy heroes
      full experience.
    marks:
    - corpus:liquipedia_dota2/denying@2379552#Denying_units
  - text: A denied tower grants half its gold bounty to each team and prevents the
      enemy player from receiving the 110-130 last-hit bonus gold.
    marks:
    - corpus:liquipedia_dota2/denying@2379552#Denying_towers
  - text: A denied hero loses gold upon death, but the enemy receives no experience
      or kill gold.
    marks:
    - corpus:liquipedia_dota2/denying@2379552#Denying_heroes
  - text: A self-denied hero receives no free Town Portal Scroll.
    marks:
    - corpus:liquipedia_dota2/denying@2379552#Denying_heroes
  - text: Poison Touch, Shadow Strike, and Venomous Gale make affected heroes deniable
      below 25% health.
    marks:
    - corpus:liquipedia_dota2/denying@2379552#Specially_Deniable
  - text: Experience from a hero deny goes only to the hero who created the deniable
      debuff, even if that hero is dead.
    marks:
    - corpus:liquipedia_dota2/denying@2379552#Specially_Deniable
  - text: Reaper’s Scythe and Winter’s Curse override deny mechanics and prevent denying.
    marks:
    - corpus:liquipedia_dota2/denying@2379552#Deny_Override
---

# Denying

> “Mm-mm denied!” — Luna [corpus:liquipedia_dota2/denying@2379552]

Denying is last-hitting a friendly unit. Enemies gain no gold and reduced experience from denied units: 50% experience from denied lane creeps and 0% from denied player-controlled units. Allied creeps and non-hero units become deniable at 50% health, heroes at 25%, and towers at 10%; heroes require special circumstances. Illusions and couriers cannot be denied. [corpus:liquipedia_dota2/denying@2379552]

Issue an attack command on the unit to deny it. Right Click also works when **Right-Click Allies** is set to anything other than **To Follow**. [corpus:liquipedia_dota2/denying@2379552]

## Denying units

Besides couriers, every non-hero unit, including creep-heroes, can be denied below 50% health. Denying an allied, non-player-controlled unit—lane creeps not taken over by players—grants enemies within the 1500 experience range 50% of its experience bounty instead of 100%. Denying a player-controlled unit grants the enemy 0% experience and grants none to the denying team. [corpus:liquipedia_dota2/denying@2379552#Denying_units]

During the laning phase, denying allied lane creeps can create gold and experience advantages. A level advantage can open an opportunity to kill the enemy, while preventing farm significantly slows enemies who depend on farming gold. Creeps should be denied whenever possible, although last hits take priority. Denying also shifts creep equilibrium toward the denying side’s tower and away from the enemy tower. [corpus:liquipedia_dota2/denying@2379552#Denying_units]

Denying creeps becomes less important as the laning phase transitions into the mid-game. Creeps provide map vision and pressure regardless of HP, and these become more important as the game progresses. Heroes also become more efficient farmers through items and levels, making time better spent farming elsewhere. [corpus:liquipedia_dota2/denying@2379552#Denying_units]

A lane creep is not considered denied when a neutral creep, such as Roshan, deals the finishing blow; it instead gives enemy heroes full experience. [corpus:liquipedia_dota2/denying@2379552#Denying_units]

Most player-controlled summons expire, allowing their bounties to be “denied” without manually killing them. This makes little difference for many small summons, but manual denial should still be attempted when possible, especially when multiple units can deny one another. Bigger summons, including **Warlock Golem** and **Spirit Bear**, should always be denied when unlikely to survive because they usually carry significant gold and experience bounties. Unlike with creeps, a neutral creep dealing the finishing blow to a player-controlled unit grants no experience. [corpus:liquipedia_dota2/denying@2379552#Denying_units]

## Denying towers

Towers become deniable at 10% health and below. A denied tower grants half its gold bounty to the enemy team and half to the denying team, while preventing an enemy player from receiving the 110-130 last-hit bonus gold. Towers can only be attacked through an attack command, regardless of the Game Settings. [corpus:liquipedia_dota2/denying@2379552#Denying_towers]

## Denying heroes

Heroes can be denied only under specific circumstances. A denied hero still loses gold upon death, but the enemy gains no experience or gold from the kill. A self-denied hero does not receive the free Town Portal Scroll awarded for dying. [corpus:liquipedia_dota2/denying@2379552#Denying_heroes]

Death to neutral creeps does not count as a deny but similarly grants the enemy team no experience or gold. In this case, the hero’s respawn time has a minimum duration and no Town Portal Scroll is gained. [corpus:liquipedia_dota2/denying@2379552#Denying_heroes]

### Specially deniable

The following debuffs make a hero deniable below 25% health:

| Hero | Ability |
|---|---|
| Dazzle | Poison Touch [corpus:liquipedia_dota2/denying@2379552#Specially_Deniable] |
| Queen of Pain | Shadow Strike [corpus:liquipedia_dota2/denying@2379552#Specially_Deniable] |
| Venomancer | Venomous Gale [corpus:liquipedia_dota2/denying@2379552#Specially_Deniable] |

Hero Denies grant experience only to the hero who created the deniable debuff. That hero receives the experience even if dead when the deny occurs, unlike regular hero kills, which grant experience only to living heroes. [corpus:liquipedia_dota2/denying@2379552#Specially_Deniable]

### Lethal self-damage

The following abilities damage their caster and can cause a self-deny:

| Hero | Ability | Condition |
|---|---|---|
| Abaddon | Borrowed Time | Because the aura has a linger duration, Abaddon normally takes self-damage when the duration ends. This damage is lethal and can be used to self-deny. [corpus:liquipedia_dota2/denying@2379552#Lethal_Self-Damage] |
| Alchemist | Unstable Concoction | Can deny Alchemist by exploding on himself when the concoction is not thrown. [corpus:liquipedia_dota2/denying@2379552#Lethal_Self-Damage] |
| Pugna | Life Drain | Can deny Pugna when cast on an ally. [corpus:liquipedia_dota2/denying@2379552#Lethal_Self-Damage] |

### Other special cases

| Category | Hero, source, or case | Ability or attack | Interaction |
|---|---|---|---|
| Special case | Doom | Doom | Applies if casted on a Neutral Creep. [corpus:liquipedia_dota2/denying@2379552#Other_Special_Cases] |
| Special case | Phoenix | Supernova | The sun becomes deniable below 50% health, denying Phoenix and the ally inside. [corpus:liquipedia_dota2/denying@2379552#Other_Special_Cases] |
| Return and self-attack | Centaur Warrunner | Retaliate | Fully works against allied attacks, damaging and possibly denying them. [corpus:liquipedia_dota2/denying@2379552#Other_Special_Cases] |
| Return and self-attack | Defiant Shell | Reciprocity | Fully works against allied attacks, counter-attacking and possibly denying them. [corpus:liquipedia_dota2/denying@2379552#Other_Special_Cases] |
| Return and self-attack | Marci | Bodyguard | Applies when casted on Marci’s own dominated creep and attacking it. [corpus:liquipedia_dota2/denying@2379552#Other_Special_Cases] |
| Return and self-attack | Ogre Magi | Fire Shield | Fully works against allied attacks, launching fireballs at and possibly denying them. [corpus:liquipedia_dota2/denying@2379552#Other_Special_Cases] |
| Return and self-attack | Io | Tether | If an enemy tames the creep connected to Io, the 25 talent causes Io to attack the same target as the creep. [corpus:liquipedia_dota2/denying@2379552#Other_Special_Cases] |
| Return and self-attack | Storm Spirit | Range Attack | Listed as a special case. [corpus:liquipedia_dota2/denying@2379552#Other_Special_Cases] |
| Ranged projectile | Chen | Holy Persuasion | Persuading a ranged creep after it launches an attack projectile toward an ally can cause a deny if that projectile deals the finishing blow. [corpus:liquipedia_dota2/denying@2379552#Other_Special_Cases] |
| Ranged projectile | Enchantress | Enchant | Enchanting a ranged creep after it launches an attack projectile toward an ally can cause a deny if that projectile deals the finishing blow. [corpus:liquipedia_dota2/denying@2379552#Other_Special_Cases] |
| Ranged projectile | Helm of the Dominator | Dominate | Dominating a ranged creep after it launches an attack projectile toward an ally can cause a deny if that projectile deals the finishing blow. [corpus:liquipedia_dota2/denying@2379552#Other_Special_Cases] |
| Ranged projectile | Helm of the Overlord | Dominate | Dominating a ranged creep after it launches an attack projectile toward an ally can cause a deny if that projectile deals the finishing blow. [corpus:liquipedia_dota2/denying@2379552#Other_Special_Cases] |
| Ranged projectile | Winter Wyvern | Winter’s Curse | If an enemy projectile aimed at the enemy’s teammate is fired during the ability but lands after it ends, the enemy may deny their ally. [corpus:liquipedia_dota2/denying@2379552#Other_Special_Cases] |
| Ally Creep Denying | Snapfire | Spit Out | Ally Creep Denying case. [corpus:liquipedia_dota2/denying@2379552#Other_Special_Cases] |
| Ally Creep Denying | Night Stalker | Hunter in the Night | Ally Creep Denying case. [corpus:liquipedia_dota2/denying@2379552#Other_Special_Cases] |

### Non-lethal self-damage

Damage from the following abilities cannot kill the player or their allies:

| Hero or item | Ability |
|---|---|
| Abaddon | Mist Coil [corpus:liquipedia_dota2/denying@2379552#Non-Lethal_Self-Damage] |
| Bloodseeker | Bloodrage [corpus:liquipedia_dota2/denying@2379552#Non-Lethal_Self-Damage] |
| Enigma | Demonic Summoning [corpus:liquipedia_dota2/denying@2379552#Non-Lethal_Self-Damage] |
| Huskar | Blood Magic [corpus:liquipedia_dota2/denying@2379552#Non-Lethal_Self-Damage] |
| Oracle | Purifying Flames [corpus:liquipedia_dota2/denying@2379552#Non-Lethal_Self-Damage] |
| Pudge | Rot [corpus:liquipedia_dota2/denying@2379552#Non-Lethal_Self-Damage] |
| Slark | Dark Pact [corpus:liquipedia_dota2/denying@2379552#Non-Lethal_Self-Damage] |
| Techies | Blast Off! [corpus:liquipedia_dota2/denying@2379552#Non-Lethal_Self-Damage] |
| Queen of Pain | Masochist¹ [corpus:liquipedia_dota2/denying@2379552#Non-Lethal_Self-Damage] |
| Blood Grenade | Throw Grenade [corpus:liquipedia_dota2/denying@2379552#Non-Lethal_Self-Damage] |
| Soul Ring | Sacrifice [corpus:liquipedia_dota2/denying@2379552#Non-Lethal_Self-Damage] |

¹ Requires selecting the corresponding facet. [corpus:liquipedia_dota2/denying@2379552#Non-Lethal_Self-Damage]

### Deny override

Some abilities ignore deny mechanics and cause specific heroes to receive kill credit. The following prevent denying:

| Hero | Ability |
|---|---|
| Necrophos | Reaper’s Scythe [corpus:liquipedia_dota2/denying@2379552#Deny_Override] |
| Winter Wyvern | Winter’s Curse [corpus:liquipedia_dota2/denying@2379552#Deny_Override] |

## Trivia

Denying is a core Warcraft 3 feature and is therefore present in every custom map, including DotA. In early DotA versions, attacking an ally hexed the attacker for one second because attacking allies was considered inappropriate for a mod such as DotA. Later versions removed the hex and replaced it with a simple stop command. [corpus:liquipedia_dota2/denying@2379552#Trivia]

Player feedback eventually led to denying being enabled in DotA, with Warcraft III used as an example of how denying could be strategic rather than merely griefing allies. The compromise permitted attacks only against non-hero units below 50% health; Warcraft III itself places no conditions on attacking allied or owned units and allows them to be attacked at any time. How and when hero-denying was added is unknown. [corpus:liquipedia_dota2/denying@2379552#Trivia]

## Version history

| Version | Date | Description |
|---|---|---|
| 7.36 | 2024-05-22 | Hero Denies now grant experience to the hero who created the deniable debuff. [corpus:liquipedia_dota2/denying@2379552#Version_History] |
| 7.29b | 2021-04-16 | Heroes no longer gain a free Town Portal Scroll if they denied themselves, or if the kill is credited to a neutral creep. [corpus:liquipedia_dota2/denying@2379552#Version_History] |
| 7.26b | 2020-04-28 | The denying player no longer gains 20% of the denied creep’s gold bounty. Increased lane creep deny experience for the denied team from 40% to 50%. [corpus:liquipedia_dota2/denying@2379552#Version_History] |
| 7.23 | 2019-11-26 | Denying a tower now grants half the team gold bounty to each team, instead of no bounty for anyone. [corpus:liquipedia_dota2/denying@2379552#Version_History] |
| 7.22 | 2019-05-24 | Increased lane creep deny experience for the denied team from 35% to 40%. [corpus:liquipedia_dota2/denying@2379552#Version_History] |
| 7.21c | 2019-03-02 | Increased lane creep deny experience for the denied team from 30% to 35%. [corpus:liquipedia_dota2/denying@2379552#Version_History] |
| 7.21b | 2019-02-16 | Increased lane creep deny experience for the denied team from 25% to 30%. [corpus:liquipedia_dota2/denying@2379552#Version_History] |
| 7.20 | 2018-11-19 | The denying team no longer gains 25% of the creep’s experience. The denying player now gains 20% of the denied creep’s gold bounty. [corpus:liquipedia_dota2/denying@2379552#Version_History] |
| 7.07 | 2017-10-31 | Reduced lane creep deny experience for the denied team from 70% to 25%. Denied XP gained by the denier reduced from 30% to 25%. Neutrals killing lane creeps is now treated like enemy creeps killing them: it is not a deny and grants full XP. The creep must be denied directly to deny its XP. [corpus:liquipedia_dota2/denying@2379552#Version_History] |
| 7.06 | 2017-05-15 | Lane creeps now give 70% experience when killed by neutral creeps or denied by allies, instead of 50%. Denying lane creeps now grants the denying team 30% of the experience bounty. [corpus:liquipedia_dota2/denying@2379552#Version_History] |
| 7.00 | 2016-12-12 | Lane creeps now give 50% experience when killed by neutral creeps, instead of 35%. [corpus:liquipedia_dota2/denying@2379552#Version_History] |
| 6.88c | 2016-08-19 | Lane creeps now give 35% experience when killed by neutral creeps, instead of 20%. [corpus:liquipedia_dota2/denying@2379552#Version_History] |
| 6.88b | 2016-07-12 | Lane creeps now give 20% experience when killed by neutral creeps, instead of 0%. [corpus:liquipedia_dota2/denying@2379552#Version_History] |
| 6.82 | 2014-09-25 | Denied creeps now give less experience: 50% experience instead of a constant 36 XP per unit. Tower bounty gold for destroying Tier 1/2/3/4 reduced from 264/312/358/405 to 160/200/240/280; denied is 50%. [corpus:liquipedia_dota2/denying@2379552#Version_History] |
| 6.79 | 2013-10-21 | Ranged heroes now receive the same denied experience as melee heroes instead of less. [corpus:liquipedia_dota2/denying@2379552#Version_History] |
| 6.78 | 2013-06-04 | Deny XP and Bonus XP/gold AoE is now the same as regular XP AoE, 1000->1200. [corpus:liquipedia_dota2/denying@2379552#Version_History] |
| 6.44 | 2026-07-25 | A hero must be below 25% health before an ally can begin denying them, assuming the hero can be denied. [corpus:liquipedia_dota2/denying@2379552#Version_History] |
| 6.38 | 2026-07-25 | Melee heroes get less denied XP than range heroes. [corpus:liquipedia_dota2/denying@2379552#Version_History] |
| 6.36b | 2026-07-25 | Lowered the recent XP deny change a little. [corpus:liquipedia_dota2/denying@2379552#Version_History] |
| 6.36 | 2026-07-25 | Denied units now give minor experience instead of none; this was planned for improved league play and was unrelated to the recent forum postings. [corpus:liquipedia_dota2/denying@2379552#Version_History] |

## Sound history

| Date | Sound | Changes |
|---|---|---|
| 25 May 2020 | Ranged deny sound | Reduced volume from 0.6 to 0.5. [corpus:liquipedia_dota2/denying@2379552#Patch_History] |
| 25 May 2020 | Melee deny sound | Added a pitch randomizer, 0/0.1. Reduced sound delay from 0.15 to 0.1. [corpus:liquipedia_dota2/denying@2379552#Patch_History] |
| 01 May 2020 | Deny sound event | Removed `pitch_rand_min`, which was -0.05. Removed `pitch_rand_max`, which was 0.05. Added mixgroup `"UI"`. Split the event into melee-deny and ranged-deny sounds. [corpus:liquipedia_dota2/denying@2379552#Patch_History] |
| 01 May 2020 | Melee deny sound | Increased volume from 80% to 100% (+25% volume) and added a 0.15-second delay. [corpus:liquipedia_dota2/denying@2379552#Patch_History] |
| 01 May 2020 | Ranged deny sound | Reduced volume from 80% to 60% (-25% volume). [corpus:liquipedia_dota2/denying@2379552#Patch_History] |

## Gallery

- Denying an allied creep. [corpus:liquipedia_dota2/denying@2379552#Gallery]

## See also

- Creep Control Techniques [corpus:liquipedia_dota2/denying@2379552#See_also]