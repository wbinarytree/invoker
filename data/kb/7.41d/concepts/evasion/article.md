---
title: Evasion
kind: concept
patch: 7.41d
card:
  entity: evasion
  sentences:
  - text: Evasion lets a unit evade an incoming attack, triggering on landing (projectile
      impact for ranged, attack point for melee), so attack modifiers and on-hit effects
      do not trigger; True Strike and Accuracy nullify it.
    marks:
    - corpus:liquipedia_dota2/evasion@2383969
  - text: A miss shows red MISS text to the attacker and white EVADE to the missed
      enemy, and plays no attack impact sound.
    marks:
    - corpus:liquipedia_dota2/evasion@2383969#Miss
  - text: 'Five mechanics cause misses: evasion, melee attack buffer, uphill miss
      chance, blind, and True Strike/Accuracy, with all evasion sources using pseudo-random
      distribution.'
    marks:
    - corpus:liquipedia_dota2/evasion@2383969#Definition
  - text: A melee attack misses 100% of the time if the target is farther than 350
      range beyond attack range (total buffer = attack range + attacker bound radius
      + target bound radius + 350), and True Strike does not help outside it.
    marks:
    - corpus:liquipedia_dota2/evasion@2383969#Attack_Range_Type
  - text: Ranged units without flying movement have a 25% uphill miss chance checked
      on projectile impact when the attacker is on lower terrain, regardless of vision
      or the size of the level difference.
    marks:
    - corpus:liquipedia_dota2/evasion@2383969#Uphill_Miss_Chance
  - text: Cleave and splash never affect the primary target and cannot miss on secondary
      targets, but a missed attack neither cleaves nor splashes.
    marks:
    - corpus:liquipedia_dota2/evasion@2383969#Cleave_&_Splash
  - text: Evasion and accuracy sources each stack diminishingly among themselves (1
      - ∏(1 - x)), while blind sources stack additively and multiplicatively with
      evasion; Final Hit Chance = 1 - Effective Evade Chance × (1 - Total Accuracy).
    marks:
    - corpus:liquipedia_dota2/evasion@2383969#Equations
  - text: Any combination of sub-100% sources stays below 100%, though 50% evasion
      on top of 35% still doubles effective HP against physical attacks.
    marks:
    - corpus:liquipedia_dota2/evasion@2383969#Stacking
  - text: Flat 100% evasion is granted by Arc Warden's Magnetic Field, Lycan Wolf's
      Hightail facet, and Windranger's Windrun, and it still stacks diminishingly
      and remains subject to blind and accuracy.
    marks:
    - corpus:liquipedia_dota2/evasion@2383969#Sources
  - text: 'Item evasion: Butterfly 35% (5450), Heaven''s Halberd 25% (3400), Radiance
      25% (4700), Talisman of Evasion 15% (1300).'
    marks:
    - corpus:liquipedia_dota2/evasion@2383969#Items
  - text: True Strike negates evasion and blind against its target but excludes buildings,
      applies no Accuracy debuff, prevents the melee 350-range miss, and can still
      be disjointed on ranged attacks.
    marks:
    - corpus:liquipedia_dota2/evasion@2383969#True_Strike
  - text: 'Proc-based outgoing accuracy grants True Strike on proc: Monkey King Bar
      80%, Bloodthorn 40%, Javelin 25%, Maelstrom/Mjollnir Chain Lightning 25%, and
      Drow''s Marksmanship 30/35/40.'
    marks:
    - corpus:liquipedia_dota2/evasion@2383969#Outgoing
---

# Evasion

Evasion is a mechanic that allows a unit to evade an incoming attack. All evasion effects trigger upon landing an attack — upon projectile impact for ranged units, and upon attack point for melee units. Any attack or ability effects that rely on attacks to hit their targets do not trigger, including most attack modifiers and on-hit effects unless explicitly specified. True Strike and Accuracy are the mechanics that nullify evasion. [corpus:liquipedia_dota2/evasion@2383969]

