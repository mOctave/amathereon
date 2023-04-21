"""
A system to handle weapon experience (WEXP)
"""

from typeclasses.characters import Character

import math

class WEXPHandler:

    def increase(character, weapon, amount):
        """
        Increases WEXP for a specific character and weapon
        """
        
        weapontype = weapon.db.tname
        
        prevlevel = 0
        try:
            prevlevel = WEXPHandler.getlevel(character.db.wexp[weapontype])
        except:
            pass
        
        print(character.db.wexp)

        if character.db.wexp == None:
            character.db.wexp = {}

        try:
            character.db.wexp[weapontype] += amount
        except:
            character.db.wexp[weapontype] = amount
        
        if WEXPHandler.getlevel(character.db.wexp[weapontype]) > prevlevel:
            character.msg("|gYou've gained a level with weapon: %s!" % weapontype)

    def getlevel(wexp):
        return math.floor(math.log2(wexp/10))