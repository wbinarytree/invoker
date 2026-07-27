---
title: Restoration Manipulation
kind: concept
patch: 7.41d
card:
  entity: restoration_manipulation
  sentences:
  - text: Restoration manipulation amplifies or reduces healing, health regeneration,
      lifesteal, spell lifesteal, mana replenish, and mana regeneration.
    marks:
    - corpus:liquipedia_dota2/restoration_manipulation@2385409
  - text: Heal, health-restoration, mana-replenish, and mana-restoration manipulation
      do not interfere because they affect different sources.
    marks:
    - corpus:liquipedia_dota2/restoration_manipulation@2385409#Stacking
  - text: Heal manipulation affects every ability that heals; incoming and outgoing
      sources stack additively, with a -100% lower cap and no upper cap.
    marks:
    - corpus:liquipedia_dota2/restoration_manipulation@2385409#Heal_Manipulation
  - text: Health-restoration manipulation affects health regeneration, lifesteal,
      and spell lifesteal; amplification and reduction each stack diminishingly before
      being added, with caps of -100% and +100%.
    marks:
    - corpus:liquipedia_dota2/restoration_manipulation@2385409#Health_Restoration_Manipulation
  - text: Health Regen Manipulation is deprecated; amplification stacks additively,
      reduction diminishingly, and the total has a -100% lower cap but no upper cap.
    marks:
    - corpus:liquipedia_dota2/restoration_manipulation@2385409#Health_Regen_Manipulation
  - text: Mana-restoration manipulation affects mana regeneration; incoming and outgoing
      sources stack additively, with caps of -100% and +100%.
    marks:
    - corpus:liquipedia_dota2/restoration_manipulation@2385409#Mana_Restoration_Manipulation
  - text: Mana-replenish manipulation affects sources that replenish mana, and all
      its sources stack additively.
    marks:
    - corpus:liquipedia_dota2/restoration_manipulation@2385409#Mana_Replenish_Manipulation
  - text: Multiple Sange- and Orb of Frost-based restoration amplifications and Kaya-based
      mana-regen amplifications do not stack; the highest value takes priority.
    marks:
    - corpus:liquipedia_dota2/restoration_manipulation@2385409#Stacking_Exceptions
  - text: Attribute Shift counts as HP regeneration and is affected by Health Regen
      Manipulation and Health Restoration, with caps of -100% and 0%.
    marks:
    - corpus:liquipedia_dota2/restoration_manipulation@2385409#Attribute_Shift
  - text: Health Freeze prevents heal and health-restoration effects from applying,
      but their values remain registered and can trigger on-heal effects.
    marks:
    - corpus:liquipedia_dota2/restoration_manipulation@2385409#Health_Freeze
  - text: Health Freeze does not prevent abilities from setting health or granting
      direct health bonuses.
    marks:
    - corpus:liquipedia_dota2/restoration_manipulation@2385409#Health_Freeze
  - text: Version 7.39 on 2025-05-21 consolidated lifesteal, spell-lifesteal, and
      health-regen manipulation into health-restoration manipulation.
    marks:
    - corpus:liquipedia_dota2/restoration_manipulation@2385409#Recent_Changes
---

# Restoration Manipulation

Restoration manipulation encompasses amplification and reduction applied to healing; health restoration, including health regeneration, lifesteal, and spell lifesteal; mana replenish; and mana restoration, including mana regeneration. [corpus:liquipedia_dota2/restoration_manipulation@2385409]

## Restoration Classification

Interaction sequence order: **Heal Manipulation; Health Restoration Manipulation; Mana Restoration Manipulation; Mana Replenish Manipulation**.

