r"""
Evennia settings file.

The available options are found in the default settings file found
here:

/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/evennia/settings_default.py

Remember:

Don't copy more from the default file than you actually intend to
change; this will make sure that you don't overload upstream updates
unnecessarily.

When changing a setting requiring a file system path (like
path/to/actual/file.py), use GAME_DIR and EVENNIA_DIR to reference
your game folder and the Evennia library folders respectively. Python
paths (path.to.module) should be given relative to the game's root
folder (typeclasses.foo) whereas paths within the Evennia library
needs to be given explicitly (evennia.foo).

If you want to share your game dir, including its settings, you can
put secret game- or server-specific settings in secret_settings.py.

"""

# Use the defaults from Evennia unless explicitly overridden
from evennia.settings_default import *

######################################################################
# Evennia base server config
######################################################################

# Basic server data
SERVERNAME = "Amathereon"
GAMEVERSION = "0.1.0"

PERMISSION_HIERARCHY = [
    "Guest",  # note-only used if GUEST_ENABLED=True
    "Player",
    "Helper",
    "Builder",
    "Celestial",
    "Admin",
    "Developer",
]

# Character settings
AUTO_CREATE_CHARACTER_WITH_ACCOUNT = False
AUTO_PUPPET_ON_LOGIN = False
MAX_NR_CHARACTERS = 65536 # Fake unlimited characters
CHARGEN_MENU = "world.char_setup"

# Gametime
TIME_FACTOR = 20
TIME_GAME_EPOCH = 372 * 31968000
TIME_UNITS = {"sec": 1,
              "min": 60,
              "hour": 60 * 60,
              "day": 60 * 60 * 30,
              "month": 60 * 60 * 30 * 37,
              "year": 60 * 60 * 30 * 37 * 8 }

# Combat
PROTOTYPE_MODULES += ["combat.weapons"]
"""GLOBAL_SCRIPTS = {
    "combatengine": {
        "typeclass": "combat.targeted_attacks.CombatEngine"
    },
}"""

# A room to send the dead to. Can be either a name or a dbref.
DEATH_ROOM = "Entropy"

# Command Prompt
COMMAND_DEFAULT_CLASS = "commands.commandtypes.MuxCommand"

# List of body parts that clothing can be worn on
CLOTHING_SLOTS = ["head","torso","hands","legs","feet"]

######################################################################
# Settings given in secret_settings.py override those in this file.
######################################################################
try:
    from server.conf.secret_settings import *
except ImportError:
    print("secret_settings.py file not found or failed to import.")
