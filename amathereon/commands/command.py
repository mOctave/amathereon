"""
Commands

Commands describe the input the account can do to the game.

"""

from commands.commandtypes import Command, MuxCommand 

from evennia.utils.evmenu import EvMenu
from evennia.utils import inherits_from, evtable, search, at_search_result

from evennia.contrib.game_systems.clothing.clothing import *

from world.data.race_data import *
from world.data.class_data import *
from world.data.subscription_data import Listings
from world.data.miscellaneous_data import MassConverter

from typeclasses.characters import Character
from typeclasses.objects import Object, Currency, Clothing
from typeclasses.rooms import Room

from world.currency import *

from combat.wexp import WEXPHandler

import math

#from world.char_setup import CharacterSetup

# from evennia import default_cmds


"""class Command(BaseCommand):
	\"""
	Base command (you may see this if a child command had no help text defined)

	Note that the class's `__doc__` string is used by Evennia to create the
	automatic help entry for the command, so make sure to document consistently
	here. Without setting one, the parent's docstring will show (like now).

	\"""

	# Each Command class implements the following methods, called in this order
	# (only func() is actually required):
	#
	#	 - at_pre_cmd(): If this returns anything truthy, execution is aborted.
	#	 - parse(): Should perform any extra parsing needed on self.args
	#		 and store the result on self.
	#	 - func(): Performs the actual work.
	#	 - at_post_cmd(): Extra actions, often things done after
	#		 every command, like prompts.
	#"""

# -------------------------------------------------------------
#
# The default commands inherit from
#
#   evennia.commands.default.muxcommand.MuxCommand.
#
# If you want to make sweeping changes to default commands you can
# uncomment this copy of the MuxCommand parent and add
#
#   COMMAND_DEFAULT_CLASS = "commands.command.MuxCommand"
#
# to your settings file. Be warned that the default commands expect
# the functionality implemented in the parse() method, so be
# careful with what you change.
#
# -------------------------------------------------------------

