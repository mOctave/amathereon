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
	"prototype_key": "MAGE_JACKET",
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
	"minLayers": 3,
	"maxLayers": 4,
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

# Headgear

CLOTHING_HEADGEAR = {
	"prototype_key": "CLOTHING_HEADGEAR",
	"typeclass": "typeclasses.objects.Clothing",
	"key": "headgear",
	"weartype": "head"
}

CAP = {
	"prototype_key": "CAP",
	"prototype_parent": "CLOTHING_HEADGEAR",
	"key": "cap",
	"desc": "This warm, soft cap provides a little bit of comfort and shelter from the elements, although it is not of much use in combat.",
	"minLayers": 0,
	"maxLayers": 3,
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
	"value": Gold(1),
	"mass": 0.1,
	"nostealth": False
}

STRAW_HAT = {
	"prototype_key": "STRAW_HAT",
	"prototype_parent": "CLOTHING_HEADGEAR",
	"key": "straw_hat",
	"desc": "This straw hat is itchy and a bit stiff, but it provides good protection from the sun and some against magical attacks.",
	"minLayers": 0,
	"maxLayers": 2,
	"layers": 1,
	"piercingBlock": 0,
	"slashingBlock": 0,
	"traumaBlock": 0,
	"magicBlock": 1,
	"piercingProtect": 0,
	"slashingProtect": 0,
	"traumaProtect": 0,
	"magicProtect": 0,
	"critProtect": 0,
	"value": Gold(1),
	"mass": 0.2,
	"nostealth": False
}

ELVYREN = {
	"prototype_key": "ELVYREN",
	"prototype_parent": "CLOTHING_HEADGEAR",
	"key": "elvyren",
	"desc": "The elvyren is a strange piece of headwear designed to be worn over another, smaller, hat. It is manufactered by the Eseri and imbued with unique defensive magics. A single elvyren costs more than many suits of armour.",
	"minLayers": 1,
	"maxLayers": 3,
	"layers": 2,
	"piercingBlock": 3,
	"slashingBlock": 4,
	"traumaBlock": 5,
	"magicBlock": 10,
	"piercingProtect": 0,
	"slashingProtect": 0,
	"traumaProtect": 1,
	"magicProtect": 2,
	"critProtect": 3,
	"value": Gold(250),
	"mass": 0.1,
	"nostealth": False
}

CHAIN_HOOD = {
	"prototype_key": "CHAIN_HOOD",
	"prototype_parent": "CLOTHING_HEADGEAR",
	"key": "chain hood",
	"desc": "This hood, made of chainmail, is designed to fit tightly under a larger helmet and provide an extra layer of protection.",
	"minLayers": 1,
	"maxLayers": 1,
	"layers": 2,
	"piercingBlock": 1,
	"slashingBlock": 2,
	"traumaBlock": 1,
	"magicBlock": 0,
	"piercingProtect": 0,
	"slashingProtect": 1,
	"traumaProtect": 0,
	"magicProtect": 0,
	"critProtect": 0,
	"value": Gold(15),
	"mass": 4,
	"nostealth": True
}

ARMET = {
	"prototype_key": "ARMET",
	"prototype_parent": "CLOTHING_HEADGEAR",
	"key": "armet",
	"desc": "An armet is a relatively lightweight but very efficient piece of armour built to withstand blows to the face. While it works best over chainmail and is not terribly effective by itself, it is still a very versatile piece of armour.",
	"minLayers": 2,
	"maxLayers": 3,
	"layers": 3,
	"piercingBlock": 4,
	"slashingBlock": 4,
	"traumaBlock": 0,
	"magicBlock": 1,
	"piercingProtect": 0,
	"slashingProtect": 2,
	"traumaProtect": 0,
	"magicProtect": 1,
	"critProtect": 0,
	"value": Gold(40),
	"mass": 6,
	"nostealth": True
}

BARBUTE = {
	"prototype_key": "BARBUTE",
	"prototype_parent": "CLOTHING_HEADGEAR",
	"key": "barbute",
	"desc": "A barbute is a solid metal helmet split by a T that lets the wearer breathe and see out. Although this design provides excellent defense against slashing attacks, it is heavy and can't help you much if you take an arrow to the eye.",
	"minLayers": 2,
	"maxLayers": 3,
	"layers": 2,
	"piercingBlock": 2,
	"slashingBlock": 5,
	"traumaBlock": 0,
	"magicBlock": 1,
	"piercingProtect": 0,
	"slashingProtect": 2,
	"traumaProtect": 0,
	"magicProtect": 0,
	"critProtect": 0,
	"value": Gold(25),
	"mass": 8,
	"nostealth": True
}

