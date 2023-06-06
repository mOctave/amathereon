from evennia.prototypes import spawner
from evennia.utils import inherits_from

import random

"""
A file containing extra utility scripts that are used in other places.
"""

class Completion(Exception):
	"""
	An exception that is meant to allow for more complicated procedures than Python 'break' allows.
	"""
	
	def __init__(self, message="Uncaught completion raised, you may be missing an 'except' statement."):
		self.message = message
		super().__init__(self.message)

def printCommandPrompt(target):
	"Prints the target's command prompt."
	if not inherits_from(target, "typeclasses.characters.Character"):
		target.msg(prompt=">>----> ")
		return

	if target.db.hp > target.maxhp*0.6:
		hpcol = "|g"
	elif target.db.hp > target.maxhp*0.3:
		hpcol = "|y"
	else:
		hpcol = "|r"

	if target.db.energy > target.maxenergy*0.6:
		encol = "|g"
	elif target.db.energy > target.maxenergy*0.3:
		encol = "|w"
	else:
		encol = "|x"

	if target.db.mana > target.maxmana*0.6:
		manacol = "|m"
	elif target.db.mana > target.maxmana*0.3:
		manacol = "|b"
	else:
		manacol = "|c"

	prompt = ">>--{HP %s%s/%s|n, E %s%s/%s|n, M %s%s/%s|n}--> " % (hpcol, target.db.hp, target.maxhp,
																  encol, target.db.energy, target.maxenergy,
																  manacol, target.db.mana, target.maxmana)
	target.msg(prompt=prompt)

def d100():
	return random.randint(0, 99)

def spawnFromKey(key, target):
		print("Spawning %s!" % key)
		objList = spawner.spawn(key)
		for obj in objList:
			obj.move_to(target)