# from evennia.utils import utils
#
#
# class MuxCommand(Command):
#	 """
#	 This sets up the basis for a MUX command. The idea
#	 is that most other Mux-related commands should just
#	 inherit from this and don't have to implement much
#	 parsing of their own unless they do something particularly
#	 advanced.
#
#	 Note that the class's __doc__ string (this text) is
#	 used by Evennia to create the automatic help entry for
#	 the command, so make sure to document consistently here.
#	 """
#	 def has_perm(self, srcobj):
#		 """
#		 This is called by the cmdhandler to determine
#		 if srcobj is allowed to execute this command.
#		 We just show it here for completeness - we
#		 are satisfied using the default check in Command.
#		 """
#		 return super().has_perm(srcobj)
#
#	 def at_pre_cmd(self):
#		 """
#		 This hook is called before self.parse() on all commands
#		 """
#		 pass
#
#	 def at_post_cmd(self):
#		 """
#		 This hook is called after the command has finished executing
#		 (after self.func()).
#		 """
#		 pass
#
#	 def parse(self):
#		 """
#		 This method is called by the cmdhandler once the command name
#		 has been identified. It creates a new set of member variables
#		 that can be later accessed from self.func() (see below)
#
#		 The following variables are available for our use when entering this
#		 method (from the command definition, and assigned on the fly by the
#		 cmdhandler):
#			self.key - the name of this command ('look')
#			self.aliases - the aliases of this cmd ('l')
#			self.permissions - permission string for this command
#			self.help_category - overall category of command
#
#			self.caller - the object calling this command
#			self.cmdstring - the actual command name used to call this
#							 (this allows you to know which alias was used,
#							  for example)
#			self.args - the raw input; everything following self.cmdstring.
#			self.cmdset - the cmdset from which this command was picked. Not
#						  often used (useful for commands like 'help' or to
#						  list all available commands etc)
#			self.obj - the object on which this command was defined. It is often
#						  the same as self.caller.
#
#		 A MUX command has the following possible syntax:
#
#		   name[ with several words][/switch[/switch..]] arg1[,arg2,...] [[=|,] arg[,..]]
#
#		 The 'name[ with several words]' part is already dealt with by the
#		 cmdhandler at this point, and stored in self.cmdname (we don't use
#		 it here). The rest of the command is stored in self.args, which can
#		 start with the switch indicator /.
#
#		 This parser breaks self.args into its constituents and stores them in the
#		 following variables:
#		   self.switches = [list of /switches (without the /)]
#		   self.raw = This is the raw argument input, including switches
#		   self.args = This is re-defined to be everything *except* the switches
#		   self.lhs = Everything to the left of = (lhs:'left-hand side'). If
#					  no = is found, this is identical to self.args.
#		   self.rhs: Everything to the right of = (rhs:'right-hand side').
#					 If no '=' is found, this is None.
#		   self.lhslist - [self.lhs split into a list by comma]
#		   self.rhslist - [list of self.rhs split into a list by comma]
#		   self.arglist = [list of space-separated args (stripped, including '=' if it exists)]
#
#		   All args and list members are stripped of excess whitespace around the
#		   strings, but case is preserved.
#		 """
#		 raw = self.args
#		 args = raw.strip()
#
#		 # split out switches
#		 switches = []
#		 if args and len(args) > 1 and args[0] == "/":
#			 # we have a switch, or a set of switches. These end with a space.
#			 switches = args[1:].split(None, 1)
#			 if len(switches) > 1:
#				 switches, args = switches
#				 switches = switches.split('/')
#			 else:
#				 args = ""
#				 switches = switches[0].split('/')
#		 arglist = [arg.strip() for arg in args.split()]
#
#		 # check for arg1, arg2, ... = argA, argB, ... constructs
#		 lhs, rhs = args, None
#		 lhslist, rhslist = [arg.strip() for arg in args.split(',')], []
#		 if args and '=' in args:
#			 lhs, rhs = [arg.strip() for arg in args.split('=', 1)]
#			 lhslist = [arg.strip() for arg in lhs.split(',')]
#			 rhslist = [arg.strip() for arg in rhs.split(',')]
#
#		 # save to object properties:
#		 self.raw = raw
#		 self.switches = switches
#		 self.args = args.strip()
#		 self.arglist = arglist
#		 self.lhs = lhs
#		 self.lhslist = lhslist
#		 self.rhs = rhs
#		 self.rhslist = rhslist
#
#		 # if the class has the account_caller property set on itself, we make
#		 # sure that self.caller is always the account if possible. We also create
#		 # a special property "character" for the puppeted object, if any. This
#		 # is convenient for commands defined on the Account only.
#		 if hasattr(self, "account_caller") and self.account_caller:
#			 if utils.inherits_from(self.caller, "evennia.objects.objects.DefaultObject"):
#				 # caller is an Object/Character
#				 self.character = self.caller
#				 self.caller = self.caller.account
#			 elif utils.inherits_from(self.caller, "evennia.accounts.accounts.DefaultAccount"):
#				 # caller was already an Account
#				 self.character = self.caller.get_puppet(self.session)
#			 else:
#				 self.character = None

