from typeclasses.objects import Weapon
from world.currency import Gold

# Basic sword. Fairly predictable damage, respectable stats.
# Use this to create other edged weapons.
SWORD = {
    "protype_key": "SWORD",
    "typeclass": "typeclasses.objects.Weapon",
    "key": "sword",
    "tname": "sword",
    "desc": "A sword is a typically bladed weapon designed to be wielded in highly discipled stances, although individual swords vary quite a bit.",
    "damageType": "slashing",
    "range": 0,
    "minDamage": 4,
    "maxDamage": 6,
    "hitChance": 80,
    "critChance": 3,
    "parryChance": 15,
    "hands": 1,
    "mass": 3,
    "value": Gold(25)
}

# Basic axe. Damage varies a lot, and it doesn't hit particularly often.
# Use this to create other heavy slashing weapons.
AXE = {
    "protype_key": "AXE",
    "typeclass": "typeclasses.objects.Weapon",
    "key": "axe",
    "tname": "axe",
    "desc": "An axe is basically just a fancy blade on a stick, designed to cleave through wood - or flesh.",
    "damageType": "slashing",
    "range": 0,
    "minDamage": 3,
    "maxDamage": 9,
    "hitChance": 60,
    "critChance": 5,
    "parryChance": 5,
    "hands": 1,
    "mass": 5,
    "value": Gold(20)
}

# Basic spear. It's fairly reliable albeit slow, and good at parrying other weapons.
# Use this to create other polearms.
SPEAR = {
    "protype_key": "SPEAR",
    "typeclass": "typeclasses.objects.Weapon",
    "key": "spear",
    "tname": "spear",
    "desc": "A spear is the simplest of all polearms, just a sharp point on a moderately long pole. It is a good defensive weapon, but is less strong on the offensive.",
    "damageType": "piercing",
    "range": 0,
    "minDamage": 5,
    "maxDamage": 6,
    "hitChance": 70,
    "critChance": 2,
    "parryChance": 20,
    "hands": 1,
    "mass": 5,
    "value": Gold(15)
}

# Basic club. It's a trauma weapon that is only moderately effective.
# Use this to create other trauma weapons.
CLUB = {
    "protype_key": "CLUB",
    "typeclass": "typeclasses.objects.Weapon",
    "key": "club",
    "tname": "club",
    "desc": "A club is a very simple weapon, just a length of wood that can be used to cause non-fatal wounds.",
    "damageType": "trauma",
    "range": 0,
    "minDamage": 2,
    "maxDamage": 4,
    "hitChance": 80,
    "critChance": 4,
    "parryChance": 10,
    "hands": 1,
    "mass": 2,
    "value": Gold(5)
}

# Basic shield. It's definitely not an offensive weapon, but it can be used as such in a pinch.
# Use this to create other shields.
SHIELD = {
    "protype_key": "SHIELD",
    "typeclass": "typeclasses.objects.Weapon",
    "key": "shield",
    "tname": "shield",
    "desc": "A shields is not an offensive weapon, but is very effective at protecting oneself from an enemy.",
    "damageType": "trauma",
    "range": 0,
    "minDamage": 0,
    "maxDamage": 3,
    "hitChance": 60,
    "critChance": 5,
    "parryChance": 40,
    "hands": 1,
    "mass": 8,
    "value": Gold(15)
}


# Swords and the like
LONGSWORD = {
    "protype_key": "LONGSWORD",
    "prototype_parent": "SWORD",
    "key": "longsword",
    "tname": "longsword",
    "desc": "A longsword is a relatively large sword that is slightly less manueverable than average but more powerful.",
    "minDamage": 6,
    "maxDamage": 8,
    "hitChance": 75,
    "critChance": 2,
    "parryChance": 20,
    "hands": 2,
    "mass": 3,
    "value": Gold(30)
}

SHORTSWORD = {
    "protype_key": "SHORTSWORD",
    "prototype_parent": "SWORD",
    "key": "shortsword",
    "tname": "shortsword",
    "desc": "A shortsword is simply a shorter than average sword that is easier to wield but less powerful.",
    "minDamage": 3,
    "maxDamage": 5,
    "hitChance": 85,
    "critChance": 3,
    "parryChance": 12,
    "hands": 1,
    "mass": 2,
    "value": Gold(20)
}

CLAYMORE = {
    "protype_key": "CLAYMORE",
    "prototype_parent": "SWORD",
    "key": "claymore",
    "tname": "claymore",
    "desc": "A claymore is a large and heavy sword, meant to be wielded with two hands.",
    "minDamage": 8,
    "maxDamage": 11,
    "hitChance": 70,
    "critChance": 1,
    "parryChance": 20,
    "hands": 2,
    "mass": 5,
    "value": Gold(35)
}