| Ability | Interaction sequence |
|---|---|
| Withering Mist | 0 · 2 · 0 · 0 |
| Spin Web | 0 · 0 · 0 |
| Divine Favor | 1 · 0 · 0 |
| Blueheart Floe | 0 · 0 · 0 |
| Pixie Dust | 0 · 1 · 0 |
| Frost Dragon | 0 · 0 · 0 |
| Nothl Boon | 0 · 0 · 0 |
| Shallow Grave | 0 · 0 · 0 |
| Frost Arrows | 0 · 0 · 0 |
| Outfight Them! | 0 · 0 · 0 |
| Dauntless | 0 · 1 · 0 · 0 |
| Heartstopper Aura | 0 · 1 · 0 · 0 |
| Ghost Shroud |  |
| Heart of Darkness | 0 · 1 · 0 · 0 |
| Guardian Angel | 1 · 2 · 0 · 0 |
| Rain of Destiny (Ally) | 0 · 0 · 0 |
| Rain of Destiny (Enemy) | 0 · 0 · 0 |
| Decrepify (Ally) | 0 · 0 · 0 |
| Saltwater Shiv (Self) | 0 · 0 · 0 |
| Saltwater Shiv (Enemy) | 0 · 0 · 0 |
| Rot | 0 · 0 · 0 |
| Poison Sting | 0 · 1 · 0 · 0 |
| Cold Attack | 0 · 0 |
| Holy Blessing | 0 · 0 · 0 |
| Pollinate | 0 · 0 · 0 |
| Kaya | 0 · 0 · 0 |
| Kaya and Sange | 0 · 0 |
| Meteor Hammer | 0 · 0 · 0 |
| Corrosion | 0 · 2 · 0 · 0 |
| Frost | 0 · 2 · 0 · 0 |
| Sange | 0 · 0 · 0 |
| Sange and Yasha | 0 · 0 · 0 |
| Soul Release | 0 · 0 |
| Yasha and Kaya | 0 · 0 · 0 |
| Heal Amplification Aura | 0 · 0 · 0 |
| Envenomed Weapon | 0 · 1 · 0 · 0 |

| Marker | Meaning |
|---|---|
| 1 | Only affect health regeneration, rather than health regen, lifesteal, and spell lifesteal. |
| 2 | Also affects Buildings. |

