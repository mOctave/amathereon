from evennia.commands.default.muxcommand import MuxCommand

from evennia.utils import inherits_from
from typeclasses.characters import Character

from typeclasses.scripts import Script

from combat.wexp import WEXPHandler

import random

class CmdTarget(MuxCommand):
	"""
	Target another character

	Usage:
	  target <character>
	  target
	
	Switches:
	  safe  - If no target is found, stop targeting anyone.

	Sets another character as the target for your attacks,
	or stop targeting another character.
	"""
	key = "target"
	aliases = ["untarget", "t"]
	switch_options = ("safe")
	lock = "cmd:all()"
	help_category = "Combat"

	def func(self):
		caller = self.caller

		# Target no one
		if not self.args:
			caller.db.target = None
			caller.msg("You are no longer targeting anyone.")
			return
		
		# Look for the target
		found = caller.search(self.args)

		if not found:
			if "safe" in self.switches:
				caller.db.target = None
				caller.msg("You are no longer targeting anyone.")
			return

		# Deal with a target that is not a character
		if not inherits_from(found, Character):
			caller.msg("You can only target other people.")
			if "safe" in self.switches:
				caller.db.target = None
				caller.msg("You are no longer targeting anyone.")
			return

		# Set a valid target
		caller.db.target = found
		caller.msg("You are now targeting " + caller.db.target.name + ".")

class CombatEngine(Script):
	"""
	Every second, all characters spontaneously undergo combat,
	lashing out at those they're currently targeting.

	This is the script that handles that.
	"""
	def at_script_creation(self):
		self.key = "combat_engine_script"
		self.desc = "Runs a cycle of combat."
		self.interval = 1
		self.persistent = True
	
	def at_repeat(self):
		characters = list(Character.objects.typeclass_search(Character, True, False))

		for character in characters:
			target = character.db.target
			if target != None and character.location == target.location and character.location != None:
				for weapon in character.db.wieldedItems:
					self.makeAttack(character, target, weapon)

	def makeAttack(self, actor: Character, target: Character, weapon):
		"""
		The actual code to make an attack.
		Takes the attacker as the first parameter, the attackee as the second,
		and the weapon as the third.
		"""
		hitChance = self.getHitChance(actor, target, weapon)
		damage, iscrit = self.getDamage(actor, target, weapon)
		#actor.msg("Weapon: %s, Hit Chance: %s, Damage: %s." % (weapon, hitChance, damage))

		if actor.random < hitChance:
			actor.msg("|yYou hit %s with %s!" % (target.name, weapon))
			actor.msg("|yYou deal %s damage!" % damage)
			target.msg("|r%s hits you with %s!" % (actor.name, weapon))
			target.msg("|rYou've been hurt, taking %s damage!" % damage)
			WEXPHandler.increase(actor, weapon, 5)
			WEXPHandler.increase(target, weapon, 1)
			if iscrit:
				actor.msg("|yIt's a critical hit!")
				target.msg("|rIt's a critical hit!")
				WEXPHandler.increase(actor, weapon, 5)
		else:
			actor.msg("|YYou make an attack at %s with %s, but it fails to connect." % (target.name, weapon))
			target.msg("|R%s attacks you with %s! Luckily, you evade the blow." % (actor.name, weapon))
			WEXPHandler.increase(actor, weapon, 1)
			WEXPHandler.increase(target, weapon, 1)

	def getHitChance(self, actor: Character, target: Character, weapon):
		# First, figure out the dexterity-agility balance
		totalhit = actor.totaldex - target.totalagi
		# Then, add then weapon hit chance
		totalhit += weapon.db.hitChance
		# Next, run through weapons carried by the target to check for parries
		try:
			for blocker in target.db.wieldedItems:
				totalhit -= blocker.db.parryChance
		except:
			target.db.wieldedItems = []
			for blocker in target.db.wieldedItems:
				totalhit -= blocker.db.parryChance

		return totalhit

	def getDamage(self, actor: Character, target: Character, weapon):
		iscrit = False
		# First, figure out base damage
		totaldmg = actor.totalstr + random.randint(weapon.db.minDamage, weapon.db.maxDamage)
		# Deal with crit chances
		critbuff = 1 + (actor.totalint - target.totalwis + actor.totaldex - actor.totalagi) / 100
		if (actor.random < weapon.db.critChance * critbuff):
			iscrit = True
			totaldmg *= 3

		# Damage resistence comes AFTER critical hits are dealt with
		totaldmg -= int(target.totalcon / 2)

		return totaldmg, iscrit