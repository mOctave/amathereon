from evennia import default_cmds
from evennia.commands.command import Command as BaseCommand

# Override the commands, to provide a custom prompt

class Command(BaseCommand):
    # ...
    def at_post_cmd(self):
        #print("COMMAND")
        "called after self.func()."
        caller = self.caller
        prompt = "{HP %s/%s, E %s/%s, M %s/%s}-->" % (caller.db.hp, caller.maxhp,
                                                   caller.db.energy, caller.maxenergy,
                                                   caller.db.mana, caller.maxmana)
        caller.msg(prompt=prompt)

class MuxCommand(default_cmds.MuxCommand):
    # ...
    def at_post_cmd(self):
        #print("MUX COMMAND")
        "called after self.func()."
        caller = self.caller
        prompt = "{HP %s/%s, E %s/%s, M %s/%s}-->" % (caller.db.hp, caller.maxhp,
                                                   caller.db.energy, caller.maxenergy,
                                                   caller.db.mana, caller.maxmana)
        caller.msg(prompt=prompt)