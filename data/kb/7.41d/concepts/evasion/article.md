---
title: Evasion
kind: concept
patch: 7.41d
card:
  entity: evasion
  sentences:
  - text: Evasion is a Dota 2 mechanic granting a unit a chance to evade an incoming
      attack, checked on projectile impact for ranged attackers and at attack point
      for melee attackers, determined by pseudo-random distribution, stacking diminishingly
      with other evasion sources, and nullified by True Strike and Accuracy.
    marks:
    - corpus:liquipedia_dota2/evasion@2383969
    - corpus:liquipedia_dota2/evasion@2383969#Definition
  - text: Total Evasion as displayed on the HUD = 1 − ∏(1 − Evasion i).
    marks:
    - corpus:liquipedia_dota2/evasion@2383969#Equations
  - text: Effective Evade Chance = (1 − (1 − Total Evasion) × (1 − Total Blind)) ×
      (1 − Melee Buffer Range Miss).
    marks:
    - corpus:liquipedia_dota2/evasion@2383969#Equations
  - text: Final Hit Chance = 1 − Effective Evade Chance × (1 − Total Accuracy), equivalently
      Total Accuracy + (1 − Total Accuracy) × (1 − Effective Evade Chance).
    marks:
    - corpus:liquipedia_dota2/evasion@2383969#Final_Hit_Chance
  - text: 'Incoming attacks resolve in the order: Accuracy or True Strike proc → Evasion
      → Blind → Melee Buffer Range check → Attack Hits.'
    marks:
    - corpus:liquipedia_dota2/evasion@2383969#Equations
  - text: Total Blind = Σ Blind i, with blind sources stacking additively up to a
      maximum of 100% and multiplicatively with evasion.
    marks:
    - corpus:liquipedia_dota2/evasion@2383969#Blind
  - text: For melee units, an attack 100% misses if the target is farther than 350
      range beyond the melee attack range (Total Melee Buffer Range = Unit Total Attack
      Range + Attacker Bound Radius + Target Bound Radius + 350), and True Strike
      does not guarantee hits outside that buffer.
    marks:
    - corpus:liquipedia_dota2/evasion@2383969#Attack_Range_Type
  - text: Uphill miss chance causes 25% of ranged attacks from units without flying
      movement to miss on projectile impact when the attacker is at a lower terrain
      level than the target, regardless of vision or the size of the difference.
    marks:
    - corpus:liquipedia_dota2/evasion@2383969#Uphill_Miss_Chance
  - text: Items granting evasion are Butterfly 35% (5450 gold), Heaven's Halberd 25%
      (3400), Radiance 25% (4700), and Talisman of Evasion 15% (1300).
    marks:
    - corpus:liquipedia_dota2/evasion@2383969#Items
  - text: The 100% evasion sources are Arc Warden's Magnetic Field, Lycan Wolf's Hightail
      (facet), and Windranger's Windrun, and they still stack diminishingly and remain
      subject to Blind and Accuracy multipliers.
    marks:
    - corpus:liquipedia_dota2/evasion@2383969#Sources
  - text: The evasion talent is a passive self-buff using a hidden modifier with values
      of 8%/10%/12%/15%/16%/20%/25%/30%/40%/50%/75%, stacking multiplicatively with
      other evasion sources.
    marks:
    - corpus:liquipedia_dota2/evasion@2383969#Talents
  - text: True Strike negates all evasion and blind sources against the target, including
      ward-type and allied units but excluding buildings, applies no Accuracy debuff,
      and does not stop ranged projectiles from being disjointed.
    marks:
    - corpus:liquipedia_dota2/evasion@2383969#True_Strike
---

# Evasion

Evasion is a mechanic that allows a unit to evade an incoming attack. All Evasion effects trigger upon landing an attack: upon projectile impact for ranged units, and upon attack point for melee units. Any attack or ability effects that rely on attacks hitting their targets do not trigger, including most attack modifiers and on-hit effects unless explicitly specified. True Strike and Accuracy are mechanics that nullify Evasion. [corpus:liquipedia_dota2/evasion@2383969]

