---
title: Gold
kind: concept
patch: 7.41d
card:
  entity: gold
  sentences:
  - text: Gold is the currency used to buy items or instantly revive a hero; every
      hero starts with 600 gold, and more is earned by killing heroes, creeps, or
      buildings.
    marks:
    - corpus:liquipedia_dota2/gold@2376164
    - corpus:liquipedia_dota2/gold@2376164#Starting_gold
  - text: 'A player’s gold is divided into reliable and unreliable pools: passive
      income and Bounty Runes are reliable, while other sources are unreliable.'
    marks:
    - corpus:liquipedia_dota2/gold@2376164#Reliable_&_Unreliable_Gold
  - text: Item purchases spend unreliable gold first, whereas buyback spends reliable
      gold first.
    marks:
    - corpus:liquipedia_dota2/gold@2376164#Reliable_&_Unreliable_Gold
  - text: A hero’s net worth is their gold plus the cost of every owned item still
      existing, regardless of where the item is on the map.
    marks:
    - corpus:liquipedia_dota2/gold@2376164#Net_Worth
  - text: Net worth affects buyback cost and the gold gained from hero kills on both
      sides.
    marks:
    - corpus:liquipedia_dota2/gold@2376164#Net_Worth
  - text: Beginning at 0:00, each player receives 1 reliable gold every 0.67 seconds,
      initially 90 gold per minute, with periodic income increasing by 2 per minute
      over time.
    marks:
    - corpus:liquipedia_dota2/gold@2376164#Periodic_Gold
  - text: A Bounty Rune grants 40 base team gold, increases by 6 per instance every
      300 seconds, and has a Turbo Mode multiplier of 2.
    marks:
    - corpus:liquipedia_dota2/gold@2376164#Bounty_Rune
  - text: Hero kills grant the killer unreliable gold with 125 base gold, while the
      first hero killed adds 135 unreliable gold for First Blood.
    marks:
    - corpus:liquipedia_dota2/gold@2376164#Hero_kills
  - text: A kill streak starts at 3 kills, and its shutdown bounty increases with
      each kill through 10 kills but not beyond.
    marks:
    - corpus:liquipedia_dota2/gold@2376164#Kill_Streaks
  - text: Heroes receive unreliable assist gold if they are within 1500 radius of
      the killed enemy or have damaged or debuffed the victim.
    marks:
    - corpus:liquipedia_dota2/gold@2376164#Assists_(AoE_gold)
  - text: Each death removes unreliable gold equal to NetWorth/40, while reliable
      gold is not lost.
    marks:
    - corpus:liquipedia_dota2/gold@2376164#Death
  - text: While dead, a player can instantly respawn at the fountain for `BuybackCost
      = ⌊ ( 200 + NetWorth / 13 ) ⌋`.
    marks:
    - corpus:liquipedia_dota2/gold@2376164#Buyback
---

# Gold

Gold is the currency used to buy items or instantly revive a hero. It is earned by killing heroes, creeps, or buildings. [corpus:liquipedia_dota2/gold@2376164]

## Reliable and unreliable gold

A player’s gold is divided into reliable and unreliable pools.

| Gold type | Sources |
|---|---|
| Reliable | Passive gold received over time; gold from activating Bounty Runes |
| Unreliable | Any other source, including hero kills, creep kills, building destruction, Hand of Midas, and Track |

