from typeclasses.objects import Weapon

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
    "mass": 3
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
    "mass": 5
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
    "mass": 5
}