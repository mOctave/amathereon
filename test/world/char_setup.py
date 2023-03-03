
from evennia.utils.evmenu import EvMenu
from typeclasses.characters import Character
from world.class_data import *

#############################
# Character Generation Menu #
#############################

def menunode_welcome(caller):
    """Starting page."""
    text = """
        |yWelcome to Amathereon!|Y
        You stand in the doorway of a mud hut, swept clean by a million footstepps over the course of twenty years. Although the hut is certainly very simple and crude, it is also very clean and well-kept. You can tell that the man who has lived here has taken good care of it. A man sits on a small rug on one side of the hut, although he hasn't noticed you yet. This man is Gundulf, the wise man who guides prospective adventurers in their quest to fulfill their dreams.
    """

    options = {"key": ("Continue"), "desc": "Approach Gundulf", "goto": "node_race"}
    return text, options

##################
# Race Selection #
##################

def node_race(caller, raw_string, **kwargs):

    text = "|yGundulf squints at you. \"So I hear you want to become an adventurer and walk Amathereon? To which race will you belong?\""

    options = (
        {"key": ("Human"),
         "desc": "I'm a human.",
         "goto": "node_human"},
        {"key": ("Halfling"),
         "desc": "I'm a halfling, sir.",
         "goto": ("node_halfling")},
        {"key": ("Dwarf"),
         "desc": "Can't you tell I'm a dwarf?!",
         "goto": ("node_dwarf")},
        {"key": ("Elf"),
         "desc": "I am an elf, one of the eldest.",
         "goto": ("node_elf")},
        {"key": ("Half-Elf"),
         "desc": "I'm a half-elf.",
         "goto": ("node_half_elf")},
        {"key": ("Urunk"),
         "desc": "I be urunk.",
         "goto": ("node_urunk")},
        {"key": ("Gnome"),
         "desc": "I am a gnome.",
         "goto": ("node_gnome")},
        {"key": ("Goblin"),
         "desc": "I amm a goblinn, missterr.",
         "goto": ("node_goblin")})

    return text, options

def node_human(caller, raw_string, **kwargs):

    caller.new_char.db.race = "Human"

    text = "|yGundulf clears his throat. \"So you're a human, eh? It seems like every adventurer is, these days.\""

    options = (
        {"key": ("Yes"),
         "desc": "I'm human, all right.",
         "goto": "node_class"},
        {"key": ("No"),
         "desc": "Wait, no, what was I saying? I'm not a human!",
         "goto": ("node_race")})

    return text, options

def node_halfling(caller, raw_string, **kwargs):

    caller.new_char.db.race = "Hafling"

    text = "|yGundulf clears his throat. \"So you're a halfling, tired of spending a life accomplishing nothing?\""

    options = (
        {"key": ("Yes"),
         "desc": "Yes, I'm a halfling.",
         "goto": "node_class"},
        {"key": ("No"),
         "desc": "Wait, no, what was I saying? I'm not a halfling!",
         "goto": ("node_race")})

    return text, options

def node_dwarf(caller, raw_string, **kwargs):

    caller.new_char.db.race = "Dwarf"

    text = "|yGundulf clears his throat. \"So you're a dwarf? A master quaffer, too, I suppose.\""

    options = (
        {"key": ("Yes"),
         "desc": "I'm a dwarf, yes...",
         "goto": "node_class"},
        {"key": ("No"),
         "desc": "Wait, no, what was I saying? I'm not a dwarf!",
         "goto": ("node_race")})

    return text, options

def node_elf(caller, raw_string, **kwargs):

    caller.new_char.db.race = "Elf"

    text = "|yGundulf clears his throat. \"You're an elf? Few of the fair people still remain. It is a pleasure to meet you.\""

    options = (
        {"key": ("Yes"),
         "desc": "I am an elf, yes. And it's a pleasure to meet you too, wise one.",
         "goto": "node_class"},
        {"key": ("No"),
         "desc": "Wait, no, what was I saying? I'm not an elf!",
         "goto": ("node_race")})

    return text, options