LAMELLAR_HELMET = {
	"prototype_key": "LAMELLAR_HELMET",
	"prototype_parent": "CLOTHING_HEADGEAR",
	"key": "lamellar helmet",
	"desc": "The traditional helmet worn by the Guardians of Oracle Hill, lamellar helmets are made of strips of metal stitched together. Lamellar helmets work well against magical attacks, and are decent all-round, but they excel at nothing.",
	"minLayers": 2,
	"maxLayers": 4,
	"layers": 3,
	"piercingBlock": 2,
	"slashingBlock": 3,
	"traumaBlock": 2,
	"magicBlock": 3,
	"piercingProtect": 0,
	"slashingProtect": 0,
	"traumaProtect": 0,
	"magicProtect": 1,
	"critProtect": 1,
	"value": Gold(30),
	"mass": 15,
	"nostealth": True
}

# Gloves

CLOTHING_HANDS = {
	"prototype_key": "CLOTHING_HANDS",
	"typeclass": "typeclasses.objects.Clothing",
	"key": "hands",
	"weartype": "hands"
}

LEATHER_GLOVES = {
	"prototype_key": "LEATHER_GLOVES",
	"prototype_parent": "CLOTHING_HANDS",
	"key": "leather gloves",
	"desc": "These gloves are durable and work well in a wide variety of situations.",
	"minLayers": 0,
	"maxLayers": 1,
	"layers": 2,
	"piercingBlock": 1,
	"slashingBlock": 1,
	"traumaBlock": 0,
	"magicBlock": 0,
	"piercingProtect": 0,
	"slashingProtect": 0,
	"traumaProtect": 0,
	"magicProtect": 0,
	"critProtect": 0,
	"value": Gold(2),
	"mass": 0.1,
	"nostealth": False
}

WOOL_GLOVES = {
	"prototype_key": "WOOL_GLOVES",
	"prototype_parent": "CLOTHING_HANDS",
	"key": "wool gloves",
	"desc": "Wool gloves are warm and affordable, as well as providing some protection against magic.",
	"minLayers": 0,
	"maxLayers": 1,
	"layers": 2,
	"piercingBlock": 0,
	"slashingBlock": 0,
	"traumaBlock": 0,
	"magicBlock": 1,
	"piercingProtect": 0,
	"slashingProtect": 0,
	"traumaProtect": 0,
	"magicProtect": 0,
	"critProtect": 0,
	"value": Gold(1),
	"mass": 0.1,
	"nostealth": False
}

COTTON_GLOVES = {
	"prototype_key": "COTTON_GLOVES",
	"prototype_parent": "CLOTHING_HANDS",
	"key": "cotton gloves",
	"desc": "Cotton gloves are not very useful in and of theirselves, but they provide a much needed layer of padding for those seeking to wear heavy armour.",
	"minLayers": 0,
	"maxLayers": 1,
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
	"value": Gold(1),
	"mass": 0.05,
	"nostealth": False
}

SILK_GLOVES = {
	"prototype_key": "SILK_GLOVES",
	"prototype_parent": "CLOTHING_HANDS",
	"key": "silk gloves",
	"desc": "These silk gloves are very fancy and exorbitantly expensive, but they are not really any more useful than ordinary gloves, except in high circles.",
	"minLayers": 0,
	"maxLayers": 1,
	"layers": 1,
	"piercingBlock": 0,
	"slashingBlock": 0,
	"traumaBlock": 0,
	"magicBlock": 0,
	"piercingProtect": 0,
	"slashingProtect": 0,
	"traumaProtect": 0,
	"magicProtect": 0,
	"critProtect": 1,
	"value": Gold(5),
	"mass": 0.05,
	"nostealth": False
}

GAUNTLETS = {
	"prototype_key": "GAUNTLETS",
	"prototype_parent": "CLOTHING_HANDS",
	"key": "gauntlets",
	"desc": "Gauntlets are large sleeved gloves made of metal designed to be worn as part of a larger suit of armour. They offer superb protection, but are expensive and a bit hard to manipulate things with.",
	"minLayers": 1,
	"maxLayers": 2,
	"layers": 3,
	"piercingBlock": 3,
	"slashingBlock": 3,
	"traumaBlock": 0,
	"magicBlock": 1,
	"piercingProtect": 0,
	"slashingProtect": 1,
	"traumaProtect": 0,
	"magicProtect": 0,
	"critProtect": 0,
	"value": Gold(20),
	"mass": 3,
	"nostealth": True
}

