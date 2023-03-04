"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia.objects.objects import DefaultCharacter

from .objects import ObjectParent

import random


class Character(ObjectParent, DefaultCharacter):
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

    def at_object_creation(self):
        """
        Called only at initial creation. This is a rather silly
        example since ability scores should vary from Character to
        Character and is usually set during some character
        generation step instead.
        """
        #set persistent attributes
        self.db.race = "Unborn"
        self.db.wideClass = "Citizen"
        self.db.narrowClass = "Would-Be Adventurer"

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

    def get_character_stats(self):
        """
        Get data such as class, stats, and skills for the player.
        """
        return self.db.race, self.db.charClass, self.db.baseDexterity, self.db.baseAgility, self.db.baseStrength, self.db.baseConstitution, self.db.baseIntelligence, self.db.baseWisdom, self.db.baseCharisma, self.db.baseResilience, self.db.earnedDexterity, self.db.earnedAgility, self.db.earnedStrength, self.db.earnedConstitution, self.db.earnedIntelligence, self.db.earnedWisdom, self.db.earnedCharisma, self.db.earnedResilience

    pass