def node_half_elf(caller, raw_string, **kwargs):

    caller.new_char.db.race = "Half-Elf"

    text = "|yGundulf clears his throat. \"You're a half-elf? It has been a long while since I met one of your kind. Forgive me.\""

    options = (
        {"key": ("Yes"),
         "desc": "Yes, I am a half-elf, and proud to be one.",
         "goto": "node_class"},
        {"key": ("No"),
         "desc": "Wait, no, what was I saying? I'm not a half-elf!",
         "goto": ("node_race")})

    return text, options

def node_urunk(caller, raw_string, **kwargs):

    caller.new_char.db.race = "Urunk"

    text = "|yGundulf clears his throat. \"You're an urunk? Now that, indeed, is strange. Very few urunks seek to make choices for themselves.\""

    options = (
        {"key": ("Yes"),
         "desc": "Yes, I be urunk.",
         "goto": "node_class"},
        {"key": ("No"),
         "desc": "Wait, no, what was I saying? I'm not an urunk!",
         "goto": ("node_race")})

    return text, options

def node_gnome(caller, raw_string, **kwargs):

    caller.new_char.db.race = "Gnome"

    text = "|yGundulf clears his throat. \"You're a gnome? One of the flying tunnelers?\""

    options = (
        {"key": ("Yes"),
         "desc": "Yes, I am indeed a gnome.",
         "goto": "node_class"},
        {"key": ("No"),
         "desc": "Wait, no, what was I saying? I'm not a gnome!",
         "goto": ("node_race")})

    return text, options

def node_goblin(caller, raw_string, **kwargs):

    caller.new_char.db.race = "Goblin"

    text = "|yGundulf clears his throat. \"You're a goblin? Ah, yes, now I see – smell, that is.\""

    options = (
        {"key": ("Yes"),
         "desc": "Yess, I amm a goblinn.",
         "goto": "node_class"},
        {"key": ("No"),
         "desc": "Wait, no, what was I saying? I'm not a goblin!",
         "goto": ("node_race")})

    return text, options

###################
# Class Selection #
###################

def node_class(caller, raw_string, **kwargs):

    text = "|yGundulf looks at you expectantly. \"Well, you've come to the right place to begin your new life of adventure, I suppose. What talents do you have?\""

    options = (
        {"key": ("Rogue"),
         "desc": "I'm good at sneaking around and getting up to mischief without being caught.",
         "goto": "node_rogue"},
        {"key": ("Warrior"),
         "desc": "I can hold my own in any fight.",
         "goto": ("node_warrior")},
        {"key": ("Outlander"),
         "desc": "I have exceptional wilderness survival skills.",
         "goto": ("node_outlander")},
        {"key": ("Mage"),
         "desc": "I know how to use magic effectively.",
         "goto": ("node_mage")},
        {"key": ("Specialist"),
         "desc": "I have... other skills.",
         "goto": ("node_specialist")})

    return text, options

def node_rogue(caller, raw_string, **kwargs):
    caller.new_char.db.charClass = "Rogue"

    text = "|y\"That's an interesting set of skills for an adventurer, sneaking around. Can you be more specific?\""

    options = (
        {"key": ("Thief"),
         "desc": "I'm great at stealing things from unsuspecting marks.",
         "goto": ("node_confirm_class", {"choice": "Thief", "last_node": "node_rogue"})},
        {"key": ("Assassin"),
         "desc": "I am skilled in the art of... disposing of unwanted individuals.",
         "goto": ("node_confirm_class", {"choice": "Assassin", "last_node": "node_rogue"})},
        {"key": ("Con Artist"),
         "desc": "I am charismatic and good at tricking people into thinking what I want them to think.",
         "goto": ("node_confirm_class", {"choice": "Con Artist", "last_node": "node_rogue"})},
        {"key": ("Spy"),
         "desc": "I can move very stealthily and gather useful information.",
         "goto": ("node_confirm_class", {"choice": "Spy", "last_node": "node_rogue"})},
        {"key": ("Back"),
         "desc": "Sorry, I must have misspoke. I'm not actually a rogue.",
         "goto": ("node_class")})

    return text, options

