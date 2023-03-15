"""
Commands

Commands describe the input the account can do to the game.

"""

from evennia.commands.command import Command as BaseCommand
from evennia.commands.default.muxcommand import MuxCommand

from evennia.utils.evmenu import EvMenu

from world.race_data import *
from world.class_data import *

#from world.char_setup import CharacterSetup

# from evennia import default_cmds


class Command(BaseCommand):
    """
    Base command (you may see this if a child command had no help text defined)

    Note that the class's `__doc__` string is used by Evennia to create the
    automatic help entry for the command, so make sure to document consistently
    here. Without setting one, the parent's docstring will show (like now).

    """

    # Each Command class implements the following methods, called in this order
    # (only func() is actually required):
    #
    #     - at_pre_cmd(): If this returns anything truthy, execution is aborted.
    #     - parse(): Should perform any extra parsing needed on self.args
    #         and store the result on self.
    #     - func(): Performs the actual work.
    #     - at_post_cmd(): Extra actions, often things done after
    #         every command, like prompts.
    #
    pass


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
#     """
#     This sets up the basis for a MUX command. The idea
#     is that most other Mux-related commands should just
#     inherit from this and don't have to implement much
#     parsing of their own unless they do something particularly
#     advanced.
#
#     Note that the class's __doc__ string (this text) is
#     used by Evennia to create the automatic help entry for
#     the command, so make sure to document consistently here.
#     """
#     def has_perm(self, srcobj):
#         """
#         This is called by the cmdhandler to determine
#         if srcobj is allowed to execute this command.
#         We just show it here for completeness - we
#         are satisfied using the default check in Command.
#         """
#         return super().has_perm(srcobj)
#
#     def at_pre_cmd(self):
#         """
#         This hook is called before self.parse() on all commands
#         """
#         pass
#
#     def at_post_cmd(self):
#         """
#         This hook is called after the command has finished executing
#         (after self.func()).
#         """
#         pass
#
#     def parse(self):
#         """
#         This method is called by the cmdhandler once the command name
#         has been identified. It creates a new set of member variables
#         that can be later accessed from self.func() (see below)
#
#         The following variables are available for our use when entering this
#         method (from the command definition, and assigned on the fly by the
#         cmdhandler):
#            self.key - the name of this command ('look')
#            self.aliases - the aliases of this cmd ('l')
#            self.permissions - permission string for this command
#            self.help_category - overall category of command
#
#            self.caller - the object calling this command
#            self.cmdstring - the actual command name used to call this
#                             (this allows you to know which alias was used,
#                              for example)
#            self.args - the raw input; everything following self.cmdstring.
#            self.cmdset - the cmdset from which this command was picked. Not
#                          often used (useful for commands like 'help' or to
#                          list all available commands etc)
#            self.obj - the object on which this command was defined. It is often
#                          the same as self.caller.
#
#         A MUX command has the following possible syntax:
#
#           name[ with several words][/switch[/switch..]] arg1[,arg2,...] [[=|,] arg[,..]]
#
#         The 'name[ with several words]' part is already dealt with by the
#         cmdhandler at this point, and stored in self.cmdname (we don't use
#         it here). The rest of the command is stored in self.args, which can
#         start with the switch indicator /.
#
#         This parser breaks self.args into its constituents and stores them in the
#         following variables:
#           self.switches = [list of /switches (without the /)]
#           self.raw = This is the raw argument input, including switches
#           self.args = This is re-defined to be everything *except* the switches
#           self.lhs = Everything to the left of = (lhs:'left-hand side'). If
#                      no = is found, this is identical to self.args.
#           self.rhs: Everything to the right of = (rhs:'right-hand side').
#                     If no '=' is found, this is None.
#           self.lhslist - [self.lhs split into a list by comma]
#           self.rhslist - [list of self.rhs split into a list by comma]
#           self.arglist = [list of space-separated args (stripped, including '=' if it exists)]
#
#           All args and list members are stripped of excess whitespace around the
#           strings, but case is preserved.
#         """
#         raw = self.args
#         args = raw.strip()
#
#         # split out switches
#         switches = []
#         if args and len(args) > 1 and args[0] == "/":
#             # we have a switch, or a set of switches. These end with a space.
#             switches = args[1:].split(None, 1)
#             if len(switches) > 1:
#                 switches, args = switches
#                 switches = switches.split('/')
#             else:
#                 args = ""
#                 switches = switches[0].split('/')
#         arglist = [arg.strip() for arg in args.split()]
#
#         # check for arg1, arg2, ... = argA, argB, ... constructs
#         lhs, rhs = args, None
#         lhslist, rhslist = [arg.strip() for arg in args.split(',')], []
#         if args and '=' in args:
#             lhs, rhs = [arg.strip() for arg in args.split('=', 1)]
#             lhslist = [arg.strip() for arg in lhs.split(',')]
#             rhslist = [arg.strip() for arg in rhs.split(',')]
#
#         # save to object properties:
#         self.raw = raw
#         self.switches = switches
#         self.args = args.strip()
#         self.arglist = arglist
#         self.lhs = lhs
#         self.lhslist = lhslist
#         self.rhs = rhs
#         self.rhslist = rhslist
#
#         # if the class has the account_caller property set on itself, we make
#         # sure that self.caller is always the account if possible. We also create
#         # a special property "character" for the puppeted object, if any. This
#         # is convenient for commands defined on the Account only.
#         if hasattr(self, "account_caller") and self.account_caller:
#             if utils.inherits_from(self.caller, "evennia.objects.objects.DefaultObject"):
#                 # caller is an Object/Character
#                 self.character = self.caller
#                 self.caller = self.caller.account
#             elif utils.inherits_from(self.caller, "evennia.accounts.accounts.DefaultAccount"):
#                 # caller was already an Account
#                 self.character = self.caller.get_puppet(self.session)
#             else:
#                 self.character = None