RAPIER = {
    "protype_key": "CLAYMORE",
    "prototype_parent": "SWORD",
    "key": "rapier",
    "tname": "rapier",
    "desc": "A rapier is a lightweight, and manueverable weapon. In the right hands, it can easily be deadly.",
    "damageType": "piercing",
    "minDamage": 3,
    "maxDamage": 5,
    "hitChance": 90,
    "critChance": 6,
    "parryChance": 25,
    "hands": 1,
    "mass": 2,
    "value": Gold(50)
}

DAGGER = {
    "protype_key": "DAGGER",
    "prototype_parent": "SWORD",
    "key": "dagger",
    "tname": "dagger",
    "desc": "A dagger is a sword shortened to the point where it is no longer usable in many combat situations.",
    "damageType": "piercing",
    "minDamage": 2,
    "maxDamage": 4,
    "hitChance": 90,
    "critChance": 6,
    "parryChance": 5,
    "hands": 1,
    "mass": 1,
    "value": Gold(15)
}

THROWING_KNIFE = {
    "protype_key": "THROWING_KNIFE",
    "prototype_parent": "SWORD",
    "key": "throwing knife",
    "tname": "throwing knife",
    "desc": "This knife is a dagger balanced perfectly for throwing.",
    "damageType": "piercing",
    "range": 1,
    "minDamage": 2,
    "maxDamage": 4,
    "hitChance": 85,
    "critChance": 5,
    "parryChance": 5,
    "hands": 1,
    "mass": 1,
    "value": Gold(25)
}

SWORDBREAKER = {
    "protype_key": "SWORDBREAKER",
    "prototype_parent": "SWORD",
    "key": "swordbreaker",
    "tname": "swordbreaker",
    "desc": "A swordbreaker is a slotted knife designed to catch and turn swords. Although it is not a very powerful weapon, it makes an excellent defensive tool.",
    "minDamage": 2,
    "maxDamage": 4,
    "hitChance": 70,
    "critChance": 4,
    "parryChance": 30,
    "hands": 1,
    "mass": 2,
    "value": Gold(20)
}

SABRE = {
    "protype_key": "SABRE",
    "prototype_parent": "SWORD",
    "key": "sabre",
    "tname": "sabre",
    "desc": "A sabre is a curved sword. Its design makes it harder to predict where a blow from it will come from, but also harder to use.",
    "minDamage": 4,
    "maxDamage": 6,
    "hitChance": 75,
    "critChance": 6,
    "parryChance": 12,
    "hands": 1,
    "mass": 3,
    "value": Gold(25)
}

# Axe-like weapons
BATTLEAXE = {
    "protype_key": "BATTLEAXE",
    "prototype_parent": "AXE",
    "key": "battleaxe",
    "tname": "battleaxe",
    "desc": "This is an axe designed especially for combat, and it has few uses outside of it.",
    "minDamage": 4,
    "maxDamage": 10,
    "hitChance": 65,
    "critChance": 5,
    "parryChance": 6,
    "hands": 1,
    "mass": 5,
    "value": Gold(25)
}

GREATAXE = {
    "protype_key": "GREATAXE",
    "prototype_parent": "AXE",
    "key": "greataxe",
    "tname": "greataxe",
    "desc": "A greataxe is a very large axe, only usable with two hands. It is harder to control, but more powerful.",
    "minDamage": 6,
    "maxDamage": 12,
    "hitChance": 55,
    "critChance": 7,
    "parryChance": 4,
    "hands": 2,
    "mass": 7,
    "value": Gold(35)
}

WARHAMMER = {
    "protype_key": "WARHAMMER",
    "prototype_parent": "AXE",
    "key": "warhammer",
    "tname": "warhammer",
    "desc": "Rather than a blade like an axe, a warhammer bears a solid chunk of metal at the end, designed to do damage to even the most heavily armoured foes.",
    "damageType": "trauma",
    "minDamage": 4,
    "maxDamage": 8,
    "hitChance": 60,
    "critChance": 10,
    "parryChance": 6,
    "hands": 1,
    "mass": 5,
    "value": Gold(25)
}


# Polearms
BARDICHE = {
    "protype_key": "BARDICHE",
    "prototype_parent": "SPEAR",
    "key": "bardiche",
    "tname": "bardiche",
    "desc": "A bardiche is a type of axe-headed polearm, basically just a very long axe, when it comes down to it. It is effecive but simple.",
    "damageType": "slashing",
    "minDamage": 5,
    "maxDamage": 7,
    "hitChance": 65,
    "critChance": 3,
    "parryChance": 20,
    "hands": 1,
    "mass": 6,
    "value": Gold(25)
}

