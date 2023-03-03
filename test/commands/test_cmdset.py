
from evennia import CmdSet

#from commands.command import CmdTestMenu

class TestCmdSet(CmdSet):

    def at_cmdset_creation(self):
        print()
        #self.add(CmdTestMenu())
