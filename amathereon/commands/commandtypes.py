from evennia.commands.default.muxcommand import MuxCommand as BaseMuxCommand
from evennia.commands.command import Command as BaseCommand
from evennia.utils import inherits_from
from utils import printCommandPrompt

# Override the commands, to provide a custom prompt

class Command(BaseCommand):
	# ...
	def at_pre_cmd(self):
		if inherits_from(self.caller, "typeclasses.characters.Character"):
			x = ("encumbered" in self.caller.conditions) + 1
			if self.caller.db.energy < x:
				self.caller.msg("|rYou're too tired to do that!")
				return "Out of Energy"
			else:
				self.caller.db.energy -= x
		super().at_pre_cmd()

	def at_post_cmd(self):
		super().at_post_cmd()
		print("COMMAND")
		"called after self.func()."
		printCommandPrompt(self.caller)
		

class MuxCommand(BaseMuxCommand):
	# ...
	def at_pre_cmd(self):
		if inherits_from(self.caller, "typeclasses.characters.Character"):
			x = ("encumbered" in self.caller.conditions) + 1
			if self.caller.db.energy < x:
				self.caller.msg("|rYou're too tired to do that!")
				return "Out of Energy"
			else:
				self.caller.db.energy -= x
		super().at_pre_cmd()

	def at_post_cmd(self):
		super().at_post_cmd()
		print("MUX COMMAND")
		"called after self.func()."
		printCommandPrompt(self.caller)