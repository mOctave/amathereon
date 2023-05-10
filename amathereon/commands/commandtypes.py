from evennia import default_cmds
from evennia.commands.command import Command as BaseCommand
from utils import printCommandPrompt

# Override the commands, to provide a custom prompt

class Command(BaseCommand):
    # ...
    def at_post_cmd(self):
        print("COMMAND")
        "called after self.func()."
        printCommandPrompt(self.caller)
        

class MuxCommand(default_cmds.MuxCommand):
    # ...
    def at_post_cmd(self):
        print("MUX COMMAND")
        "called after self.func()."
        printCommandPrompt(self.caller)