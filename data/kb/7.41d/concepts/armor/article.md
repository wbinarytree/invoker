---
title: Armor
kind: concept
patch: 7.41d
card:
  entity: armor
  sentences:
  - text: Armor is a unit stat that reduces incoming physical damage from abilities
      and attacks when positive and increases it when negative; each hero agility
      point adds 0.167 or 1/6 armor, and its physical-damage factor is bounded from
      0 to 2.
    marks:
    - corpus:liquipedia_dota2/armor@2374627
    - corpus:liquipedia_dota2/armor@2374627#Armor_Damage_Factor
  - text: Every unit, including buildings, has an inherent base-armor value.
    marks:
    - corpus:liquipedia_dota2/armor@2374627#Armor_Damage_Factor
  - text: Actual total armor has up to two decimal places; the HUD rounds it down,
      while the details tab rounds it up.
    marks:
    - corpus:liquipedia_dota2/armor@2374627#Definition
  - text: Main armor is the white HUD value and equals base armor plus agility-based
      armor.
    marks:
    - corpus:liquipedia_dota2/armor@2374627#Main_Armor
  - text: Base armor is fixed and never changes during a game.
    marks:
    - corpus:liquipedia_dota2/armor@2374627#Base_Armor
  - text: Bonus armor is the green +Armor value displayed after the white armor number.
    marks:
    - corpus:liquipedia_dota2/armor@2374627#Bonus_Armor
  - text: Illusions do not benefit from bonus-armor sources even though their HUD
      displays the granted value.
    marks:
    - corpus:liquipedia_dota2/armor@2374627#Bonus_Armor
  - text: The physical-damage factor is 1 − (0.06 × ΣArmor) / (1 + 0.06 × |ΣArmor|).
    marks:
    - corpus:liquipedia_dota2/armor@2374627#Equations
  - text: Effective HP increases by 6% of MaxHP per armor.
    marks:
    - corpus:liquipedia_dota2/armor@2374627#Armor_Damage_Factor
  - text: Armor values of 10 and -10 produce physical-damage factors of 63% and 138%,
      respectively.
    marks:
    - corpus:liquipedia_dota2/armor@2374627#Armor_Damage_Factor
  - text: Armor-negation sources manipulate main armor without interacting with attack
      classes.
    marks:
    - corpus:liquipedia_dota2/armor@2374627#Armor_Negation_Sources
  - text: Pure damage fully ignores armor and damage block.
    marks:
    - corpus:liquipedia_dota2/armor@2374627#Pure_Damage
---

# Armor

Armor is a stat that reduces physical damage a unit takes from abilities and attacks, or increases it when negative. Every unit can gain or lose armor; most begin with a small amount of base armor, while some begin with negative armor. A hero’s armor can passively increase through agility gained from leveling, certain items, talents, and abilities. Abilities can also temporarily increase or reduce any unit’s armor. Each point of agility increases a hero’s armor by `0.167` or `1/6`. [corpus:liquipedia_dota2/armor@2374627]

## Definition

