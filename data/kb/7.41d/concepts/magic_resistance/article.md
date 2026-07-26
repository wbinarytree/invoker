---
title: Magic Resistance
kind: concept
patch: 7.41d
card:
  entity: magic_resistance
  sentences:
  - text: Magic resistance is a unit stat that reduces—or, when negative, increases—the
      percentage of magical damage taken from spells and magic attacks; all heroes
      have 25% base resistance, and every 10 intelligence grants 1% additional base
      resistance.
    marks:
    - corpus:liquipedia_dota2/magic_resistance@2394734
    - corpus:liquipedia_dota2/magic_resistance@2394734#Heroes
    - corpus:liquipedia_dota2/magic_resistance@2394734#Definition
  - text: Base magic resistance contains a fixed value set individually for each unit,
      and the value can be negative.
    marks:
    - corpus:liquipedia_dota2/magic_resistance@2394734#Base_Magic_Resistance
  - text: A negation multiplier affects only base magic resistance, leaving other
      bonus sources unaffected.
    marks:
    - corpus:liquipedia_dota2/magic_resistance@2394734#Definition
  - text: Magic-resistance bonuses and reductions from abilities, items, talents,
      and other mechanics stack multiplicatively.
    marks:
    - corpus:liquipedia_dota2/magic_resistance@2394734#Definition
  - text: Spell immunity prevents most abilities from targeting a unit and is separate
      from 100% magic resistance and debuff immunity.
    marks:
    - corpus:liquipedia_dota2/magic_resistance@2394734#Spell_Immunity
  - text: Pure damage does not interact with magic resistance or armor.
    marks:
    - corpus:liquipedia_dota2/magic_resistance@2394734#Pure_Damage
  - text: Magic-resistance reductions from multiple ethereal effects do not stack;
      the higher value takes priority.
    marks:
    - corpus:liquipedia_dota2/magic_resistance@2394734#Ethereal
  - text: Illusions do not benefit from bonus magic resistance, so their magic-resistance-modifying
      sources are set to 0.
    marks:
    - corpus:liquipedia_dota2/magic_resistance@2394734#Definition
  - text: Combining +30% and +40% magic resistance produces a 0.42 incoming multiplier,
      so 100 magical damage deals 42 damage.
    marks:
    - corpus:liquipedia_dota2/magic_resistance@2394734#Stacking
  - text: Fate’s Edict grants 100% magic resistance and a 0 incoming multiplier, causing
      the affected unit to take 0 magical damage regardless of negative-resistance
      sources.
    marks:
    - corpus:liquipedia_dota2/magic_resistance@2394734#Stacking
  - text: Effective HP against magical damage equals CurrentHP divided by the final
      magic-damage multiplier.
    marks:
    - corpus:liquipedia_dota2/magic_resistance@2394734#Effective_Health
  - text: Heroes’ default 25% magic resistance gives them 133.33% effective HP against
      magical damage.
    marks:
    - corpus:liquipedia_dota2/magic_resistance@2394734#Effective_Health
---

# Magic Resistance

Magic resistance is a stat that reduces—or, when negative, increases—the percentage of magical damage a unit takes from spells and magic attacks. Every unit can gain or lose it, and most units begin with a small amount of base magic resistance. A hero can passively increase it through talents, certain items, and abilities; abilities can also temporarily increase or reduce any unit’s magic resistance. [corpus:liquipedia_dota2/magic_resistance@2394734]

## Definition