HALBERD = {
    "protype_key": "HALBERD",
    "prototype_parent": "SPEAR",
    "key": "halberd",
    "tname": "halberd",
    "desc": "A halberd is a fearsome weapon, tipped with a spearpoint but bearing both an axe blade and a hook. In the hands of a skilled soldier, it can be used to great effect, although it is heavy and expensive.",
    "damageType": "slashing",
    "minDamage": 5,
    "maxDamage": 8,
    "hitChance": 75,
    "critChance": 4,
    "parryChance": 20,
    "hands": 2,
    "mass": 7,
    "value": Gold(35)
}

MILITARY_FORK = {
    "protype_key": "MILITARY_FORK",
    "prototype_parent": "SPEAR",
    "key": "military fork",
    "tname": "military fork",
    "desc": "A military fork is a two-pronged spear, as simple as a spear and even easier to use.",
    "damageType": "piercing",
    "minDamage": 5,
    "maxDamage": 6,
    "hitChance": 80,
    "critChance": 4,
    "parryChance": 20,
    "hands": 2,
    "mass": 4,
    "value": Gold(15)
}

PIKE = {
    "protype_key": "PIKE",
    "prototype_parent": "SPEAR",
    "key": "pike",
    "tname": "pike",
    "desc": "A pike is an unusually long spear designed to be wielded by infantry in formation. It is great at parrying blows, but also very unwieldy.",
    "damageType": "piercing",
    "minDamage": 5,
    "maxDamage": 6,
    "hitChance": 65,
    "critChance": 1,
    "parryChance": 30,
    "hands": 2,
    "mass": 6,
    "value": Gold(20)
}

PARTISAN = {
    "protype_key": "PARTISAN",
    "prototype_parent": "SPEAR",
    "key": "partisan",
    "tname": "partisan",
    "desc": "A partisan is a spear designed for fighting off sword thrusts. It is slightly less effective on the offense, but still a formideable weapon.",
    "damageType": "piercing",
    "minDamage": 5,
    "maxDamage": 6,
    "hitChance": 70,
    "critChance": 5,
    "parryChance": 25,
    "hands": 2,
    "mass": 5,
    "value": Gold(20)
}

SCYTHE = {
    "protype_key": "SCYTHE",
    "prototype_parent": "SPEAR",
    "key": "scythe",
    "tname": "scythe",
    "desc": "A military scythe is made by placing a long, curved blade on the end of an even longer pole. It is not a common weapon, but can occasionally prove devastating.",
    "damageType": "slashing",
    "minDamage": 4,
    "maxDamage": 8,
    "hitChance": 65,
    "critChance": 6,
    "parryChance": 20,
    "hands": 2,
    "mass": 6,
    "value": Gold(20)
}

JAVELIN = {
    "protype_key": "JAVELIN",
    "prototype_parent": "SPEAR",
    "key": "javelin",
    "tname": "javelin",
    "desc": "This spear is designed as a weapon to be thrown at the enemy.",
    "damageType": "piercing",
    "range": 1,
    "minDamage": 4,
    "maxDamage": 5,
    "hitChance": 60,
    "critChance": 3,
    "parryChance": 15,
    "hands": 1,
    "mass": 4,
    "value": Gold(20)
}


# Trauma Weapons
QUATERSTAFF = {
    "protype_key": "QUARTERSTAFF",
    "prototype_parent": "CLUB",
    "key": "quarterstaff",
    "tname": "quaterstaff",
    "desc": "A quaterstaff is a long length of wood, slightly longer than the height of its wielder, often used by farmers. It is an easy weapon to use, but a hard one to master.",
    "range": 0,
    "minDamage": 2,
    "maxDamage": 5,
    "hitChance": 85,
    "critChance": 6,
    "parryChance": 30,
    "hands": 2,
    "mass": 4,
    "value": Gold(10)
}

FLAIL = {
    "protype_key": "FLAIL",
    "prototype_parent": "CLUB",
    "key": "flail",
    "tname": "flail",
    "desc": "A flail consists of a spiked ball on the end of a chain, handled with a short pole. It is unpredictable, and can occasionally wreak havoc by eluding an enemy's defenses.",
    "range": 0,
    "minDamage": 1,
    "maxDamage": 6,
    "hitChance": 90,
    "critChance": 10,
    "parryChance": 15,
    "hands": 2,
    "mass": 4,
    "value": Gold(15)
}

MACE = {
    "protype_key": "MACE",
    "prototype_parent": "CLUB",
    "key": "mace",
    "tname": "mace",
    "desc": "A mace is essentially a reinforced club, made of metal and designed to do as much damage as possible and tipped with a head designed to smash through armour.",
    "range": 0,
    "minDamage": 4,
    "maxDamage": 6,
    "hitChance": 75,
    "critChance": 5,
    "parryChance": 10,
    "hands": 1,
    "mass": 3,
    "value": Gold(20)
}
