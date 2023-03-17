# General definition of what a character class is

class CharacterClass:
	wide: str = "Citizen"
	wide_after_a: str = " Citizen"
	narrow: str = "Would-Be Adventurer"
	narrow_after_a: str = " Would-Be Adventurer"
	desc: str = "An ordinary person who wishes to take up a life of adventure."
	specials: list[str] = []
	languages: list[str] = []
	inventory: list[str] = []
	skills: list[str] = []
	dex: int = 0
	agi: int = 0
	str: int = 0
	con: int = 0
	int: int = 0
	wis: int = 0
	cha: int = 0
	res: int = 0
	dex_up: int = 0
	agi_up: int = 0
	str_up: int = 0
	con_up: int = 0
	int_up: int = 0
	wis_up: int = 0
	cha_up: int = 0
	res_up: int = 0

	def __new__ (cls, *args, **kwargs):
		return super().__new__(cls)
	
	def __init__(self, wide: str = "Citizen", wide_after_a: str = " Citizen", narrow: str = "Would-Be Adventurer", narrow_after_a: str = " Would-Be Adventurer", desc: str = "An ordinary person who wishes to take up a life of adventure.", specials: list[str] = [], languages: list[str] = [], inventory: list[str] = [], skills: list[str] = [], dex: int = 0, agi: int = 0, str: int = 0, con: int = 0, int: int = 0, wis: int = 0, cha: int = 0, res: int = 0, dex_up: int = 0, agi_up: int = 0, str_up: int = 0, con_up: int = 0, int_up: int = 0, wis_up: int = 0, cha_up: int = 0, res_up: int = 0):
		self.wide = wide
		self.wide_after_a = wide_after_a
		self.narrow = narrow
		self.narrow_after_a = narrow_after_a
		self.desc = desc
		self.specials = specials
		self.languages = languages
		self.inventory = inventory
		self.skills = skills
		self.dex = dex
		self.agi = agi
		self.str = str
		self.con = con
		self.int = int
		self.wis = wis
		self.cha = cha
		self.res = res
		self.dex_up = dex_up
		self.agi_up = agi_up
		self.str_up = str_up
		self.con_up = con_up
		self.int_up = int_up
		self.wis_up = wis_up
		self.cha_up = cha_up
		self.res_up = res_up
	
	def __repr__(self) -> str:
		return f"{type(self).__name__}(\n\twide=\"{self.wide}\", \"{self.wide_after_a}\"; narrow=\"{self.narrow}\", \"{self.narrow_after_a}\"; desc=\"{self.desc}\";\n\tspecials={self.specials}; languages={self.languages}; inventory={self.inventory}; skills={self.skills};\n\tdex={self.dex}, agi={self.agi}, str={self.str}, con={self.con}, int={self.int}, wis={self.wis}, cha={self.cha}, res={self.res};\n\tdex_up={self.dex_up}, agi_up={self.agi_up}, str_up={self.str_up}, con_up={self.con_up}, int_up={self.int_up}, wis_up={self.wis_up}, cha_up={self.cha_up}, res_up={self.res_up}\n)"

# Actual classes

