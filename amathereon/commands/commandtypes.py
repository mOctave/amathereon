from evennia.commands.default.muxcommand import MuxCommand as BaseMuxCommand
from evennia.commands.command import Command as BaseCommand
from utils import printCommandPrompt

# Override the commands, to provide a custom prompt

class Command(BaseCommand):
    # ...
    def at_post_cmd(self):
        print("COMMAND")
        "called after self.func()."
        printCommandPrompt(self.caller)
        

class MuxCommand(BaseMuxCommand):
    # ...
    def at_post_cmd(self):
        print("MUX COMMAND")
        "called after self.func()."
        printCommandPrompt(self.caller)