# Legwear

CLOTHING_LEGWEAR = {
	"prototype_key": "CLOTHING_LEGWEAR",
	"typeclass": "typeclasses.objects.Clothing",
	"key": "legwear",
	"weartype": "legs"
}

DENIM_PANTS = {
	"prototype_key": "DENIM_PANTS",
	"prototype_parent": "CLOTHING_LEGWEAR",
	"key": "denim pants",
	"desc": "Denim pants are made of tightly woven cotton, and are far more durable than regular cotton pants, if a tad less comfortable.",
	"minLayers": 0,
	"maxLayers": 1,
	"layers": 2,
	"piercingBlock": 0,
	"slashingBlock": 1,
	"traumaBlock": 0,
	"magicBlock": 1,
	"piercingProtect": 0,
	"slashingProtect": 0,
	"traumaProtect": 0,
	"magicProtect": 0,
	"critProtect": 0,
	"value": Gold(5),
	"mass": 0.3,
	"nostealth": False
}

COTTON_PANTS = {
	"prototype_key": "COTTON_PANTS",
	"prototype_parent": "CLOTHING_LEGWEAR",
	"key": "cotton pants",
	"desc": "Regularly woven cotton works well for pants, although it is tears rather easily. Cotton also works well as an underlayer for armour.",
	"minLayers": 0,
	"maxLayers": 0,
	"layers": 1,
	"piercingBlock": 0,
	"slashingBlock": 0,
	"traumaBlock": 0,
	"magicBlock": 1,
	"piercingProtect": 0,
	"slashingProtect": 0,
	"traumaProtect": 0,
	"magicProtect": 0,
	"critProtect": 0,
	"value": Gold(3),
	"mass": 0.1,
	"nostealth": False
}

SILK_LEGGINGS = {
	"prototype_key": "SILK_LEGGINGS",
	"prototype_parent": "CLOTHING_LEGWEAR",
	"key": "silk leggings",
	"desc": "Silk leggings are stylish but pricy and far more useful in a ballroom than in combat.",
	"minLayers": 0,
	"maxLayers": 0,
	"layers": 1,
	"piercingBlock": 0,
	"slashingBlock": 0,
	"traumaBlock": 1,
	"magicBlock": 1,
	"piercingProtect": 0,
	"slashingProtect": 0,
	"traumaProtect": 0,
	"magicProtect": 0,
	"critProtect": 2,
	"value": Gold(10),
	"mass": 0.1,
	"nostealth": False
}

CHAIN_LEGGINGS = {
	"prototype_key": "CHAIN_LEGGINGS",
	"prototype_parent": "CLOTHING_LEGWEAR",
	"key": "chain leggings",
	"desc": "These pants are made out of chainmail, offering decent but far from perfect protection.",
	"minLayers": 1,
	"maxLayers": 1,
	"layers": 3,
	"piercingBlock": 1,
	"slashingBlock": 4,
	"traumaBlock": 1,
	"magicBlock": 1,
	"piercingProtect": 0,
	"slashingProtect": 1,
	"traumaProtect": 0,
	"magicProtect": 1,
	"critProtect": 0,
	"value": Gold(50),
	"mass": 12,
	"nostealth": True
}

LEG_PLATE = {
	"prototype_key": "LEG_PLATE",
	"prototype_parent": "CLOTHING_LEGWEAR",
	"key": "leg plate",
	"desc": "These pieces of plate armour designed for your legs, greaves and cuisses, are good at blocking the majority of blows, although they won't turn a bludgeoning attack.",
	"minLayers": 1,
	"maxLayers": 1,
	"layers": 3,
	"piercingBlock": 4,
	"slashingBlock": 6,
	"traumaBlock": 0,
	"magicBlock": 2,
	"piercingProtect": 2,
	"slashingProtect": 2,
	"traumaProtect": 0,
	"magicProtect": 0,
	"critProtect": 0,
	"value": Gold(100),
	"mass": 15,
	"nostealth": True
}

