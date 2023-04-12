#from typeclasses.characters import Character

from commands.gametime import custom_gametime

class Lighting:
    def CalcLighting(char):
        """
        Returns a report of lighting in the room of the given character.
        \n0 - Dark - It is hard to make out anything.
        \n1 - Dim - It is possible to make out shapes, but not details.
        \n2 - Lit - Everything is visible in full detail.
        """

        year, month, day, hour, min, sec = custom_gametime.custom_gametime(absolute=True)
        isoutside = "outdoors" in char.location.db.flags
        islit = "lit" in char.location.db.flags
        isdim = "semilit" in char.location.db.flags
        isunlit = "unlit" in char.location.db.flags
        darkvision = "Darkvision" in char.db.specials
        if isunlit or ((not (islit or isdim)) and isoutside and (hour < 6 or hour > 26)):
            return(1 if darkvision else 0)
        if isdim or ((not islit) and isoutside and (hour == 6 or hour == 26)):
            return(2 if darkvision else 1)
        if islit or (isoutside and hour > 6 and hour < 26):
            return(2)
