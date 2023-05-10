"""
Room

Rooms are simple containers that has no location of their own.

"""

from commands.gametime import custom_gametime

from evennia.objects.objects import DefaultRoom
from evennia import TICKER_HANDLER
from evennia.utils import inherits_from

from world.lighting import Lighting

from .objects import ObjectParent

from utils import printCommandPrompt

import random

class Room(ObjectParent, DefaultRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """
    def on_object_creation(self):
        self.db.flags = []
        self.db.saleprots = []
        self.db.markup = 1.10
        TICKER_HANDLER.add(20, self.print_flavour_text)

    def print_flavour_text(self, *args, **kwargs):
        echoes = Echoes.ECHOES_EMPTY
        year, month, day, hour, min, sec = custom_gametime.custom_gametime(absolute=True)
        if hour < 6 or hour > 26:
            echoes += Echoes.ECHOES_NIGHT
        """if Lighting.CalcLighting() == 0:
            echoes += Echoes.ECHOES_DARKNESS
        elif Lighting.CalcLighting() == 1:
            echoes += Echoes.ECHOES_DIMNESS""" # Deal with this later

        if "outdoors" in self.db.flags:
            echoes += Echoes.ECHOES_OUTDOORS
            echoes.append(Echoes.ECHOES_TIME[hour])
        if "street" in self.db.flags and hour > 6 and hour < 26:
            echoes += Echoes.ECHOES_STREET
        if "urban" in self.db.flags:
            echoes += Echoes.ECHOES_URBAN
        if "forest" in self.db.flags:
            echoes += Echoes.ECHOES_FOREST
        
        chosenEcho = random.choice(echoes)
        if chosenEcho != "":
            self.msg_contents(chosenEcho)
            for obj in self.contents:
                if inherits_from(obj, "typeclasses.characters.Character"):
                    printCommandPrompt(obj)
    
    def getRecursiveLightingCheck(self):
        total_contents = self.contents
        for obj in self.contents:
            total_contents.extend(obj.contents)

        for obj in total_contents:
            try:
                if obj.db.isLit:
                    return True
            except:
                pass

        return False

class Echoes:
    ECHOES_EMPTY = [
        "",
        "",
        "",
        "",
        ""
    ]

    ECHOES_NIGHT = [
        "For a moment, the night is silent.",
        "It is nighttime, and your bones long for rest.",
        "You yawn, unable to stop yourself.",
        "Little creatures, inaudible in the daytime, sing to each other in chirps and whistles.",
        "You think of all the crimes that have been committed while the world is sleeping.",
        ""
    ]

    ECHOES_DARKNESS = [
        "You hold up your hand in fron of your face, but can't see it.",
        "It's pitch black.",
        "You wonder what you cannot see in this inky blackness."
    ]

    ECHOES_DIMNESS = [
        "Something hairy moves in the twilight.",
        "Vague shapes move at the edge of your vision.",
        "You see the world, painted in shades of grey."
    ]

    ECHOES_TIME = [
        "It must be around midnight.",
        "You hear a scuffling noise in the darkness.",
        "A wolf howls in the distance, still audible across dozens of leagues.",
        "It's the middle of the night.",
        "In the distance, you hear the crow of an insomniac rooster.",
        "It's the middle of the night.",
        "It must be almost dawn.",
        "The horizon is smudged with a slightly lighter shade of black.",
        "Day is dawning, the sun is only now visible.",
        "The early morning sun casts long shadows.",
        "The sun rises inexorably in the sky.",
        "It's about midmorning.",
        "It's about the time that most of the nobility starts in on breakfast, now.",
        "The sun approaches its apex.",
        "Everything begins to warm up as it approaches noon."
        "It's noon, 15 bells. The sun stands high in the sky.",
        "The sun begins to slide back down through the heavens.",
        "It's easy to see and hard to hide in the early afternoon sun.",
        "The hot afternoon sun beats down on you.",
        "It's beginning to get rather toasty out.",
        "It's mid-afternoon and getting later by the minute.",
        "The sun is about three quarters of the way through its daily journey.",
        "Now, the sun is often obscured, as it's approaching evening.",
        "It is dusk and the sun is setting.",
        "The sky is streaked with many colours, as if an elcectic artist is mourning the day's passing.",
        "It is night, but the night is still young.",
        "It's the middle of the night.",
        "Bats flutter by.",
        "It's the middle of the night.",
        "It's the middle of the night."
    ]

    ECHOES_OUTDOORS = [
        "A light breeze buffets you."
    ]

    ECHOES_STREET = [
        "A carriage clatters by.",
        "Some mounted watchmen ride past you in a hurry.",
        "A hard-looking man walks past, frowning at you.",
        "A nearby peddler tries to raise his voice over everyone else's.",
        "Laughing children run by.",
        "You are pressed to the edge of the street by the crowd.",
        "You watch as a would-be pickpocket gets caught in the act.",
        "A town crier tries to make an announcement, but cannot be heard over the din.",
        "Iron-shod hooves clatter on the cobbles."
    ]
    
    ECHOES_URBAN = [
        "People hurry by in the streets.",
        "You catch a whiff of a foul odour emanating from the sewers.",
        "Bugles sound as a minor noble and his escort pass by.",
    ]
    
    ECHOES_FOREST = [
        "A twig snaps underfoot.", 
        "You hear a rustling in the bushes.",
        "A squirrel darts up the trunk of a nearby tree.",
        "You get the feeling that someone is watching you.",
        "A cool breeze rustles the trees' leaves.",
        "Birds twitter in the branches.",
        "A deer glances warily at you before turning and vanishing into the forest.",
        "A bird flies across your path.",
        "An eagle soars way above the trees.",
        "A single leaf falls to the ground.",
        "It is eerily silent.",
        "The silence is almost oppressive."
    ]