def node_warrior(caller, raw_string, **kwargs):
    caller.new_char.db.charClass = "Warrior"

    text = "|y\"So many adventurers these days only wish to be known for how many people they can slay with their blades... Could you be more specific as to what kind of warrior you are?\""

    options = (
        {"key": ("Brawler"),
         "desc": "I can fight just as well with my fists as with anything else.",
         "goto": ("node_confirm_class", {"choice": "Brawler", "last_node": "node_warrior"})},
        {"key": ("Knight"),
         "desc": "I am skilled in the use of heavy armour, and will hold strong no matter what happens.",
         "goto": ("node_confirm_class", {"choice": "Knight", "last_node": "node_warrior"})},
        {"key": ("Soldier"),
         "desc": "I have fought for a long time, and have great experience.",
         "goto": ("node_confirm_class", {"choice": "Soldier", "last_node": "node_warrior"})},
        {"key": ("Paladin"),
         "desc": "I fight for justice and for my god, as a holy knight.",
         "goto": ("node_confirm_class", {"choice": "Paladin", "last_node": "node_warrior"})},
        {"key": ("Back"),
         "desc": "Sorry, I must have misspoke. I'm not actually a warrior.",
         "goto": ("node_class")})

    return text, options

def node_outlander(caller, raw_string, **kwargs):
    caller.new_char.db.charClass = "Outlander"

    text = "|y\"You are doomed to wander, and have a hard life, then: the kind of life that is the subject of legends but that few want to live. What kind of an outlander are you?\""

    options = (
        {"key": ("Barbarian"),
         "desc": "My ways may be simple, but they are efficient and versatile.",
         "goto": ("node_confirm_class", {"choice": "Barbarian", "last_node": "node_outlander"})},
        {"key": ("Ranger"),
         "desc": "I can track anyone, and have diverse skills.",
         "goto": ("node_confirm_class", {"choice": "Ranger", "last_node": "node_outlander"})},
        {"key": ("Druid"),
         "desc": "I am a druid: I have much knowledge of woodcraft, and some skill with simple magic.",
         "goto": ("node_confirm_class", {"choice": "Druid", "last_node": "node_outlander"})},
        {"key": ("Bard"),
         "desc": "People come from far and wide to hear my stories and my music.",
         "goto": ("node_confirm_class", {"choice": "Bard", "last_node": "node_outlander"})},
        {"key": ("Back"),
         "desc": "Sorry, I must have misspoke. I'm not actually an outlander.",
         "goto": ("node_class")})

    return text, options

def node_mage(caller, raw_string, **kwargs):
    caller.new_char.db.charClass = "Mage"

    text = "|y\"You can use the powers of magic, then? But there are so many kinds of magic, and so many kinds of mage. Which kind of mage are you?\""

    options = (
        {"key": ("Wizard"),
         "desc": "I know a lot of the science of magic, and of wizardcraft.",
         "goto": ("node_confirm_class", {"choice": "Wizard", "last_node": "node_mage"})},
        {"key": ("Sorcerer"),
         "desc": "I can touch the magic of Reality, and shape it according to my wishes.",
         "goto": ("node_confirm_class", {"choice": "Sorcerer", "last_node": "node_mage"})},
        {"key": ("Cleric"),
         "desc": "I use divine magic to further my god's kingdom and church.",
         "goto": ("node_confirm_class", {"choice": "Cleric", "last_node": "node_mage"})},
        {"key": ("Necromancer"),
         "desc": "I can commune with those who are no more, and touch the strands of life.",
         "goto": ("node_confirm_class", {"choice": "Necromancer", "last_node": "node_mage"})},
        {"key": ("Back"),
         "desc": "Sorry, I must have misspoke. I'm not actually a mage.",
         "goto": ("node_class")})

    return text, options