class CmdStats(BaseCommand):
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

            race, charClass, bDex, bAgi, bStr, bCon, bInt, bWis, bCha, bRes, eDex, eAgi, eStr, eCon, eInt, eWis, eCha, eRes, specials, skillpts = self.caller.get_character_stats()
            raceData = Races.getRaceFromKey(race)
            classData = Classes.getClassFromKey(charClass)

            data = []
            data.append("|yHere's a summary of your stats:")
            data.append("|w- You're a%s" % (raceData.after_a))
            data.append("|w- You're a%s, more specifically a%s" % (classData.wide_after_a, classData.narrow_after_a))
            data.append("|w- Your total dexterity is %s |W(base: %s, bonuses: %s, earned: %s)" % (bDex + eDex + raceData.dex + classData.dex, bDex, raceData.dex + classData.dex, eDex))
            data.append("|w- Your total agility is %s |W(base: %s, bonuses: %s, earned: %s)" % (bAgi + eAgi + raceData.agi + classData.agi, bAgi, raceData.agi + classData.agi, eAgi))
            data.append("|w- Your total strength is %s |W(base: %s, bonuses: %s, earned: %s)" % (bStr + eStr + raceData.str + classData.str, bStr, raceData.str + classData.str, eStr))
            data.append("|w- Your total constitution is %s |W(base: %s, bonuses: %s, earned: %s)" % (bCon + eCon + raceData.con + classData.con, bCon, raceData.con + classData.con, eCon))
            data.append("|w- Your total intelligence is %s |W(base: %s, bonuses: %s, earned: %s)" % (bInt + eInt + raceData.int + classData.int, bInt, raceData.int + classData.int, eInt))
            data.append("|w- Your total wisom is %s |W(base: %s, bonuses: %s, earned: %s)" % (bWis + eWis + raceData.wis + classData.wis, bWis, raceData.wis + classData.wis, eWis))
            data.append("|w- Your total charisma is %s |W(base: %s, bonuses: %s, earned: %s)" % (bCha + eCha + raceData.cha + classData.cha, bCha, raceData.cha + classData.cha, eCha))
            data.append("|w- Your total resilience is %s |W(base: %s, bonuses: %s, earned: %s)" % (bRes + eRes + raceData.res + classData.res, bRes, raceData.res + classData.res, eRes))
            data.append("|w- You have %s skill points to spend." % (skillpts))

            # Print out the list of stat information

            for entry in data:
                self.caller.msg(entry)

class CmdSkills(BaseCommand):
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

class CmdGiveSkillPts(MuxCommand):
    """
    Give skill points to user

    Usage:
      skillget <int>

    Gives you the requested number of skill points.
    """

    key = "skillget"
    aliases = ["skget"]
    lock = "perm(Admin)"
    help_category = "Testing"

    def func(self):
        caller = self.caller

        if not self.args:
            caller.msg("Usage: skillget <int>")
            return
        else:
            caller.db.skillpts += int(self.args)
            caller.msg(self.args + " skill points given!")

class CmdCreateChar(Command):

    key = "new character"
    aliases = ["new","chargen","charcreate"]
    lock = "cmd:all()"
    help_category = "General"

    def func(self):
        caller = self.caller
        EvMenu(caller, "world.char_setup", startnode = "node_name", cmdset_mergetype = "Replace")