from typeclasses.objects import Weapon
from world.currency import Gold

# Basic sword. Fairly predictable damage, respectable stats.
# Use this to create other edged weapons.
SWORD = {
    "protype_key": "SWORD",
    "typeclass": "typeclasses.objects.Weapon",
    "key": "sword",
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
    "damageType": "piercing",
    "range": 0,
    "minDamage": 5,
    "maxDamage": 6,
    "hitChance": 70,
    "critChance": 2,
    "parryChance": 25,
    "hands": 1,
    "mass": 5,
    "value": Gold(15)
}

# Swords and the like
LONGSWORD = {
    "protype_key": "LONGSWORD",
    "prototype_parent": "SWORD",
    "key": "longsword",
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
