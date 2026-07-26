---
title: Spell Redirection
kind: concept
patch: 7.41d
card:
  entity: spell_redirection
  sentences:
  - text: Spell Redirection is a mechanic that redirects an offensive unit-targeted
      ability from its intended targeted unit to another unit.
    marks:
    - corpus:liquipedia_dota2/spell_redirection@2357986
  - text: Spell Block, Spell Reflection, and Spell Redirection work independently
      of each other.
    marks:
    - corpus:liquipedia_dota2/spell_redirection@2357986#Definition
  - text: The mechanic shares the offensive ability and its effects on the intended
      enemy target with an allied unit.
    marks:
    - corpus:liquipedia_dota2/spell_redirection@2357986#Mechanics
  - text: Most shared abilities ignore cast range on the secondary target while retaining
      their ability notes and restrictions.
    marks:
    - corpus:liquipedia_dota2/spell_redirection@2357986#Mechanics
  - text: The ability visually casts simultaneously on both targets but always casts
      on the primary target first.
    marks:
    - corpus:liquipedia_dota2/spell_redirection@2357986#Mechanics
  - text: Spell Redirection does not additionally proc on-cast effects.
    marks:
    - corpus:liquipedia_dota2/spell_redirection@2357986#Mechanics
  - text: Redirected spells remain subject to Spell Block and Spell Reflection but
      not to other Spell Redirection sources.
    marks:
    - corpus:liquipedia_dota2/spell_redirection@2357986#Mechanics
  - text: For channeling abilities, Spell Redirection sources proc for the primary
      and secondary targets simultaneously.
    marks:
    - corpus:liquipedia_dota2/spell_redirection@2357986#Mechanics
  - text: Each Spell Redirection source proc consumes a single charge per ability
      cast.
    marks:
    - corpus:liquipedia_dota2/spell_redirection@2357986#Mechanics
  - text: Active attack modifiers and creep ability casts do not proc Spell Redirection
      sources.
    marks:
    - corpus:liquipedia_dota2/spell_redirection@2357986#Mechanics
  - text: Grimstroke’s Soulbind applies the spell to the second target even if the
      main target blocked it.
    marks:
    - corpus:liquipedia_dota2/spell_redirection@2357986#Spell_Redirect_Sources
  - text: Spirit Breaker’s Planar Pocket has higher priority than Spell Block and
      Spell Reflection.
    marks:
    - corpus:liquipedia_dota2/spell_redirection@2357986#Spell_Redirect_Sources
---

# Spell Redirection

Spell Redirection redirects an offensive unit-targeted ability from the intended targeted unit to another unit. [corpus:liquipedia_dota2/spell_redirection@2357986]

## Definition

| Mechanic type | Definition | Example |
|---|---|---|
| Spell Block | Blocks the offensive unit-targeted ability. | Spellblock [corpus:liquipedia_dota2/spell_redirection@2357986#Definition] |
| Spell Reflection | Reflects the offensive unit-targeted ability from the targeted unit to its caster. | Echo Shell [corpus:liquipedia_dota2/spell_redirection@2357986#Definition] |
| Spell Redirection | Redirects the unit-targeted ability from the intended targeted unit to another unit. | Soulbind [corpus:liquipedia_dota2/spell_redirection@2357986#Definition] |

All three mechanics work independently of each other. [corpus:liquipedia_dota2/spell_redirection@2357986#Definition]

## Mechanics

Spell Redirection sources have the `MODIFIER_PROPERTY_REDIRECT_SPELL` decorator. The mechanic causes the offensive unit-targeted ability and its effects on the intended enemy target to be shared with its allied unit. Upon proc, most shared abilities ignore cast range on the secondary target, with their ability notes and restrictions applied. [corpus:liquipedia_dota2/spell_redirection@2357986#Mechanics]

When the proc conditions are met, the unit-targeted ability is visually cast simultaneously on both the primary and secondary targets, regardless of whether it is projectile-based. However, the ability is always cast on the primary target first. [corpus:liquipedia_dota2/spell_redirection@2357986#Mechanics]

Spell Redirection does not additionally proc on-cast effects. Redirected spells remain subject to Spell Block and Spell Reflection, but not to other Spell Redirection sources. For channeling abilities, Spell Redirection sources proc for the primary and secondary targets simultaneously. Each Spell Redirection source proc consumes a single charge per ability cast. [corpus:liquipedia_dota2/spell_redirection@2357986#Mechanics]

The following do not proc Spell Redirection sources: [corpus:liquipedia_dota2/spell_redirection@2357986#Mechanics]

| Excluded source |
|---|
| Active attack modifiers |
| Creep ability casts |

Clones, illusions, and the Spirit Bear are considered heroes; other creep-heroes are considered creeps. Certain redirected abilities with different interactions against Spell Block and Spell Reflection sources are listed in their respective ability notes. [corpus:liquipedia_dota2/spell_redirection@2357986#Mechanics]

## Spell Redirect Sources

| Source | Interaction |
|---|---|
| Grimstroke — Soulbind | Applies the spell to the second target even if the main target blocked the spell. [corpus:liquipedia_dota2/spell_redirection@2357986#Spell_Redirect_Sources] |
| Spirit Breaker — Planar Pocket | Has a higher priority than Spell Block and Spell Reflection. [corpus:liquipedia_dota2/spell_redirection@2357986#Spell_Redirect_Sources] |

## Recent Changes

Main article: **Spell Redirection/Changelogs**. [corpus:liquipedia_dota2/spell_redirection@2357986#Recent_Changes]