class CmdStats(Command):
		"""
		List stats

		Usage:
		  stats

		Displays a list of your stats.
		"""
		key = "stats"
		aliases = ["st"]
		lock = "cmd:all()"
		help_category = "General"

		def func(self):
			# Get stats, and put them in a list

			caller = self.caller
			race, charClass, bDex, bAgi, bStr, bCon, bInt, bWis, bCha, bRes, eDex, eAgi, eStr, eCon, eInt, eWis, eCha, eRes, specials, skillpts = caller.get_character_stats()
			raceData = caller.raceData
			classData = caller.classData

			# Stat Header
			data = []
			data.append("|yHere's a summary of your stats:")
			# Basic Info
			data.append("|w- You're a%s" % (raceData.after_a))
			data.append("|w- You're a%s, more specifically a%s" % (classData.wide_after_a, classData.narrow_after_a))
			# Ability Scores
			if "encumbered" in caller.conditions:
				data.append("|w- Your total dexterity is %s |W(base: %s, bonuses: %s, earned: %s, |Rencumbered|W)" % (caller.totaldex, bDex, raceData.dex + classData.dex, eDex))
				data.append("|w- Your total agility is %s |W(base: %s, bonuses: %s, earned: %s, |Rencumbered|W)" % (caller.totalagi, bAgi, raceData.agi + classData.agi, eAgi))
			else:
				data.append("|w- Your total dexterity is %s |W(base: %s, bonuses: %s, earned: %s)" % (caller.totaldex, bDex, raceData.dex + classData.dex, eDex))
				data.append("|w- Your total agility is %s |W(base: %s, bonuses: %s, earned: %s)" % (caller.totalagi, bAgi, raceData.agi + classData.agi, eAgi))
			data.append("|w- Your total strength is %s |W(base: %s, bonuses: %s, earned: %s)" % (caller.totalstr, bStr, raceData.str + classData.str, eStr))
			data.append("|w- Your total constitution is %s |W(base: %s, bonuses: %s, earned: %s)" % (caller.totalcon, bCon, raceData.con + classData.con, eCon))
			data.append("|w- Your total intelligence is %s |W(base: %s, bonuses: %s, earned: %s)" % (caller.totalint, bInt, raceData.int + classData.int, eInt))
			data.append("|w- Your total wisdom is %s |W(base: %s, bonuses: %s, earned: %s)" % (caller.totalwis, bWis, raceData.wis + classData.wis, eWis))
			data.append("|w- Your total charisma is %s |W(base: %s, bonuses: %s, earned: %s)" % (caller.totalcha, bCha, raceData.cha + classData.cha, eCha))
			data.append("|w- Your total resilience is %s |W(base: %s, bonuses: %s, earned: %s)" % (caller.totalres, bRes, raceData.res + classData.res, eRes))
			# Skills and level
			data.append("|w- You have %s skill points to spend" % (skillpts))
			data.append("|w- You are level %s |W(%s / %s EXP for next level)" % (caller.db.lvl, caller.db.exp, caller.expreq))
			# HP, Energy, Mana and Encumbrance
			data.append("|w- You have %s out of %s HP" % (caller.db.hp, caller.maxhp))
			data.append("|w- You have %s out of %s energy" % (caller.db.energy, caller.maxenergy))
			data.append("|W- You gain an energy point every %s seconds." % str((20 - math.floor(math.sqrt(caller.totalres)))/10))
			data.append("|w- You have %s out of %s mana" % (caller.db.mana, caller.maxmana))
			data.append("|W- You gain a mana point every %s seconds." % str((20 - math.floor(math.log(caller.totalres)))/5))
			encumbrance = 0
			for obj in caller.contents:
					encumbrance += obj.db.mass

			data.append("|W- You are carrying about %s of stuff." % MassConverter.AsString(encumbrance, 2))
			data.append("|W- You could carry up to %s of stuff before being encumbered." % MassConverter.AsString(caller.maxcarry, 2))
			data.append("|w- That means you are carrying %s%% of your comfortable maximum right now." % round(encumbrance / caller.maxcarry * 100))

			# Tell the caller who they're targeting
			if caller.db.target == None:
				data.append("|W- You aren't currently targeting anyone.")
			else:
				data.append("|w- You're currently targeting %s." % caller.db.target.name)

			# Print out the list of stat information

			for entry in data:
				self.caller.msg(entry)

class CmdSkills(Command):
		"""
		List skills

		Usage:
		  skills

		Displays a list of every skill and your proficiency in it.
		"""
		key = "skills"
		aliases = ["sk"]
		lock = "cmd:all()"
		help_category = "General"

		def func(self):
			caller = self.caller
			skillData = caller.db.skills

			print(caller.name + str(skillData))

			caller.msg("|yYou have the following skills:")
			for i in range(0, len(skillData)):
				x = str(list(skillData.keys())[i])
				if x == "Knowledge" or x == "Mental" or x == "Physical" or x == "Weapons":
					caller.msg("|w%s - %s" % (str(list(skillData.keys())[i]), str(list(skillData.values())[i])))
				else:
					caller.msg("|n%s - %s" % (str(list(skillData.keys())[i]), str(list(skillData.values())[i])))
			caller.msg("|wYou have %s skill points to spend." % caller.db.skillpts)

class CmdBuySkill(MuxCommand):
		"""
		Buy a skill

		Usage:
		  skillbuy <skill>

		Opens a menu that allows you to buy skills using skill points.
		"""
		key = "skillbuy"
		aliases = ["skbuy"]
		lock = "cmd:all()"
		help_category = "General"

		def func(self):
			caller = self.caller
			skillData = caller.db.skills

			if not self.args:
				caller.msg("Usage: skillbuy <skill>")
				return
			if not caller.db.skillpts:
				caller.msg("You have no skill points to spend!")
				return
			for i in range(0, len(skillData)):
				if str(list(skillData.keys())[i]) == self.args.title():
					skillData[str(list(skillData.keys())[i])] += 1
					caller.db.skillpts -= 1
					caller.msg("|wSkill bought: %s, now level %s." % (str(list(skillData.keys())[i]),str(list(skillData.values())[i])))
					caller.msg("|nYou have %s skill points remaining." % caller.db.skillpts)
					return
			caller.msg("No skill was found with that name!")

