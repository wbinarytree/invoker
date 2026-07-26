---
title: Health
kind: concept
patch: 7.41d
card:
  entity: health
  sentences:
  - text: 'Health, or HP (health points), is a unit’s life force: a unit dies at 0
      current health, every hero has an unalterable 120HP base pool, and each strength
      point grants 22HP.'
    marks:
    - corpus:liquipedia_dota2/health@2400187
  - text: Total hero health is defined as `Base Health + 22 × (Base Strength + (Level
      - 1) × ⌊Strength Gain⌋ ± Bonus Strength) ± Flat Bonus Health Values × % Bonus
      Current/Max Health Values`.
    marks:
    - corpus:liquipedia_dota2/health@2400187
  - text: The HUD shows the selected unit’s current health at center-left and maximum
      health at center-right, rounding both visible values up.
    marks:
    - corpus:liquipedia_dota2/health@2400187#HUD_Health_Bar
  - text: Healing increases current health but cannot raise it beyond maximum health.
    marks:
    - corpus:liquipedia_dota2/health@2400187#Healing
  - text: Damage reduces current health, with damage types behaving differently against
      defenses such as armor and magic resistance.
    marks:
    - corpus:liquipedia_dota2/health@2400187#Damaging
  - text: Minimum Health keeps health from falling below a configured value but does
      not prevent instant-kill sources such as Culling Blade.
    marks:
    - corpus:liquipedia_dota2/health@2400187#Min_Health
  - text: Directly setting health is registered as neither healing nor damage, so
      effects reacting to either ignore it.
    marks:
    - corpus:liquipedia_dota2/health@2400187#Setting_Health
  - text: Changing maximum health through means other than strength usually preserves
      current-health percentage, so no healing occurs.
    marks:
    - corpus:liquipedia_dota2/health@2400187#Maximum_Health_Affecting_Abilities
  - text: Heal manipulation amplifies or reduces healing effects and applies to every
      ability listed as healing.
    marks:
    - corpus:liquipedia_dota2/health@2400187#Heal_Manipulation
  - text: Health Freeze prevents healing and health restoration while still registering
      their values for on-heal effects.
    marks:
    - corpus:liquipedia_dota2/health@2400187#Health_Freezing
  - text: Only health gain classified as healing or health regeneration triggers on-heal
      effects; setting health does not.
    marks:
    - corpus:liquipedia_dota2/health@2400187#On-heal_Effects
  - text: Health Regeneration restores health each second, and each strength point
      adds 0.1HP of health regeneration.
    marks:
    - corpus:liquipedia_dota2/health@2400187#Health_Regeneration
---

# Health

Health, or HP (health points), represents a unit’s life force. A unit dies when its current health reaches 0. Every hero has an unalterable base health pool of 120HP, so maximum health cannot fall below 120HP. Each strength point grants 22HP; heroes therefore gain health through strength and strength growth while leveling. Base strength cannot fall below 1, although negative bonus strength can produce 0 strength. [corpus:liquipedia_dota2/health@2400187]

Total hero health is defined as:

```text
Base Health
+ 22 × (Base Strength + (Level - 1) × ⌊Strength Gain⌋ ± Bonus Strength)
± Flat Bonus Health Values
× % Bonus Current/Max Health Values
```

[corpus:liquipedia_dota2/health@2400187]

## Display