Upon missing an attack on an enemy, red floating text reading MISS appears, visible to the attacking player only; the missed enemy sees white floating text reading EVADE instead. A missed attack also does not play any of the attack impact sounds. [corpus:liquipedia_dota2/evasion@2383969#Miss]

## Miss sources

Five distinct mechanics can cause an attack to miss: [corpus:liquipedia_dota2/evasion@2383969#Definition]

- **Evasion** — grants the affected unit a chance to evade an incoming attack, stacking diminishingly with other evasion sources.
- **Melee attack buffer** — if a melee unit's target is beyond the attack buffer range, the attack misses 100% of the time. It fully affects Instant Attack sources and is negated by neither True Strike nor Accuracy.
- **Uphill miss chance** — ranged projectiles from units without flying movement have a 25% chance to miss when the attacker is at a lower terrain level than the target, regardless of vision. It stacks diminishingly with other evasion sources.
- **Blind** — a debuff causing the affected unit to have a chance to miss when attacking. Blind sources stack additively with each other up to 100%, and the total blind multiplier stacks diminishingly with evasion sources.
- **True Strike / Accuracy** — True Strike completely negates all evasion sources but does not work when attacking buildings; Accuracy applies a debuff making incoming attacks ignore evasion on the affected unit. All evasion sources use pseudo-random distribution. [corpus:liquipedia_dota2/evasion@2383969#Definition]

### Melee attack buffer range

For melee units, if the target is farther than 350 range beyond the melee unit's attack range, the attack misses 100% of the time, and True Strike does not guarantee hits on units outside the buffer range. For most melee heroes: [corpus:liquipedia_dota2/evasion@2383969#Attack_Range_Type]

```
Total Melee Buffer Range = Unit Total Attack Range + Attacker Bound Radius + Target Bound Radius + 350
```
[corpus:liquipedia_dota2/evasion@2383969#Attack_Range_Type]

### Uphill miss chance

For ranged units without flying movement, uphill miss chance is applied conditionally upon projectile impact rather than at the unit's attack point, causing 25% of ranged attacks to miss if the attacker is on a lower terrain level than the target, regardless of the size of the terrain level difference. A unit counts as being on higher elevated terrain when it is no longer visible to the player due to the terrain, and the miss chance applies whether or not the attacked unit is within vision. Because the check happens on impact, moving up onto elevated terrain after a projectile has been launched can cause it to miss even though both units were on the same ground level at launch. Uphill miss chance is considered an evasion source and does not apply to units with flying movement. [corpus:liquipedia_dota2/evasion@2383969#Uphill_Miss_Chance]

### Cleave and splash

Cleave does not affect the primary target and cannot miss when hitting secondary targets, but a missed attack does not cleave. Splash behaves the same way: it does not affect the primary target, cannot miss on secondary targets, and applies no damage within its radius if the attack misses. [corpus:liquipedia_dota2/evasion@2383969#Cleave_&_Splash]

## Equations

Evasion, blind, and accuracy sources are all determined by pseudo-random distribution. Accuracy and blind do not directly change the attacked unit's evasion value; instead they raise (blind) or lower (accuracy) the unit's effective evasion rate. Evasion sources and accuracy sources each stack diminishingly among themselves, while blind sources stack additively with each other and multiplicatively with evasion. [corpus:liquipedia_dota2/evasion@2383969#Equations]

```
Total Evasion  = 1 - ∏(1 - Evasion_i)
Total Blind    = Σ Blind_i
Total Accuracy = 1 - ∏(1 - Accuracy_i)

Effective Evade Chance = (1 - (1 - Total Evasion) × (1 - Total Blind)) × (1 - Melee Buffer Range Miss)
Final Hit Chance       = 1 - Effective Evade Chance × (1 - Total Accuracy)
```
[corpus:liquipedia_dota2/evasion@2383969#Equations]

Equivalently, the final hit chance can be written as `Total Accuracy + (1 - Total Accuracy) × (1 - Effective Evade Chance)`: attacks have a guaranteed chance to trigger True Strike equal to Total Accuracy, and the remaining `(1 - Total Accuracy)` of attacks are subjected to the effective evade chance. [corpus:liquipedia_dota2/evasion@2383969#Final_Hit_Chance]

## Stacking

Multiple evasion sources stack diminishingly, while blind sources stack additively with each other and multiplicatively with evasion. For an attack to land, it must bypass each evasion source in sequence — only if every source fails does the attack deal damage — so stacking evasion is equivalent to multiplying the corresponding chances to hit. Because a unit's chance to be hit is inversely proportional to its effective HP against attacks, each added evasion source raises effective HP against physical attacks more than the last: applying a 50% evasion source on top of 35% evasion still doubles effective hit points against physical attacks. Consequently, any combination of sources individually below 100% also stays below 100%, though a few abilities grant a flat 100% evasion, such as Magnetic Field and Windrun. [corpus:liquipedia_dota2/evasion@2383969#Stacking]

## Sources

Evasion causes a unit to evade attacks of all kinds, whereas disjointing only evades projectile-based attacks. Sources granting 100% evasion still stack diminishingly with other evasion sources and remain subject to blind and accuracy multipliers. 100% evasion is granted by Arc Warden's Magnetic Field, Lycan Wolf's Hightail (facet), and Windranger's Windrun. Other evasion sources include Brewmaster's Drunken Brawler (Storm Stance), Storm's Drunken Brawler (talent), Mirana's Moonlight Shadow (talent), Naga Siren's Eelskin, Phantom Assassin's Immaterial, Phantom Lancer's Phantom Rush, and the 25% uphill miss chance against ranged attacks. [corpus:liquipedia_dota2/evasion@2383969#Sources]

### Items

| Item | Evasion | Cost | Cost per point |
| --- | --- | --- | --- |
| Butterfly | 35% | 5450 | 155.71 |
| Heaven's Halberd | 25% | 3400 | 136 |
| Radiance | 25% | 4700 | 188 |
| Talisman of Evasion | 15% | 1300 | 86.67 |

Values do not include portions from actives or auras. [corpus:liquipedia_dota2/evasion@2383969#Items]

### Talents

Evasion talents are passive, affect the hero itself, and stack multiplicatively with other evasion sources. Talent evasion values are 8%/10%/12%/15%/16%/20%/25%/30%/40%/50%/75%. Separate talents grant a hero's attacks True Strike so they cannot miss. [corpus:liquipedia_dota2/evasion@2383969#Talents] [corpus:liquipedia_dota2/evasion@2383969#True_Strike_Talents]

### Blind sources

Arc Warden's Tempest Double, Broodmother's Incapacitating Bite, Keeper of the Light's Blinding Light, Ringmaster's Spotlight, Sand King's Sand Storm (facet), Riki's Smoke Screen, Tinker's Laser, and Troll Warlord's Whirling Axes (Melee). Although combined blind sources can exceed 100%, they are treated as capping at 100% for effective evasion calculations. [corpus:liquipedia_dota2/evasion@2383969#Blind]

## Accuracy and True Strike

Accuracy is applied as a debuff on the affected target and does not directly increase the attacked unit's evasion value; for calculation purposes the accuracy multiplier can be treated as an evasion source. True Strike sources can be regarded as outgoing accuracy: True Strike means the attacking unit's attack cannot be missed, outgoing accuracy is a chance-based conditional True Strike that procs on attack, and incoming accuracy is a debuff preventing incoming attacks on the affected unit from being missed. [corpus:liquipedia_dota2/evasion@2383969#Accuracy]

True Strike negates both evasion and blind against its target, including ward-type and allied units, but excludes buildings, and it does not apply an Accuracy debuff on the attacked unit. Ranged attacks with True Strike can still be disjointed. For melee units, True Strike also prevents a miss when the target moves more than 350 range away at the attack point. All attacks against runes and destroyable items have True Strike, and spell damage-based attacks ignore evasion and blind. [corpus:liquipedia_dota2/evasion@2383969#True_Strike]

Proc-based outgoing accuracy sources grant True Strike to the attack that procs them: Drow Ranger's Marksmanship (30/35/40, +10% talent), Javelin's Pierce (25%), Maelstrom and Mjollnir's Chain Lightning (25%), Bloodthorn's Pierce (40%), and Monkey King Bar's Pierce (80%). Chance-based outgoing accuracy sources instead grant attacks a chance not to miss: Fountain Damage (25% accuracy), Ancient Rumblehide's War Drums Aura (25 accuracy, 1200 neutral radius), and Witch Doctor's Death Ward and Voodoo Switcheroo (50% accuracy, not applying to bounces). [corpus:liquipedia_dota2/evasion@2383969#Outgoing]

Incoming accuracy is applied by Bloodthorn's Soul Rend, Meepo's Earthbind (talent), and planted Observer and Sentry Wards. [corpus:liquipedia_dota2/evasion@2383969#Incoming]

## Recent changes

- **7.22e (2019-07-14)** — Uphill miss chance and the blind sources Incapacitating Bite, Blinding Light, Burn, Sand Storm, Smoke Screen, and Whirling Axes (Melee) now use pseudo-random distribution.
- **7.20 (2018-11-19)** — Shine no longer grants 40% outgoing accuracy against the affected target; Fountain Damage attacks now have 25% accuracy.
- **7.07 (2017-10-31)** — Pierce sources now grant attacks True Strike upon proc; Solar Crest outgoing accuracy increased from 35% to 40%. [corpus:liquipedia_dota2/evasion@2383969#Recent_Changes]