class CmdCreateChar(Command):

	key = "new character"
	aliases = ["new","chargen","charcreate"]
	lock = "cmd:all()"
	help_category = "General"

	def func(self):
		caller = self.caller
		EvMenu(caller, "world.char_setup", startnode = "node_name", cmdset_mergetype = "Replace")

class CmdLanguages(Command):
	 
	key = "languages"
	aliases = ["languages","lang"]
	lock = "cmd:all()"
	help_category = "General"

	def func(self):
		caller = self.caller

		data = []
		data.append("|wYou know the following languages:")

		for i in caller.db.languages:
			data.append("- " + i)

		recChance = caller.langRecChance
		recChance = recChance if recChance > 0 else 0

		getChance = caller.langUnderstandChance
		getChance = getChance if getChance > 0 else 0

		data.append("|wYou have a %s%% chance of recognizing a language you do not know." % recChance)
		data.append("|wYou have a %s%% chance of understanding what is spoken in another language." % getChance)

		for entry in data:
			self.caller.msg(entry)

class CmdValue(MuxCommand):
	"""
	Change the value of an object

	Usage:
	  value <obj> <value>

	Change the value of an object.

	"""

	key = "@value"
	aliases = ["@revalue"]
	locks = "cmd:perm(value) or perm(Builder)"
	help_category = "Building"

	def func(self):
		caller = self.caller

		if not self.args:
			caller.msg("Usage: <obj> = <value>")
			return
		obj = caller.search(self.arglist[0])
		if not obj:
			return
		try:
			obj.db.value = Gold(float(self.rhs))
			caller.msg("Revalued " + obj.name + " at " + self.rhs + " grains of gold.")
		except:
			caller.msg("|RFailed to revalue " + obj.name + ". Check that there is a valid number to the right of the '='.")

class CmdInventory(MuxCommand):
	"""
	view inventory

	Usage:
	  inventory
	  inv

	Shows your inventory.
	"""

	# Alternate version of the inventory command which separates
	# worn, carried, and wielded items.

	key = "inventory"
	aliases = ["inv", "i"]
	locks = "cmd:all()"
	arg_regex = r"$"

	def func(self):
		"""check inventory"""
		if not self.caller.contents:
			self.caller.msg("You are not carrying or wearing anything.")
			return

		message_list = []

		items = self.caller.contents

		carry_table = evtable.EvTable(border="header")
		wear_table = evtable.EvTable(border="header")
		wield_table = evtable.EvTable(border="header")

		carried = [obj for obj in items if not obj in self.caller.wornItemList]
		wearLists = list(self.caller.db.wornItems.values())
		wielded = [obj for obj in self.caller.db.wieldedItems]

		currencyWorth = 0

		message_list.append("|wYou are carrying:|n")
		for item in carried:
			try:
				if item.isCurrency:
					currencyWorth += float(item.db.value)
			except:
				print("Error with currency detection. This probably means it isn't currency.")
			carry_table.add_row(
				item.get_display_name(self.caller)#, item.get_display_desc(self.caller)
			)
		if carry_table.nrows == 0:
			carry_table.add_row("Nothing.", "")
		message_list.append(str(carry_table))

		message_list.append("|wYou are wearing:|n")
		for i in range(len(list(wearLists))):
			txt = list(self.caller.db.wornItems.keys())[i]
			for worn in reversed(wearLists[i]):
				item_name = worn.get_display_name(self.caller)
				if ":" in txt:
					txt += ", " + item_name
				else:
					txt += ": |u" + item_name + "|n"
			if len(wearLists[i]) == 0:
				txt += ": Nothing."
			wear_table.add_row(txt)
		if wear_table.nrows == 0:
			wear_table.add_row("Nothing.", "")
		message_list.append(str(wear_table))

		message_list.append("|wYou are wielding:|n")
		for helditem in wielded:
			# There should always be a held item, but this will avoid
			# a traceback and the inventory not displaying, just in case
			if helditem is not None:
				item_name = helditem.get_display_name(self.caller)
				wield_table.add_row(item_name)#, item.get_display_desc(self.caller)
		if wield_table.nrows == 0:
			wield_table.add_row("Nothing.", "")
		message_list.append(str(wield_table))

		if self.caller.handsFull == 0:
			message_list.append("|wYou have both hands free.")
		elif self.caller.handsFull == 1:
			message_list.append("|wYou have one hand free.")
		else:
			message_list.append("|wYour hands are full.")

		message_list.append("\n|wTotal cash:|n " + str(Gold(currencyWorth)) + ".")
		self.caller.msg("\n".join(message_list))

