"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia.objects.objects import DefaultCharacter
from evennia.contrib.game_systems.clothing import ClothedCharacter
from evennia import TICKER_HANDLER

from world.class_data import Classes
from world.race_data import Races

import typeclasses.scripts

from .objects import ObjectParent

import random
import math

class Character(ObjectParent, ClothedCharacter):
    """
    The Character defaults to reimplementing some of base Object's hook methods with the
    following functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead).
    at_post_move(source_location) - Launches the "look" command after every move.
    at_post_unpuppet(account) -  when Account disconnects from the Character, we
                    store the current location in the pre_logout_location Attribute and
                    move it to a None-location so the "unpuppeted" character
                    object does not need to stay on grid. Echoes "Account has disconnected"
                    to the room.
    at_pre_puppet - Just before Account re-connects, retrieves the character's
                    pre_logout_location Attribute and move it back on the grid.
    at_post_puppet - Echoes "AccountName has entered the game" to the room.

    """

    specials: list[str] = [""]
    skillpts: int = 0

    @property
    def totaldex(self):
        return(self.db.baseDexterity + self.db.earnedDexterity + self.classData.dex + self.raceData.dex)

    @property
    def totalagi(self):
        return(self.db.baseAgility + self.db.earnedAgility + self.classData.agi + self.raceData.agi)

    @property
    def totalstr(self):
        return(self.db.baseStrength + self.db.earnedStrength + self.classData.str + self.raceData.str)

    @property
    def totalcon(self):
        return(self.db.baseConstitution + self.db.earnedConstitution + self.classData.con + self.raceData.con)

    @property
    def totalint(self):
        return(self.db.baseIntelligence + self.db.earnedIntelligence + self.classData.int + self.raceData.int)

    @property
    def totalwis(self):
        return(self.db.baseWisdom + self.db.earnedWisdom + self.classData.wis + self.raceData.wis)

    @property
    def totalcha(self):
        return(self.db.baseCharisma + self.db.earnedCharisma + self.classData.cha + self.raceData.cha)

    @property
    def totalres(self):
        return(self.db.baseResilience + self.db.earnedResilience + self.classData.res + self.raceData.res)

    @property
    def maxhp(self):
        return(10 + (3 + (2 * self.totalcon) + self.totalres) * self.db.lvl)
    
    @property
    def maxenergy(self):
        _endurancebonus = 10 * self.db.skills["Physical: Endurance"]
        return(20 + (3 + self.totalres) * self.db.lvl + (2 * self.totalres) + _endurancebonus)
    
    @property
    def expreq(self):
        return(30 * math.floor(self.db.lvl ** 1.5))
    
    @property
    def classData(self):
        return(Classes.getClassFromKey(self.db.charClass))
    
    @property
    def raceData(self):
        return(Races.getRaceFromKey(self.db.race))
    
    @property
    def random(self):
        return(random.randint(0, 99))

    energy_counter: int = 0

    def at_object_creation(self):
        #set persistent attributes
        self.db.race = "Unborn"
        self.db.charClass = "Would-Be Adventurer"

        self.db.baseDexterity = random.randint(3,7)
        self.db.baseAgility = random.randint(3,7)
        self.db.baseStrength = random.randint(3,7)
        self.db.baseConstitution = random.randint(3,7)
        self.db.baseIntelligence = random.randint(3,7)
        self.db.baseWisdom = random.randint(3,7)
        self.db.baseCharisma = random.randint(3,7)
        self.db.baseResilience = random.randint(3,7)

        self.db.earnedDexterity = 0
        self.db.earnedAgility = 0
        self.db.earnedStrength = 0
        self.db.earnedConstitution = 0
        self.db.earnedIntelligence = 0
        self.db.earnedWisdom = 0
        self.db.earnedCharisma = 0
        self.db.earnedResilience = 0

        self.db.specials: list[str] = []
        self.db.skillpts = 0
        self.db.skills: dict = {
            "Knowledge": 0,
            "Knowledge: Arcana": 0,
            "Knowledge: Culture": 0,
            "Knowledge: History": 0,
            "Knowledge: Linguistics": 0,
            "Knowledge: Medicine": 0,
            "Knowledge: Wilderness": 0,
            "Mental": 0,
            "Mental: Deception": 0,
            "Mental: Intimidation": 0,
            "Mental: Investigation": 0,
            "Mental: Perception": 0,
            "Mental: Performance": 0,
            "Mental: Persuasion": 0,
            "Physical": 0,
            "Physical: Acrobatics": 0,
            "Physical: Athletics": 0,
            "Physical: Endurance": 0,
            "Physical: Intimidation": 0,
            "Physical: Sleight of Hand": 0,
            "Physical: Stealth": 0,
            "Weapons": 0,
            "Weapons: Improvised": 0,
            "Weapons: Melee": 0,
            "Weapons: Piercing": 0,
            "Weapons: Ranged": 0,
            "Weapons: Slashing": 0,
            "Weapons: Trauma": 0
        }

        self.db.lvl = 1
        self.db.exp = 0
        TICKER_HANDLER.add(5, self.check_level_up)

        self.db.hp = self.maxhp

        self.db.energy = self.maxenergy
        self.scripts.add(typeclasses.scripts.UpdateEnergy)

    def check_level_up(self):
        """
        Check if it's time for the player's character to gain a level, and award bonuses if so.
        """
        if self.db.exp >= self.expreq:
            # Store max HP and energy from before level-up
            mhp = self.maxhp
            men = self.maxenergy

            # Level up
            self.db.lvl += 1
            self.db.skillpts += 1 + math.ceil(math.sqrt(self.db.lvl))
            self.msg("|gSuddenly, you're feeling stronger! You've levelled up to level " + str(self.db.lvl) + "!")
            self.msg("|G+%s skill points!" % (1 + math.ceil(math.sqrt(self.db.lvl))))

            # Boost ability scores
            if self.random < self.classData.dex_up:
                self.db.earnedDexterity += 1
                self.msg("|G+1 DEX!")
            if self.random < self.classData.agi_up:
                self.db.earnedAgility += 1
                self.msg("|G+1 AGI!")
            if self.random < self.classData.str_up:
                self.db.earnedStrength += 1
                self.msg("|G+1 STR!")
            if self.random < self.classData.con_up:
                self.db.earnedConstitution += 1
                self.msg("|G+1 CON!")
            if self.random < self.classData.int_up:
                self.db.earnedIntelligence += 1
                self.msg("|G+1 INT!")
            if self.random < self.classData.wis_up:
                self.db.earnedWisdom += 1
                self.msg("|G+1 WIS!")
            if self.random < self.classData.cha_up:
                self.db.earnedCharisma += 1
                self.msg("|G+1 CHA!")
            if self.random < self.classData.res_up:
                self.db.earnedResilience += 1
                self.msg("|G+1 RES!")
            
            # Report max energy and HP change
            self.msg("|G+%s max HP!" % (self.maxhp - mhp))
            self.msg("|G+%s max energy!" % (self.maxenergy - men))

            # Rescale HP
            self.db.hp = math.floor(self.db.hp * self.maxhp / mhp)

    def get_character_stats(self):
        """
        Get data such as class, stats, and skills for the player.
        """
        return self.db.race, self.db.charClass, self.db.baseDexterity, self.db.baseAgility, self.db.baseStrength, self.db.baseConstitution, self.db.baseIntelligence, self.db.baseWisdom, self.db.baseCharisma, self.db.baseResilience, self.db.earnedDexterity, self.db.earnedAgility, self.db.earnedStrength, self.db.earnedConstitution, self.db.earnedIntelligence, self.db.earnedWisdom, self.db.earnedCharisma, self.db.earnedResilience, self.db.specials, self.db.skillpts