LEATHER_PANTS = {
	"prototype_key": "LEATHER_PANTS",
	"prototype_parent": "CLOTHING_LEGWEAR",
	"key": "leather pants",
	"desc": "Leather pants are stiff and an absolute pain when wet, but they provide decent protection against most hazards and are more affordable than metal armour.",
	"minLayers": 0,
	"maxLayers": 1,
	"layers": 2,
	"piercingBlock": 1,
	"slashingBlock": 1,
	"traumaBlock": 1,
	"magicBlock": 1,
	"piercingProtect": 0,
	"slashingProtect": 0,
	"traumaProtect": 0,
	"magicProtect": 0,
	"critProtect": 0,
	"value": Gold(5),
	"mass": 1,
	"nostealth": False
}

# Footwear

CLOTHING_FOOTWEAR = {
	"prototype_key": "CLOTHING_FOOTWEAR",
	"typeclass": "typeclasses.objects.Clothing",
	"key": "footwear",
	"weartype": "feet"
}

WOOL_SOCKS = {
	"prototype_key": "WOOL_SOCKS",
	"prototype_parent": "CLOTHING_FOOTWEAR",
	"key": "wool socks",
	"desc": "It has been said by some that good socks are the mainstay of a nation's economy, and these fit the bill. Woolen socks are warm, only slightly scratchy, and very versatile.",
	"minLayers": 0,
	"maxLayers": 1,
	"layers": 1,
	"piercingBlock": 0,
	"slashingBlock": 0,
	"traumaBlock": 0,
	"magicBlock": 1,
	"piercingProtect": 0,
	"slashingProtect": 0,
	"traumaProtect": 0,
	"magicProtect": 0,
	"critProtect": 0,
	"value": Gold(1),
	"mass": 0.05,
	"nostealth": False
}

SILK_SOCKS = {
	"prototype_key": "SILK_SOCKS",
	"prototype_parent": "CLOTHING_FOOTWEAR",
	"key": "silk socks",
	"desc": "For those who are too rich to be able to afford wool socks, silk is also an option. These socks are comfortable, but they are not good for much else.",
	"minLayers": 0,
	"maxLayers": 0,
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
	"value": Gold(3),
	"mass": 0.05,
	"nostealth": False
}

SANDLES = {
	"prototype_key": "SANDLES",
	"prototype_parent": "CLOTHING_FOOTWEAR",
	"key": "sandles",
	"desc": "Sandles provide some basic level of protection for their wearer's feet, fending off jagged rocks while still being easily affordable.",
	"minLayers": 0,
	"maxLayers": 1,
	"layers": 2,
	"piercingBlock": 2,
	"slashingBlock": 0,
	"traumaBlock": 0,
	"magicBlock": 0,
	"piercingProtect": 0,
	"slashingProtect": 0,
	"traumaProtect": 0,
	"magicProtect": 0,
	"critProtect": 0,
	"value": Gold(3),
	"mass": 0.1,
	"nostealth": False
}

BOOTS = {
	"prototype_key": "BOOTS",
	"prototype_parent": "CLOTHING_FOOTWEAR",
	"key": "boots",
	"desc": "These good leather boots can last almost forever and defend one's feet from all sorts of mishaps.",
	"minLayers": 1,
	"maxLayers": 2,
	"layers": 3,
	"piercingBlock": 1,
	"slashingBlock": 1,
	"traumaBlock": 0,
	"magicBlock": 1,
	"piercingProtect": 0,
	"slashingProtect": 0,
	"traumaProtect": 0,
	"magicProtect": 0,
	"critProtect": 0,
	"value": Gold(5),
	"mass": 0.1,
	"nostealth": False
}

SABATONS = {
	"prototype_key": "SABATONS",
	"prototype_parent": "CLOTHING_FOOTWEAR",
	"key": "sabatons",
	"desc": "These metal shoes are a part of any suit of plate armour. They can protect against all manner of attacks, including something as simple as stubbing your toe.",
	"minLayers": 1,
	"maxLayers": 1,
	"layers": 4,
	"piercingBlock": 1,
	"slashingBlock": 1,
	"traumaBlock": 2,
	"magicBlock": 1,
	"piercingProtect": 0,
	"slashingProtect": 0,
	"traumaProtect": 1,
	"magicProtect": 0,
	"critProtect": 0,
	"value": Gold(10),
	"mass": 0.2,
	"nostealth": True
}
