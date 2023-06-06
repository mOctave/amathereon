"""
File-based help entries. These complements command-based help and help entries
added in the database using the `sethelp` command in-game.

Control where Evennia reads these entries with `settings.FILE_HELP_ENTRY_MODULES`,
which is a list of python-paths to modules to read.

A module like this should hold a global `HELP_ENTRY_DICTS` list, containing
dicts that each represent a help entry. If no `HELP_ENTRY_DICTS` variable is
given, all top-level variables that are dicts in the module are read as help
entries.

Each dict is on the form
::

	{'key': <str>,
	 'text': <str>}``     # the actual help text. Can contain # subtopic sections
	 'category': <str>,   # optional, otherwise settings.DEFAULT_HELP_CATEGORY
	 'aliases': <list>,   # optional
	 'locks': <str>       # optional, 'view' controls seeing in help index, 'read'
	                      #		   if the entry can be read. If 'view' is unset,
	                      #		   'read' is used for the index. If unset, everyone
	                      #		   can read/view the entry.

"""

HELP_ENTRY_DICTS = [
	{
		"key": "evennia",
		"aliases": ["ev"],
		"category": "General",
		"locks": "read:perm(Developer)",
		"text": """
			Evennia is a MU-game server and framework written in Python. You can read more
			on https://www.evennia.com.

			# subtopics

			## Installation

			You'll find installation instructions on https://www.evennia.com.

			## Community

			There are many ways to get help and communicate with other devs!

			### Discussions

			The Discussions forum is found at https://github.com/evennia/evennia/discussions.

			### Discord

			There is also a discord channel for chatting - connect using the
			following link: https://discord.gg/AJJpcRUhtF

		""",
	},
	{
		"key": "conflict",
		"category": "General",
		"text": """
			Amathereon uses a fairly complex combat system. Combat is handled automatically
            at one second intervals on a character-by-character basis. In order to attack
            someone, you do not use an attack command, rather you |lchelp target|lttarget|le
            them with the appropriate command.
            
            Every turn that you are in a non-safe room with your target, you will attack them
            with any weapons you are currently wielding. As of right now, unarmed combat is
            not implemented. To wield/unwield weapons, use the aptly named |lchelp wield|ltwield|le
            and |lchelp unwield|ltunwield|le commands.
            
            Before an attack can deal damage, it first must be decided if it "hits" its target
            or not. To do this, a number of factors are taken into consideration: the attacker's
            dexterity, the defender's agility, the individual hit and parry chance stats of the
            weapons they both carry, their experience with those weapons, any weapon skills they
            possess, and the clothing worn by the defender.

			All attacks that hit deal a certain amount of randomized damage, of a certain type.
            Besides magic, the damage types are: piercing, slashing, and trauma. In general, it
            is best to attack most foes with piercing or slashing weapons as they tend to do more
            damage, but trauma weapons work well against heavily armoured enemies.
            
            Other factors affecting damage are the strength of the attacker, and the constitution
            of the defender. Additionally, an attack will occasionally be a critical hit. Attacks
            are more likely to be critical hits for attackers with high intelligence and dexterity
            and more rare weapons, and less likely to be critical hits against defenders with high
            wisdom and agility and rarer armour. Additionally, those dressed in fancy clothes are
            more likely to be underestimated and so are marginally better at dodging critical hits.
		""",
	},
	{
		"key": "clothing",
		"category": "General",
		"text": """
			Amathereon uses a unique clothing system. Clothing provides various benefits, mainly
            in combat, and can be worn using the |lchelp wear|ltwear|le command. When you're
            wearing clothing, you can then take off the outermost layer of clothing on some
            body part using |lchelp unwear|ltunwear|le.
            
            An important aspect of clothing in Amathereon is that each garment has a certain
            thickness, and can only be worn over top of a certain number of thickness layers.
            More flexible pieces of clothing may have several different options for how many
            layers they must have underneath, while others (like some pieces of plate armour)
            have very strict requirements.
		""",
	},
	{
		"key": "energy",
		"category": "General",
		"text": """
			An important number to keep an eye on in Amathereon, especially during combat or when
            you're sending lots of commands, is energy. Just about every in-character action (and
            some out-of-character ones) require energy. Energy refills at a rate determined by your
            character's stats, but it can take time, and so it's best to be careful not to let it
            get too low, lest you end up in a battle you don't have the strength to run away from.
            
            When you're |lchelp encumbrance|ltencumbered|le, you burn through your energy twice as fast.
		""",
	},
	{
		"key": "encumbrance",
		"category": "General",
		"text": """
			Everything has mass, and while this isn't normally an issue, if you're carrying a
            lot of gear you might become encumbered. When you're encumbered, you spend twice as
            much energy performing actions, and your dexterity and agility scores are reduced
            to 70%% of their typical value (rounded down).
		""",
	},
	{
		"key": "currency",
		"category": "General",
		"text": """
			On Amathereon, many different currencies are used. For this reason, everything is
            assigned a value in terms of grains of gold (gr gold).
		""",
	},
]
