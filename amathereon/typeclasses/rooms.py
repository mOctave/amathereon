"""
Room

Rooms are simple containers that has no location of their own.

"""

from evennia.objects.objects import DefaultRoom
from evennia import TICKER_HANDLER

from .objects import ObjectParent

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
        TICKER_HANDLER.add(60, self.print_flavour_text)
    
    ECHOES_STREET = ["People hurry by in the streets.", 
              "A carriage clatters by.",
              "Some mounted watchmen ride past you in a hurry.",
              "A hard-looking man walks past you, frowning at you.",
              "A nearby peddler tries to raise his voice over everyone else's."]
    
    ECHOES_FOREST = ["A twig snaps underfoot.", 
              "You hear a rustling in the bushes.",
              "A squirrel darts up the trunk of a nearby tree.",
              "You get the feeling that someone is watching you.",
              "A cool breeze rustles the trees' leaves.",
              "Birds twitter in the branches.",
              "A deer glances warily at you before turning and vanishing into the forest.",
              "A bird flies across your path.",
              "An eagle soars way above the trees.",
              "A leaf falls to the grounds.",
              "It is eerily silent."]

    def print_flavour_text(self, *args, **kwargs):
        echoes = []
        if "street" in self.db.flags:
            echoes += random.choice(self.ECHOES_STREET)
        if "forest" in self.db.flags:
            echoes += random.choice(self.ECHOES_FOREST)
        self.msg_contents(random.choice(echoes))
