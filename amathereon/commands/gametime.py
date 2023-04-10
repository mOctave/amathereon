"""
Gametime related stuff
"""

from evennia.commands.command import Command
from evennia.contrib.base_systems import custom_gametime

class TimeArrays():
	monthArray = ["Heatrise","Harvestgold","Treefall","Waterlength","Icefall","Newthaw","Leafbloom","Longingday"]
	dayArray = ["First of the New","Second of the New","Third of the New","Fourth of the New","Fifth of the New","Sixth of the New","Seventh of the New","Eighth of the New","Ninth of the New","Tenth of the New","Eleventh of the New","Twelfth of the New","Thirteenth of the New","Fourteenth of the New","Fifteenth of the New","Sixteenth of the New","Seventeenth of the New","Eighteenth of the New","Middleday","First of the Old","Second of the Old","Third of the Old","Fourth of the Old","Fifth of the Old","Sixth of the Old","Seventh of the Old","Eighth of the Old","Ninth of the Old","Tenth of the Old","Eleventh of the Old","Twelfth of the Old","Thirteenth of the Old","Fourteenth of the Old","Fifteenth of the Old","Sixteenth of the Old","Seventeenth of the Old","Eighteenth of the Old"]

class CmdTime(Command):

    """
    Display the time.

    Syntax:
        time

    """

    key = "time"
    locks = "cmd:all()"

    def func(self):
        """Execute the time command."""
        # Get the absolute game time
        year, month, day, hour, min, sec = custom_gametime.custom_gametime(absolute=True)
        string = "It is the %s, %s, in the year %s." % (TimeArrays.dayArray[day], TimeArrays.monthArray[month], year)
        if hour == 0:
            string += "\nIt looks to be a little past midnight."
        else:
            string += "\nIt looks to be a little past {hour} bells."
        self.msg(string.format(year=year, month=month, day=day,
                hour=hour, min=min, sec=sec))