A unit’s health is displayed in the game world and again in the HUD when the unit is selected. The green bar shows health, and the number on its right shows health regeneration. [corpus:liquipedia_dota2/health@2400187#Display]

### HUD health bar

The selected unit’s health appears at the bottom of the HUD as a green bar, or blue in colorblind mode; all HUD health bars become blue in that mode. The center-left number is current health and the center-right number is maximum health. Total health uses decimal numbers internally, but the HUD always rounds the visible values up. Health regeneration is also shown for every unit: although only one decimal is displayed and rounded up, the underlying value uses more decimals. [corpus:liquipedia_dota2/health@2400187#HUD_Health_Bar]

### Overhead health bars

Every unit has a health bar above its head. Unlike HUD bars, overhead colors depend on alliances: allied units are green and enemies, including neutral creeps, are red. Neutral creeps are ocher for spectators. In colorblind mode, allied and the player’s own overhead bars are blue. With Differentiate Ally Healthbars enabled, allied bars are ocher while the player’s own bar remains green. [corpus:liquipedia_dota2/health@2400187#Over-head_Health_Bar]

There are 4 health-bar types—hero, creep-hero, building, and creep—which differ in shade, size, and smaller details. Hero and creep-hero bars have vertical divisions: by default, thin lines mark every 250HP and thick lines every 1000HP. Most display options can be configured with the `dota_health_per_vertical_marker` console command. [corpus:liquipedia_dota2/health@2400187#Over-head_Health_Bar]

| Unit or structure | Health-bar appearance |
|---|---|
| Heroes | Bright green or red, segmented by lines; by default, thin lines mark every 250HP and thick lines every 1000HP. They have a level plate on the right and a thick border. |
| Creep-heroes | Identical to hero bars except for darker green and red tones and no level plate. |
| Creeps | Smaller, with the same darker green and red tones as creep-heroes, and no lines. |
| Neutral creeps | The same as other creep bars, but ocher instead of red in spectator mode. |
| Roshan | The same type as other creep bars, but much bigger and with a brighter red similar to heroes; ocher for spectators. |
| Couriers | Brighter than creep bars but darker than hero bars, with the default courier icon on the left. |
| Both ancients | Very large, brightly colored bars with thicker bars and borders. A shield icon appears while Backdoor Protection is enabled. |
| Towers and barracks | Short, brightly colored bars; tower bars are shorter than barracks bars. A shield icon appears while Backdoor Protection is enabled. |
| Effigy buildings | Very short, dark-colored bars. They never show the backdoor-protection icon, even when it is enabled. |

[corpus:liquipedia_dota2/health@2400187#Over-head_Health_Bar]

## Modifying health

Some heroes, units—including neutral creeps and summoned units—and items possess abilities that affect current or maximum health. [corpus:liquipedia_dota2/health@2400187#Modifying_Health]

### Healing

Increasing current health is generally called healing. Healing cannot raise health beyond maximum health. A spell may restore health in one burst or over time through multiple instances. Unlike regeneration, healing is independent of regeneration ticks, its intervals can vary, and it does not appear in the health-regeneration number. [corpus:liquipedia_dota2/health@2400187#Healing]

Besides lifesteal and spell lifesteal, the following sources heal units:

| Source | Ability |
|---|---|
| Abaddon | Mist Coil |
| Abaddon | Borrowed Time — requires Aghanim’s Scepter |
| Bloodseeker | Thirst |
| Chen | Hand of God |
| Clinkz | Death Pact |
| Dark Seer | Ion Shell — requires Aghanim’s Scepter |
| Dawnbreaker | Luminosity |
| Dazzle | Shadow Wave |
| Dazzle | Shadow Grave — requires talent |
| Death Prophet | Spirit Siphon |
| Enchantress | Enchant |
| Enchantress | Nature’s Attendants |
| Faceless Void | Time Walk |
| Hill Troll Priest | Heal |
| Io | Tether |
| Lone Druid | True Form |
| Meepo | Ransack |
| Meepo | Dig |
| Necrophos | Death Pulse |
| Necrophos | Death Seeker |
| Night Stalker | Hunter in the Night |
| Omniknight | Purification |
| Oracle | Purifying Flames |
| Oracle | Rain of Destiny |
| Oracle | False Promise |
| Phoenix | Sun Ray |
| Pudge | Dismember |
| Pugna | Nether Ward — requires Aghanim’s Shard |
| Pugna | Life Drain |
| Shadow Demon | Demonic Cleanse |
| Shadow Fiend | Requiem of Souls — requires Aghanim’s Scepter |
| Snapfire | Firesnap Cookie — requires Aghanim’s Shard |
| Treant Protector | Leech Seed |
| Treant Protector | Living Armor |
| Undying | Soul Rip |
| Visage | Gravekeeper’s Cloak — requires Aghanim’s Shard |
| Warlock | Shadow Word |
| Winter Wyvern | Cold Embrace |
| Witch Doctor | Voodoo Restoration |
| Cheese | Fondue |
| Faerie Fire | Imbue |
| Guardian Greaves | Mend |
| Holy Locket | Energy Charge |
| Magic Stick | Energy Charge |
| Magic Wand | Energy Charge |
| Mekansm | Restore |
| Runes | Water |
| Buildings | Backdoor Protection |

[corpus:liquipedia_dota2/health@2400187#Healing]

| Healing source with creep penalty | Ability |
|---|---|
| Beastmaster | Drums of Slom |
| Bloodseeker | Sanguivore 5 |
| Shadow Fiend | Requiem of Souls 2a |
| Tinker | March of the Machines 3 |
| Outworld Destroyer | Astral Imprisonment 3 |

[corpus:liquipedia_dota2/health@2400187#Healing]

The following sources heal according to damage dealt, so damage amplification or reduction changes the healing value. The resulting heal remains subject to heal manipulation. [corpus:liquipedia_dota2/health@2400187#Healing]

| Source | Ability |
|---|---|
| Bane | Brain Sap |
| Death Prophet | Crypt Swarm (Exorcism Spirits) — requires Aghanim’s Scepter |
| Death Prophet | Silence (Exorcism Spirits) — requires Aghanim’s Scepter |
| Death Prophet | Spirit Siphon (Exorcism Spirits) — requires Aghanim’s Scepter |
| Death Prophet | Exorcism |
| Keeper of the Light | Illuminate (Spirit Form) |

The requirement markers used by these healing lists are: `1` requires a talent, `2a` requires Aghanim’s Scepter, and `2b` requires Aghanim’s Shard. [corpus:liquipedia_dota2/health@2400187#Healing]

Several other abilities increase current health without counting as healing. Like damage flagged as HP Removal ignoring on-damage effects, these effects completely ignore abilities that react to healing, including Ice Blast, False Promise, and Tether. [corpus:liquipedia_dota2/health@2400187#Healing]

### Minimum health

Minimum Health prevents death by manipulating health rather than directly reducing or negating damage. `MODIFIER_PROPERTY_MIN_HEALTH` prevents health from falling below its configured value. It does not alter the damage itself: on-damage effects react to the full damage rather than only the amount effectively dealt and can trigger normally. Minimum Health does not prevent instant-kill sources such as Culling Blade. [corpus:liquipedia_dota2/health@2400187#Min_Health]

Its priority is:

```text
Wraith Delay ➤ Shallow Grave / Battle Trance
```

| Source | Ability |
|---|---|
| Dazzle | Shallow Grave |
| Shadow Shaman | Fowl Play |
| Troll Warlord | Battle Trance |
| Wraith King | Wraith Delay — requires Aghanim’s Scepter |

The requirement markers are: `1` requires a talent, `2a` requires Aghanim’s Scepter, and `2b` requires Aghanim’s Shard. [corpus:liquipedia_dota2/health@2400187#Min_Health]

### Damaging

Damage reduces current health. Unlike healing, damage has multiple types that behave differently according to a unit’s defenses, principally armor and magic resistance. [corpus:liquipedia_dota2/health@2400187#Damaging]

### Setting health

Health can be directly set to particular values instead of being healed or damaged. This is registered as neither healing nor damage and is ignored by effects reacting to either. Setting health can never be lethal or raise health beyond maximum health. When the following abilities are cast with less health than their health cost, the caster is reduced to 1HP. [corpus:liquipedia_dota2/health@2400187#Setting_Health]

HP Removal is different from setting health: it remains damage, but is flagged to bypass several, though not all, on-damage effects and can still be lethal. [corpus:liquipedia_dota2/health@2400187#Setting_Health]

| Health-setting source | Ability |
|---|---|
| Armlet of Mordiggian | Unholy Strength |
| Chen | Holy Persuasion |
| Dazzle | Bad Juju |
| Enigma | Demonic Summoning |
| Enigma | Midnight Pulse |
| Helm of the Dominator | Dominate |
| Helm of the Overlord | Dominate |
| Huskar | Burning Spear |
| Lifestealer | Infest |
| Lone Druid | True Form |
| Morphling | Attribute Shift (Agility Gain) |
| Morphling | Attribute Shift (Strength Gain) |
| Phoenix | Icarus Dive |
| Phoenix | Fire Spirits |
| Phoenix | Sun Ray |
| Phoenix | Supernova |
| Soul Ring | Sacrifice |
| Terrorblade | Sunder |
| Terrorblade | Demon Zeal |
| Timbersaw | Whirling Death |
| Tinker | Laser |
| Undying | Decay |
| Undying | Soul Rip |
| Undying | Flesh Golem |
| Weaver | Time Lapse |

[corpus:liquipedia_dota2/health@2400187#Setting_Health]

### Maximum-health-affecting abilities

Maximum health can be changed through means other than strength. Usually, changing maximum health this way preserves the unit’s current-health percentage so no healing occurs. Strength sources are excluded from the following list. [corpus:liquipedia_dota2/health@2400187#Maximum_Health_Affecting_Abilities]

| Source | Ability |
|---|---|
| Ancient Granite Golem | Granite Aura |
| Chen | Holy Persuasion |
| Clinkz | Death Pact |
| Dark Seer | Ion Shell — requires Aghanim’s Scepter |
| Enchantress | Enchant |
| Helm of the Dominator | Dominate |
| Helm of the Overlord | Dominate |
| Io | Tether — requires talent |
| Lifestealer | Infest |
| Lone Druid | True Form |
| Roshan | Strength of the Immortal |
| Tinker | Laser — requires Aghanim’s Scepter |

The requirement markers are: `1` requires a talent, `2a` requires Aghanim’s Scepter, and `2b` requires Aghanim’s Shard. [corpus:liquipedia_dota2/health@2400187#Maximum_Health_Affecting_Abilities]

### Items

Items can increase their equipped owner’s maximum health through strength, a flat bonus, or both. In every case, current-health percentage remains unchanged. These effects are limited to the item’s owner while the item is equipped. [corpus:liquipedia_dota2/health@2400187#Items]

#### Flat-rate and strength health

| Item | Value | Item Cost | Cost/Value Point |
|---|---:|---:|---:|
| Aghanim’s Scepter | 395 | 4200 | 10.63 |
| Bracer | 160 | 505 | 3.16 |
| Consecrated Wraps | 360 | 2600 | 7.22 |
| Crella’s Crozier | 582 | 4800 | 8.25 |
| Hurricane Pike | 530 | 4450 | 8.4 |
| Khanda | 626 | 5600 | 8.95 |

Values exclude portions from actives or auras. [corpus:liquipedia_dota2/health@2400187#Items]

#### Flat-rate health

| Item | Value | Item Cost | Cost/Value Point |
|---|---:|---:|---:|
| Aeon Disk | 250 | 3000 | 12 |
| Blood Grenade | 50 | 50 | 1 |
| Bloodstone | 625 | 4700 | 7.52 |
| Brawny Enchantment | 0 | N/A | N/A |
| Crimson Guard | 250 | 3725 | 14.9 |
| Falcon Blade | 200 | 1125 | 5.63 |
| Fluffy Hat | 125 | 250 | 2 |
| Force Staff | 175 | 2200 | 12.57 |
| Gleipnir | 450 | 4650 | 10.33 |
| Hulking Enchantment | Expression error: Unexpected `<` operator. | N/A | N/A |
| Octarine Core | 450 | 4900 | 10.89 |
| Pavise | 175 | 1350 | 7.71 |
| Point Booster | 175 | 1200 | 6.86 |
| Rod of Atos | 275 | 2250 | 8.18 |
| Solar Crest | 200 | 2575 | 12.88 |
| Soul Booster | 425 | 3000 | 7.06 |
| Vanguard | 250 | 1700 | 6.8 |
| Veil of Discord | 175 | 1700 | 9.71 |
| Vitality Booster | 250 | 1000 | 4 |

Values exclude portions from actives or auras. [corpus:liquipedia_dota2/health@2400187#Items]

#### Strength health

| Item | Value | Item Cost | Cost/Value Point |
|---|---:|---:|---:|
| Abyssal Blade | 572 | 6250 | 10.93 |
| Belt of Strength | 132 | 450 | 3.41 |
| Black King Bar | 220 | 4050 | 18.41 |
| Boots of Bearing | 176 | 4225 | 24.01 |
| Circlet | 44 | 155 | 3.52 |
| Crown | 88 | 450 | 5.11 |
| Diadem | 132 | 1000 | 7.58 |
| Dragon Lance | 220 | 1900 | 8.64 |
| Drum of Endurance | 176 | 1625 | 9.23 |
| Echo Sabre | 330 | 2700 | 8.18 |
| Essence Distiller | 66 | 1775 | 26.89 |
| Ethereal Blade | 528 | 5200 | 9.85 |
| Eye of Skadi | 770 | 5900 | 7.66 |
| Gauntlets of Strength | 66 | 140 | 2.12 |
| Ghost Scepter | 110 | 1500 | 13.64 |
| Harpoon | 550 | 4700 | 8.55 |
| Heart of Tarrasque | 880 | 5100 | 5.8 |
| Helm of the Dominator | 132 | 2550 | 19.32 |
| Helm of the Overlord | 462 | 5650 | 12.23 |
| Holy Locket | 154 | 2250 | 14.61 |
| Hydra’s Breath | 330 | 5900 | 17.88 |
| Iron Branch | 22 | 55 | 2.5 |
| Kaya and Sange | 352 | 4200 | 11.93 |
| Linken’s Sphere | 352 | 4800 | 13.64 |
| Magic Wand | 66 | 460 | 6.97 |
| Manta Style | 220 | 4650 | 21.14 |
| Meteor Hammer | 132 | 2850 | 21.59 |
| Null Talisman | 44 | 505 | 11.48 |
| Ogre Axe | 220 | 1000 | 4.55 |
| Overwhelming Blink | 550 | 6800 | 12.36 |
| Phylactery | 132 | 2600 | 19.7 |
| Power Treads (Strength) | 220 | 1400 | 6.36 |
| Reaver | 550 | 2800 | 5.09 |
| Sange | 352 | 2100 | 5.97 |
| Sange and Yasha | 352 | 4200 | 11.93 |
| Satanic | 550 | 5050 | 9.18 |
| Skull Basher | 220 | 2875 | 13.07 |
| Soul Ring | 132 | 805 | 6.1 |
| Spirit Vessel | 220 | 2725 | 12.39 |
| Ultimate Orb | 330 | 2800 | 8.48 |
| Urn of Shadows | 44 | 825 | 18.75 |
| Wraith Band | 44 | 505 | 11.48 |

Values exclude portions from actives or auras. [corpus:liquipedia_dota2/health@2400187#Items]

### Talents

The Health talent is passive, affects self, and has a varying health bonus. It increases maximum-health capacity while preserving current-health percentage and uses a hidden modifier. Its possible values are:

```text
100/125/150/175/200/225/250/275/300/325/350/375/400/450/475/500/600/650/700/800/900/1000
```

[corpus:liquipedia_dota2/health@2400187#Talents]

Flat health-bonus talents are organized by Level 10, Level 15, Level 20, and Level 25, each with Left and Right positions. The listed Health bonuses are:

| Health bonus |
|---:|
| +200 |
| +200 |
| +200 |
| +200 |
| +150 |
| +175 |
| +200 |
| +200 |
| +200 |
| +250 |
| +300 |
| +350 |
| +250 |
| +250 |
| +250 |
| +325 |
| +500 |
| +300 |
| +400 |

[corpus:liquipedia_dota2/health@2400187#Talents]

The following talents increase the health of specified summoned or controlled units:

| Hero and talent position | Talent | Affected units |
|---|---|---|
| Brewmaster — Level 20 Right | -12s Primal Split Cooldown | Earth, Storm, and Fire |
| Beastmaster — Level 20 Left | +250 Max Health to Beastmaster and His Units | All units under Beastmaster’s control, including himself |
| Broodmother — Level 25 Left | +7% Spin Web Move Speed Unlocks Max Move Speed | Spiderlings, and Spiderites |
| Nature’s Prophet — Level 25 Left | ×3 Treant Health/Damage | Treants, and Greater Treants |
| Pugna — Level 15 Left | +250 Health | Nether Ward |
| Shadow Shaman — Level 20 Left | x1.5 Serpent Ward Hit Count | Mass Serpent Wards |
| Venomancer — Level 25 Left | 2.5x Plague Ward Health/Damage | Plague Wards |

[corpus:liquipedia_dota2/health@2400187#Talents]

## Heal manipulation

Heal manipulation is amplification or reduction applied to healing effects and affects every ability listed under healing. [corpus:liquipedia_dota2/health@2400187#Heal_Manipulation]

| Category | Source |
|---|---|
| Heal Manipulation | Chen – Divine Favor |
| Heal Manipulation | Dazzle – Shallow Grave |
| Heal Manipulation | Necrophos – Ghost Shroud |
| Heal Manipulation | Oracle – Rain of Destiny (Ally) |
| Heal Manipulation | Pugna – Decrepify (Ally) |
| Heal Manipulation | Hill Troll Priest – Heal Amplification Aura |
| Incoming Healing Decrease | Oracle – Rain of Destiny (Enemy) |
| Outgoing Healing Increase | Holy Locket – Holy Blessing |

The requirement markers are: `1` requires a talent, `2a` requires Aghanim’s Scepter, and `2b` requires Aghanim’s Shard. [corpus:liquipedia_dota2/health@2400187#Heal_Manipulation]

### Health freezing

Health Freeze prevents all healing and health-restoration effects from applying to a unit. Their values are still registered and can trigger on-heal effects. [corpus:liquipedia_dota2/health@2400187#Health_Freezing]

| Source | Duration | Effect |
|---|---|---|
| Ancient Apparition – Ice Blast | 12/24/46 ( ) | The debuff prevents affected units’ current health from increasing. |
| Doom – Doom | 12/14/16 | The debuff silences and prevents affected units’ current health from increasing. |
| Oracle – False Promise | 7/8.5/10 ( 8.5/10/11.5) | Also negates all damage taken for the duration. |

[corpus:liquipedia_dota2/health@2400187#Health_Freezing]

## On-heal effects

Some abilities react when a unit is healed or regenerates health, similarly to abilities that react when a unit takes damage. Only health gain classified as healing or health regeneration triggers on-heal effects; other health gains, such as setting health, do not. [corpus:liquipedia_dota2/health@2400187#On-heal_Effects]

| Ability | Reaction |
|---|---|
| Io – Tether | Whenever the caster is healed or regenerates health, it heals the tethered ally by a percentage of the healing and regeneration received by the caster. |
| Oracle – False Promise | Registers only actual healing and regeneration and ignores other ways of gaining health. |

[corpus:liquipedia_dota2/health@2400187#On-heal_Effects]

## Abilities modified by health

### Maximum-health-based effects

The following abilities have effects based on maximum health:

| Source | Ability |
|---|---|
| Aegis of the Immortal | Reincarnation Expire Regeneration |
| Aeon Disk | Combo Breaker |
| Ancient Apparition | Ice Blast |
| Bloodseeker | Bloodrage |
| Bloodseeker | Thirst |
| Clinkz | Death Pact |
| Doom | Infernal Blade |
| Elder Titan | Earth Splitter |
| Enigma | Black Hole — requires Aghanim’s Shard |
| Fountain | Rejuvenation Aura |
| Guardian Greaves | Guardian Aura |
| Huskar | Berserker’s Blood |
| Heart of Tarrasque | Max Health as Health Regen |
| Io | Overcharge |
| Jakiro | Liquid Frost |
| Juggernaut | Healing Ward |
| Lifestealer | Feast |
| Lifestealer | Open Wounds |
| Lifestealer | Infest |
| Lone Druid | Summon Spirit Bear |
| Necrophos | Heartstopper Aura |
| Nyx Assassin | Burrow |
| Phantom Assassin | Fan of Knives |
| Phoenix | Sun Ray |
| Pudge | Dismember — requires Aghanim’s Shard |
| Runes | Regeneration |
| Techies | Blast Off! |
| Tinker | Laser — requires Aghanim’s Scepter |
| Timbersaw | Chakram |
| Timbersaw | Second Chakram |
| Underlord | Firestorm |
| Undying Zombie | Deathlust |
| Winter Wyvern | Cold Embrace |
| Witch Doctor | Voodoo Restoration — requires talent |

The requirement markers are: `1` requires a talent, `2a` requires Aghanim’s Scepter, and `2b` requires Aghanim’s Shard. [corpus:liquipedia_dota2/health@2400187#Max_Health_Based]

### Current-health-based effects

Illusions have current health and mana based on the current health and mana of the unit on which they are based. The following abilities also have effects based on current health: [corpus:liquipedia_dota2/health@2400187#Current_Health_Based]

| Source | Ability |
|---|---|
| Bloodseeker | Rupture |
| Enigma | Midnight Pulse |
| Huskar | Burning Spear |
| Huskar | Life Break |
| Legion Commander | Overwhelming Odds |
| Phoenix | Fire Spirits |
| Phoenix | Icarus Dive |
| Phoenix | Sun Ray |
| Terrorblade | Demon Zeal |
| Tinker | Laser — requires Aghanim’s Scepter |
| Winter Wyvern | Arctic Burn |

The requirement markers are: `1` requires a talent, `2a` requires Aghanim’s Scepter, and `2b` requires Aghanim’s Shard. [corpus:liquipedia_dota2/health@2400187#Current_Health_Based]

### Other health-based effects

The following abilities have other health-based effects, mostly involving health thresholds:

| Ability | Health-based value or rule | Effect |
|---|---|---|
| Abaddon – Borrowed Time | Passive Health Threshold: 100% | Automatically activates when taking damage while below the health threshold. |
| Axe – Culling Blade | Kill Health Threshold: ( ) | Instantly kills targets below the health threshold. |
| Necrophos – Reaper’s Scythe | Damage per Missing Health: 1.5 | Deals damage according to how much health the target is missing. |
| Razor – Eye of the Storm | Lowest health | The storm targets the enemy with the lowest health in its range. |
| Witch Doctor – Maledict | Lost Health as Burst Damage: ( ) | Every seconds, hit enemies take damage based on how much health they have lost since the curse began. Nothing happens if their current health is higher than it was when the curse began. |

[corpus:liquipedia_dota2/health@2400187#Other_Health_Based_Effects]

## Health regeneration

Health Regeneration determines how much health a unit regains each second. It appears as a small number with a `+` sign on the right side of the unit’s health bar. Heroes also receive health regeneration from strength: each strength point increases health regeneration by 0.1HP. [corpus:liquipedia_dota2/health@2400187#Health_Regeneration]

## Recent changes

| Version | Date | Change |
|---|---|---|
| 7.33 | 2023-04-20 | Reduced hero base health from 200 to 120. |
| 7.33 | 2023-04-20 | Increased health bonus per strength from 20 to 22. |
| 7.33 | 2023-04-20 | Added special health bars displaying the hero attacks required to destroy ward-type units. |
| 7.27 | 2020-06-28 | Heal manipulation now stacks multiplicatively instead of additively. |
| 7.27 | 2020-06-28 | Health regen manipulation now stacks multiplicatively instead of additively. |
| 7.27 | 2020-06-28 | Lifesteal manipulation now stacks multiplicatively instead of additively. |
| 7.27 | 2020-06-28 | Spell lifesteal manipulation now stacks multiplicatively instead of additively. |
| 7.26a | 2020-04-21 | Fixed heal manipulation to disallow negative heal values. |
| 7.26a | 2020-04-21 | Fixed health regen manipulation to disallow negative health-regeneration values. |
| 7.26a | 2020-04-21 | Fixed lifesteal manipulation to disallow negative lifesteal values. |

[corpus:liquipedia_dota2/health@2400187#Recent_Changes]