class CmdFlagRoom(MuxCommand):
	"""
	Adds or removes flags to a room.
	
	Usage:
	  flag <room>
	  flag/add <room> = <flag1>[,<flag2>,<flag3>...]
	  flag/remove <room> = <flag1>[,<flag2>,<flag3>...]
	  flag/clear <room>

	Examples:
	  flag here  (list all the flags in the given room)
	  flag/add #2 = forest  (add the "forest" flag to #2)
	  flag/remove Dark Hole = comfortable lit (remove the flags "comfortable" and "lit" from Dark Hole)
	  flag/clear Nondescript Room  (clear all flags from Nondescript Room)
	"""

	key = "@flag"
	aliases = []
	switch_options = ("add", "remove", "clear")
	locks = "cmd:perm(flag) or perm(Builder)"
	help_category = "Building"

	def func(self):
		caller = self.caller
		switches = self.switches
		
		# Get the location from the room.
		loc = caller.search(self.lhs)
		if not inherits_from(loc, Room):
			caller.msg("|gFlag|n: |wYou can only use this command on a room.")
			return

		# Create flag array for a room with no flags.
		if loc.db.flags == None:
			loc.db.flags = []

		if switches == []:
			if len(loc.db.flags) == 0:
				caller.msg(f"No flags attached to {loc.name}. Use flag/add to add some.")
			else:
				caller.msg("Flags:")
				for flag in loc.db.flags:
					caller.msg(f" - {flag}")

		elif switches == ["add"]:
			newflags = 0
			for flag in self.rhslist:
				if flag in loc.db.flags:
					caller.msg(f"Flag {flag} already attached to room.")
				else:
					loc.db.flags.append(flag)
					newflags += 1
			caller.msg(f"{newflags} flags added to {loc.name}.")

		elif switches == ["remove"]:
			lostflags = 0
			for flag in self.rhslist:
				if not flag in loc.db.flags:
					caller.msg(f"Flag {flag} not found!")
				else:
					loc.db.flags.remove(flag)
					lostflags += 1
			caller.msg(f"{lostflags} flags removed from {loc.name}.")

		elif switches == ["clear"]:
			lostflags = len(loc.db.flags)
			loc.db.flags = []
			caller.msg(f"All {lostflags} flags removed from {loc.name}.")

		else:
			caller.msg("You can only use one of the listed switches with this command.")

# Alternate version of the "say" command for multiple languages
class CmdLangSay(MuxCommand):
	"""
	speak as your character

	Usage:
	  say[/language] <message>

	Talk to those in your current location.
	If no language is specified you will speak in the first language
	you know (usually Common).

	Note: Language names should be all lowercase for switches.
	"""

	key = "say"
	aliases = ['"', "'"]
	switch_options = ("common",
				"dwarvish",
				"elvish",
				"uruthk",
				"underspeak",
				"koboldic",
				"giant",
				"draconic",
				"celestial",
				"thieves' cant",
				"druidic"
	)
	locks = "cmd:all()"
	help_category = "General"

	# don't require a space after `say/'/"`
	arg_regex = None

	def func(self):
		"""Run the say command"""

		caller = self.caller
		switches = self.switches

		if not self.args:
			caller.msg("Say what?")
			return

		print(switches)
		speech = self.args

		# Calling the at_pre_say hook on the character
		speech = caller.at_pre_say(speech)

		# If speech is empty, stop here
		if not speech:
			return

		# If you do not know the language you're speaking, stop here
		if len(switches) > 0 and (not switches[0].title() in caller.db.languages):
			caller.msg("You don't know that language!")
			return

		# Call the at_post_say hook on the character
		print("Saying: " + speech)
		print("Language: " + (switches[0] if len(switches) > 0 else caller.db.languages[0]).title())
		caller.at_say(speech, msg_self=True, **{"lang": (switches[0] if len(switches) > 0 else caller.db.languages[0]).title()})

