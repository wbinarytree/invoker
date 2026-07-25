# Evasion

Evasion is a mechanic that allows a unit to evade an incoming attack.[corpus:liquipedia_dota2/evasion@2383969] All evasion effects trigger upon landing an attack — upon projectile impact for ranged units, and upon the attack point for melee units.[corpus:liquipedia_dota2/evasion@2383969] When an attack is evaded, any attack or ability effects that rely on attacks hitting their targets do not trigger, including most attack modifiers and on-hit effects unless explicitly specified.[corpus:liquipedia_dota2/evasion@2383969] True Strike and Accuracy are the mechanics that nullify evasion.[corpus:liquipedia_dota2/evasion@2383969]

All evasion sources use pseudo-random distribution.[corpus:liquipedia_dota2/evasion@2383969#Definition]

## Miss feedback

Upon missing an attack on an enemy, a red floating text reading **MISS** appears, visible to the attacking player only, while the enemy that was missed sees a white floating text reading **EVADE**.[corpus:liquipedia_dota2/evasion@2383969#Miss] A missed attack also does not play any of the attack impact sounds.[corpus:liquipedia_dota2/evasion@2383969#Miss]

## Other miss sources

**Melee attack buffer.** For melee units, if the target is farther than 350 range beyond the melee unit's attack range, the attack misses 100% of the time, and True Strike does not guarantee hits on units outside the buffer range.[corpus:liquipedia_dota2/evasion@2383969#Attack_Range_Type] For most melee heroes the buffer is: Total Melee Buffer Range = Unit Total Attack Range + Attacker Bound Radius + Target Bound Radius + 350.[corpus:liquipedia_dota2/evasion@2383969#Attack_Range_Type] The buffer fully affects Instant Attack sources and is negated by neither True Strike nor Accuracy.[corpus:liquipedia_dota2/evasion@2383969#Definition]

**Uphill miss chance.** For ranged units without flying movement, 25% of ranged attacks miss if the attacker is at a lower terrain level than the target, regardless of the size of the terrain level difference.[corpus:liquipedia_dota2/evasion@2383969#Uphill_Miss_Chance] It is checked upon projectile impact rather than at the attack point, so moving up onto elevated ground after a projectile has been launched can cause it to miss even though both units were on the same level when it was fired.[corpus:liquipedia_dota2/evasion@2383969#Uphill_Miss_Chance] A unit counts as being on higher terrain when it is no longer visible to the player due to that terrain, and uphill miss chance applies whether or not the attacked unit is within vision.[corpus:liquipedia_dota2/evasion@2383969#Uphill_Miss_Chance] Uphill miss chance is itself considered an evasion source and does not apply against units with flying movement.[corpus:liquipedia_dota2/evasion@2383969#Uphill_Miss_Chance]

**Blind.** Blind is a debuff applied to the *attacker*, causing it to miss when attacking.[corpus:liquipedia_dota2/evasion@2383969#Blind] Blind sources stack additively with each other, and although a combination can exceed 100%, for effective evasion calculations they cap at 100%.[corpus:liquipedia_dota2/evasion@2383969#Blind] The total blind multiplier then stacks diminishingly with evasion sources.[corpus:liquipedia_dota2/evasion@2383969#Definition]

## Stacking and equations

Multiple evasion sources stack diminishingly with each other, while blind sources stack additively with each other and multiplicatively with evasion.[corpus:liquipedia_dota2/evasion@2383969#Stacking] Evasion, blind, and accuracy are all determined by pseudo-random distribution.[corpus:liquipedia_dota2/evasion@2383969#Equations]

Accuracy and blind do not directly change the attacked unit's evasion value; instead they raise (blind) or lower (accuracy) its effective evasion rate.[corpus:liquipedia_dota2/evasion@2383969#Equations]

- Total Evasion = 1 − ∏(1 − Evasion*ᵢ*)[corpus:liquipedia_dota2/evasion@2383969#Equations]
- Total Blind = Σ Blind*ᵢ*[corpus:liquipedia_dota2/evasion@2383969#Equations]
- Total Accuracy = 1 − ∏(1 − Accuracy*ᵢ*)[corpus:liquipedia_dota2/evasion@2383969#Equations]
- Effective Evade Chance = (1 − (1 − Total Evasion) × (1 − Total Blind)) × (1 − Melee Buffer Range Miss)[corpus:liquipedia_dota2/evasion@2383969#Equations]
- Final Hit Chance = 1 − Effective Evade Chance × (1 − Total Accuracy)[corpus:liquipedia_dota2/evasion@2383969#Equations]

An equivalent form is Final Hit Chance = Total Accuracy + (1 − Total Accuracy) × (1 − Effective Evade Chance): attacks trigger True Strike at the Total Accuracy rate, and the remaining (1 − Total Accuracy) of attacks are subject to the Effective Evade Chance.[corpus:liquipedia_dota2/evasion@2383969#Final_Hit_Chance]

For an attack to land it must bypass every evasion source in sequence, so stacking evasion multiplies the chances to hit; while the evade chance itself has diminishing returns, each added source increases effective HP against physical attacks more than the last.[corpus:liquipedia_dota2/evasion@2383969#Stacking] For example, applying a 50% evasion source while already having 35% evasion still doubles effective hit points against physical attacks, and any combination of sources individually below 100% also stays below 100%.[corpus:liquipedia_dota2/evasion@2383969#Stacking] Incoming attacks hit a Butterfly wielder 65% of the time, because the item grants 35% evasion.[corpus:liquipedia_dota2/evasion@2383969#Stacking]

## Cleave and splash interaction

Cleave does not affect the primary target and cannot miss against secondary targets, but a missed attack does not cleave at all.[corpus:liquipedia_dota2/evasion@2383969#Cleave_&_Splash] Splash behaves the same way: it cannot miss secondary targets, yet no splash damage is applied within the radius if the attack itself misses.[corpus:liquipedia_dota2/evasion@2383969#Cleave_&_Splash]

## Sources

Evasion causes a unit to evade attacks of all kinds, whereas disjointing only evades projectile-based attacks.[corpus:liquipedia_dota2/evasion@2383969#Sources] Sources granting 100% evasion still stack diminishingly with other evasion sources and remain subject to blind and accuracy multipliers.[corpus:liquipedia_dota2/evasion@2383969#Sources]

100% evasion sources include Arc Warden's Magnetic Field, the Lycan Wolf's Hightail (facet-dependent), and Windranger's Windrun.[corpus:liquipedia_dota2/evasion@2383969#Sources] Partial evasion sources include Brewmaster's Drunken Brawler (Storm Stance), Mirana's Moonlight Shadow (talent), Naga Siren's Eelskin, Phantom Assassin's Immaterial, and Phantom Lancer's Phantom Rush.[corpus:liquipedia_dota2/evasion@2383969#Sources]

### Items

| Item | Evasion | Cost | Cost per point |
|---|---|---|---|
| Butterfly | 35% | 5450 | 155.71 |
| Heaven's Halberd | 25% | 3400 | 136 |
| Radiance | 25% | 4700 | 188 |
| Talisman of Evasion | 15% | 1300 | 86.67 |

These values do not include portions from actives or auras.[corpus:liquipedia_dota2/evasion@2383969#Items]

### Talents

Evasion talents grant the hero evasion that stacks multiplicatively with other evasion sources, with values of 8%/10%/12%/15%/16%/20%/25%/30%/40%/50%/75% depending on the talent.[corpus:liquipedia_dota2/evasion@2383969#Talents]

## Accuracy and True Strike

Accuracy is applied as a debuff on the affected target and does not directly increase that unit's evasion value; for calculation purposes the accuracy multiplier can be treated as an evasion source, and True Strike sources can be considered outgoing accuracy.[corpus:liquipedia_dota2/evasion@2383969#Accuracy] Multiple accuracy sources stack diminishingly with each other.[corpus:liquipedia_dota2/evasion@2383969#Equations] A 100% accuracy source prevents all incoming attacks from being missed, while non-100% sources are treated as chance-based True Strike.[corpus:liquipedia_dota2/evasion@2383969#Definition]

True Strike prevents a unit's attacks from missing, negating both evasion and blind against the target — including ward-type and allied units — but not against buildings, and it does not apply an accuracy debuff to the attacked unit.[corpus:liquipedia_dota2/evasion@2383969#True_Strike] Ranged attack projectiles with True Strike can still be disjointed.[corpus:liquipedia_dota2/evasion@2383969#True_Strike] For melee units, True Strike also prevents a miss when the target moves more than 350 range away upon the attack point.[corpus:liquipedia_dota2/evasion@2383969#True_Strike] All attacks against runes and destroyable items have True Strike, and spell damage-based attacks ignore evasion and blind entirely.[corpus:liquipedia_dota2/evasion@2383969#True_Strike]

### Proc-based outgoing accuracy

Attacks that proc these effects gain True Strike: Drow Ranger's Marksmanship at 30/35/40 (+10% talent), Javelin's Pierce at 25%, Maelstrom and Mjollnir's Chain Lightning at 25%, Bloodthorn's Pierce at 40%, and Monkey King Bar's Pierce at 80%.[corpus:liquipedia_dota2/evasion@2383969#Outgoing]

Chance-based outgoing accuracy sources instead grant attacks a chance to not miss: Fountain Damage at 25% accuracy, Ancient Rumblehide's War Drums Aura at 25 accuracy, and Witch Doctor's Death Ward and Voodoo Switcheroo at 50% accuracy — the latter's increased accuracy does not apply to bounces.[corpus:liquipedia_dota2/evasion@2383969#Outgoing]

### Incoming accuracy

Incoming accuracy debuffs come from Bloodthorn's Soul Rend, Meepo's Earthbind (talent), and planted Observer and Sentry Wards.[corpus:liquipedia_dota2/evasion@2383969#Incoming]

## Recent changes

- **7.22e (2019-07-14):** Uphill Miss Chance and the blind sources Incapacitating Bite, Blinding Light, Burn, Sand Storm, Smoke Screen and Whirling Axes (Melee) began using pseudo-random distribution.[corpus:liquipedia_dota2/evasion@2383969#Recent_Changes]
- **7.20 (2018-11-19):** Shine no longer grants 40% outgoing accuracy against the affected target; Fountain Damage attacks gained 25% accuracy.[corpus:liquipedia_dota2/evasion@2383969#Recent_Changes]
- **7.07 (2017-10-31):** Pierce sources began granting attacks True Strike upon proc, and Solar Crest's outgoing accuracy was increased from 35% to 40%.[corpus:liquipedia_dota2/evasion@2383969#Recent_Changes]