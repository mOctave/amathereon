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
from evennia.utils import make_iter
from evennia.utils.evmenu import EvMenu

from world.data.class_data import Classes
from world.data.race_data import Races

import typeclasses.scripts

from server.conf import settings

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
    isItem = False

    specials: list[str] = [""]
    languages: list[str] = [""]
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
    def maxmana(self):
        _max_mana = 5 + self.db.lvl
        if self.db.charClass == "Wizard":
            _max_mana *= 4
        if self.db.charClass in ["Necromancer", "Cleric"]:
            _max_mana *= 3
        if self.db.charClass in ["Sorcerer", "Druid", "Paladin"]:
            _max_mana *= 2
        return(_max_mana)

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
    def maxcarry(self):
        return(20 + (self.totalstr * 3) + (self.totalcon * 2) + self.totalres)
    
    @property
    def handsFull(self):
        hands = 0
        for weapon in self.db.wieldedItems:
            hands += weapon.db.hands
        return hands
    
    @property
    def langRecChance(self):
        recChance = self.db.skills["Knowledge: Linguistics"] + (self.totalwis + self.totalint)/2
        return round(100*(1-(1/(recChance/8))),1)
    
    @property
    def langUnderstandChance(self):
        getChance = (self.db.skills["Knowledge: Linguistics"] + (self.totalwis + self.totalint + self.totalcha)/2)/2
        return round(100*(1-(1/(getChance/8))),1)

    @property
    def random(self):
        return(random.randint(0, 99))
    

    energy_counter: int = 0
    mana_counter: int = 0

    def changeHP(self, value):
        self.db.hp += value
        if self.db.hp > self.maxhp:
            self.db.hp = self.maxhp
        elif self.db.hp < 0:
            self.die()

    def changeEnergy(self, value):
        self.db.energy += value
        if self.db.energy > self.maxenergy:
            self.db.energy = self.maxenergy
        elif self.db.energy < 0:
            self.db.energy = 0

    def changeMana(self, value):
        self.db.mana += value
        if self.db.mana > self.maxmana:
            self.db.mana = self.maxmana
        elif self.db.mana < 0:
            self.db.mana = 0

    def die(self):
        # Notify the character about their death
        loc = self.location
        self.location = self.search(settings.DEATH_ROOM, global_search=True)
        self.msg("|rYou collapse, unable to feel anything in your pain...")
        self.msg("""|X|[R
|       <--------------->       |
|        YOU HAVE DIED          |
|       <--------------->       |
|n""")

        # Notify the room about their death
        loc.msg_contents(self.name + " has died!")
        for char in loc.contents:
            try:
                char.db.target = None
            except:
                print("Could not remove target for " + char.name)

        # Drop every carried object
        for obj in self.contents:
            obj.location = self.location
            self.db.wieldedItems = []
        
        # Meet up with Onarezuron
        self.db.hp = 1
        self.msg("You float in the mists of the plane of Entropy, detached for good from your body, and yet... perhaps you need not be...")
        EvMenu(self, "world.death", startnode = "node_main", cmdset_mergetype = "Replace")

    def at_object_creation(self):
        #set persistent attributes
        self.db.race = "Unborn"
        self.db.charClass = "Would-Be Adventurer"

        self.db.nationality = "Wildlands"

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

        self.db.mana = self.maxmana

        self.scripts.add(typeclasses.scripts.UpdateEnergy, None, False)
    
    def at_post_move(self, source_location, move_type='move', **kwargs):
        if source_location == None:
            self.db.hp = self.maxhp
            self.db.energy = self.maxenergy
            self.db.mana = self.maxmana
    
    # Energy handling scripts
    def at_init(self):
        #print("at_init() triggered for " + self.name + ", disabling energy update script.")
        self.scripts.stop("energy_update_script")
        if self.has_account:
            print("Enabling energy update script for puppeted character " + self.name + ".")
            self.scripts.add(typeclasses.scripts.UpdateEnergy, None, False)
            self.scripts.start("energy_update_script")

    def at_pre_puppet(self, account, session, **kwargs):
        #print("at_pre_puppet() triggered for " + self.name + ", enabling energy update script.")
        ClothedCharacter.at_pre_puppet(self, account, session)
        self.scripts.add(typeclasses.scripts.UpdateEnergy, None, False)
        self.scripts.start("energy_update_script")
    
    def at_server_reload(self):
        #print("at_server_reload() triggered for " + self.name + ", disabling energy update script.")
        self.scripts.stop("energy_update_script")
    
    def at_server_shutdown(self):
        #print("at_server_shutdown() triggered for " + self.name + ", disabling energy update script.")
        self.scripts.stop("energy_update_script")
        self.scripts.stop("combat_engine_script")
    
    def at_pre_unpuppet(self):
        #print("at_pre_unpuppet() triggered for " + self.name + ", disabling energy update script.")
        self.scripts.stop("energy_update_script")
        self.scripts.stop("combat_engine_script")

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
            self.msg("|gSuddenly, you're feeling stronger! You've levelled up to level " + str(self.db.lvl) + "!")

            # Give a random skill from the class skill list
            x = random.randint(0, len(self.classData.skills) - 1)
            self.db.skills[self.classData.skills[x]] += 1
            self.msg("|G+1 level in %s!" % self.classData.skills[x])

            # Give skill points
            self.db.skillpts += 1 + math.ceil(math.sqrt(self.db.lvl))
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
    
    def get_objects(self):
        """
        Returns a list of objects carried by the player, with currency filreted out.
        """

        objlist = []

        for obj in self.contents:
            try:
                if not obj.isCurrency:
                    objlist.append(obj)
            except:
                pass
        
        return objlist

    def at_say(self, message, msg_self = False, msg_location = False, receivers = None, msg_receivers = False, **kwargs):
        msg_type = "say"
        if kwargs.get("whisper", False):
            # whisper mode
            msg_type = "whisper"
            msg_self = (
                '{self} whisper to {all_receivers}, {q}|n{speech}|n{q} {inlang}'
                if msg_self is True
                else msg_self
            )
            msg_receivers = msg_receivers or '{object} whispers: {q}|n{speech}|n{q} {inlang}'
            msg_location = None
        else:
            msg_self = '{self} say, {q}|n{speech}|n{q} {inlang}' if msg_self is True else msg_self
            msg_location = msg_location or '{object} says, {q}{speech}{q} {inlang}'
            msg_receivers = msg_receivers or message

        custom_mapping = kwargs.get("mapping", {})
        receivers = make_iter(receivers) if receivers else None
        location = self.location

        if msg_self:
            self_mapping = {
                "self": "You",
                "object": self.get_display_name(self),
                "location": location.get_display_name(self) if location else None,
                "receiver": None,
                "all_receivers": ", ".join(recv.get_display_name(self) for recv in receivers)
                if receivers
                else None,
                "speech": message,
                "q": '"',
                "inlang": "in " + kwargs["lang"]
            }
            self_mapping.update(custom_mapping)
            self.msg(text=(msg_self.format_map(self_mapping), {"type": msg_type}), from_obj=self)

        if receivers and msg_receivers:
            receiver_mapping = {
                "self": "You",
                "object": None,
                "location": None,
                "receiver": None,
                "all_receivers": None,
                "speech": message,
                "q": '"',
                "inlang": "in " + kwargs["lang"]
            }
            for receiver in make_iter(receivers):
                speech = message
                q = '"'
                inlang = "in " + kwargs["lang"]

                if (not kwargs["lang"] in receiver.db.languages) and (receiver.random < receiver.langUnderstandChance):
                    q = ''
                    speech = "something"
                    if receiver.random >= receiver.langRecChance:
                        inlang = "in a language you do not understand"

                individual_mapping = {
                    "object": self.get_display_name(receiver),
                    "location": location.get_display_name(receiver),
                    "receiver": receiver.get_display_name(receiver),
                    "all_receivers": ", ".join(recv.get_display_name(recv) for recv in receivers)
                    if receivers
                    else None,
                    "speech": speech,
                    "q": q,
                    "inlang": inlang
                }
                receiver_mapping.update(individual_mapping)
                receiver_mapping.update(custom_mapping)
                receiver.msg(
                    text=(msg_receivers.format_map(receiver_mapping), {"type": msg_type}),
                    from_obj=self,
                )

        if self.location and msg_location:
            location_mapping = {
                "self": "You",
                "object": self,
                "location": location,
                "all_receivers": ", ".join(str(recv) for recv in receivers) if receivers else None,
                "receiver": None,
                "speech": message,
                "q": '"',
                "inlang": "in " + kwargs["lang"]
            }
            location_mapping.update(custom_mapping)
            exclude = []
            if msg_self:
                exclude.append(self)
            if receivers:
                exclude.extend(receivers)
            self.location.msg_contents(
                text=(msg_location, {"type": msg_type}),
                from_obj=self,
                exclude=exclude,
                mapping=location_mapping,
            )