class CmdWeapons(Command):
	"""
	Reports weapon experience

	Usage:
	  weapons

	Displays a list of every weapon you know and your skill with it.
	"""
	key = "weapons"
	aliases = ["wexp"]
	lock = "cmd:all()"
	help_category = "Combat"

	def func(self):
		caller = self.caller

		if len(caller.db.wexp) == 0:
			caller.msg("|yYou have no experience with any weapons.")
			return
		
		caller.msg("|yYou have experience with the following weapons:")
		for item in range(len(caller.db.wexp)):
			key = list(caller.db.wexp.keys())[item]
			val = list(caller.db.wexp.values())[item]
			s = "" if val == 1 else "s"
			caller.msg("|w- %s - %s level%s" % (key, WEXPHandler.getlevel(val), s))

class CmdShop(MuxCommand):
	"""
	Interact with a shop

	Usage:
	  buy <obj>
	  shop

	Pays the shopkeeper in exchange for ownership of an item, or lists the contents of a shop.
	"""
	key = "buy"
	aliases = ["shop", "$"]
	lock = "cmd:all()"
	help_category = "General"

	def func(self):
		key = self.args
		caller = self.caller

		if not self.args:
			ShopMessager.ReturnArray(caller.location, caller)
			return

		if not "shop" in caller.location.db.flags:
			caller.msg("This is not a shop! You cannot buy anything.")
			return
		
		if not caller.location.db.owner.location == caller.location:
			caller.msg("The shop is closed: the owner is not present.")
			return

		matches = list(search.object_search(key, None, None, caller.location.db.owner.get_objects()))

		if len(matches) == 0:
			ShopMessager.ReturnArray(caller.location, caller)
			return
		
		obj = at_search_result(matches, caller, key)
		print(obj)

		if obj == None:
			return

		if "Merchant" in caller.db.specials:
			price = Shopkeeping.FindPrice(Shopkeeping, obj.db.value * caller.location.db.markup, 'buyer')
		else:
			price = Shopkeeping.FindPrice(Shopkeeping, obj.db.value * caller.location.db.markup, 'none')

		success, overpayment = Shopkeeping.FindCoinage(Shopkeeping, caller, caller.location.db.owner, price)
		if success == True:
			obj.move_to(caller)
			caller.msg("|gYou bought %s for %s!" % (obj, price + overpayment))

class CmdOwnRoom(MuxCommand):
	"""
	Sets the owner of a room.
	
	Usage:
	  owner <room> = <character>
	  owner/clear <room>
	  owner <room>

	Give or clear ownership of the chosen room to the selected character, or check who owns it.
	"""

	key = "@owner"
	aliases = []
	switch_options = ("clear",)
	locks = "cmd:perm(own) or perm(Builder)"
	help_category = "Building"

	def func(self):
		caller = self.caller
		
		# Get the location from the room.
		loc = caller.search(self.lhs)
		if not inherits_from(loc, Room):
			caller.msg("You can only use this command on a room.")
			return
		
		# Clear ownership.
		if "clear" in self.switches:
			loc.db.owner = None
			caller.msg("Cleared ownership of %s." % loc)
			return

		# Check ownership.
		if not self.rhs:
			caller.msg("Owner of %s is %s." % (loc, loc.db.owner))
			return

		# Add ownership
		char = caller.search(self.rhs)
		if not inherits_from(char, Character):
			caller.msg("Only characters can own a room.")
			return

		loc.db.owner = char
		caller.msg("Assigned ownership of %s to %s." % (loc, char))