A unit’s actual total armor according to `ent_text` has up to two decimal places. The HUD displays a rounded-down value next to the hero portrait, while the details tab displays the value rounded up. [corpus:liquipedia_dota2/armor@2374627#Definition]

| Armor type | Definition | Example |
|---|---|---|
| Main Armor | The armor value shown in white numbers near the HUD’s shield icon. Grants `+0.167` per agility. | Agility-based Armor |
| Base Armor | The unit’s predefined armor value in the game files, which can be positive or negative. For heroes, it is defined in `npc_heroes`. Since only heroes utilize agility, their main armor is the sum of both the Base and Main Armor. | |
| Bonus Armor | The `+ x` armor value shown in green numbers near the HUD’s shield icon. Most armor-manipulating sources modify bonus armor. Created illusions do not benefit from it. | Platemail |
| Armor Damage Factor | Incoming physical-damage instances are reduced by a factor based on the attacked unit’s current total armor. The attacked unit’s current-health-to-incoming-physical-damage factor is its Effective HP. | |

[corpus:liquipedia_dota2/armor@2374627#Definition]

### Equations

The armor equation is a passive effect affecting self. Incoming physical-damage instances are reduced by a factor based on the attacked unit’s current total armor. [corpus:liquipedia_dota2/armor@2374627#Equations]

| Constant | Value |
|---|---:|
| Armor Formula Base `b` | 1 |
| Armor Formula Factor `f` | 0.06 |
| Base Armor Bonus per Agi | 0.167 |

All heroes receive the stated base armor bonus per agility. [corpus:liquipedia_dota2/armor@2374627#Equations]

```text
Physical Damage Factor: 1 - ( 0.06 × ΣArmor ) / ( 1 + 0.06 × |ΣArmor|)
ΣArmor: Main × f(ArmorNegation) ± FlatBonus
Main Armor: Base + ( ΣCurrentAGI × 0.167 )
```

For self-illusions, all granted attributes and secondary-stat bonuses, including main armor bonuses, are functional. [corpus:liquipedia_dota2/armor@2374627#Equations]

### Armor Damage Factor

All units, including buildings, have an inherent Base Armor value and attack class. Every physical-damage instance applied to a unit is multiplied by its armor damage factor, producing damage reduction or an increase according to the target’s total armor and affecting its Effective HP. A lower factor produces higher Effective HP and vice versa. The factor’s lower and upper limits are `0` and `2`, respectively. Effective HP increases by `6%` of the unit’s MaxHP per armor. [corpus:liquipedia_dota2/armor@2374627#Armor_Damage_Factor]

| Armor (+) | Factor | Armor (-) | Factor |
|---:|---:|---:|---:|
| 1 | 94% | -1 | 106% |
| 2 | 89% | -2 | 111% |
| 3 | 85% | -3 | 115% |
| 4 | 81% | -4 | 119% |
| 5 | 77% | -5 | 123% |
| 6 | 74% | -6 | 126% |
| 7 | 70% | -7 | 130% |
| 8 | 68% | -8 | 132% |
| 9 | 65% | -9 | 135% |
| 10 | 63% | -10 | 138% |
| 11 | 60% | -11 | 140% |
| 12 | 58% | -12 | 142% |
| 13 | 56% | -13 | 144% |
| 14 | 54% | -14 | 146% |
| 15 | 53% | -15 | 147% |
| 16 | 51% | -16 | 149% |
| 17 | 50% | -17 | 150% |
| 18 | 48% | -18 | 152% |
| 19 | 47% | -19 | 153% |
| 20 | 45% | -20 | 155% |
| 21 | 44% | -21 | 156% |
| 22 | 43% | -22 | 157% |
| 23 | 42% | -23 | 158% |
| 24 | 41% | -24 | 159% |
| 25 | 40% | -25 | 160% |
| 26 | 39% | -26 | 161% |
| 27 | 38% | -27 | 162% |
| 28 | 37% | -28 | 163% |
| 29 | 36% | -29 | 164% |
| 30 | 36% | -30 | 164% |
| 31 | 35% | -31 | 165% |
| 32 | 34% | -32 | 166% |
| 33 | 34% | -33 | 166% |
| 34 | 33% | -34 | 167% |
| 35 | 32% | -35 | 168% |
| 36 | 32% | -36 | 168% |
| 37 | 31% | -37 | 169% |
| 38 | 30% | -38 | 170% |
| 39 | 30% | -39 | 170% |
| 40 | 29% | -40 | 171% |
| 41 | 29% | -41 | 171% |
| 42 | 28% | -42 | 172% |
| 43 | 28% | -43 | 172% |
| 44 | 27% | -44 | 173% |
| 45 | 27% | -45 | 173% |

[corpus:liquipedia_dota2/armor@2374627#Armor_Damage_Factor]

### Pure Damage

Pure Damage interacts with neither Armor nor Magic Resistance. It is not amplified by magical-damage-amplification abilities, fully ignores Armor and Damage Block, and does not affect invulnerable units. Some sources can manipulate Pure Damage through the mechanic called damage reduction; Dispersion is one such source. Pure damage affects units with Spell Immunity because spell immunity does not block damage, but an ability dealing pure damage is not necessarily able to target spell-immune units. [corpus:liquipedia_dota2/armor@2374627#Pure_Damage]

## Main Armor

Main Armor is the white armor value shown near the HUD’s shield icon and is the sum of base armor and agility-based armor. It can be improved by leveling up, acquiring certain items, or using certain abilities. [corpus:liquipedia_dota2/armor@2374627#Main_Armor]

### Base Armor

Base Armor is a fixed, predefined component of each individual unit’s main armor and never changes during a game. Because only heroes utilize agility, non-hero HUDs show only base armor. [corpus:liquipedia_dota2/armor@2374627#Base_Armor]

#### Heroes

| Hero | Armor |
|---|---:|
| | -2 |
| | -1 |
| | 0 |
| | 1 |
| | 2 |
| | 3 |
| | 4 |
| | 5 |
| | 6 |

[corpus:liquipedia_dota2/armor@2374627#Heroes]

#### Creeps

| Unit | Armor |
|---|---:|
| Undying Zombie, Kobold, Hill Troll Priest, Satyr Banisher, Ogre Frostmage, Mud Golem, Hill Troll, Skeleton Warrior, Shard Golem, Treant, Spiderling, Lycan Wolf | 0 |
| Minor Imp, Pollywog, Kobold Soldier, Hill Troll Berserker, Vhoul Assassin, Fell Spirit, Harpy Scout, Centaur Courser, Giant Wolf, Ogre Bruiser, Razorback | 1 |
| Ghost, Boglet, Marshmage Apprentice, Zealot, Kobold Foreman, Harpy Stormcrafter, Satyr Mindstealer, Satyr Tormenter, Wildwing, Ancient Black Drake, Wraith King Skeleton | 2 |
| Eidolon | 2/3/4/5 |
| Ancient Ice Shaman, Croaker, Marshmage, Alpha Wolf, Hellbear, Ancient Rumblehide, Ancient Thunderhide | 3 |
| Demonic Archer, Demonic Warrior, Centaur Conqueror, Hellbear Smasher, Wildwing Ripper, Dark Troll Summoner, Ancient Black Dragon, Ancient Rock Golem | 4 |
| Ancient Croaker, Ancient Marshmage | 5 |
| Warpine Raider, Raptor | 6 |
| Ancient Frostbitten Golem | 7 |
| Ancient Granite Golem | 8 |
| Ancient Prowler Acolyte | 11 |
| Ancient Prowler Shaman | 12 |
| Tormentor | 20 |
| Roshan | 30 |

[corpus:liquipedia_dota2/armor@2374627#Creeps]

#### Summons

| Unit | Armor |
|---|---:|
| Astral Spirit | 0 |
| Fire | 0/8/16/24 |
| Storm | 2 |
| Familiar | 2/3/4 |
| Earth | 3/5/7/9 |
| Warlock Golem | 8/12/14 |

[corpus:liquipedia_dota2/armor@2374627#Summons]

### Main Armor Sources

These sources directly manipulate agility and affect a hero’s main armor. [corpus:liquipedia_dota2/armor@2374627#Main_Armor_Sources]

| Main Armor Affecting Source |
|---|
| Attributes – Attribute Bonus |
| Alchemist – Aghanim's Scepter Synth |
| Evolved Enchantment – Primary Attribute Bonus |
| Drow Ranger – Precision Aura |
| Magnus – Reverse Polarity<sup>1</sup> |
| Riki – Tricks of the Trade |
| Slark – Essence Shift |
| Power Treads – Switch Attribute |
| Phantom Lancer – Phantom Rush |
| Morphling – Morph<sup>2a</sup> |
| Invoker – Wex |
| Morphling – Attribute Shift (Strength Gain) |
| Timbersaw – Whirling Death<sup>3</sup> |

| Marker | Condition |
|---|---|
| 1 | Requires a Talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |
| 3 | Only affects universal heroes and heroes with agility as their primary attribute. |

[corpus:liquipedia_dota2/armor@2374627#Main_Armor_Sources]

### Armor Negation Sources

Armor Negation sources manipulate a unit’s main armor unless an ability’s notes explicitly state otherwise. They do not interact with Attack Classes. [corpus:liquipedia_dota2/armor@2374627#Armor_Negation_Sources]

| Armor Negate Source |
|---|
| Clinkz – Infernal Shred<sup>4</sup> |
| Drow Ranger – Marksmanship |
| Elder Titan – Natural Order |

| Marker | Condition |
|---|---|
| 1 | Requires a Talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |
| 4 | Interacts with total armor. |

[corpus:liquipedia_dota2/armor@2374627#Armor_Negation_Sources]

### Armor Piercing Sources [corpus:liquipedia_dota2/armor@2374627#Armor_Piercing_Sources]

## Bonus Armor

Bonus Armor is the `+Armor` value displayed in green, with a plus sign on its left, after the white armor number. Most manipulation sources affect bonus armor. Reduction sources can bring total armor below zero when main armor is sufficiently small. Illusions do not benefit from bonus-armor sources, although their HUD displays the granted bonus armor for camouflage. [corpus:liquipedia_dota2/armor@2374627#Bonus_Armor]

### Armor Increasing Sources

| Armor Increasing Source |
|---|
| Ancient Black Dragon – Dragonhide Aura |
| Axe – Berserker's Call |
| Axe – Culling Blade |
| Chen – Divine Favor |
| Dazzle – Bad Juju |
| Dazzle – Shadow Wave |
| Dragon Knight – Dragon Blood |
| Elder Titan – Astral Spirit |
| Legion Commander – Overwhelming Odds<sup>2b</sup> |
| Lone Druid – Spirit Link |
| Lone Druid – True Form |
| Monkey King – Wukong's Command |
| Ogre Frostmage – Ice Armor |
| Oracle – False Promise<sup>1</sup> |
| Primal Beast – Uproar |
| Roshan – Strength of the Immortal |
| Skywrath Mage – Shield of the Scion |
| Slardar – Guardian Sprint<sup>2a</sup> |
| Sven – Warcry |
| Timbersaw – Reactive Armor |
| Tiny – Grow |
| Treant Protector – Living Armor |
| Towers – Tower Protection |
| Troll Warlord – Berserker's Rage |
| Wildwing Ripper – Toughness Aura |

| Armor Increasing Item Source |
|---|
| Armlet of Mordiggian – Unholy Strength |
| Assault Cuirass – Assault Aura |
| Buckler – Buckler Aura |
| Medallion of Courage – Valor |
| Ring of Aquila – Aquila Aura |
| Solar Crest – Shine |
| Helm of the Dominator – Dominate<sup>1</sup> |
| Helm of the Overlord – Dominate<sup>1</sup> |
| Vladmir's Offering – Vladmir's Aura |

| Marker | Condition |
|---|---|
| 1 | Requires a Talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |
| 3 | Affects the player-controlled creep. |
| 1 | Affects the player-controlled creep. |

[corpus:liquipedia_dota2/armor@2374627#Armor_Increasing_Sources]

### Talents

Bonus Armor is a passive talent effect affecting self. Selecting the respective talent grants a unit flat bonus armor; the Armor Bonus varies. [corpus:liquipedia_dota2/armor@2374627#Talents]

The following heroes have talents that grant bonus armor to their player-controlled units:

| Hero | Player-controlled unit |
|---|---|
| Enchantress | Enchanted Creep |
| Lone Druid | Summon Spirit Bear |
| Warlock | Chaotic Offering |

Different ability IDs exist for the following armor values:

| Ability ID | Armor |
|---:|---:|
| 6110 | +2 |
| 5930 | +3 |
| 5931 | +4 |
| 5932 | +5 |
| 5933 | +6 |
| 5970 | +7 |
| 5937 | +8 |
| 6136 | +9 |
| 6004 | +10 |
| 6286 | +12 |
| 6175 | +15 |
| 6503 | +20 |
| 6645 | +30 |

The following entries describe talents that grant their heroes bonus armor:

| Entry |
|---|
| Bonus |
| Level 10 |
| Level 15 |
| Level 20 |
| Level 25 |
| Left |
| Right |
| Left |
| Right |
| Left |
| Right |
| Left |
| Right |
| Armor |
| +4 |
| +4 |
| +4 |
| +4 |
| +5 |
| +4 |

[corpus:liquipedia_dota2/armor@2374627#Talents]

### Items

The following items increase the owner’s armor while equipped. Each provides a flat armor bonus. [corpus:liquipedia_dota2/armor@2374627#Items]

| Item | Flat Armor | Item Cost | Cost/Value Point |
|---|---:|---:|---:|
| Armlet of Mordiggian | 6 | 2500 | 416.67 |
| Assault Cuirass | 10 | 5125 | 512.5 |
| Blade Mail | 7 | 2400 | 342.86 |
| Buckler | 1 | 425 | 425 |
| Chainmail | 4 | 500 | 125 |
| Crimson Guard | 6 | 3725 | 620.83 |
| Essence Distiller | 6 | 1775 | 295.83 |
| Guardian Greaves | 5 | 4450 | 890 |
| Heaven's Halberd | 9 | 3400 | 377.78 |
| Helm of Iron Will | 4 | 975 | 243.75 |
| Helm of the Dominator | 6 | 2550 | 425 |
| Helm of the Overlord | 7 | 5650 | 807.14 |
| Lotus Orb | 10 | 3850 | 385 |
| Mekansm | 5 | 1775 | 355 |
| Nullifier | 10 | 4350 | 435 |
| Parasma | 7 | 5975 | 853.57 |
| Pavise | 3 | 1350 | 450 |
| Phase Boots | 4 | 1450 | 362.5 |
| Platemail | 10 | 1400 | 140 |
| Ring of Protection | 2 | 175 | 87.5 |
| Shiva's Guard | 17 | 4500 | 264.71 |
| Solar Crest | 7 | 2575 | 367.86 |
| Soul Ring | 2 | 805 | 402.5 |
| Spirit Vessel | 2 | 2725 | 1362.5 |
| Splintmail | 7 | 950 | 135.71 |
| Tough Enchantment | 0 | N/A | N/A |
| Urn of Shadows | 2 | 825 | 412.5 |
| Vladmir's Offering | 1 | 2200 | 2200 |
| Witch Blade | 5 | 2775 | 555 |
| Wraith Band | 1.75 | 505 | 288.57 |

Values exclude portions supplied by actives or auras. [corpus:liquipedia_dota2/armor@2374627#Items]

### Armor Reducing Sources

| Armor Reducing Source |
|---|
| Alchemist – Acid Spray |
| Ancient Rock Golem – Weakening Aura |
| Bristleback – Viscous Nasal Goo |
| Bristleback – Hairball |
| Chaos Knight – Reality Rift |
| Dazzle – Poison Touch |
| Dazzle – Shadow Wave<sup>2a</sup> |
| Forged Spirit – Melting Strike |
| Lycan – Howl |
| Naga Siren – Rip Tide |
| Pangolier – Lucky Shot |
| Razor – Eye of the Storm |
| Shadow Fiend – Presence of the Dark Lord |
| Slardar – Slithereen Crush<sup>2b</sup> |
| Slardar – Corrosive Haze |
| Slark – Essence Shift |
| Snapfire – Lil' Shredder |
| Templar Assassin – Meld |
| Tidehunter – Gush |
| Vengeful Spirit – Wave of Terror |
| Viper – Poison Attack<sup>2b</sup> |
| Weaver – The Swarm |

| Armor Reducing Item Source |
|---|
| Assault Cuirass – Assault Aura |
| Mask of Madness – Berserk |
| Orb of Blight – Lesser Corruption |
| Desolator – Corruption |
| Orb of Corrosion – Corrosion |
| Stygian Desolator – Greater Corruption |

| Marker | Condition |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |

[corpus:liquipedia_dota2/armor@2374627#Armor_Reducing_Sources]

#### Armor Corruption

Armor Corruption is a passive effect affecting enemies and is granted by learning a talent. Attacks then reduce the affected target’s armor by a varying amount for a duration of `10`. The debuff is applied per successful attack, stacks independently with other Armor Corruption or armor-reduction sources, and has its duration refreshed when reapplied. [corpus:liquipedia_dota2/armor@2374627#Armor_Corruption]

It affects:

| Affected unit |
|---|
| Ally units |
| Buildings |
| Ward-type units |

Different modifiers exist for the following armor-reduction values:

| Modifier | Armor reduction |
|---:|---:|
| 439 | 2.5 |
| 7383 | 3 |
| 7011 | 4 |
| 6846 | 5 |

The ability effects are applied in the following order:

| Order | Effect |
|---:|---|
| 1 | The Armor Corruption debuff |
| 2 | The hero's attack damage instance |

[corpus:liquipedia_dota2/armor@2374627#Armor_Corruption]

## Armor-based Sources

The following sources use the hero’s current armor value as an ability effect:

| Armor-based Source |
|---|
| Axe – Battle Hunger |
| Axe – One Man Army |
| Clockwerk – Armor Power |

[corpus:liquipedia_dota2/armor@2374627#Armor-based_Sources]

## Calculation Examples

### Example 1 — Armor with Agility Sources

For a hero-level Terrorblade with Blade of Alacrity and Blade Mail equipped:

```text
Base Armor: 6
Bonus Armor: Blade Mail +7
Total agility: 23 + 4 * 10 + Blade of Alacrity (10)

Main Armor
= Base + (ΣAgi / 6)
= 6 + (23 + 4 * 10 + 10) / 6
= 18.17

Total Armor
= Main Armor + Bonus Armor
= 18.17 + 7
= 25.17
```

Terrorblade has `18.17` main armor and total armor of `25.17` displayed on his HUD. [corpus:liquipedia_dota2/armor@2374627#Armor_Calculations]

### Example 2 — Various Armor Sources with Armor Negation Interactions

Terrorblade from the previous example is affected by level `3` Natural Order:

```text
Armor Negation: Natural Order (80%)

Total Armor
= Main Armor * (1 - ArmorNegation) + Bonus Armor
= 18.166666666667 * (1 - 80%) + 7
= 15.433333333333
```

Terrorblade has `15.433333333333` total armor. Natural Order affects the main-armor component but not the bonus-armor component. [corpus:liquipedia_dota2/armor@2374627#Armor_Calculations]

### Example 3 — Incoming Physical Damage with Total Armor Interactions [corpus:liquipedia_dota2/armor@2374627#Armor_Calculations]

### Example 4 — Effective HP Against Incoming Physical Damage [corpus:liquipedia_dota2/armor@2374627#Effective_HP_Calculations]

## Recent Changes

### 7.32e — 2023-03-07

Reinforced units receive `10%` less damage from:

| Source |
|---|
| Summons, excluding creep-heroes and illusions |
| Dominated Creeps |

[corpus:liquipedia_dota2/armor@2374627#Recent_Changes]

### 7.31 — 2022-02-23

Attack Types and Armor Types are represented through abilities; most damage remains unchanged. The following attack-type abilities were added:

| Ability | Effect |
|---|---|
| Runty | `25%` and `30%` attack-damage reduction against Heroes and Reinforced units, respectively. |
| Piercing | `50%` and `65%` attack-damage reduction against Heroes and Reinforced units, respectively. Deals `50%` more attack damage against Non-Hero units. |
| Reinforced | `50%`, `30%`, and `65%` incoming attack-damage reduction against Heroes, Non-Hero units, and Piercing units, respectively. Deals `50%` more attack damage against other Reinforced units. |

These abilities are not acquirable in any way, including through Devour. The following units have the Piercing ability:

| Unit |
|---|
| Ranged Creep and Mega Ranged Creep |
| Serpent Ward |
| Plague Ward |
| Most neutral creeps with the previous Piercing attack class |

The following units have the Reinforced ability:

| Unit |
|---|
| Siege Creep |
| All buildings |

The following units have the Runty ability:

| Unit |
|---|
| Melee Creep and Mega Melee Creep |

Eidolon, Treant, and Lycan Wolf no longer have the Basic attack class. All neutral creeps have the standard attack type, with their damage adjusted so that net damage is similar. [corpus:liquipedia_dota2/armor@2374627#Recent_Changes]

### 7.27 — 2020-06-28

The Armor formula changed:

| Formula | Expression |
|---|---|
| OLD | `(0.052 × MainArmor)/(0.9 + 0.048 × \|MainArmor\|)` |
| NEW | `(0.06 × MainArmor)/(1 + 0.06 × \|MainArmor\|)` |

[corpus:liquipedia_dota2/armor@2374627#Recent_Changes]