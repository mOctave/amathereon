"""
Clothing Prototypes
"""

from world.currency import Gold

# Shirts, etc.

CLOTHING_TOP = {
	"prototype_key": "CLOTHING_TOP",
	"typeclass": "typeclasses.objects.Clothing",
	"key": "top",
	"weartype": "torso"
}

COTTON_SHIRT = {
	"prototype_key": "COTTON_SHIRT",
	"prototype_parent": "CLOTHING_TOP",
	"key": "cotton shirt",
	"desc": "Cotton is a very versatile material, useful in a variety of situations. Shirts made of cotton are worn wherever the plant grows, and are pleasant to wear, albeit a bit pricy.",
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
	"critProtect": 0,
	"value": Gold(8),
	"mass": 0.4,
	"nostealth": False
}

WOOL_SHIRT = {
	"prototype_key": "WOOL_SHIRT",
	"prototype_parent": "CLOTHING_TOP",
	"key": "wool shirt",
	"desc": "While wool can be uncomfortable to wear and a bit bulky, it is also highly effective at keeping its wearer warm. Woolen shirts are affordable, do a good job in winter, and even offer a bit of protection against magical and trauma weapons.",
	"minLayers": 0,
	"maxLayers": 3,
	"layers": 2,
	"piercingBlock": 0,
	"slashingBlock": 0,
	"traumaBlock": 1,
	"magicBlock": 1,
	"piercingProtect": 0,
	"slashingProtect": 0,
	"traumaProtect": 0,
	"magicProtect": 0,
	"critProtect": 0,
	"value": Gold(4),
	"mass": 0.5,
	"nostealth": False
}

SILK_SHIRT = {
	"prototype_key": "SILK_SHIRT",
	"prototype_parent": "CLOTHING_TOP",
	"key": "silk shirt",
	"desc": "The exorbitant cost of silk means that most people will never have a chance to wear a shirt made out of it. However, for those that do it is quite a comfortable fabric, and also exceptionally durable and light.",
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
	"critProtect": 2,
	"value": Gold(15),
	"mass": 0.3,
	"nostealth": False
}

LEATHER_COAT = {
	"prototype_key": "LEATHER_COAT",
	"prototype_parent": "CLOTHING_TOP",
	"key": "leather coat",
	"desc": "A leather coat serves both as a style accessory and also as armour against lightweight weapons. While it might not do much to fend off blows, it pads the wearer from those that do make it through other defenses.",
	"minLayers": 1,
	"maxLayers": 3,
	"layers": 2,
	"piercingBlock": 0,
	"slashingBlock": 1,
	"traumaBlock": 0,
	"magicBlock": 0,
	"piercingProtect": 1,
	"slashingProtect": 1,
	"traumaProtect": 1,
	"magicProtect": 1,
	"critProtect": 0,
	"value": Gold(10),
	"mass": 4,
	"nostealth": False
}

MAGE_JACKET = {
	"prototype_key": "MAGE_JACKER",
	"prototype_parent": "CLOTHING_TOP",
	"key": "mage jacket",
	"desc": "Mage jackets were first crafted long ago, a short time after the Rift, as a way to protect nobles and military officers from magic-wielding foes. Although they do an exceptional job at this, their cost is prohibitively expensive, far beyond the reach  of most common folk.",
	"minLayers": 2,
	"maxLayers": 4,
	"layers": 4,
	"piercingBlock": 2,
	"slashingBlock": 2,
	"traumaBlock": 2,
	"magicBlock": 10,
	"piercingProtect": 0,
	"slashingProtect": 0,
	"traumaProtect": 0,
	"magicProtect": 2,
	"critProtect": 4,
	"value": Gold(300),
	"mass": 3,
	"nostealth": False
}

CHAIN_SHIRT = {
	"prototype_key": "CHAIN_SHIRT",
	"prototype_parent": "CLOTHING_TOP",
	"key": "chain shirt",
	"desc": "A shirt of chainmail is a very versatile piece of armour, very efficient at blocking slashes to the torso. It is less than perfect at dealing with piercing and trauma weapons, but still better than nothing.",
	"minLayers": 2,
	"maxLayers": 4,
	"layers": 3,
	"piercingBlock": 1,
	"slashingBlock": 5,
	"traumaBlock": 1,
	"magicBlock": 1,
	"piercingProtect": 0,
	"slashingProtect": 2,
	"traumaProtect": 0,
	"magicProtect": 1,
	"critProtect": 0,
	"value": Gold(60),
	"mass": 15,
	"nostealth": True
}

CHESTPLATE = {
	"prototype_key": "CHESTPLATE",
	"prototype_parent": "CLOTHING_TOP",
	"key": "chestplate",
	"desc": "A chestplate is a large curved piece of metal built to be worn as the outermost layer of armour. While it is excellent at blocking most blows, it is less effective against trauma weapons, as well as being absurdly expensive.",
	"minLayers": 4,
	"maxLayers": 5,
	"layers": 4,
	"piercingBlock": 8,
	"slashingBlock": 10,
	"traumaBlock": 0,
	"magicBlock": 3,
	"piercingProtect": 1,
	"slashingProtect": 3,
	"traumaProtect": 0,
	"magicProtect": 1,
	"critProtect": 0,
	"value": Gold(150),
	"mass": 20,
	"nostealth": True
}

SHELL_PLATE = {
	"prototype_key": "SHELL_PLATE",
	"prototype_parent": "CLOTHING_TOP",
	"key": "shell plate",
	"desc": "This bizzare piece of armour, made by people along the southern coast of Amathereon and occasionally worn by the Aqinaé elves, is made of hundreds of pieces of shell stitched together. The result is heavier than plate armour, but similarly effective and slightly more useful against magical attacks.",
	"minLayers": 3,
	"maxLayers": 5,
	"layers": 5,
	"piercingBlock": 7,
	"slashingBlock": 7,
	"traumaBlock": 0,
	"magicBlock": 5,
	"piercingProtect": 2,
	"slashingProtect": 2,
	"traumaProtect": 0,
	"magicProtect": 2,
	"critProtect": 5,
	"value": Gold(150),
	"mass": 25,
	"nostealth": True
}

LAMINAR_MAIL_SHIRT = {
	"prototype_key": "LAMINAR_MAIL_SHIRT",
	"prototype_parent": "CLOTHING_TOP",
	"key": "laminar mail shirt",
	"desc": "Made of thousands of disks stitchen together, laminar armour is similar to chainmail, but it offers slightly more protection against piercing and magical attacks. This mail shirt is no exception to that rule, although it's a rare find: laminar armour is common primarily in Oracle Hill.",
	"minLayers": 2,
	"maxLayers": 4,
	"layers": 3,
	"piercingBlock": 4,
	"slashingBlock": 4,
	"traumaBlock": 0,
	"magicBlock": 5,
	"piercingProtect": 1,
	"slashingProtect": 1,
	"traumaProtect": 0,
	"magicProtect": 2,
	"critProtect": 1,
	"value": Gold(70),
	"mass": 15,
	"nostealth": True
}
