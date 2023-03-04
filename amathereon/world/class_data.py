class CharacterClass:
	wide: str = "Citizen"
	wide_after_a: str = " Citizen"
	narrow: str = "Would-Be Adventurer"
	narrow_after_a: str = " Would-Be Adventurer"
	desc: str = "An ordinary person who wishes to take up a life of adventure."
	specials: list[str] = []
	languages: list[str] = []
	inventory: list[str] = []
	dex: int = 0
	agi: int = 0
	str: int = 0
	con: int = 0
	int: int = 0
	wis: int = 0
	cha: int = 0
	res: int = 0

	def __new__ (cls, *args, **kwargs):
		return super().__new__(cls)
	
	def __init__(self, wide: str = "Citizen", wide_after_a: str = " Citizen", narrow: str = "Would-Be Adventurer", narrow_after_a: str = " Would-Be Adventurer", desc: str = "An ordinary person who wishes to take up a life of adventure.", specials: list[str] = [], languages: list[str] = [], inventory: list[str] = [], dex: int = 0, agi: int = 0, str: int = 0, con: int = 0, int: int = 0, wis: int = 0, cha: int = 0, res: int = 0):
		self.wide = wide
		self.wide_after_a = wide_after_a
		self.narrow = narrow
		self.narrow_after_a = narrow_after_a
		self.desc = desc
		self.specials = specials
		self.languages = languages
		self.inventory = inventory
		self.dex = dex
		self.agi = agi
		self.str = str
		self.con = con
		self.int = int
		self.wis = wis
		self.cha = cha
		self.res = res
	
	def __repr__(self) -> str:
		return f"{type(self).__name__}(\n\twide=\"{self.wide}\", \"{self.wide_after_a}\"; narrow=\"{self.narrow}\", \"{self.narrow_after_a}\"; desc=\"{self.desc}\";\n\tspecials={self.specials}; languages={self.languages}; inventory={self.inventory};\n\tdex={self.dex}, agi={self.agi}, str={self.str}, con={self.con}, int={self.int}, wis={self.wis}, cha={self.cha}, res={self.cha}\n)"

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
	def buildNarrowClass(_class:CharacterClass, narrow:str, narrow_after_a:str, desc:str, specials:list[str], languages:list[str], inventory:list[str], dex:int, agi:int, str:int, con:int, int:int, wis:int, cha:int, res:int):
		_class.narrow = narrow
		_class.narrow_after_a = narrow_after_a
		_class.desc = desc
		for i in specials:
			_class.specials.append(i)
		for i in languages:
			_class.specials.append(i)
		for i in inventory:
			_class.specials.append(i)
		_class.dex += dex
		_class.agi += agi
		_class.str += str
		_class.con += con
		_class.int += int
		_class.wis += wis
		_class.cha += cha
		_class.res += res

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
		dex = 1,
		agi = 0,
		str = 0,
		con = 0,
		int = 0,
		wis = 0,
		cha = 1,
		res = 0
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
		dex = 0,
		agi = 0,
		str = 1,
		con = 0,
		int = 0,
		wis = 0,
		cha = 0,
		res = 1
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
		dex = 0,
		agi = 1,
		str = 0,
		con = 1,
		int = 0,
		wis = 0,
		cha = 0,
		res = 0
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
		dex = 0,
		agi = 0,
		str = 0,
		con = 0,
		int = 1,
		wis = 1,
		cha = 0,
		res = 0
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
		dex = 0,
		agi = 0,
		str = 0,
		con = 0,
		int = 0,
		wis = 0,
		cha = 0,
		res = 0
	)

	Thief: CharacterClass = Rogue
	buildNarrowClass(Thief,
		narrow = "Thief",
		narrow_after_a = " Thief",
		desc = "Someone who is very good at sneaking around and relieving people of their posessions.",
		specials = ["Stealth Expert"],
		languages = [],
		inventory = [],
		dex = 0,
		agi = 0,
		str = 0,
		con = 0,
		int = 1,
		wis = 0,
		cha = 0,
		res = 0
	)

	Assassin: CharacterClass = Rogue
	buildNarrowClass(Assassin,
		narrow = "Assassin",
		narrow_after_a = "n Assassin",
		desc = "Someone skilled in the art of desposing of inconvenient people, often in exchange for gold.",
		specials = ["Killing Blow"],
		languages = [],
		inventory = [],
		dex = 1,
		agi = 0,
		str = 0,
		con = 0,
		int = 0,
		wis = 0,
		cha = 0,
		res = 0
	)
	
	ConArtist: CharacterClass = Rogue
	buildNarrowClass(ConArtist,
		narrow = "Con Artist",
		narrow_after_a = " Con Artist",
		desc = "Someone who can trick people into believing what they want just long enough to make a profit.",
		specials = ["Interpersonal Skills"],
		languages = [],
		inventory = [],
		dex = 0,
		agi = 0,
		str = 0,
		con = 0,
		int = 0,
		wis = 0,
		cha = 1,
		res = 0
	)

	Spy: CharacterClass = Rogue
	buildNarrowClass(Spy,
		narrow = "Spy",
		narrow_after_a = " Spy",
		desc = "Someone who can gather information and use it to their advantage.",
		specials = ["Stealth Expert"],
		languages = [],
		inventory = [],
		dex = 0,
		agi = 1,
		str = 0,
		con = 0,
		int = 0,
		wis = 0,
		cha = 0,
		res = 0
	)

	Brawler: CharacterClass = Warrior
	buildNarrowClass(Brawler,
		narrow = "Brawler",
		narrow_after_a = " Brawler",
		desc = "Someone who can hold their own in any fight, even if they don't have any weapons.",
		specials = ["Unarmed Combat"],
		languages = [],
		inventory = [],
		dex = 0,
		agi = 0,
		str = 1,
		con = 0,
		int = 0,
		wis = 0,
		cha = 0,
		res = 0
	)

	Knight: CharacterClass = Warrior
	buildNarrowClass(Knight,
		narrow = "Knight",
		narrow_after_a = " Knight",
		desc = "Someone who is skilled in the use of armour as a means of protecting themselves and others.",
		specials = ["Heavy Armour"],
		languages = [],
		inventory = [],
		dex = 0,
		agi = 0,
		str = 0,
		con = 1,
		int = 0,
		wis = 0,
		cha = 0,
		res = 0
	)

	Soldier: CharacterClass = Warrior
	buildNarrowClass(Soldier,
		narrow = "Soldier",
		narrow_after_a = " Soldier",
		desc = "Someone who has been fighting in combat for years and has picked up some tricks.",
		specials = ["Veteran"],
		languages = [],
		inventory = [],
		dex = 0,
		agi = 0,
		str = 0,
		con = 0,
		int = 0,
		wis = 0,
		cha = 0,
		res = 1
	)

	Paladin: CharacterClass = Warrior
	buildNarrowClass(Brawler,
		narrow = "Paladin",
		narrow_after_a = " Paladin",
		desc = "Someone who fights for the advancement of their god or religion, and for the upholding of ideals.",
		specials = ["Divination"],
		languages = [],
		inventory = [],
		dex = 0,
		agi = 1,
		str = 0,
		con = 0,
		int = 0,
		wis = 0,
		cha = 0,
		res = 0
	)

	Ranger: CharacterClass = Outlander
	buildNarrowClass(Ranger,
		narrow = "Ranger",
		narrow_after_a = " Ranger",
		desc = "Someone with lots of experience with the wilderness and some skill with weapons.",
		specials = ["Tracking"],
		languages = [],
		inventory = [],
		dex = 1,
		agi = 0,
		str = 0,
		con = 0,
		int = 0,
		wis = 0,
		cha = 0,
		res = 0
	)

	Barbarian: CharacterClass = Outlander
	buildNarrowClass(Barbarian,
		narrow = "Barbarian",
		narrow_after_a = " Barbarian",
		desc = "Someone who appears at first glance to be simple and uneducated, but who has substantial survival experience.",
		specials = ["Rage"],
		languages = [],
		inventory = [],
		dex = 0,
		agi = 0,
		str = 1,
		con = 0,
		int = 0,
		wis = 0,
		cha = 0,
		res = 0
	)

	Druid: CharacterClass = Outlander
	buildNarrowClass(Druid,
		narrow = "Druid",
		narrow_after_a = " Druid",
		desc = "Someone with experience both with the wilderness and in druidic magic.",
		specials = ["Druidcraft"],
		languages = ["Druidic"],
		inventory = [],
		dex = 0,
		agi = 0,
		str = 0,
		con = 0,
		int = 0,
		wis = 1,
		cha = 0,
		res = 0
	)

	Bard: CharacterClass = Outlander
	buildNarrowClass(Bard,
		narrow = "Bard",
		narrow_after_a = " Bard",
		desc = "Someone who is a skilled musician, wandering from place to place seeking glory and gold.",
		specials = ["Musicianship"],
		languages = [],
		inventory = [],
		dex = 0,
		agi = 0,
		str = 0,
		con = 0,
		int = 0,
		wis = 0,
		cha = 1,
		res = 0
	)

	Wizard: CharacterClass = Mage
	buildNarrowClass(Wizard,
		narrow = "Wizard",
		narrow_after_a = " Wizard",
		desc = "Someone who has devoted their life to the scientific study of magic, and who uses that knowledge in their own spells.",
		specials = ["Select a Language", "Wizardraft"],
		languages = [],
		inventory = [],
		dex = 0,
		agi = 0,
		str = 0,
		con = 0,
		int = 0,
		wis = 1,
		cha = 0,
		res = 0
	)

	Sorcerer: CharacterClass = Mage
	buildNarrowClass(Sorcerer,
		narrow = "Sorcerer",
		narrow_after_a = " Sorcerer",
		desc = "Someone who draws magical power from the plane of Posibility and uses it to shape the world.",
		specials = ["Sorcery"],
		languages = [],
		inventory = [],
		dex = 0,
		agi = 0,
		str = 0,
		con = 0,
		int = 1,
		wis = 0,
		cha = 0,
		res = 0
	)

	Cleric: CharacterClass = Mage
	buildNarrowClass(Cleric,
		narrow = "Cleric",
		narrow_after_a = " Cleric",
		desc = "Someone who uses holy magic to further the goals of their religion and to promote its ideals.",
		specials = ["Divination"],
		languages = [],
		inventory = [],
		dex = 0,
		agi = 0,
		str = 0,
		con = 0,
		int = 0,
		wis = 0,
		cha = 0,
		res = 1
	)

	Necromancer: CharacterClass = Mage
	buildNarrowClass(Necromancer,
		narrow = "Necromancer",
		narrow_after_a = " Necromancer",
		desc = "Someone who can communicate with the dead, drawing power from the plane of Entropy to create magical effects.",
		specials = ["Necromancy"],
		languages = [],
		inventory = [],
		dex = 0,
		agi = 0,
		str = 0,
		con = 1,
		int = 0,
		wis = 0,
		cha = 0,
		res = 0
	)

	Monk: CharacterClass = Specialist
	buildNarrowClass(Monk,
		narrow = "Monk",
		narrow_after_a = " Monk",
		desc = "Someone who is sworn to protect others of their religious order by whatever means possible.",
		specials = ["Unarmed Combat"],
		languages = [],
		inventory = [],
		dex = 1,
		agi = 1,
		str = 0,
		con = 0,
		int = 0,
		wis = 0,
		cha = 0,
		res = 1
	)

	Artificer: CharacterClass = Specialist
	buildNarrowClass(Artificer,
		narrow = "Artificer",
		narrow_after_a = "n Artificer",
		desc = "Someone who is skilled with machinery and can create almost anything someone wants, for a price.",
		specials = ["Repairs"],
		languages = [],
		inventory = [],
		dex = 1,
		agi = 0,
		str = 1,
		con = 0,
		int = 1,
		wis = 0,
		cha = 0,
		res = 0
	)

	Merchant: CharacterClass = Specialist
	buildNarrowClass(Merchant,
		narrow = "Merchant",
		narrow_after_a = " Merchant",
		desc = "Someone who could sell someone the air they breathe or a plot of land at the summit of one of the Grey Mountains.",
		specials = ["Haggling"],
		languages = [],
		inventory = [],
		dex = 0,
		agi = 0,
		str = 0,
		con = 1,
		int = 0,
		wis = 1,
		cha = 1,
		res = 0
	)

	Aristocrat: CharacterClass = Specialist
	buildNarrowClass(Aristocrat,
		narrow = "Aristocrat",
		narrow_after_a = "n Aristocrat",
		desc = "Someone who is used to being in a position of authority and knows how to use that power.",
		specials = ["Interpersonal Skills"],
		languages = [],
		inventory = [],
		dex = 0,
		agi = 1,
		str = 0,
		con = 0,
		int = 0,
		wis = 0,
		cha = 1,
		res = 1
	)
	