class CmdSubscription(MuxCommand):
	"""
	Handles characters' subscriptions.
	
	Usage:
	  sub <character>
	  sub/add <character> = <subscription id>,<period (seconds)>
	  sub/remove <character> = <subscription1>[,<subscription2>,<subscription3>...]
	  sub/clear <character>
	  sub/list

	Examples:
	  sub me  (list all the caller's subscriptions)
	  sub/add Bob = foodstuffs,60  (add a subscription for foodstuffs (one delivery every minute) to Bob)
	  sub/remove Argarath = elephants  (stop giving Argarath elephant deliveries)
	  sub/clear Tomas  (remove all of Tomas' subscriptions)
	  sub/list  (list all the possible subscriptions)
	"""

	key = "@sub"
	aliases = []
	switch_options = ("add", "remove", "clear","list")
	locks = "cmd:perm(sub) or perm(Builder)"
	help_category = "Building"

	def func(self):
		caller = self.caller
		switches = self.switches
		
		# Get a character.
		char = None
		if switches != ["list"]:
			char = caller.search(self.lhs)
			if not inherits_from(char, Character):
				caller.msg("|gSub|n: |wYou can only use this command on a character.")
				return

		if switches == []:
			if len(char.db.subscriptions) == 0:
				caller.msg(f"No subscriptions attached to {char.name}. Use sub/add to add some.")
			else:
				caller.msg("Subscriptions:")
				for sub in char.db.subscriptions:
					caller.msg(f" - {sub[0]}, every {sub[1]} seconds")

		elif switches == ["add"]:
			if len(self.rhslist) < 2:
				caller.msg("You need to provide both a subscription ID and a period!")
			elif len(self.rhslist) > 2:
				caller.msg("Extra arguments ignored.")
			char.db.subscriptions.append([self.rhslist[0],int(self.rhslist[1])])
			caller.msg(f"Subscription added to {char.name}.")

		elif switches == ["remove"]:
			lostsubs = 0
			for sub in self.rhslist:
				for entry in char.db.subscriptions:
					if entry[0] == sub:
						char.db.subscriptions.remove(entry)
						lostsubs += 1
			caller.msg(f"{lostsubs} subscriptions removed from {char.name}.")

		elif switches == ["clear"]:
			lostsubs = len(char.db.subscriptions)
			char.db.subscriptions = []
			caller.msg(f"All {lostsubs} subscriptions removed from {char.name}.")

		elif switches == ["list"]:
			for sub in Listings.All:
				caller.msg(" - "+sub[0])

		else:
			caller.msg("You can only use one of the listed switches with this command.")

class CmdWear(MuxCommand):
	"""
	Wear clothing

	Usage:
	  wear <clothing>

	Puts on the indicaated, held, article of clothing
	"""
	key = "wear"
	aliases = ["put on", "don"]
	lock = "cmd:all()"
	help_category = "General"

	def func(self):
		caller = self.caller

		# Find out if the passed args are valid
		if not self.args:
			caller.msg("Usage: wear <clothing>")
			return

		target = caller.search(self.args)

		if not target:
			return

		if not target.isClothing:
			caller.msg("That isn't clothing.")
			return
		
		if not target in caller.contents:
			caller.msg("You aren't carrying that.")
			return
		
		if target in caller.wornItemList:
			caller.msg("You're already wearing that!")
			return

		# For backwards compatibility, ensure that every character has the wornItems array and the buffness dict
		if caller.db.wornItems == None:
			caller.db.wornItems = {}
			for slot in settings.CLOTHING_SLOTS:
				caller.db.wornItems[slot] = []

		# Check if the caller can fit the clothing, and try to put it on.
		buffness = caller.buffness
		if buffness[target.db.weartype] < target.db.minLayers:
			caller.msg("That's too baggy: you'll need to wear something more underneath it.")
		elif buffness[target.db.weartype] > target.db.maxLayers:
			caller.msg("There's so much on your %s already that you can't fit that on." % target.db.weartype)
		else:
			caller.db.wornItems[target.db.weartype].append(target)
			caller.msg("You put on " + target.name + ".")

class CmdUnwear(MuxCommand):
	"""
	Take off clothing

	Usage:
	  unwear <clothing>

	Takes off the indicaated article of clothing if it is on the outside layer
	"""
	key = "unwear"
	aliases = ["take off", "doff"]
	lock = "cmd:all()"
	help_category = "General"

	def func(self):
		caller = self.caller

		# Find out if the passed args are clothing
		if not self.args:
			caller.msg("Usage: unwear <clothing>")
			return

		target = caller.search(self.args)

		if not target:
			return

		if not target.isClothing:
			caller.msg("That isn't clothing.")
			return
		
		if not target in caller.wornItemList:
			caller.msg("You aren't wearing that.")
			return
			
		if target == caller.db.wornItems[target.db.weartype][-1]:
			del caller.db.wornItems[target.db.weartype][-1]
			caller.msg("You take %s off your %s." % (target, target.db.weartype))
		else:
			caller.msg("You'd have to remove stuff on top of that before removing it!")
