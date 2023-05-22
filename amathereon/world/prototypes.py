#import evennia.contrib.game_systems.clothing.clothing
from typeclasses.objects import Currency
from world.currency import Gold

"""
Prototypes

A prototype is a simple way to create individualized instances of a
given typeclass. It is dictionary with specific key names.

For example, you might have a Sword typeclass that implements everything a
Sword would need to do. The only difference between different individual Swords
would be their key, description and some Attributes. The Prototype system
allows to create a range of such Swords with only minor variations. Prototypes
can also inherit and combine together to form entire hierarchies (such as
giving all Sabres and all Broadswords some common properties). Note that bigger
variations, such as custom commands or functionality belong in a hierarchy of
typeclasses instead.

A prototype can either be a dictionary placed into a global variable in a
python module (a 'module-prototype') or stored in the database as a dict on a
special Script (a db-prototype). The former can be created just by adding dicts
to modules Evennia looks at for prototypes, the latter is easiest created
in-game via the `olc` command/menu.

Prototypes are read and used to create new objects with the `spawn` command
or directly via `evennia.spawn` or the full path `evennia.prototypes.spawner.spawn`.

A prototype dictionary have the following keywords:

Possible keywords are:
- `prototype_key` - the name of the prototype. This is required for db-prototypes,
  for module-prototypes, the global variable name of the dict is used instead
- `prototype_parent` - string pointing to parent prototype if any. Prototype inherits
  in a similar way as classes, with children overriding values in their parents.
- `key` - string, the main object identifier.
- `typeclass` - string, if not set, will use `settings.BASE_OBJECT_TYPECLASS`.
- `location` - this should be a valid object or #dbref.
- `home` - valid object or #dbref.
- `destination` - only valid for exits (object or #dbref).
- `permissions` - string or list of permission strings.
- `locks` - a lock-string to use for the spawned object.
- `aliases` - string or list of strings.
- `attrs` - Attributes, expressed as a list of tuples on the form `(attrname, value)`,
  `(attrname, value, category)`, or `(attrname, value, category, locks)`. If using one
   of the shorter forms, defaults are used for the rest.
- `tags` - Tags, as a list of tuples `(tag,)`, `(tag, category)` or `(tag, category, data)`.
-  Any other keywords are interpreted as Attributes with no category or lock.
   These will internally be added to `attrs` (equivalent to `(attrname, value)`.

See the `spawn` command and `evennia.prototypes.spawner.spawn` for more info.

"""

## example of module-based prototypes using
## the variable name as `prototype_key` and
## simple Attributes

# from random import randint
#
# GOBLIN = {
# "key": "goblin grunt",
# "health": lambda: randint(20,30),
# "resists": ["cold", "poison"],
# "attacks": ["fists"],
# "weaknesses": ["fire", "light"],
# "tags": = [("greenskin", "monster"), ("humanoid", "monster")]
# }
#
# GOBLIN_WIZARD = {
# "prototype_parent": "GOBLIN",
# "key": "goblin wizard",
# "spells": ["fire ball", "lighting bolt"]
# }
#
# GOBLIN_ARCHER = {
# "prototype_parent": "GOBLIN",
# "key": "goblin archer",
# "attacks": ["short bow"]
# }
#
# This is an example of a prototype without a prototype
# (nor key) of its own, so it should normally only be
# used as a mix-in, as in the example of the goblin
# archwizard below.
# ARCHWIZARD_MIXIN = {
# "attacks": ["archwizard staff"],
# "spells": ["greater fire ball", "greater lighting"]
# }
#
# GOBLIN_ARCHWIZARD = {
# "key": "goblin archwizard",
# "prototype_parent" : ("GOBLIN_WIZARD", "ARCHWIZARD_MIXIN")
# }

CLOTHING_TOP = {
	"protype_key": "CLOTHING_TOP",
	"typeclass": "typeclasses.objects.Clothing",
	"key": "top",
	"weartype": "torso"
}

T_SHIRT = {
	"protype_key": "T_SHIRT",
	"prototype_parent": "CLOTHING_TOP",
	"key": "t-shirt",
	"minLayers": 0,
	"maxLayers": 2,
	"layers": 1,
	"piercingBlock": 0,
	"slashingBlock": 0,
	"traumaBlock": 0,
	"magicBlock": 0,
	"piercingProtect": 0,
	"slashingProtect": 0,
	"traumaProtect": 0,
	"magicProtect": 0,
	"critProtect": 0
}

LEATHER_COAT = {
	"protype_key": "leather_coat",
	"prototype_parent": "CLOTHING_TOP",
	"key": "leather coat",
	"minLayers": 2,
	"maxLayers": 3,
	"layers": 3,
	"piercingBlock": 0,
	"slashingBlock": 1,
	"traumaBlock": 0,
	"magicBlock": 0,
	"piercingProtect": 1,
	"slashingProtect": 1,
	"traumaProtect": 1,
	"magicProtect": 1,
	"critProtect": 0
}

# Currency Types

CURRENCY = {
	"prototype_key": "CURRENCY",
	"typeclass": "typeclasses.objects.Currency",
	"key": "currency"
}

CURRENCY_GOLD_CROWN_HILLROCKIA = {
	"prototype_key": "hillrockian_gold_crown",
	"prototype_parent": "CURRENCY",
	"key": "hillrockian gold crown",
	"desc": "This Hillrockian gold crown is not-quite pure gold, weighing about forty grains. It has been stamped with the head of some minor prince, which appears to be a tradition of the royal family. Worth: 40 gr gold.",
	"value": lambda: Gold(40),
	"mass": 40/16/120
}

CURRENCY_GOLD_MARK_HILLROCKIA = {
	"prototype_key": "hillrockian_gold_mark",
	"prototype_parent": "CURRENCY",
	"key": "hillrockian gold mark",
	"desc": "This Hillrockian gold mark is slightly smaller than a gold crown, and worth about half as much. It is decorated with an intricate geometric design. Worth: 20 gr gold.",
	"value": lambda: Gold(20),
	"mass": 20/16/80
}

CURRENCY_GOLD_PENNY_HILLROCKIA = {
	"prototype_key": "hillrockian_gold_penny",
	"prototype_parent": "CURRENCY",
	"key": "hillrockian gold penny",
	"desc": "This Hillrockian gold penny is the smallest unit of currency in Hillrockia when it comes to gold. It bears no design, being just a thick, small disk of pure gold. Worth: 5 gr gold.",
	"value": lambda: Gold(5),
	"mass": 5/16/480
}

CURRENCY_SILVER_PENNY_HILLROCKIA = {
	"prototype_key": "hillrockian_silver_penny",
	"prototype_parent": "CURRENCY",
	"key": "hillrockian silver penny",
	"desc": "This Hillrockian silver penny is used among Hillrockians for when even their smallest gold coins are too valuable. Worth: 1 gr gold.",
	"value": lambda: Gold(1),
	"mass": 4/16/480
}

CURRENCY_SILVER_FIFTHPENNY_HILLROCKIA = {
	"prototype_key": "hillrockian_silver_fifthpenny",
	"prototype_parent": "CURRENCY",
	"key": "hillrockian silver fifthpenny",
	"desc": "This coin is, quite literally, a fifth of a Hillrockian silver penny. Worth: 0.2 gr gold.",
	"value": lambda: Gold(0.2),
	"mass": 4/5/16/480
}