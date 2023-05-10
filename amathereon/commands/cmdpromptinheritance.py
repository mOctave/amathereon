from evennia import default_cmds, CmdSet
from evennia.commands.default import syscommands
from commands.commandtypes import Command, MuxCommand

class PromptCommandSet(CmdSet):
    def at_cmdset_creation(self):
        self.add(CmdLook())
        self.add(CmdNick())
        self.add(CmdSetDesc())
        self.add(CmdGet())
        self.add(CmdDrop())
        self.add(CmdGive())
        self.add(CmdSay())
        self.add(CmdWhisper())
        self.add(CmdPose())
        self.add(CmdAccess())
        #self.add(SystemNoInput())
        #self.add(SystemNoMatch())
        #self.add(SystemMultimatch())
        #self.add(SystemSendToChannel())


class CmdLook(default_cmds.CmdLook, MuxCommand):
    pass

class CmdNick(default_cmds.CmdNick, MuxCommand):
    pass

class CmdSetDesc(default_cmds.CmdSetDesc, MuxCommand):
    pass

class CmdGet(default_cmds.CmdGet, MuxCommand):
    pass

class CmdDrop(default_cmds.CmdDrop, MuxCommand):
    pass

class CmdGive(default_cmds.CmdGive, MuxCommand):
    pass

class CmdSay(default_cmds.CmdSay, MuxCommand):
    pass

class CmdWhisper(default_cmds.CmdWhisper, MuxCommand):
    pass

class CmdPose(default_cmds.CmdPose, MuxCommand):
    pass

class CmdAccess(default_cmds.CmdAccess, MuxCommand):
    pass

class SystemNoInput(syscommands.SystemNoInput, MuxCommand):
    pass

class SystemNoMatch(syscommands.SystemNoMatch, MuxCommand):
    pass

class SystemMultimatch(syscommands.SystemMultimatch, MuxCommand):
    pass