class Classes():

	# Select a class using a key
	def getClassFromKey(key):
		if key == "Rogue":
			return Classes.Rogue
		elif key == "Warrior":
			return Classes.Warrior
		elif key == "Outlander":
			return Classes.Outlander
		elif key == "Mage":
			return Classes.Mage
		elif key == "Specialist":
			return Classes.Specialist
		elif key == "Thief":
			return Classes.Thief
		elif key == "Assassin":
			return Classes.Assassin
		elif key == "Con Artist":
			return Classes.ConArtist
		elif key == "Spy":
			return Classes.Spy
		elif key == "Brawler":
			return Classes.Brawler
		elif key == "Knight":
			return Classes.Knight
		elif key == "Soldier":
			return Classes.Soldier
		elif key == "Paladin":
			return Classes.Paladin
		elif key == "Ranger":
			return Classes.Ranger
		elif key == "Barbarian":
			return Classes.Barbarian
		elif key == "Druid":
			return Classes.Druid
		elif key == "Bard":
			return Classes.Bard
		elif key == "Wizard":
			return Classes.Wizard
		elif key == "Sorcerer":
			return Classes.Sorcerer
		elif key == "Cleric":
			return Classes.Cleric
		elif key == "Necromancer":
			return Classes.Necromancer
		elif key == "Monk":
			return Classes.Monk
		elif key == "Artificer":
			return Classes.Artificer
		elif key == "Merchant":
			return Classes.Merchant
		elif key == "Aristocrat":
			return Classes.Aristocrat
		else:
			return CharacterClass

	# Fill in data for a specific class
	def buildNarrowClass(parent:CharacterClass, _class:CharacterClass, narrow:str, narrow_after_a:str, desc:str, specials:list[str], languages:list[str], inventory:list[str], skills:list[str], dex:int, agi:int, str:int, con:int, int:int, wis:int, cha:int, res:int, dex_up:int, agi_up:int, str_up:int, con_up:int, int_up:int, wis_up:int, cha_up:int, res_up:int):
		_class.wide = parent.wide
		_class.wide_after_a = parent.wide_after_a
		_class.narrow = narrow or parent.narrow
		_class.narrow_after_a = narrow_after_a or parent.narrow_after_a
		_class.desc = desc or parent.desc
		_class.specials = []
		_class.languages = []
		_class.inventory = []
		_class.skills = []
		for i in parent.specials:
			_class.specials.append(i)
		for i in specials:
			_class.specials.append(i)
		for i in parent.languages:
			_class.languages.append(i)
		for i in languages:
			_class.languages.append(i)
		for i in parent.inventory:
			_class.inventory.append(i)
		for i in inventory:
			_class.inventory.append(i)
		for i in parent.skills:
			_class.skills.append(i)
		for i in skills:
			_class.skills.append(i)
		_class.dex = parent.dex + dex
		_class.agi = parent.agi + agi
		_class.str = parent.str + str
		_class.con = parent.con + con
		_class.int = parent.int + int
		_class.wis = parent.wis + wis
		_class.cha = parent.cha + cha
		_class.res = parent.res + res
		_class.dex_up = parent.dex_up + dex_up
		_class.agi_up = parent.agi_up + agi_up
		_class.str_up = parent.str_up + str_up
		_class.con_up = parent.con_up + con_up
		_class.int_up = parent.int_up + int_up
		_class.wis_up = parent.wis_up + wis_up
		_class.cha_up = parent.cha_up + cha_up
		_class.res_up = parent.res_up + res_up

	# Wide Classes

	Rogue: CharacterClass = CharacterClass(
		wide = "Rogue",
		wide_after_a = " Rogue",
		narrow = "Rogue",
		narrow_after_a = " Rogue",
		desc = "Skilled at sneaking around and getting up to mischief without being caught.",
		specials = ["Shadowy Connections", "Select a Skill", "Select a Skill", "Select a Skill", "Select a Skill"],
		languages = ["Thieves' Cant"],
		inventory = [],
		skills = ["Knowledge", "Mental", "Mental: Deception", "Mental: Performance", "Physical: Acrobatics", "Weapons", "Weapons: Piercing"],
		dex = 1,
		agi = 0,
		str = 0,
		con = 0,
		int = 0,
		wis = 0,
		cha = 1,
		res = 0,
		dex_up = 15,
		agi_up = 5,
		str_up = 2,
		con_up = 2,
		int_up = 5,
		wis_up = 3,
		cha_up = 10,
		res_up = 4
	)

	Warrior: CharacterClass = CharacterClass(
		wide = "Warrior",
		wide_after_a = " Warrior",
		narrow = "Warrior",
		narrow_after_a = " Warrior",
		desc = "A skilled fighter.",
		specials = ["Select a Skill", "Select a Skill", "Select a Skill", "Select a Skill", "Select a Skill", "Select a Skill"],
		languages = [],
		inventory = [],
		skills = ["Knowledge", "Mental: Perception", "Physical", "Physical: Athletics", "Physical: Intimidation", "Weapons", "Weapons: Melee"],
		dex = 0,
		agi = 0,
		str = 1,
		con = 0,
		int = 0,
		wis = 0,
		cha = 0,
		res = 1,
		dex_up = 5,
		agi_up = 2,
		str_up = 15,
		con_up = 5,
		int_up = 3,
		wis_up = 4,
		cha_up = 2,
		res_up = 10
	)

	Outlander: CharacterClass = CharacterClass(
		wide = "Outlander",
		wide_after_a = "n Outlander",
		narrow = "Outlander",
		narrow_after_a = "n Outlander",
		desc = "A wanderer with considerable survival skills.",
		specials = ["Select a Language", "Wildcraft", "Select a Skill", "Select a Skill", "Select a Skill", "Select a Skill"],
		languages = [],
		inventory = [],
		skills = ["Knowledge: Medicine", "Knowledge: Wilderness", "Mental: Investigation", "Mental: Perception", "Physical", "Physical: Endurance", "Weapons: Ranged"],
		dex = 0,
		agi = 1,
		str = 0,
		con = 1,
		int = 0,
		wis = 0,
		cha = 0,
		res = 0,
		dex_up = 5,
		agi_up = 4,
		str_up = 3,
		con_up = 10,
		int_up = 2,
		wis_up = 5,
		cha_up = 2,
		res_up = 15
	)

	Mage: CharacterClass = CharacterClass(
		wide = "Mage",
		wide_after_a = " Mage",
		narrow = "Mage",
		narrow_after_a = " Mage",
		desc = "A magic user who can break the laws of the universe.",
		specials = ["Select a Language", "Select a Skill", "Select a Skill", "Select a Skill", "Select a Skill", "Select a Skill"],
		languages = [],
		inventory = [],
		skills = ["Knowledge: Arcana", "Knowledge: Linguistics", "Knowledge: Medicine", "Mental", "Mental: Perception", "Mental: Performance", "Physical: Sleight of Hand"],
		dex = 0,
		agi = 0,
		str = 0,
		con = 0,
		int = 1,
		wis = 1,
		cha = 0,
		res = 0,
		dex_up = 3,
		agi_up = 5,
		str_up = 2,
		con_up = 2,
		int_up = 10,
		wis_up = 15,
		cha_up = 5,
		res_up = 4
	)

	Specialist: CharacterClass = CharacterClass(
		wide = "Specialist",
		wide_after_a = " Specialist",
		narrow = "Specialist",
		narrow_after_a = " Specialist",
		desc = "Someone with a unique skill set.",
		specials = ["Select a Skill", "Select a Skill", "Select a Skill", "Select a Skill", "Select a Skill", "Select a Skill"],
		languages = [],
		inventory = [],
		skills = ["Knowledge", "Mental", "Physical", "Weapons"],
		dex = 0,
		agi = 0,
		str = 0,
		con = 0,
		int = 0,
		wis = 0,
		cha = 0,
		res = 0,
		dex_up = 5,
		agi_up = 7,
		str_up = 6,
		con_up = 6,
		int_up = 6,
		wis_up = 5,
		cha_up = 6,
		res_up = 5
	)

	# Narrow Classes

	Thief: CharacterClass = CharacterClass()
	buildNarrowClass(Rogue, Thief,
		narrow = "Thief",
		narrow_after_a = " Thief",
		desc = "Someone who is very good at sneaking around and relieving people of their posessions.",
		specials = ["Stealth Expert"],
		languages = [],
		inventory = [],
		skills = ["Mental: Deception", "Mental: Perception", "Physical: Acrobatics", "Physical: Sleight of Hand", "Physical: Stealth"],
		dex = 0,
		agi = 0,
		str = 0,
		con = 0,
		int = 1,
		wis = 0,
		cha = 0,
		res = 0,
		dex_up = 4,
		agi_up = 8,
		str_up = 0,
		con_up = 4,
		int_up = 4,
		wis_up = 0,
		cha_up = 0,
		res_up = 0
	)

	Assassin: CharacterClass = CharacterClass()
	buildNarrowClass(Rogue, Assassin,
		narrow = "Assassin",
		narrow_after_a = "n Assassin",
		desc = "Someone skilled in the art of desposing of inconvenient people, often in exchange for gold.",
		specials = ["Killing Blow"],
		languages = [],
		inventory = [],
		skills = ["Knowledge: Culture", "Mental: Perception", "Physical: Stealth", "Weapons", "Weapons: Piercing"],
		dex = 1,
		agi = 0,
		str = 0,
		con = 0,
		int = 0,
		wis = 0,
		cha = 0,
		res = 0,
		dex_up = 4,
		agi_up = 8,
		str_up = 4,
		con_up = 0,
		int_up = 0,
		wis_up = 0,
		cha_up = 4,
		res_up = 0
	)
	
	ConArtist: CharacterClass = CharacterClass()
	buildNarrowClass(Rogue, ConArtist,
		narrow = "Con Artist",
		narrow_after_a = " Con Artist",
		desc = "Someone who can trick people into believing what they want just long enough to make a profit.",
		specials = ["Interpersonal Skills"],
		languages = [],
		inventory = [],
		skills = ["Knowledge: Culture", "Mental: Deception", "Mental: Intimidation", "Mental: Performance", "Mental: Persuasion"],
		dex = 0,
		agi = 0,
		str = 0,
		con = 0,
		int = 0,
		wis = 0,
		cha = 1,
		res = 0,
		dex_up = 0,
		agi_up = 0,
		str_up = 0,
		con_up = 4,
		int_up = 8,
		wis_up = 0,
		cha_up = 8,
		res_up = 0
	)

	Spy: CharacterClass = CharacterClass()
	buildNarrowClass(Rogue, Spy,
		narrow = "Spy",
		narrow_after_a = " Spy",
		desc = "Someone who can gather information and use it to their advantage.",
		specials = ["Stealth Expert"],
		languages = [],
		inventory = [],
		skills = ["Mental: Deception", "Mental: Investigation", "Mental: Perception", "Physical: Endurance", "Weapons: Improvised"],
		dex = 0,
		agi = 1,
		str = 0,
		con = 0,
		int = 0,
		wis = 0,
		cha = 0,
		res = 0,
		dex_up = 0,
		agi_up = 8,
		str_up = 0,
		con_up = 0,
		int_up = 8,
		wis_up = 0,
		cha_up = 0,
		res_up = 4
	)

	Brawler: CharacterClass = CharacterClass()
	buildNarrowClass(Warrior, Brawler,
		narrow = "Brawler",
		narrow_after_a = " Brawler",
		desc = "Someone who can hold their own in any fight, even if they don't have any weapons.",
		specials = ["Unarmed Combat"],
		languages = [],
		inventory = [],
		skills = ["Physical", "Physical: Athletics", "Physical: Endurance", "Physical: Intimidation", "Weapons: Improvised"],
		dex = 0,
		agi = 0,
		str = 1,
		con = 0,
		int = 0,
		wis = 0,
		cha = 0,
		res = 0,
		dex_up = 0,
		agi_up = 0,
		str_up = 12,
		con_up = 8,
		int_up = 0,
		wis_up = 0,
		cha_up = 0,
		res_up = 0
	)

	Knight: CharacterClass = CharacterClass()
	buildNarrowClass(Warrior, Knight,
		narrow = "Knight",
		narrow_after_a = " Knight",
		desc = "Someone who is skilled in the use of armour as a means of protecting themselves and others.",
		specials = ["Heavy Armour"],
		languages = [],
		inventory = [],
		skills = ["Knowledge: Culture", "Mental: Persuasion", "Physical: Athletics", "Physical: Endurance", "Weapons: Melee"],
		dex = 0,
		agi = 0,
		str = 0,
		con = 1,
		int = 0,
		wis = 0,
		cha = 0,
		res = 0,
		dex_up = 0,
		agi_up = 0,
		str_up = 4,
		con_up = 8,
		int_up = 0,
		wis_up = 0,
		cha_up = 4,
		res_up = 4
	)

	Soldier: CharacterClass = CharacterClass()
	buildNarrowClass(Warrior, Soldier,
		narrow = "Soldier",
		narrow_after_a = " Soldier",
		desc = "Someone who has been fighting in combat for years and has picked up some tricks.",
		specials = ["Veteran"],
		languages = [],
		inventory = [],
		skills = ["Knowledge: Medicine", "Knowledge: Wilderness", "Physical: Endurance", "Weapons: Melee", "Weapons: Slashing"],
		dex = 0,
		agi = 0,
		str = 0,
		con = 0,
		int = 0,
		wis = 0,
		cha = 0,
		res = 1,
		dex_up = 0,
		agi_up = 4,
		str_up = 4,
		con_up = 8,
		int_up = 0,
		wis_up = 4,
		cha_up = 0,
		res_up = 0
	)

	Paladin: CharacterClass = CharacterClass()
	buildNarrowClass(Warrior, Paladin,
		narrow = "Paladin",
		narrow_after_a = " Paladin",
		desc = "Someone who fights for the advancement of their god or religion, and for the upholding of ideals.",
		specials = ["Divination"],
		languages = [],
		inventory = [],
		skills = ["Knowledge: Arcana", "Knowledge: Linguistics", "Mental: Intimidation", "Physical: Athletics", "Weapons: Slashing"],
		dex = 0,
		agi = 1,
		str = 0,
		con = 0,
		int = 0,
		wis = 0,
		cha = 0,
		res = 0,
		dex_up = 4,
		agi_up = 0,
		str_up = 4,
		con_up = 0,
		int_up = 4,
		wis_up = 0,
		cha_up = 8,
		res_up = 0
	)

	Ranger: CharacterClass = CharacterClass()
	buildNarrowClass(Outlander, Ranger,
		narrow = "Ranger",
		narrow_after_a = " Ranger",
		desc = "Someone with lots of experience with the wilderness and some skill with weapons.",
		specials = ["Tracking"],
		languages = [],
		inventory = [],
		skills = ["Knowledge: Wilderness", "Mental: Perception", "Physical: Endurance", "Physical: Stealth", "Weapons: Ranged"],
		dex = 1,
		agi = 0,
		str = 0,
		con = 0,
		int = 0,
		wis = 0,
		cha = 0,
		res = 0,
		dex_up = 0,
		agi_up = 8,
		str_up = 0,
		con_up = 8,
		int_up = 0,
		wis_up = 4,
		cha_up = 0,
		res_up = 0
	)

	Barbarian: CharacterClass = CharacterClass()
	buildNarrowClass(Outlander, Barbarian,
		narrow = "Barbarian",
		narrow_after_a = " Barbarian",
		desc = "Someone who appears at first glance to be simple and uneducated, but who has substantial survival experience.",
		specials = ["Rage"],
		languages = [],
		inventory = [],
		skills = ["Knowledge", "Physical: Athletics", "Physical: Endurance", "Weapons: Melee", "Weapons: Trauma"],
		dex = 0,
		agi = 0,
		str = 1,
		con = 0,
		int = 0,
		wis = 0,
		cha = 0,
		res = 0,
		dex_up = 0,
		agi_up = 0,
		str_up = 8,
		con_up = 12,
		int_up = 0,
		wis_up = 0,
		cha_up = 0,
		res_up = 0
	)

	Druid: CharacterClass = CharacterClass()
	buildNarrowClass(Outlander, Druid,
		narrow = "Druid",
		narrow_after_a = " Druid",
		desc = "Someone with experience both with the wilderness and in druidic magic.",
		specials = ["Druidcraft"],
		languages = ["Druidic"],
		inventory = [],
		skills = ["Knowledge: Arcana", "Knowledge: History", "Knowledge: Medicine", "Mental: Investigation", "Physical: Sleight of Hand"],
		dex = 0,
		agi = 0,
		str = 0,
		con = 0,
		int = 0,
		wis = 1,
		cha = 0,
		res = 0,
		dex_up = 4,
		agi_up = 4,
		str_up = 0,
		con_up = 4,
		int_up = 0,
		wis_up = 4,
		cha_up = 4,
		res_up = 0
	)

	Bard: CharacterClass = CharacterClass()
	buildNarrowClass(Outlander, Bard,
		narrow = "Bard",
		narrow_after_a = " Bard",
		desc = "Someone who is a skilled musician, wandering from place to place seeking glory and gold.",
		specials = ["Musicianship"],
		languages = [],
		inventory = [],
		skills = ["Knowledge: Culture", "Knowledge: Linguistics", "Mental: Deception", "Mental: Performance", "Mental: Persuasion"],
		dex = 0,
		agi = 0,
		str = 0,
		con = 0,
		int = 0,
		wis = 0,
		cha = 1,
		res = 0,
		dex_up = 0,
		agi_up = 8,
		str_up = 4,
		con_up = 0,
		int_up = 0,
		wis_up = 0,
		cha_up = 8,
		res_up = 0
	)

	Wizard: CharacterClass = CharacterClass()
	buildNarrowClass(Mage, Wizard,
		narrow = "Wizard",
		narrow_after_a = " Wizard",
		desc = "Someone who has devoted their life to the scientific study of magic, and who uses that knowledge in their own spells.",
		specials = ["Select a Language", "Wizardraft"],
		languages = [],
		inventory = [],
		skills = ["Knowledge", "Knowledge: Arcana", "Knowledge: Culture", "Knowledge: History", "Mental: Investigation"],
		dex = 0,
		agi = 0,
		str = 0,
		con = 0,
		int = 0,
		wis = 1,
		cha = 0,
		res = 0,
		dex_up = 0,
		agi_up = 0,
		str_up = 0,
		con_up = 0,
		int_up = 12,
		wis_up = 8,
		cha_up = 0,
		res_up = 0
	)

	Sorcerer: CharacterClass = CharacterClass()
	buildNarrowClass(Mage, Sorcerer,
		narrow = "Sorcerer",
		narrow_after_a = " Sorcerer",
		desc = "Someone who draws magical power from the plane of Posibility and uses it to shape the world.",
		specials = ["Sorcery"],
		languages = [],
		inventory = [],
		skills = ["Mental: Intimidation", "Mental: Investigation", "Mental: Perception", "Physical: Endurance", "Weapons: Slashing"],
		dex = 0,
		agi = 0,
		str = 0,
		con = 0,
		int = 1,
		wis = 0,
		cha = 0,
		res = 0,
		dex_up = 0,
		agi_up = 4,
		str_up = 4,
		con_up = 0,
		int_up = 12,
		wis_up = 0,
		cha_up = 0,
		res_up = 0
	)

	Cleric: CharacterClass = CharacterClass()
	buildNarrowClass(Mage, Cleric,
		narrow = "Cleric",
		narrow_after_a = " Cleric",
		desc = "Someone who uses holy magic to further the goals of their religion and to promote its ideals.",
		specials = ["Divination"],
		languages = [],
		inventory = [],
		skills = ["Knowledge: Culture", "Knowledge: Medicine", "Mental", "Mental: Intimidation", "Mental: Persuasion"],
		dex = 0,
		agi = 0,
		str = 0,
		con = 0,
		int = 0,
		wis = 0,
		cha = 0,
		res = 1,
		dex_up = 0,
		agi_up = 0,
		str_up = 0,
		con_up = 4,
		int_up = 4,
		wis_up = 4,
		cha_up = 4,
		res_up = 4
	)

	Necromancer: CharacterClass = CharacterClass()
	buildNarrowClass(Mage, Necromancer,
		narrow = "Necromancer",
		narrow_after_a = " Necromancer",
		desc = "Someone who can communicate with the dead, drawing power from the plane of Entropy to create magical effects.",
		specials = ["Necromancy"],
		languages = [],
		inventory = [],
		skills = ["Knowledge", "Knowledge: History", "Mental: Performance", "Physical: Sleight of Hand", "Weapons: Improvised"],
		dex = 0,
		agi = 0,
		str = 0,
		con = 1,
		int = 0,
		wis = 0,
		cha = 0,
		res = 0,
		dex_up = 0,
		agi_up = 8,
		str_up = 0,
		con_up = 0,
		int_up = 0,
		wis_up = 4,
		cha_up = 8,
		res_up = 0
	)

	Monk: CharacterClass = CharacterClass()
	buildNarrowClass(Specialist, Monk,
		narrow = "Monk",
		narrow_after_a = " Monk",
		desc = "Someone who is sworn to protect others of their religious order by whatever means possible.",
		specials = ["Unarmed Combat"],
		languages = [],
		inventory = [],
		skills = ["Knowledge: Culture", "Knowledge: History", "Knowledge: Linguistics", "Mental: Perception", "Physical: Acrobatics", "Weapons: Improvised", "Weapons: Melee", "Weapons: Trauma"],
		dex = 1,
		agi = 1,
		str = 0,
		con = 0,
		int = 0,
		wis = 0,
		cha = 0,
		res = 1,
		dex_up = 8,
		agi_up = 8,
		str_up = 0,
		con_up = 0,
		int_up = 4,
		wis_up = 0,
		cha_up = 0,
		res_up = 0
	)

	Artificer: CharacterClass = CharacterClass()
	buildNarrowClass(Specialist, Artificer,
		narrow = "Artificer",
		narrow_after_a = "n Artificer",
		desc = "Someone who is skilled with machinery and can create almost anything someone wants, for a price.",
		specials = ["Repairs"],
		languages = [],
		inventory = [],
		skills = ["Knowledge", "Knowledge: Arcana", "Mental: Investigation", "Mental: Perception", "Physical: Athletics", "Physical: Endurance", "Physical: Sleight of Hand", "Weapons: Piercing"],
		dex = 1,
		agi = 0,
		str = 1,
		con = 0,
		int = 1,
		wis = 0,
		cha = 0,
		res = 0,
		dex_up = 4,
		agi_up = 4,
		str_up = 4,
		con_up = 4,
		int_up = 4,
		wis_up = 0,
		cha_up = 0,
		res_up = 0
	)

	Merchant: CharacterClass = CharacterClass()
	buildNarrowClass(Specialist, Merchant,
		narrow = "Merchant",
		narrow_after_a = " Merchant",
		desc = "Someone who could sell someone the air they breathe or a plot of land at the summit of one of the Grey Mountains.",
		specials = ["Haggling"],
		languages = [],
		inventory = [],
		skills = ["Knowledge", "Knowledge: Culture", "Mental: Deception", "Mental: Perception", "Mental: Performance", "Mental: Persuasion", "Physical: Endurance", "Weapons: Trauma"],
		dex = 0,
		agi = 0,
		str = 0,
		con = 1,
		int = 0,
		wis = 1,
		cha = 1,
		res = 0,
		dex_up = 0,
		agi_up = 0,
		str_up = 0,
		con_up = 4,
		int_up = 0,
		wis_up = 8,
		cha_up = 8,
		res_up = 0
	)

	Aristocrat: CharacterClass = CharacterClass()
	buildNarrowClass(Specialist, Aristocrat,
		narrow = "Aristocrat",
		narrow_after_a = "n Aristocrat",
		desc = "Someone who is used to being in a position of authority and knows how to use that power.",
		specials = ["Interpersonal Skills"],
		languages = [],
		inventory = [],
		skills = ["Knowledge: Culture", "Knowledge: History", "Knowledge: Linguistics", "Mental: Intimidation", "Mental: Persuasion", "Physical: Acrobatics", "Physical: Stealth", "Weapons: Ranged"],
		dex = 0,
		agi = 1,
		str = 0,
		con = 0,
		int = 0,
		wis = 0,
		cha = 1,
		res = 1,
		dex_up = 4,
		agi_up = 0,
		str_up = 4,
		con_up = 0,
		int_up = 0,
		wis_up = 0,
		cha_up = 12,
		res_up = 0
	)
	