Death removes only unreliable gold. Item purchases spend unreliable gold before reliable gold, while buyback spends reliable gold first. Hovering over the HUD gold display shows a tooltip with both totals. [corpus:liquipedia_dota2/gold@2376164#Reliable_&_Unreliable_Gold]

## Net worth

A hero’s net worth is the sum of their gold and the cost of every item they own, regardless of where those items are on the map. Consumed or destroyed items do not count because they no longer exist. Besides indicating player performance, net worth unfavorably affects buyback cost and the gold gained from hero kills on both sides. [corpus:liquipedia_dota2/gold@2376164#Net_Worth]

The following items are excluded under the stated conditions:

| Item or category | Condition |
|---|---|
| Items in a unit’s inventory | The unit belongs to the enemy team |
| Gem of True Sight | On the ground |
| Divine Rapier | On the ground; once an enemy of the owner first picks it up, it becomes owned by whoever has it in their inventory |
| Items obtained by randomizing the hero pick | Always excluded |
| Items found by the Trusty Shovel | Always excluded |
| Town Portal Scrolls | Obtained by dying or from Boots of Travel |

If any excluded item is part of an item stack, it is consumed first. [corpus:liquipedia_dota2/gold@2376164#Net_Worth]

Some consumables apply a buff that increases the target’s net worth by the item’s cost when used, preventing the team’s net worth from decreasing:

| Consumable |
|---|
| Moon Shard |
| Aghanim’s Blessing |
| Aghanim’s Blessing - Roshan |
| Aghanim’s Scepter Synth |
| Aghanim’s Shard |
| Aghanim’s Shard - Consumable |

[corpus:liquipedia_dota2/gold@2376164#Net_Worth]

## Acquiring gold

### Starting gold

Every hero begins with **600 gold** and **1 Town Portal Scroll**. Randoming also grants a **Faerie Fire** and an **Enchanted Mango**. None of these free items can be sold. [corpus:liquipedia_dota2/gold@2376164#Starting_gold]

### Periodic gold

Beginning at **0:00**, each player passively receives **1 reliable gold every 0.67 seconds**, initially producing **90 gold every minute**. Periodic income increases over time by **2 per minute** based on the in-game clock. [corpus:liquipedia_dota2/gold@2376164#Periodic_Gold]

| Time in game | GPM from this time onward |
|---|---:|
| 0:00 | 90 |
| 12:00 | 94.8 |
| 30:00 | 99.8 |
| 45:00 | 105.5 |
| 62:00 | 112.8 |
| 87:00 | 120.5 |
| 112:00 | 129 |
| 140:00 | 139 |
| 175:00 | 150.5 |

The other passive gold source listed is **Kobold – Prospecting Aura**. [corpus:liquipedia_dota2/gold@2376164#Periodic_Gold]

### Talents

**Gold Income** is passive, affects self, and has a varying gold-per-minute bonus. It increases the hero’s periodic gold-per-minute income, but the granted gold is unreliable. [corpus:liquipedia_dota2/gold@2376164#Talents]

| Existing values |
|---|
| 30/60/90/120/150/180/210/240/300/420 |

| Status effect | Description |
|---|---|
| ? | Hidden modifier |

Heroes may have this talent at the left or right talent choice at Level 10, Level 15, Level 20, or Level 25; its bonus is expressed in **gold/min**. [corpus:liquipedia_dota2/gold@2376164#Talents]

### Bounty Runes

Bounty is listed as an ability with the value **No**, affects **Self / Allied Heroes**, and grants bonus reliable gold based on the in-game time when the rune is created. [corpus:liquipedia_dota2/gold@2376164#Bounty_Rune]

| Property | Value |
|---|---:|
| Cast Animation | 0 + 0 |
| Effect Radius | Global |
| Base Team Gold | 40 |
| Gold Bonus Increase per Instance | 6 |
| Increase Interval | 300 |
| Turbo Mode Multiplier | 2 |

The first pair of Bounty Runes spawns at the river Power Rune spots and grants a greater reliable-gold bonus. Subsequent runes spawn in each faction’s jungle after fixed in-game intervals. Bounty Runes are less effective and replenish a Bottle only to a limited extent. [corpus:liquipedia_dota2/gold@2376164#Bounty_Rune]

| Property | Value |
|---|---:|
| First-pair Team Gold Bonus | 40 |
| Subsequent Spawn Interval | 240 |
| Charge Restore per Other Rune | 2 |

[corpus:liquipedia_dota2/gold@2376164#Bounty_Rune]

### Gold-granting abilities

Most gold-granting abilities award unreliable gold. Only a few items and abilities can grant gold directly in other ways. [corpus:liquipedia_dota2/gold@2376164#Abilities]

| Unreliable-gold source |
|---|
| Alchemist – Greevil’s Greed |
| Alchemist – Aghanim’s Scepter Synth³ |
| Bounty Hunter – Jinada |
| Bounty Hunter – Track |
| Doom – Devour |
| Hand of Midas – Transmute |

| Marker | Requirement |
|---|---|
| 1 | Requires talent |
| 2a | Requires Aghanim’s Scepter |
| 2b | Requires Aghanim’s Shard |
| 3 | Only upon refunding the ally’s Aghanim’s Scepter or Aghanim’s Blessing |

[corpus:liquipedia_dota2/gold@2376164#Abilities]

| Reliable-gold source | Values and rules |
|---|---|
| Alchemist – Greevil’s Greed | Gold Type: Reliable; Bounty Rune Multiplier: 40; directly multiplies reliable gold from Bounty Runes |
| Runes – Bounty | Gold Type: Reliable |
| Kobold – Prospecting Aura | Gold per Minute: 20/25/30/40; Gold Type: Reliable |

[corpus:liquipedia_dota2/gold@2376164#Abilities]

### Hero kills

Hero kills grant unreliable gold to the killer. The first hero killed in a match grants the killer a bonus **135 unreliable gold**, called **First Blood!** Stopping kill streaks also awards bonus gold. [corpus:liquipedia_dota2/gold@2376164#Hero_kills]

When a hero dies to enemy creeps or an enemy tower:

| Recent enemy-hero involvement | Gold outcome |
|---|---|
| No enemy hero damaged the victim in the last 20 seconds, regardless of distance | Kill gold is split among all enemy heroes |
| Only one enemy damaged the victim | That enemy receives kill credit |
| Two or more enemies damaged the victim | Gold is divided equally among all heroes who assisted |

Damage negated to **0** also grants assist credit. [corpus:liquipedia_dota2/gold@2376164#Hero_kills]

| Component | Gold |
|---|---:|
| Hero Kills Base Gold | 125 |
| First Blood Gold | 135 |

`Σ BountyGold = bGold + (DeadHeroLVL × 8) + StreakGold + FB` [corpus:liquipedia_dota2/gold@2376164#Hero_kills]

### Kill streaks

A hero who earns multiple kills without dying is on a Kill Streak. Ending another player’s streak grants an additional bounty, sometimes called Shutdown Gold. Kill streaks begin at **3 kills**, increase with each kill through **10 kills**, and do not increase beyond **10 kills**. [corpus:liquipedia_dota2/gold@2376164#Kill_Streaks]

The streak bounty formula is:

`f(x) = (5k^2 + 5x)` [corpus:liquipedia_dota2/gold@2376164#Kill_Streaks]

| Streak-length value | Short-time count (18 secs) | Short-time announcement | Streak name | Streak value |
|---:|---:|---|---|---:|
| 0 | N/A | N/A | N/A | N/A |
| 0 | 1 | First Blood! | N/A | N/A |
| 0 | 2 | Double Kill! | N/A | N/A |
| 0 | 3 | Triple Kill! | Player is on a killing spree | 60 |
| 4 |  | Ultra Kill! | Player is dominating | 100 |
| 5 |  | Rampage! | Player is on a mega Kill streak | 150 |
| 6 |  |  | Player is unstoppable! | 210 |
| 7 |  |  | Player is wicked sick | 280 |
| 8 |  |  | Player is on a monster kill streak | 360 |
| 9 |  |  | Player is GODLIKE | 450 |
| 10+ |  |  | Player is beyond GODLIKE, someone kill them!! | 550 |

Announcer responses are customizable. [corpus:liquipedia_dota2/gold@2376164#Kill_Streaks]

The following deaths neither stop a kill streak nor count as First Blood:

| Death condition |
|---|
| The killing blow is dealt by neutral creeps, including Roshan and Tormentors |
| The killing blow is dealt by the dying hero’s team |
| The killing blow is dealt by an enemy tower or lane creep, with no enemy-hero damage during the previous 20 seconds |
| The death triggers Reincarnation |

[corpus:liquipedia_dota2/gold@2376164#Kill_Streaks]

### Assists and area gold

Allied heroes within **1500 radius** of a killed enemy, including the killer, receive experience and unreliable gold if they assisted. A hero qualifies by either being within that radius or having damaged or debuffed the victim. [corpus:liquipedia_dota2/gold@2376164#Assists_(AoE_gold)]

The scoreboard’s assist counter instead requires the player to have damaged or debuffed the victim or buffed the killer. Gold and experience are awarded independently of that counter. The assist-gold amount is identical for the killer and every assisting hero. [corpus:liquipedia_dota2/gold@2376164#Assists_(AoE_gold)]

`f = 15 + ((50 + (VictimNetWorth × 0.037)) / Number of Heroes)`

`A = Σ VictimTeam NetWorth / Σ KillerTeam NetWorth × f` [corpus:liquipedia_dota2/gold@2376164#Assists_(AoE_gold)]

### Buildings

Destroying an enemy tower awards unreliable gold to every player on the team. The player who lands the final hit receives destruction credit and additional unreliable gold. If a tower is denied, each team receives **50%** of its team bounty. If lane creeps destroy it without a player landing the final hit, no player receives the extra bonus. [corpus:liquipedia_dota2/gold@2376164#Buildings]

| Building | Team bounty Regular | Team bounty Turbo | Deny bounty Regular | Deny bounty Turbo | Last-hit bounty Regular | Last-hit bounty Turbo | Last-hit total Regular | Last-hit total Turbo | No-last-hit total Regular | No-last-hit total Turbo | Denied total Regular | Denied total Turbo |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Tower (Tier 1) | 90 | 180 | 45 | 90 | 110‒130 | 220‒260 | 560‒580 | 1120‒1160 | 450 | 900 | 225 | 450 |
| Tower (Tier 2) | 110 | 220 | 55 | 110 | 130‒130 | 260‒260 | 680‒700 | 1360‒1400 | 550 | 1100 | 275 | 550 |
| Tower (Tier 3) | 125 | 250 | 62.5 | 125 | 150‒130 | 300‒260 | 775‒795 | 1550‒1590 | 625 | 1250 | 312.5 | 625 |
| Tower (Tier 4) | 145 | 290 | 72.5 | 145 | 170‒130 | 340‒260 | 895‒915 | 1790‒1830 | 725 | 1450 | 362.5 | 725 |
| Ranged Barracks | 90 | 180 | 90 | 180 | 90‒135 | 180‒270 | 540‒585 | 1080‒1170 | 450 | 900 | 450 | 900 |
| Melee Barracks | 155 | 310 | 155 | 310 | 90‒135 | 180‒270 | 865‒910 | 1730‒1820 | 775 | 1550 | 775 | 1550 |
| Effigy Building | - | - | - | - | 68 | 136 | - | - | - | - | - | - |

[corpus:liquipedia_dota2/gold@2376164#Buildings]

### Lane creeps

Regular lane-creep bounty increases by **1 gold every 7 minutes 30 seconds**, while super-creep bounty increases by **1.5**. In Turbo Mode, regular lane-creep bounty increases by **3 gold every 2 minutes 30 seconds**, while super-creep bounty increases by **4.5**. [corpus:liquipedia_dota2/gold@2376164#Lane_creeps]

| Unit | Starting bounty | Turbo Mode |
|---|---:|---:|
| Siege Creep | 59‒72 | 118‒144 |
| Super Melee Creep | 20‒26 | 40‒52 |
| Mega Melee Creep | 20‒26 | 40‒52 |
| Super Ranged Creep | 19‒25 | 38‒50 |
| Mega Ranged Creep | 19‒25 | 38‒50 |
| Super Siege Creep | 59‒72 | 118‒144 |
| Mega Siege Creep | 59‒72 | 118‒144 |
| Flagbearer Creep | 34‒39 | 68‒78 |
| Super Flagbearer Creep | 20‒26 | 40‒52 |
| Mega Flagbearer Creep | 20‒26 | 40‒52 |
| Melee Creep | 34‒39 | 68‒78 |
| Ranged Creep | 43‒52 | 86‒104 |

[corpus:liquipedia_dota2/gold@2376164#Lane_creeps]

### Neutral creeps

When neutral creeps are stacked, the stacking player gains gold equal to **30%** of whatever the allied player farming that camp receives. [corpus:liquipedia_dota2/gold@2376164#Neutral_creeps]

| Unit | Bounty | Stack Value | Turbo Mode | Turbo Mode Stack Value |
|---|---:|---:|---:|---:|
| Ghost | 25‒27 |  | 50‒54 |  |
| Warpine Raider | 50‒52 |  | 100‒104 |  |
| Tormentor | 0 |  | 0 |  |
| Ancient Frostbitten Golem | 39‒45 |  | 78‒90 |  |
| Ancient Ice Shaman | 78‒82 |  | 156‒164 |  |
| Pollywog | 17‒19 |  | 34‒38 |  |
| Boglet | 25‒29 |  | 50‒58 |  |
| Croaker | 37‒41 |  | 74‒82 |  |
| Ancient Croaker | 53‒56 |  | 106‒112 |  |
| Marshmage Apprentice | 25‒29 |  | 50‒58 |  |
| Marshmage | 37‒41 |  | 74‒82 |  |
| Ancient Marshmage | 53‒56 |  | 106‒112 |  |
| Kobold | 5‒7 |  | 10‒14 |  |
| Kobold Soldier | 14‒16 |  | 28‒32 |  |
| Kobold Foreman | 21‒23 |  | 42‒46 |  |
| Hill Troll Berserker | 19‒21 |  | 38‒42 |  |
| Hill Troll Priest | 20‒22 |  | 40‒44 |  |
| Vhoul Assassin | 18‒20 |  | 36‒40 |  |
| Fell Spirit | 14‒15 |  | 28‒30 |  |
| Harpy Scout | 16‒18 |  | 32‒36 |  |
| Harpy Stormcrafter | 27‒29 |  | 54‒58 |  |
| Centaur Courser | 18‒20 |  | 36‒40 |  |
| Centaur Conqueror | 56‒62 |  | 112‒124 |  |
| Giant Wolf | 20‒24 |  | 40‒48 |  |
| Alpha Wolf | 34‒36 |  | 68‒72 |  |
| Satyr Banisher | 14‒16 |  | 28‒32 |  |
| Satyr Mindstealer | 22‒26 |  | 44‒52 |  |
| Ogre Bruiser | 24‒28 |  | 48‒56 |  |
| Ogre Frostmage | 30‒34 |  | 60‒68 |  |
| Mud Golem | 24‒26 |  | 48‒52 |  |
| Satyr Tormenter | 62‒68 |  | 124‒136 |  |
| Hellbear | 32‒40 |  | 64‒80 |  |
| Hellbear Smasher | 64‒68 |  | 128‒136 |  |
| Wildwing | 18‒20 |  | 36‒40 |  |
| Wildwing Ripper | 60‒66 |  | 120‒132 |  |
| Hill Troll | 20‒24 |  | 40‒48 |  |
| Dark Troll Summoner | 42‒48 |  | 84‒96 |  |
| Skeleton Warrior | 4‒6 |  | 8‒12 |  |
| Ancient Black Drake | 39‒45 |  | 78‒90 |  |
| Ancient Black Dragon | 78‒82 |  | 156‒164 |  |
| Ancient Rock Golem | 39‒45 |  | 78‒90 |  |
| Ancient Granite Golem | 78‒82 |  | 156‒164 |  |
| Ancient Rumblehide | 39‒45 |  | 78‒90 |  |
| Ancient Thunderhide | 78‒82 |  | 156‒164 |  |
| Shard Golem¹ | 8‒12 |  | 16‒24 |  |
| Ancient Prowler Acolyte | 37‒43 |  | 74‒86 |  |
| Ancient Prowler Shaman | 76‒80 |  | 152‒160 |  |
| Roshan | 200‒290<br>+ 135 | - | 400‒580<br>+ 270 | - |

¹ Shard Golems grant the stacking player no gold because their spawning conditions differ and they are not counted as part of the Mud Golem camp. [corpus:liquipedia_dota2/gold@2376164#Neutral_creeps]

### Summons

Summoned units have static bounties that never change. [corpus:liquipedia_dota2/gold@2376164#Summons]

| Unit | Bounty | Turbo Mode |
|---|---:|---:|
| Minor Imp | 3 | 6 |
| Demonic Archer | 150 | 300 |
| Demonic Warrior | 150 | 300 |
| Zealot | 34‒39 | 68‒78 |
| Skeleton Warrior | 4‒6 | 8‒12 |
| Shard Golem¹ | 8‒12 | 16‒24 |
| Raptor | 30/40/50/60 | 60/80/100/120 |
| Razorback | 26‒38 | 52‒76 |
| Treant | 8 | 16 |
| Spiderling | 9 | 18 |
| Eidolon | 17‒20 | 34‒40 |
| Wraith King Skeleton | 5 | 10 |
| Forged Spirit | 32‒46 | 64‒92 |
| Lycan Wolf | 21/26/36/41 | 42/52/72/82 |
| Spirit Bear | 165 + 10 |  |
| Tempest Double¹ | 70 10 | - |

¹ Because Tempest Double is a hero clone, Turbo Mode does not affect its bounty. [corpus:liquipedia_dota2/gold@2376164#Summons]

### Wards

Wards have static bounties that never change. [corpus:liquipedia_dota2/gold@2376164#Wards]

| Unit | Bounty | Turbo Mode |
|---|---:|---:|
| Observer Ward | 100 + 4/min | 200 + 8/min |
| Proximity Mine | 15 | 30 |
| Ice Spire | 20 | 40 |
| Phoenix Sun | 20 | 40 |
| Sticky Bomb | 10 | 20 |
| Power Cog | 16‒20 | 32‒40 |
| Jex | 150 | 300 |
| Skeleton Archer | 20 | 40 |
| Roshan’s Banner | 200 | 400 |
| Treant’s Eyes | 50 | 100 |
| M.A.D. | 10 | 20 |
| Keen Cannon | 5/10/15 | 10/20/30 |
| Anchor | 50 | 100 |
| Tombstone | 125/150/175/200 | 250/300/350/400 |
| Beetle | 32‒34 | 64‒68 |
| Plague Ward | 10/14/18/22 | 20/28/36/44 |
| Nimbus | 125 | 250 |
| Nether Ward | 20/40/60/80 | 40/80/120/160 |
| Psionic Trap | 25 | 50 |
| Healing Ward | 75 | 150 |
| Serpent Ward | 20‒26 | 40‒52 |
| Homing Missile | 50 | 100 |
| Phantom | 10 | 20 |
| Ignis Fatuus | 100 | 200 |

[corpus:liquipedia_dota2/gold@2376164#Wards]

### Couriers

Killing a courier grants **25 + 5 per hero level to each player on the killing team**. Couriers cannot be killed in Turbo Mode. [corpus:liquipedia_dota2/gold@2376164#Couriers]

### Selling

An item can be sold while its carrier is within range of any shop, returning **50%** of its purchase price. Only units controlled by the item’s owner may sell it unless it is completely shareable. A completely shareable item may be sold by any member of the owner’s team, and the selling player receives the gold. [corpus:liquipedia_dota2/gold@2376164#Selling]

## Spending and losing gold

### Drafting phase

During the drafting phase of All Pick and Ranked All Pick, a player who has not selected a hero when the selection timer expires loses **2 gold per second**. [corpus:liquipedia_dota2/gold@2376164#Drafting_phase]

### Items

Gold’s main purpose is purchasing items. The player with the most gold can buy the most powerful items and therefore has a very strong hero. Purchases depend on the player’s team role and many other factors. [corpus:liquipedia_dota2/gold@2376164#Items]

| Item | Purchase and sale rule |
|---|---|
| Divine Rapier | Cannot be sold |
| Gem of True Sight | Cannot be sold |
| Cheese | Cannot be purchased; can be sold for 500 gold |
| Refresher Shard | Cannot be purchased; can be sold for 500 gold |

[corpus:liquipedia_dota2/gold@2376164#Items]

### Death

Each death removes unreliable gold according to the following expression. Reliable gold is not lost. [corpus:liquipedia_dota2/gold@2376164#Death]

`GoldLoss = NetWorth/40` [corpus:liquipedia_dota2/gold@2376164#Death]

### Buyback

While dead, a player may spend gold to buy their hero back, instantly respawning at the fountain. Buyback is listed as an ability with the value **No** and affects **Self**. [corpus:liquipedia_dota2/gold@2376164#Buyback]

`BuybackCost = ⌊ ( 200 + NetWorth / 13 ) ⌋` [corpus:liquipedia_dota2/gold@2376164#Buyback]

| Property | Value |
|---|---:|
| Base Gold Cost | 200 |
| Networth Gold Divisor | 13 |
| Next Respawn Time Increase | 25 |
| Neutral Set Respawn Time | 26 |
| Additional listed value | 480 |

[corpus:liquipedia_dota2/gold@2376164#Buyback]

#### Details

The buyback button appears on the hero portrait while the hero is dead. Buyback cannot be used while reincarnating or while the dead hero remains stunned. [corpus:liquipedia_dota2/gold@2376164#Details]

| Example of a stun persisting through death |
|---|
| Toss |
| Walrus PUNCH! |
| Walrus Kick |
| Winter’s Curse |

[corpus:liquipedia_dota2/gold@2376164#Details]

Buyback spends reliable gold before unreliable gold. Its base cost is **200**, plus a fraction of the hero’s net worth rounded down:

`200 + NetWorth / 13` [corpus:liquipedia_dota2/gold@2376164#Details]

The respawn-time increase applies to the next respawn and does not count deaths involving Reincarnation. Because buyback has a high cooldown, high gold cost, and heavy penalties, it can backfire and should be considered carefully. [corpus:liquipedia_dota2/gold@2376164#Details]

| Situation | Guidance |
|---|---|
| A crucial team fight begins while the hero is dead | Buyback may allow the hero to join |
| The base needs defending | Buyback may be appropriate |
| The hero died in a team fight that their team still won and the team is attempting a final push | Buyback may be appropriate |
| Skipping the death timer to farm | Buyback generally should not be used because its gold cost is usually too high |

The death-time penalty is added to the next death. Particularly at high levels, an early or ill-fated buyback can produce a very long respawn time on the following death. [corpus:liquipedia_dota2/gold@2376164#Details]

| NetWorthNW | Buyback Cost |
|---:|---:|
| 1k | 276 |
| 2k | 353 |
| 3k | 430 |
| 4k | 507 |
| 5k | 584 |
| 6k | 661 |
| 7k | 738 |
| 8k | 815 |
| 9k | 892 |
| 10k | 969 |
| 11k | 1046 |
| 12k | 1123 |
| 13k | 1200 |
| 14k | 1276 |
| 15k | 1353 |
| 16k | 1430 |
| 17k | 1507 |
| 18k | 1584 |
| 19k | 1661 |
| 20k | 1738 |
| 21k | 1815 |
| 22k | 1892 |
| 23k | 1969 |
| 24k | 2046 |
| 25k | 2123 |
| 26k | 2200 |
| 27k | 2276 |
| 28k | 2353 |
| 29k | 2430 |
| 30k | 2507 |

[corpus:liquipedia_dota2/gold@2376164#Details]

### Abandoning the game

After a player has been disconnected for more than **5 minutes**, all their gold is divided equally among their remaining teammates. Distribution continues every second, so later gold income is also distributed. It stops when the player reconnects, but previously distributed gold is not reimbursed. [corpus:liquipedia_dota2/gold@2376164#Abandoning_the_game]

## Recent changes

| Version | Date | Changes |
|---|---|---|
| 7.40 | 2025-12-15 | Reworked Gold Assist formula. **OLD:** `60 + ((VictimNetworth * 0.037) / NumHeroes)` **NEW:** `15 + ((50 + (VictimNetworth * 0.037)) / NumHeroes)` |
| 7.33 | 2023-04-20 | Reworked Gold Assist formula. **OLD:** `(30 + (VictimNetworth * 0.038)) / NumHeroes` **NEW:** `60 + ((VictimNetworth * 0.037) / NumHeroes)` |
| 7.31 | 2022-02-23 | Increased hero-kill bounty. **OLD:** `120 + (KilledHeroLevel × 8) + KillStreakValue` **NEW:** `125 + (KilledHeroLevel × 8) + KillStreakValue`. Rescaled the kill-streak gold bonus from `100/135/170/205/240/275/310/345` to `60/100/150/210/280/360/450/550`. Kill-gold information now shows a breakdown of killer bounty and proximity gold. |

[corpus:liquipedia_dota2/gold@2376164#Recent_Changes]

## Gallery

| Entry |
|---|
| Unused Buyback gold penalty icon |
| Buyback placeholder icon |

[corpus:liquipedia_dota2/gold@2376164#Gallery]