def node_specialist(caller, raw_string, **kwargs):
    caller.new_char.db.charClass = "Specialist"

    text = "|y\"A specialist? That's very vague. Could you be a bit more specific in what exactly you specialize in?\""

    options = (
        {"key": ("Monk"),
         "desc": "I am a master of precise unarmed combat as a means of defense.",
         "goto": ("node_confirm_class", {"choice": "Monk", "last_node": "node_specialist"})},
        {"key": ("Artificer"),
         "desc": "I can make almost anything you describe, given enough time.",
         "goto": ("node_confirm_class", {"choice": "Artificer", "last_node": "node_specialist"})},
        {"key": ("Merchant"),
         "desc": "I could sell people the air they breathe, if I so wished, and they would buy it.",
         "goto": ("node_confirm_class", {"choice": "Merchant", "last_node": "node_specialist"})},
        {"key": ("Aristocrat"),
         "desc": "I was born to a high position, and am comfortable among the elite and in command.",
         "goto": ("node_confirm_class", {"choice": "Aristocrat", "last_node": "node_specialist"})},
        {"key": ("Developer"),
         "desc": "I'm a developer. I can't be bothered to deal with unimplemented nodes.",
         "goto": ("node_name")},
        {"key": ("Back"),
         "desc": "Sorry, I must have misspoke. I'm not actually a specialist.",
         "goto": ("node_class")})

    return text, options

def node_confirm_class(caller, raw_string, **kwargs):
    caller.new_char.db.charClass = kwargs["choice"]

    classData = Classes.getClassFromKey(caller.new_char.db.charClass)

    text = "|y\"So you wish to become a%s?\"" % classData.narrow_after_a

    options = (
        {"key": ("Yes"),
         "desc": "Yes, that's right.",
         "goto": "node_name"},
        {"key": ("No"),
         "desc": "No, that's not what I meant to say.",
         "goto": (kwargs["last_node"])})
    
    return text, options

##################
# Name Selection #
##################

def node_name(caller, raw_string, **kwargs):

    text = "|y\"There is just one more step remaining before I can send you to Amathereon. What do you wish to be called?\""

    if error := kwargs.get("error"):
        text = "|yGundulf squints at you. \"I know someone with that name, and it's not you. Is there something else you would like to be called, instead?\""
    else:
        # there was no error, so just ask them to enter a name.
        text = "|y\"There is just one more step remaining before I can send you to Amathereon. What do you wish to be called?\""

    options = ({"key":"_default",
                "goto": _check_name})

    return text, options


def _check_name(caller, raw_string, **kwargs):
    """Check and confirm name choice"""

    # strip any extraneous whitespace from the raw text
    # if you want to do any other validation on the name, e.g. no punctuation allowed, this
    # is the place!
    charname = raw_string.strip()

    # aside from validation, the built-in normalization function from the caller's Account does
    # some useful cleanup on the input, just in case they try something sneaky
    charname = caller.account.normalize_username(charname)

    # check to make sure that the name doesn't already exist
    candidates = Character.objects.filter_family(db_key__iexact=charname)
    if len(candidates):
        # the name is already taken - report back with the error
        return (
            "node_choose_name",
            {"error": f"|w{charname}|n is unavailable.\n\nEnter a different name."},
        )
    else:
        # it's free! set the character's key to the name to reserve it
        caller.new_char.key = charname
        # continue on to the confirmation node
        return "node_name_confirm"

def node_name_confirm(caller, raw_string, **kwargs):
    text = "|y\"Your name will be %s?\"" % (raw_string)

    options = (
        {"key": ("Yes"),
         "desc": "Yes, that's right.",
         "goto": "node_end"},
        {"key": ("No"),
         "desc": "No, you must have heard me wrong.",
         "goto": ("node_name")})

    return text, options

##########################
# Finish Character Setup #
##########################

def node_end(caller, raw_string):
    """End-of-chargen cleanup."""
    char = caller.new_char
    caller.execute_cmd("ic %s" % char)
    # since everything is finished and confirmed, we actually create the starting objects now
    #create_objects(char)

    text = "Suddenly, you find yourself swept up in a whirlwind that seems to have come from nowhere and everywhere at the same time... Your life as an adventurer has begun!"

    return text, None