from evennia.commands.command import Command
from evennia.commands.default.muxcommand import MuxCommand

from evennia.utils import inherits_from
from typeclasses.objects import Weapon

class CmdWield(MuxCommand):
		"""
		Wield a weapon

		Usage:
		  wield <weapon>

		Holds the indicated weapon ready to be used in combat.
		"""
		key = "wield"
		aliases = ["hold"]
		lock = "cmd:all()"
		help_category = "Combat"

		def func(self):
			caller = self.caller

			# Find out if the passed args are a weapon
			if not self.args:
				caller.msg("Usage: wield <weapon>")
				return

			target = caller.search(self.args)

			if not inherits_from(target, Weapon):
				caller.msg("That isn't a weapon.")
				return
			
			if not target in caller.contents:
				caller.msg("You aren't carrying that.")
				return

			# For backwards compatibility, ensure that every character has the wieldedItems array
			if caller.db.wieldedItems == None:
				caller.db.wieldedItems = []

			# Check if the caller has enough hands to wield the weapon, and do so if yes
			if caller.handsFull + target.db.hands <= 2:
				caller.db.wieldedItems.append(target)
				caller.msg("You start wielding a " + target.name + ".")

class CmdUnwield(MuxCommand):
		"""
		Stop wielding a weapon

		Usage:
		  unwield <weapon>

		Stows the given wielded weapon.
		"""
		key = "unwield"
		aliases = ["stow"]
		lock = "cmd:all()"
		help_category = "Combat"

		def func(self):
			caller = self.caller

			# Find out if the passed args are a weapon
			if not self.args:
				caller.msg("Usage: unwield <weapon>")
				return
			
			target = caller.search(self.args)

			# Stow the weapon or throw an error
			if target in caller.db.wieldedItems:
				caller.db.wieldedItems.remove(target)
				caller.msg("You stow a " + target.name + ".")
			else:
				caller.msg("You're not wielding that.")