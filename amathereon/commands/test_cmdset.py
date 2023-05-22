
from evennia import CmdSet

from commands.commandtypes import Command, MuxCommand

#from commands.command import CmdTestMenu

class TestCmdSet(CmdSet):

	def at_cmdset_creation(self):
		self.add(CmdGiveSkillPts())
		self.add(CmdGiveExp())
		self.add(CmdGiveHP())
		self.add(CmdGiveEnergy())
		self.add(CmdGiveMana())

class CmdGiveSkillPts(MuxCommand):
	"""
	Give skill points to user

	Usage:
	  skillget <int>

	Gives you the requested number of skill points.
	"""

	key = "skillget"
	aliases = ["skget"]
	locks = "perm(Celestial)"
	help_category = "Testing"

	def func(self):
		caller = self.caller

		if not self.args:
			caller.msg("Usage: skillget <int>")
			return
		else:
			caller.db.skillpts += int(self.args)
			caller.msg(self.args + " skill points given!")

class CmdGiveExp(MuxCommand):
	"""
	Give EXP to user

	Usage:
	  expget <int>

	Gives you the requested amount of EXP.
	"""

	key = "expget"
	aliases = ["exp"]
	locks = "perm(Celestial)"
	help_category = "Testing"

	def func(self):
		caller = self.caller

		if not self.args:
			caller.msg("Usage: expget <int>")
			return
		else:
			caller.db.exp += int(self.args)
			caller.msg(self.args + " EXP given!")

class CmdGiveHP(MuxCommand):
	"""
	Give HP to user

	Usage:
	  hpget <int>

	Gives you the requested amount of HP.
	"""

	key = "hpget"
	aliases = ["hp"]
	locks = "perm(Celestial)"
	help_category = "Testing"

	def func(self):
		caller = self.caller

		if not self.args:
			caller.msg("Usage: hpget <int>")
			return
		else:
			caller.db.hp += int(self.args)
			caller.msg(self.args + " HP given!")

class CmdGiveEnergy(MuxCommand):
	"""
	Give energy to user

	Usage:
	  energyget <int>

	Gives you the requested amount of energy.
	"""

	key = "energyget"
	aliases = ["en"]
	locks = "perm(Celestial)"
	help_category = "Testing"

	def func(self):
		caller = self.caller

		if not self.args:
			caller.msg("Usage: energyget <int>")
			return
		else:
			caller.db.energy += int(self.args)
			caller.msg(self.args + " energy given!")

class CmdGiveMana(MuxCommand):
	"""
	Give mana to user

	Usage:
	  managet <int>

	Gives you the requested amount of mana.
	"""

	key = "managet"
	aliases = ["ma"]
	locks = "perm(Celestial)"
	help_category = "Testing"

	def func(self):
		caller = self.caller

		if not self.args:
			caller.msg("Usage: managet <int>")
			return
		else:
			caller.db.mana += int(self.args)
			caller.msg(self.args + " mana given!")