## Definition

All evasion sources use pseudo-random distribution. [corpus:liquipedia_dota2/evasion@2383969#Definition]

| Mechanic | Definition | Ranged trigger | Melee trigger | Examples |
|---|---|---|---|---|
| Evasion | Grants the affected unit a chance to evade an incoming attack. Stacks diminishingly with other evasion sources. | Upon projectile impact | Upon attack point | Butterfly |
| Melee Attack Buffer | If the attacked target of a melee unit is greater than the attack buffer range, the attack will 100% miss. Fully affects Instant Attack sources. Neither negated by True Strike nor Accuracy sources. | Upon projectile impact | Not applicable | — |
| Uphill Miss Chance | Affects ranged projectiles of units without flying movement. These projectiles have a 25% chance to miss upon attacking if the attacker is at a lower terrain level than the target, regardless of vision. Stacks diminishingly with other evasion sources. | Upon projectile impact | Not applicable | — |
| Blind | Applies a debuff causing affected units to have a chance to miss upon attacking. Stacks additively with other blind sources up to 100%. The total blind debuff multiplier stacks diminishingly with evasion sources. | Upon projectile impact | Upon attack point | Blinding Light |
| True Strike | Completely negates all evasion sources. Does not work when attacking buildings. | — | — | Astral Step |
| Accuracy | Applies a debuff causing incoming attacks to ignore evasion sources on the affected unit. 100% accuracy prevents all incoming attacks from being missed. Non-100% accuracy sources are considered chance-based True Strike. | Upon projectile impact | Upon attack point | Soul Rend, Monkey King Bar |

[corpus:liquipedia_dota2/evasion@2383969#Definition]

### Equations

All evasion, blind, and accuracy sources are determined by pseudo-random distribution. Accuracy and Blind sources do not directly increase the attacked unit's evasion value; instead they increase the effective evasion rate of the attacked unit for blind and lower it for accuracy. For effective evasion rate calculation purposes, multiple sources of evasion and accuracy stack diminishingly with each other respectively, while blind sources stack additively with each other and multiplicatively with evasion. [corpus:liquipedia_dota2/evasion@2383969#Equations]

- Total Evasion (as displayed on the HUD) = 1 − ∏(1 − Evasion i)
- Total Blind = Σ Blind i
- Total Accuracy = 1 − ∏(1 − Accuracy i)
- Effective Evade Chance = (1 − (1 − Total Evasion) × (1 − Total Blind)) × (1 − Melee Buffer Range Miss)
- Final Hit Chance = 1 − Effective Evade Chance × (1 − Total Accuracy)

Incoming attacks are resolved through: Accuracy Sources or True Strike Sources proc → Evasion → Blind → Melee Buffer Range check → Attack Hits. The formula is color-coded in sections, where blue indicates the chance that accuracy does not proc, red the total blind multiplier, and green the evasion multiplier. [corpus:liquipedia_dota2/evasion@2383969#Equations]

## Miss

Upon missing an attack on an enemy, a red floating text appears reading MISS, visible to the attacking player only. The enemy who was just missed also sees a floating text, but in white and reading EVADE instead. A missed attack does not play any of the attack impact sounds. [corpus:liquipedia_dota2/evasion@2383969#Miss]

### Attack Range Type

For melee units, if the target is farther than 350 range more than the melee unit's attack range, the attack 100% misses; True Strike does not guarantee hits on units outside of the buffer range. For most melee heroes: [corpus:liquipedia_dota2/evasion@2383969#Attack_Range_Type]

> Total Melee Buffer Range = Unit Total Attack Range + Attacker Bound Radius + Target Bound Radius + 350 [corpus:liquipedia_dota2/evasion@2383969#Attack_Range_Type]

### Uphill Miss Chance

For ranged units without Flying Movement, the uphill miss chance is conditionally applied upon a ranged attack projectile impact and not on the unit's attack point — it causes 25% of ranged attacks to miss if the attacking unit is at a lower terrain level than the target, regardless of the terrain level difference. A unit is considered to be on higher elevated terrain when it is no longer visible to the player due to the terrain. When an enemy stands on a relatively higher ramp, uphill miss chance applies whether the attacked unit is within vision or not. [corpus:liquipedia_dota2/evasion@2383969#Uphill_Miss_Chance]

This means moving up onto an elevated area after an attack projectile has been launched may cause the projectile to miss on impact due to uphill miss chance, even when both units were on the same ground level as the projectile was launched. Uphill miss chance is considered an evasion source, and does not apply to units with flying movement. [corpus:liquipedia_dota2/evasion@2383969#Uphill_Miss_Chance]

### Cleave & Splash

Cleave causes the unit's attack to deal damage in a trapezoid in front of the attacking unit, based on the unit's total attack damage values. Cleave can only be used by melee units; ranged units cannot cleave by default. Cleave does not affect the primary target and cannot miss when hitting secondary targets — however, a missed attack does not cleave. [corpus:liquipedia_dota2/evasion@2383969#Cleave_&_Splash]

Splash is in some ways the ranged version of cleave, working similarly, with the main difference being that damage is typically dealt in a circle around the attacked unit instead of a trapezoid in front of the attacking unit. Splash does not affect the primary target and cannot miss when hitting secondary targets; however, if an attack misses, no splash damage is applied within the radius. Splash damage works with attack modifiers the same way cleave does. [corpus:liquipedia_dota2/evasion@2383969#Cleave_&_Splash]

### Blind

Blind is a debuff that makes a unit miss upon attacking other units. Blind sources stack additively with each other, rendering an affected unit unable to land any attack. Although a combination of different blind sources can exceed 100%, for effective evasion rate calculation convenience they stack up to a maximum value of 100%. Total Blind = Σ Blind i. [corpus:liquipedia_dota2/evasion@2383969#Blind]

**Blind Sources**

| Source |
|---|
| Arc Warden – Tempest Double |
| Broodmother – Incapacitating Bite |
| Keeper of the Light – Blinding Light |
| Ringmaster – Spotlight |
| Sand King – Sand Storm³ |
| Riki – Smoke Screen |
| Tinker – Laser |
| Troll Warlord – Whirling Axes (Melee) |

¹ Requires a talent. ²ᵃ Requires Aghanim's Scepter. ²ᵇ Requires Aghanim's Shard. ³ Requires the selected facet. [corpus:liquipedia_dota2/evasion@2383969#Blind]

## Sources

The following sources grant evasion and are determined by pseudo-random distribution as long as their value is neither 0% nor 100%. Evasion causes a unit to evade attacks of all kinds, while disjointing only evades projectile-based attacks. Sources that grant 100% evasion still stack diminishingly with other evasion sources despite the evasion value being 100%; these sources are still subjected to Blind and Accuracy multipliers like regular evasion sources. Total Evasion (HUD) = 1 − ∏(1 − Evasion i). [corpus:liquipedia_dota2/evasion@2383969#Sources]

**100% Evasion Sources**

| Source |
|---|
| Arc Warden – Magnetic Field |
| Lycan Wolf – Hightail³ |
| Windranger – Windrun |

³ Requires selecting the corresponding facet. [corpus:liquipedia_dota2/evasion@2383969#Sources]

**Evasion Sources**

| Source |
|---|
| Brewmaster – Drunken Brawler (Storm Stance) |
| Storm – Drunken Brawler¹ |
| Mirana – Moonlight Shadow¹ |
| Naga Siren – Eelskin |
| Phantom Assassin – Immaterial |
| Phantom Lancer – Phantom Rush |
| Evasion – 25% Uphill Miss Chance (Ranged Attacks) |

¹ Requires talent. [corpus:liquipedia_dota2/evasion@2383969#Sources]

### Items

The following items grant the wielder an evasion bonus. Values do not include portions from actives or auras. [corpus:liquipedia_dota2/evasion@2383969#Items]

| Item | Value | Item Cost | Cost/Value Point |
|---|---|---|---|
| Butterfly | 35% | 5450 | 155.71 |
| Heaven's Halberd | 25% | 3400 | 136 |
| Quickened Enchantment | — | N/A | N/A |
| Radiance | 25% | 4700 | 188 |
| Talisman of Evasion | 15% | 1300 | 86.67 |

[corpus:liquipedia_dota2/evasion@2383969#Items]

### Talents

The evasion talent is a passive that affects Self and grants the hero evasion (value varies). It stacks multiplicatively with other evasion sources, uses a hidden modifier, and has the following evasion values: 8%/10%/12%/15%/16%/20%/25%/30%/40%/50%/75%. Heroes with such a talent gain a bonus of +15% Evasion. [corpus:liquipedia_dota2/evasion@2383969#Talents]

## Accuracy

Accuracy is applied as a debuff on the affected target. It does not directly increase the attacked unit's evasion value; for calculation purposes the accuracy multiplier can be considered as an evasion source as well. Total Accuracy = 1 − ∏(1 − Accuracy i). True Strike sources can also be considered as outgoing accuracy. [corpus:liquipedia_dota2/evasion@2383969#Accuracy]

| Mechanic | Definition | Ability Examples |
|---|---|---|
| True Strike | The attacking unit's attack cannot be missed. | Walrus PUNCH! |
| Outgoing Accuracy | Chance-based conditional True Strike that procs on attack. | Pierce, Fountain Damage |
| Incoming Accuracy | Applies a debuff that prevents incoming attacks on the affected unit from being missed. | Soul Rend |

[corpus:liquipedia_dota2/evasion@2383969#Accuracy]

### True Strike

True Strike prevents the unit's attacks from missing, negating both evasion and blind sources against their target, including ward-type units and allied units, excluding Buildings. However, it does not apply an Accuracy debuff on the attacked unit. For ranged units, although True Strike prevents the attack from missing, attack projectiles of ranged units with True Strike can still be disjointed. For melee units, it also prevents the attacking unit's attack from missing when the attacked target moves more than 350 range away upon its attack point. All attacks against Runes and against destroyable items have True Strike. Spell damage-based attacks ignore evasion and blind. [corpus:liquipedia_dota2/evasion@2383969#True_Strike]

**Hero Ensured True Strike Sources**

| Source |
|---|
| Dark Seer – Normal Punch |
| Kez – Shodo Sai Mark⁴ ⁶ |
| Meepo – Earthbind¹ |
| Nyx Assassin – Vendetta⁶ |
| Tusk – Walrus PUNCH! |

**Hero Ensured True Strike Sources [Instant Attack]⁵**

| Source |
|---|
| Clinkz – Burning Barrage⁶ |
| Dawnbreaker – Starbreaker⁶ |
| Kez – Kazurai Katana⁶ |
| Kez – Talon Toss |
| Luna – Lunar Orbit⁶ |
| Mars – God's Rebuke |
| Monkey King – Boundless Strike |
| Pangolier – Swashbuckle⁶ |
| Pangolier – Shield Crash²ᵃ |
| Phantom Assassin – Stifling Dagger⁶ |
| Sand King – Stinger⁶ |
| Sand King – Epicenter²ᵃ |
| Sand King – Epicenter²ᵃ ²ᵇ |
| Sniper – Assassinate⁶ |
| Shadow Fiend – Shadowraze¹ ⁶ |
| Tidehunter – Anchor Smash⁶ |
| Tiny – Tree Throw⁶ |
| Tiny – Tree Volley⁶ |
| Void Spirit – Astral Step⁶ |

**Hero Chance-based True Strike Sources**

| Source |
|---|
| Drow Ranger – Marksmanship |
| Witch Doctor – Death Ward |
| Witch Doctor – Voodoo Switcheroo |

**Item Ensured True Strike Sources**

| Source |
|---|
| Bloodthorn – Soul Rend |
| Parasma – Witch Blade |
| Silver Edge – Shadow Walk⁶ |
| Witch Blade – Witch Blade |

**Other Chance-based True Strike Sources**

| Source |
|---|
| Bloodthorn – Pierce |
| Javelin – Pierce |
| Maelstrom – Chain Lightning |
| Mjollnir – Chain Lightning |
| Monkey King Bar – Pierce |
| Serrated Shiv – Gut 'Em |
| Ancient Rumblehide – War Drums Aura |
| Fountain – Fountain Attack |

¹ Requires a talent. ²ᵃ Requires Aghanim's Scepter. ²ᵇ Requires Aghanim's Shard. ³ Requires the selected facet. ⁴ Attack from Kez on the unit marked by this ability has True Strike. ⁵ Not all abilities with Instant Attack have true strike. ⁶ This is not stated in the ability description. [corpus:liquipedia_dota2/evasion@2383969#True_Strike]

### True Strike Talents

The True Strike talent is a passive that affects Self, granting the hero's attack True Strike so they cannot miss, via a hidden modifier. Some heroes have a talent that grants them True Strike. [corpus:liquipedia_dota2/evasion@2383969#True_Strike_Talents]

### Outgoing Accuracy

Attacks that proc the following sources are granted True Strike. [corpus:liquipedia_dota2/evasion@2383969#Outgoing]

**Proc-based Outgoing Accuracy**

| Source | Proc Chance | Note |
|---|---|---|
| Drow Ranger – Marksmanship | 30/35/40 (+10% talent) | Attacks proccing Marksmanship cannot miss |
| Javelin – Pierce | 25% | Attacks proccing Pierce cannot miss |
| Maelstrom – Chain Lightning | 25% | Attacks proccing Chain Lightning cannot miss |
| Mjollnir – Chain Lightning | 25% | Attacks proccing Chain Lightning cannot miss |
| Monkey King Bar – Pierce | 80% | Attacks proccing Pierce cannot miss |
| Bloodthorn – Pierce | 40% | Attacks proccing Pierce cannot miss |

Percentage-based outgoing accuracy sources grant attacks a chance to not miss on the target. [corpus:liquipedia_dota2/evasion@2383969#Outgoing]

**Chance-based Outgoing Accuracy**

| Source | Values | Note |
|---|---|---|
| Fountain – Fountain Damage | Accuracy: 25% | Attacks have a chance to not miss |
| Ancient Rumblehide – War Drums Aura | Neutral Radius: 1200; Player Controlled Radius: 40%/43%/46%/51%; Accuracy: 25 | Effects provided by an aura granting allies a chance to not miss on attacks |
| Witch Doctor – Death Ward | Accuracy: 50% | Attacks have a chance to not miss; increased accuracy does not apply to bounces |
| Witch Doctor – Voodoo Switcheroo | Same values and notes as Death Ward | — |

[corpus:liquipedia_dota2/evasion@2383969#Outgoing]

### Incoming Accuracy

| Source |
|---|
| Bloodthorn – Soul Rend |
| Meepo – Earthbind¹ |
| Observer Ward – Planted Ward |
| Sentry Ward – Planted Ward |

¹ Requires talent. ²ᵃ Requires Aghanim's Scepter. ²ᵇ Requires Aghanim's Shard. [corpus:liquipedia_dota2/evasion@2383969#Incoming]

## Stacking

Multiple sources of evasion stack diminishingly with each other, while sources of blind effects stack additively with each other and multiplicatively with evasion. All evasion and accuracy sources are determined by pseudo-random distribution. [corpus:liquipedia_dota2/evasion@2383969#Stacking]

A more concrete way of thinking about evasion stacking: for an attack to bypass an evasion stack and hit, the attack must bypass each source of evasion in sequence — only if all sources of evasion fail can the attack deal attack damage. Consider the chance to be hit, which is 1 − evade chance. A unit's chance to be hit is inversely proportional to its effective HP against attacks, and stacking multiple evasion sources is equivalent to multiplying their corresponding chances to hit. Thus evasion's effectiveness stacks multiplicatively — while the actual chance to evade is diminishing, each source of evasion increases effective HP against physical attacks more than the last. Consequences: [corpus:liquipedia_dota2/evasion@2383969#Stacking]

- Applying a 50% evasion source while already having 35% evasion still doubles your effective hit points against physical attacks.
- A combination of evasion sources that are individually less than 100% is also less than 100%. A few abilities grant 100% evasion (e.g. Magnetic Field and Windrun). [corpus:liquipedia_dota2/evasion@2383969#Stacking]

**Example 1** — Incoming attacks hit Butterfly's wielder 65% of the time, because the item grants 35% evasion. Arc Warden within the Magnetic Field radius has 30/60/90/120 evasion; without any other evasion negating sources, all incoming attacks against Arc Warden are missed while it is within the radius. [corpus:liquipedia_dota2/evasion@2383969#Stacking]

**Example 2a** — Multiple evasion sources stack multiplicatively with diminishing returns: an enemy attacking a Phantom Assassin with Butterfly (0.35 evasion) and level 4 Blur combines via Effective Evade Chance = 1 − (1 − Total Evasion) × (1 − Total Blind), with Final Hit Chance = 1 − Effective Evade Chance. Alternatively, Blur and Butterfly's individual chances to hit (Butterfly: 0.65) multiply together, showing multiplicative stacking. [corpus:liquipedia_dota2/evasion@2383969#Stacking]

**Example 2b** — Blind sources stack additively with each other (no overlaps), are summed, then stack multiplicatively/diminishingly with evasion as the unit's Effective Evade Chance. With the attacking enemy affected by Burn and level 4 Smoke Screen (0.7 blind), Effective Evade Chance = 1 − (1 − Total Evasion) × (1 − Total Blind) and Final Hit Chance = 1 − Effective Evade Chance. Although Phantom Assassin's total evasion did not change, the blind applied to the enemy increases her effective evade chance. [corpus:liquipedia_dota2/evasion@2383969#Stacking]

### Final Hit Chance

Given a unit with an Effective Evade Chance and subjected to Total Accuracy: [corpus:liquipedia_dota2/evasion@2383969#Final_Hit_Chance]

> Final Hit Chance = Total Accuracy + (1 − Total Accuracy) × (1 − Effective Evade Chance)

Intuitively: the attacking unit's attacks have a guaranteed chance to trigger True Strike based on the Total Accuracy value, whereas (1 − Total Accuracy) of the attacks that do not trigger True Strike are subjected to the Effective Evade Chance. Alternatively simplified: [corpus:liquipedia_dota2/evasion@2383969#Final_Hit_Chance]

> Final Hit Chance = 1 − Effective Evade Chance × (1 − Total Accuracy)

Interpreted as: normally, Effective Evade Chance of the attacks would miss, but due to accuracy only (1 − Total Accuracy) of these would-be-missed attacks actually miss, since attacks based on the Total Accuracy value hit the target due to True Strike. [corpus:liquipedia_dota2/evasion@2383969#Final_Hit_Chance]

**Example 3** — Accuracy overwrites Effective Evade Chance. The same enemy, still affected by Burn and level 4 Smoke Screen (0.7), acquires a Monkey King Bar (Pierce accuracy: 0.8) and continues attacking Phantom Assassin. With Monkey King Bar equipped, 80% of attacks are guaranteed to hit due to True Strike; the remaining 20% that do not have True Strike are subjected to the Effective Evade Chance. Both formulas above yield the same result. [corpus:liquipedia_dota2/evasion@2383969#Final_Hit_Chance]

## Recent Changes

| Version | Description |
|---|---|
| 7.22e (2019-07-14) | The following sources now use pseudo-random distribution: Uphill Miss Chance; Blind sources: Incapacitating Bite, Blinding Light, Burn, Sand Storm, Smoke Screen, Whirling Axes (Melee) |
| 7.20 (2018-11-19) | Shine no longer grants 40% outgoing accuracy against the affected target. Fountain Damage attacks now have 25% accuracy. |
| 7.07 (2017-10-31) | The following sources now grant attacks True Strike upon proc: Pierce, Pierce. Increased Solar Crest outgoing accuracy from 35% to 40%. |

[corpus:liquipedia_dota2/evasion@2383969#Recent_Changes]