Every 10 points of intelligence grants an additional 1% base magic resistance. A negation multiplier affects and reduces only base magic resistance; other bonus sources are unaffected. Bonuses and reductions from abilities, items, talents, and other mechanics stack multiplicatively. [corpus:liquipedia_dota2/magic_resistance@2394734#Definition]

The incoming magical-damage multiplier is applied to all incoming magical damage sources to determine the total magical damage received after damage-barrier reductions. [corpus:liquipedia_dota2/magic_resistance@2394734#Definition]

### Equations

The HUD total and incoming magical-damage multiplier \(f\) are defined as:

```text
Total Magic Resistance = 1 - f

Magic Damage Multiplier =
(1 - Negation Multiplier)
× ( Current Magic Resistance )
× ( 1 - MAX Ethereal )
× ( 1 - Magic Resistance Modifiers i )
```

[corpus:liquipedia_dota2/magic_resistance@2394734#Equations]

### Actual magical damage received

Actual magical damage is the health a target immediately loses as a direct result. Its factors are applied in this order:

```text
Actual Magical Damage Received =
Total Magical Damage
- Magic Damage Block
× Magic Resistance Multiplier
- Magic Damage Barrier
× Other generic incoming damage manipulation Sources
```

Before these calculations, the damage dealer’s generic outgoing-damage manipulation, such as spell amplification, can amplify the total magical damage. [corpus:liquipedia_dota2/magic_resistance@2394734#Actual_Magic_Damage_Received]

### Spell immunity

Spell immunity, formerly called magic immunity, prevents most abilities from targeting the affected unit, including single-targeted, area-of-effect, passive, and active abilities. Having 100% magic resistance is not the same as being spell immune or debuff immune; all three are separate mechanics. [corpus:liquipedia_dota2/magic_resistance@2394734#Spell_Immunity]

Spell-immune units do not interact with spell damage at all, whereas magic resistance reduces incoming magical damage from abilities. Spell immunity is usually given to some units as an additional protective layer, commonly on ward-type units or together with invulnerability. [corpus:liquipedia_dota2/magic_resistance@2394734#Spell_Immunity]

## Base magic resistance

Base magic resistance contains one fixed value set individually for each unit, and that value can be negative. [corpus:liquipedia_dota2/magic_resistance@2394734#Base_Magic_Resistance]

### Heroes

All heroes currently have the same base magic resistance:

| Stat | Value |
|---|---:|
| Base Magic Resist | 25% |

[corpus:liquipedia_dota2/magic_resistance@2394734#Heroes]

Each point of intelligence grants heroes a base-magic-resistance bonus. Intelligence can be gained through leveling, certain items, or certain abilities. [corpus:liquipedia_dota2/magic_resistance@2394734#Details]

#### Base-increasing sources

| Source | Ability or mechanic |
|---|---|
| Attributes | Attribute Bonus |
| Alchemist | Aghanim's Scepter Synth |
| Evolved Enchantment | Primary Attribute Bonus |
| Invoker | Exort |
| Power Treads | Switch Attribute |
| Magnus | Reverse Polarity¹ |
| Silencer | Glaives of Wisdom |
| Skywrath Mage | Shield of the Scion |
| Morphling | Morph²ᵃ |

¹ Requires talent.  
²ᵃ Requires Aghanim's Scepter.  
²ᵇ Requires Aghanim's Shard.  
[corpus:liquipedia_dota2/magic_resistance@2394734#Base_Increasing_Sources]

### Creeps

| Unit | Magic Resistance |
|---|---:|
| Ghost, Minor Imp, Pollywog, Boglet, Croaker, Marshmage Apprentice, Marshmage, Zealot, Kobold, Kobold Soldier, Kobold Foreman, Hill Troll Berserker, Hill Troll Priest, Vhoul Assassin, Fell Spirit, Harpy Scout, Harpy Stormcrafter, Centaur Courser, Centaur Conqueror, Giant Wolf, Alpha Wolf, Satyr Banisher, Satyr Mindstealer, Ogre Bruiser, Ogre Frostmage, Satyr Tormenter, Hellbear, Hellbear Smasher, Wildwing, Wildwing Ripper, Hill Troll, Dark Troll Summoner, Skeleton Warrior, Razorback, Ancient Prowler Acolyte, Ancient Prowler Shaman, Forged Spirit | 0 |
| Ancient Black Drake, Treant, Spiderling | 0.25 |
| Warpine Raider, Ancient Frostbitten Golem, Ancient Ice Shaman, Ancient Croaker, Ancient Marshmage, Mud Golem, Ancient Black Dragon, Ancient Rock Golem, Ancient Granite Golem, Ancient Rumblehide, Ancient Thunderhide, Shard Golem | 0.3 |
| Raptor, Eidolon | 0.3/0.4/0.5/0.6 |
| Undying Zombie | 0.33 |
| Demonic Archer, Demonic Warrior | 0.4 |
| Lycan Wolf | 0.45/0.5/0.55/0.6 |
| Wraith King Skeleton | 0.5 |
| Tormentor, Roshan | 0.55 |

[corpus:liquipedia_dota2/magic_resistance@2394734#Creeps]

### Summons

| Unit | Magic Resistance |
|---|---:|
| Earth, Astral Spirit, Fire | 0 |
| Storm | 0.25 |
| Warlock Golem | 0.33 |
| Familiar | 0.35 |

[corpus:liquipedia_dota2/magic_resistance@2394734#Summons]

### Base magic-resistance negation

Some abilities negate or ignore a percentage of a target’s base magic resistance. This affects only base magic resistance; bonus sources are unaffected. Natural Order and Astral Spirit’s Natural Order work differently from ordinary multiplicative magic-resistance sources by acting as a multiplier for base magic resistance. They are currently the only two base-magic-resistance-negation sources. [corpus:liquipedia_dota2/magic_resistance@2394734#Base_Magic_Resistance_Negation]

For heroes with 25% base magic resistance, Natural Order applies a base-magic-resistance-negation multiplier of 0, reducing base magic resistance to 0%. [corpus:liquipedia_dota2/magic_resistance@2394734#Base_Magic_Resistance_Negation]

| Source | Ability |
|---|---|
| Elder Titan | Natural Order |
| Astral Spirit | Natural Order |

[corpus:liquipedia_dota2/magic_resistance@2394734#Base_Magic_Resistance_Negation]

#### Pure damage

Pure damage interacts with neither armor nor magic resistance. Magical-damage amplification abilities do not amplify it, and it fully ignores armor and damage block. It does not affect invulnerable units. [corpus:liquipedia_dota2/magic_resistance@2394734#Pure_Damage]

Some sources can manipulate pure damage through the damage-reduction mechanic; Dispersion is one such source. Pure damage affects spell-immune units because spell immunity does not block damage, but an ability dealing pure damage is not necessarily able to target spell-immune units. [corpus:liquipedia_dota2/magic_resistance@2394734#Pure_Damage]

## Modifying magic resistance

Several abilities and items grant or reduce magic resistance. [corpus:liquipedia_dota2/magic_resistance@2394734#Modifying_Magic_Resistance]

### Increasing sources

| Source | Ability or mechanic |
|---|---|
| Anti-Mage | Counterspell |
| Arc Warden | Magnetic Field |
| Brewmaster | Drunken Brawler Earth Stance |
| Centaur Courser | Cloak Aura |
| Dragon Knight | Black Dragon Form²ᵃ |
| Huskar | Berserker's Blood |
| Lina | Flame Cloak |
| Meepo | Divided We Stand |
| Oracle | Fate's Edict |
| Pipe of Insight | Insight Aura |
| Vambrace | Switch Attribute |
| Viper | Corrosive Skin |

¹ Requires talent.  
²ᵃ Requires Aghanim's Scepter.  
²ᵇ Requires Aghanim's Shard.  
[corpus:liquipedia_dota2/magic_resistance@2394734#Increasing_Sources]

### Debuff immunity

Debuff immunity stops most debuff effects on a unit without dispelling the debuffs and grants a magic-resistance bonus. [corpus:liquipedia_dota2/magic_resistance@2394734#Debuff_Immunity]

| Category | Source | Ability |
|---|---|---|
| Debuff Immunity Sources | Black King Bar | Avatar |
| Debuff Immunity Sources | Elder Titan | Astral Spirit²ᵃ |
| Debuff Immunity Sources | Huskar | Life Break |
| Debuff Immunity Sources | Juggernaut | Blade Fury |
| Debuff Immunity Sources | Lifestealer | Rage |
| Debuff Immunity Sources | Pangolier | Rolling Thunder |
| Debuff Immunity Sources without Basic Dispel | Dawnbreaker | Starbreaker²ᵇ |
| Debuff Immunity Sources without Basic Dispel | Chen | Hand of God²ᵃ |
| Debuff Immunity Sources without Basic Dispel | Lion | Mana Drain²ᵇ |
| Debuff Immunity Sources without Basic Dispel | Omniknight | Repel |
| Debuff Immunity Sources without Basic Dispel | Pangolier | Roll Up |
| Debuff Immunity Sources without Basic Dispel | Ringmaster | Tame the Beasts¹ |
| Passive Debuff Immunity | Grimstroke | Dark Portrait (Illusion) |

¹ Requires talent.  
²ᵃ Requires Aghanim's Scepter.  
²ᵇ Requires Aghanim's Shard.  
[corpus:liquipedia_dota2/magic_resistance@2394734#Debuff_Immunity]

### Talents

The magic-resistance talent is a passive ability affecting the hero and grants a varying bonus. It increases the hero’s magic resistance and stacks multiplicatively with other sources. Its modifier is hidden. [corpus:liquipedia_dota2/magic_resistance@2394734#Talents]

The following talent values exist:

```text
5%/6%/8%/10%/12%/14%/15%/20%/25%/30%/35%/40%/50%/80%/100%
```

The listed magic-resistance bonus entries are `+10%/+15%/+10%/+15%`, under talent-table headings for Level 10, Level 15, Level 20, and Level 25 with Left and Right sides. [corpus:liquipedia_dota2/magic_resistance@2394734#Talents]

With 25% magic resistance and no other sources:

| Starting resistance | Talent | Magic Resistance Total | Increased Value |
|---|---:|---:|---:|
| Basic Magic Resistance (25%) | +8% | 31% | +6% |
| Basic Magic Resistance (25%) | +12% | 34% | +9% |
| Basic Magic Resistance (25%) | +15% | 36.25% | +11.25% |
| Basic Magic Resistance (25%) | +20% | 40% | +15% |
| Basic Magic Resistance (25%) | +25% | 43.75% | +18.75% |

[corpus:liquipedia_dota2/magic_resistance@2394734#Talents]

### Items

The following equipped items grant percentage-based bonus magic resistance:

| Item | Value | Item Cost | Cost/Value Point |
|---|---:|---:|---:|
| Cloak | 18% | 900 | 50 |
| Consecrated Wraps | 12% | 2600 | 216.67 |
| Glimmer Cape | 20% | 2150 | 107.5 |
| Mage Slayer | 18% | 3100 | 172.22 |
| Mystical Enchantment | 0% | N/A | N/A |
| Pipe of Insight | 20% | 3725 | 186.25 |
| Shawl | 10% | 450 | 45 |

The values exclude portions supplied by actives or auras. [corpus:liquipedia_dota2/magic_resistance@2394734#Items]

### Reduction sources

| Source | Ability |
|---|---|
| Ancient Apparition | Ice Vortex |
| Keeper of the Light | Solar Bind |
| Skywrath Mage | Ancient Seal |
| Shadow Fiend | Requiem of Souls |
| Techies | Proximity Mines |
| Viper | Poison Attack |
| Ethereal Blade | Ether Blast |
| Ghost Scepter | Ghost Form |
| Leshrac | Nihilism |
| Muerta | Pierce the Veil¹ |
| Necrophos | Ghost Shroud² |
| Pugna | Decrepify |

¹ Requires talent.  
²ᵃ Requires Aghanim's Scepter.  
²ᵇ Requires Aghanim's Shard.  
[corpus:liquipedia_dota2/magic_resistance@2394734#Reduction_Sources]

### Ethereal

Ethereal, sometimes called ghost form, makes affected units immune to all physical damage, grants attack immunity, and disarms them. It usually—but not always—reduces magic resistance, causing additional magical damage to be taken. Affected units retain control over every other aspect of their character. [corpus:liquipedia_dota2/magic_resistance@2394734#Ethereal]

Reductions from multiple ethereal effects do not stack; the higher value takes priority:

```text
Ethereal Magic Resistance Reduction =
(1 + MAX Ethereal Magic Resistance Reduction)
```

[corpus:liquipedia_dota2/magic_resistance@2394734#Ethereal]

| Source | Ability |
|---|---|
| Ethereal Blade | Ether Blast |
| Ghost Scepter | Ghost Form |
| Leshrac | Nihilism |
| Muerta | Pierce the Veil¹ |
| Necrophos | Ghost Shroud² |
| Pugna | Decrepify |

¹ Requires talent.  
²ᵃ Requires Aghanim's Scepter.  
²ᵇ Requires Aghanim's Shard.  
[corpus:liquipedia_dota2/magic_resistance@2394734#Ethereal]

### Illusion negation

For illusions, magic-resistance-modifying sources are set to 0 because illusions do not benefit from bonus magic resistance. [corpus:liquipedia_dota2/magic_resistance@2394734#Definition]

Bonus magic-resistance negation affects only an illusion’s bonus magic resistance. Its base magic resistance remains unaffected and can still be manipulated normally by base-magic-resistance-negation sources. [corpus:liquipedia_dota2/magic_resistance@2394734#Illusions_Negation]

## Stacking

Each magic-resistance source acts independently as an incoming magical-damage multiplier. An effect that increases magic resistance by 30%, or states “+30% Magic resistance,” acts as \(1 - 0.3 = 0.7\). Applying multiple effects multiplies their corresponding damage multipliers, similarly to evasion stacking. [corpus:liquipedia_dota2/magic_resistance@2394734#Stacking]

A unit with +30% and +40% magic resistance has an incoming multiplier of \(0.7 * 0.6 = 0.42\), so a 100 magical-damage instance deals 42 damage. Activating Black King Bar reduces the magical damage a hero takes by half regardless of its existing magic resistance. [corpus:liquipedia_dota2/magic_resistance@2394734#Stacking]

In the other direction, −40% and −60% magic resistance produce an incoming multiplier of \(1.4 * 1.6 = 2.24\). Consequently, combining multiple magic-resistance sources individually below 100% also remains effectively below 100%. [corpus:liquipedia_dota2/magic_resistance@2394734#Stacking]

Fate’s Edict grants 100% magic resistance, corresponding to a 0 incoming magical-damage multiplier. Multiplication by this 0 makes the final multiplier 0 regardless of other negative-magic-resistance sources, so the affected unit always takes 0 magical damage. [corpus:liquipedia_dota2/magic_resistance@2394734#Stacking]

The HUD displays magic resistance calculated from the final multiplier after all effects. A multiplier of 2.24 appears as −124% magic resistance. [corpus:liquipedia_dota2/magic_resistance@2394734#Stacking]

```text
Total Magic Resistance = 1 - Final Magic Damage Multiplier

Final Magic Damage Multiplier =
∏ᵢ₌₁ⁿ (Magic Damage Multiplier i)

For base magic resistance:
Magic Damage Multiplier Base =
[1 - Negation Multiplier × (0.25 + 0.001 × )]

For other magic resistance sources:
Magic Damage Multiplier i = 1 - Magic Resistance

In full:
Total Magic Resistance =
1 - [1 - Negation Multiplier × (0.25 + 0.001 × )]
× ∏ᵢ₌₁ⁿ (1 - Magic Resistance Modifiers i)
```

[corpus:liquipedia_dota2/magic_resistance@2394734#Stacking]

### Stacking example 1: bonuses

Anti-Mage has level 4 Counterspell and a Mage Slayer, without accounting for intelligence-based base-magic-resistance increases:

```text
Base hero magic resistance: 0.25
Bonus magic resistance:
Counterspell: 0.35
Mage Slayer: 0.18

Final Magic Damage Multiplier
= (1 - 0.25) * (1 - 0.35) * (1 - 0.18)
= 0.39975
```

All incoming magical damage is multiplied by 0.4. The current total magic resistance is \(1 - 0.39975 = 60.03\%\). [corpus:liquipedia_dota2/magic_resistance@2394734#Stacking]

### Stacking example 2: reductions

Marci is affected by level 4 Ancient Seal, level 4 Decrepify, and Nihilism, without accounting for intelligence-based base-magic-resistance increases:

```text
Base hero magic resistance: 0.25
Magic resistance reduction:
Ancient Seal: -0.35
Decrepify: -0.5
Nihilism: -0.3

Final Magic Damage Multiplier
= (1 - 0.25) * (1 - -0.35) * (1 - -0.5)
= 1.51875
```

All incoming magical damage is multiplied by 1.52. The current total magic resistance is \(1 - 1.52 = -51.875\%\). Nihilism’s ethereal reduction is not included because Decrepify has the higher magic-resistance-reduction value. [corpus:liquipedia_dota2/magic_resistance@2394734#Stacking]

## Effective health

The total magical damage a unit can take because of magic resistance is its Effective HP, or EHP. Although each additional resistance source increases the displayed resistance by less as resistance rises, each source increases effective HP against magical damage by its base value. [corpus:liquipedia_dota2/magic_resistance@2394734#Effective_Health]

A unit with 0% magic resistance has 100% effective HP against magical damage, requiring magical damage equal to 100% of its health to kill it. Heroes’ default 25% magic resistance gives them 133.33% effective HP against magical damage. [corpus:liquipedia_dota2/magic_resistance@2394734#Effective_Health]

| Magic Resistance | Effective HP |
|---:|---:|
| -100% | 500 |
| -75% | 571 |
| -50% | 667 |
| -25% | 800 |
| 0% | 1000 |
| 25% | 1333 |
| 50% | 2000 |
| 75% | 4000 |
| 100% | ∞ |

[corpus:liquipedia_dota2/magic_resistance@2394734#Effective_Health]

This definition assumes all incoming damage is magical. Armor modifies effective HP against physical damage, including basic hero attacks. Effective HP against magical damage is:

```text
EHP = CurrentHP / Final Magic Damage Multiplier
```

[corpus:liquipedia_dota2/magic_resistance@2394734#Effective_Health]

### Effective-health example 1

Level 6 Marci has 1048 health:

```text
Base magic resistance: 0.2804

EHPmagic
= 1048 / 0.7196
= 1456.36
```

Marci has 1456.36 EHP against magical damage. [corpus:liquipedia_dota2/magic_resistance@2394734#Effective_Health]

### Effective-health example 2

The same Marci is affected by level 4 Ancient Seal and level 4 Decrepify:

```text
Health: 1048
Base magic resistance: 0.2804
Magic resistance reduction:
Ancient Seal: -0.35
Decrepify: -0.5

Final Magic Damage Multiplier
= (1 - 0.2804) * (1 - -0.35) * (1 - -0.5)
= 1.45719

EHPmagic
= 1048 / 1.45719
= 719
```

Marci has 719 EHP against magical damage. [corpus:liquipedia_dota2/magic_resistance@2394734#Effective_Health]

## Recent changes

| Version | Date | Changes |
|---|---|---|
| 7.33 | 2023-04-20 | Added the new Debuff Immunity mechanic. Debuff Immunity stops most debuff effects on a unit without dispelling the debuffs while granting a magic-resistance bonus. Magical Damage Barrier now stacks additively with barriers of the same damage type and independently from other damage-type barriers, and now absorbs damage calculated before all magic-resistance reductions. Intelligence now grants 0.1% Base Magic Resistance per point. |
| 7.07 | 2017-10-31 | Fixed magical-damage sources from attacks not being blocked by magic-damage-barrier abilities, including Barrier and Flame Guard. |
| 6.52 | 2026-07-25 | Fixed Phantom Edge not stacking with other magic-resistance sources. |

[corpus:liquipedia_dota2/magic_resistance@2394734#Recent_Changes]