[corpus:liquipedia_dota2/restoration_manipulation@2385409#Restoration_Classification]

## Stacking

Heal manipulation, health restoration manipulation, mana replenish manipulation, and mana restoration manipulation do not interfere with one another because they affect different sources. [corpus:liquipedia_dota2/restoration_manipulation@2385409#Stacking]

### Heal Manipulation

Sources are summed and then applied to the healing source, stacking additively. Heal manipulation has a lower cap of `-100%`, which completely negates healing, and no upper cap. [corpus:liquipedia_dota2/restoration_manipulation@2385409#Stacking]

### Health Restoration Manipulation

Amplification and reduction sources are calculated separately. Amplifications stack diminishingly with one another, as do reductions. Total health restoration manipulation is the sum of the stacked amplifications and reductions. Its lower cap is `-100%`, completely negating restoration, and its upper cap is `+100%`, doubling restoration. [corpus:liquipedia_dota2/restoration_manipulation@2385409#Stacking]

### Health Regen Manipulation

Amplification and reduction sources are calculated separately. Amplifications stack diminishingly, while reductions stack addictively. Total health regen manipulation is the sum of the stacked amplifications and reductions. Its lower cap is `-100%`, completely negating regeneration, and it has no upper cap. Total Health Regen Manipulation usually stacks addictively with Total Health Restoration. [corpus:liquipedia_dota2/restoration_manipulation@2385409#Stacking]

### Mana Manipulation

Mana restoration manipulation sources are summed and applied to the mana restoration source, stacking additively without an upper or lower cap. Mana replenish manipulation sources are likewise summed and applied to the mana restoration source, stacking additively without an upper or lower cap. [corpus:liquipedia_dota2/restoration_manipulation@2385409#Stacking]

### Mathematical Definition

Let `An` be a list of all amplifcations and `Rm` a list of all reductions, both converted to decimals.

```text
For Heal Manipulation:
Total Heal Manipulation = 1 + max ( nsumi (Ai) - msumj (Rj , -1)

For Health Restoration Manipulation:
Health Restoration Amplifications = x = 1 - nprodi (1 - Ai)
Health Restoration Reductions = y = 1 - mprodj (1 - Rj)
Total Health Restoration Manipulation = 1 + clamp (x - y, -1, 1)

For Mana Restoration Manipulation:
Total Mana Restoration Manipulation = 1 + ( nsumi (Ai) - msumj (Rj )

For Mana Replenish Manipulation:
Total Mana Replenish Manipulation = 1 + ( nsumi (Ai) - msumj (Rj )
```

[corpus:liquipedia_dota2/restoration_manipulation@2385409#Mathematic_Definition]

### Stacking Exceptions

| Multiple-instance source | Rule |
|---|---|
| Sange-based items | Restoration amplification does not stack; the highest value takes priority. |
| Orb of Frost-based items | Restoration amplification does not stack; the highest value takes priority. |
| Kaya-based items | Mana regen amplification does not stack; the highest value takes priority. |

[corpus:liquipedia_dota2/restoration_manipulation@2385409#Stacking_Exceptions]

## Heal Manipulation

Heal manipulation affects every ability that heals a unit. Incoming and outgoing sources stack additively. Total heal manipulation has a lower cap of `-100%` and no upper cap. [corpus:liquipedia_dota2/restoration_manipulation@2385409#Heal_Manipulation]

| Effect | Source |
|---|---|
| Incoming healing increase | Chen – Divine Favor |
| Incoming healing increase | Dazzle – Shallow Grave |
| Incoming healing increase | Necrophos – Ghost Shroud |
| Incoming healing increase | Oracle – Rain of Destiny (Ally) |
| Incoming healing increase | Pugna – Decrepify (Ally) |
| Incoming healing increase | Hill Troll Priest – Heal Amplification Aura |
| Incoming healing decrease | Oracle – Rain of Destiny (Enemy) |
| Outgoing healing increase | Holy Locket – Holy Blessing |

| Marker | Requirement |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |

[corpus:liquipedia_dota2/restoration_manipulation@2385409#Heal_Manipulation]

## Health Restoration Manipulation

Health restoration manipulation affects health regeneration, lifesteal, and spell lifesteal. Amplifications and reductions are calculated separately, each stacking diminishingly, and then added together for the final result. Total health restoration manipulation has a lower cap of `-100%` and an upper cap of `+100%`. [corpus:liquipedia_dota2/restoration_manipulation@2385409#Health_Restoration_Manipulation]

| Effect | Source |
|---|---|
| Increase | Legion Commander – Outfight Them! |
| Increase | Necrophos – Ghost Shroud |
| Increase | Slark – Saltwater Shiv |
| Increase | Kaya and Sange – Health Restoration Amp |
| Increase | Sange – Health Restoration Amp |
| Increase | Sange and Yasha – Health Restoration Amp |
| Decrease | Abaddon – Withering Mist |
| Decrease | Dragon Knight – Frost Dragon3 |
| Decrease | Drow Ranger – Frost Arrows2a |
| Decrease | Necrophos – Ghost Shroud3 |
| Decrease | Pudge – Rot2a |
| Decrease | Slark – Saltwater Shiv |
| Decrease | Eye of Skadi – Cold Attack |
| Decrease | Jidi Pollen Bag – Pollinate |
| Decrease | Orb of Corrosion – Corrosion |
| Decrease | Orb of Frost – Frost |
| Decrease | Spirit Vessel – Soul Release |

| Marker | Requirement |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |

[corpus:liquipedia_dota2/restoration_manipulation@2385409#Health_Restoration_Manipulation]

## Health Regen Manipulation

Health Regen Manipulation is a deprecated mechanic affecting all health regeneration of a unit. Health Regen Reduction stacks diminishingly, while Health Regen Amp stacks additively. Amplifications and reductions are calculated separately and then added together for the final result. Total Health Regen Manipulation has a lower cap of `-100%` and no upper cap, and usually stacks addictively with Total Health Restoration. It explicitly affects the affected unit’s health-regeneration value; despite being deprecated, the following abilities still use it. [corpus:liquipedia_dota2/restoration_manipulation@2385409#Health_Regen_Manipulation]

| Effect | Source |
|---|---|
| Increase | Chen – Divine Favor |
| Increase | Dark Willow – Pixie Dust |
| Increase | Mars – Dauntless |
| Increase | Night Stalker – Heart of Darkness |
| Increase | Omniknight – Guardian Angel2a |
| Decrease | Necrophos – Heartstopper Aura1 |
| Decrease | Venomancer – Poison Sting1 |
| Decrease | Vhoul Assassin – Envenomed Weapon |

| Marker | Requirement |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim's Scepter. Capped at 100% |

[corpus:liquipedia_dota2/restoration_manipulation@2385409#Health_Regen_Manipulation]

### Attribute Shift

Attribute Shift is considered HP regeneration and is affected by Health Regen Manipulation and Health Restoration. Its lower cap is `-100%`, while its higher cap is `0%`. The reduction’s effectiveness directly depends on the percentage of missing HP: if Morphling’s current health is `100%`, HP-gain reduction has no effect, and vice versa. [corpus:liquipedia_dota2/restoration_manipulation@2385409#Attribute_Shift]

```text
Formula for calculating efficiency:
22 - (% total reduction from % missing HP) [?]
```

MAX HP always increases by `22`. Under certain circumstances, each reduced HP gain decreases the percentage of current HP, which causes the next HP gain to decrease even more. [corpus:liquipedia_dota2/restoration_manipulation@2385409#Attribute_Shift]

## Health Freeze

Health Freeze prevents all heal and health-restoration effects from applying to the unit. Their values are still registered and can still trigger on-heal effects. [corpus:liquipedia_dota2/restoration_manipulation@2385409#Health_Freeze]

| Source | Duration and effects |
|---|---|
| Ancient Apparition – Ice Blast | Duration: `12/24/46 ( )`. The debuff prevents affected units’ current health from increasing. |
| Doom – Doom | Duration: `12/14/16`. The debuff silences affected units and prevents their current health from increasing. |
| Oracle – False Promise | Duration: `7/8.5/10 ( 8.5/10/11.5)`. Also negates all damage taken for the duration. |

Health Freeze does not prevent abilities from setting a unit’s health or granting direct health bonuses:

| Health Freeze-ignoring source |
|---|
| Beastmaster – +250 Health Aura 1 |
| Essence Ring – Life Essence |
| Lone Druid – True Form |
| Lycan – Shapeshift |
| Lycan – Wolf Bite |
| Phoenix – Supernova |
| Terrorblade – Sunder |
| Undying – Decay |
| Weaver – Time Lapse |

[corpus:liquipedia_dota2/restoration_manipulation@2385409#Health_Freeze]

## Mana Restoration Manipulation

Mana restoration manipulation affects mana regeneration. All incoming and outgoing sources stack additively. Total mana restoration manipulation has a lower cap of `-100%` and an upper cap of `+100%`. [corpus:liquipedia_dota2/restoration_manipulation@2385409#Mana_Restoration_Manipulation]

| Mana Regen Manipulation source |
|---|
| Crystal Maiden – Blueheart Floe |
| Meteor Hammer – Mana Regen Amp |
| Kaya – Mana Regen Amp |
| Kaya and Sange – Mana Regen Amp |
| Necrophos – Ghost Shroud |
| Necrophos – Ghost Shroud 3 |
| Yasha and Kaya – Mana Regen Amp |

| Marker | Requirement |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |

[corpus:liquipedia_dota2/restoration_manipulation@2385409#Mana_Restoration_Manipulation]

## Mana Replenish Manipulation

Mana replenish manipulation affects sources that replenish a unit’s mana. All mana replenish manipulation sources stack additively with one another. [corpus:liquipedia_dota2/restoration_manipulation@2385409#Mana_Replenish_Manipulation]

| Mana Replenish Manipulation source |
|---|
| Necrophos – Ghost Shroud |
| Necrophos – Ghost Shroud3 |

| Marker | Requirement |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |

[corpus:liquipedia_dota2/restoration_manipulation@2385409#Mana_Replenish_Manipulation]

## Recent Changes

| Version | Date | Changes |
|---|---|---|
| 7.39 | 2025-05-21 | Lifesteal manipulation, spell lifesteal manipulation, and health regen manipulation were summed into health restoration manipulation. It provides a percentage increase or decrease to health regen, lifesteal, and spell lifesteal. Its amplifications and reductions are calculated separately, stack diminishingly, and are then added for the final result. It is capped at `-100%` and `+100%`. Heal manipulation remains independent and affects only what the game considers healing; health regen, lifesteal, and spell lifesteal are not considered healing. Heal manipulation sources now stack additively instead of diminishingly. `[?]` Heal manipulation gained a lower cap of `-100%` and has no upper cap. |
| 7.27 | 2020-06-28 | Lifesteal manipulation no longer affects spell lifesteal. Spell lifesteal manipulation was added as a separate mechanic. Heal manipulation, health regen manipulation, lifesteal manipulation, and spell lifesteal manipulation changed from additive to diminishing stacking. |
| 7.26a | 2020-04-21 | Fixed heal manipulation affecting lifesteal; only lifesteal manipulation now does so. Lifesteal manipulation was added as a separate mechanic. Fixed heal manipulation, health regen manipulation, and lifesteal manipulation to disallow negative heal, health-regeneration, and lifesteal values. Fixed mana restore manipulation and mana regen manipulation to disallow negative mana-restore and mana-regeneration values. |

[corpus:liquipedia_dota2/restoration_manipulation@2385409#Recent_Changes]