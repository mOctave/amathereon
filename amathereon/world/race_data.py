class CharacterRace:
	name: str = "Unborn"
	after_a: str = "n Unborn"
	desc: str = "A mistlike being waiting to come into the world."
	specials: list[str] = []
	languages: list[str] = []
	dex: int = 0
	agi: int = 0
	str: int = 0
	con: int = 0
	int: int = 0
	wis: int = 0
	cha: int = 0
	res: int = 0

class Races():

	# Select a race using a key
	def getRaceFromKey(key):
		if key == "Human":
			return Races.Human
		elif key == "Halfling":
			return Races.Halfling
		elif key == "Dwarf":
			return Races.Dwarf
		elif key == "Elf":
			return Races.Elf
		elif key == "Half-Elf":
			return Races.Half_Elf
		elif key == "Urunk":
			return Races.Urunk
		elif key == "Gnome":
			return Races.Gnome
		elif key == "Goblin":
			return Races.Goblin
		else:
			return CharacterRace

	# Fill in data for a CharacterRace
	def populateRace(race:CharacterRace, name:str, after_a:str, desc:str, specials:list[str], languages:list[str], dex:int, agi:int, str:int, con:int, int:int, wis:int, cha:int, res:int):
		race.name = name
		race.after_a = after_a
		race.desc = desc
		race.specials = specials
		race.languages = languages
		race.dex = dex
		race.agi = agi
		race.str = str
		race.con = con
		race.int = int
		race.wis = wis
		race.cha = cha
		race.res = res

	Human = CharacterRace()
	populateRace(
		Human,
		name = "Human",
		after_a = " Human",
		desc = "Very versatile, but not particularly strong in any given field. Somewhat cunning.",
		specials = ["Select a Skill", "Select a Skill"],
		languages = ["Common"],
		dex = 1,
		agi = 1,
		str = 1,
		con = 1,
		int = 2,
		wis = 1,
		cha = 1,
		res = 1
	)

	Halfling = CharacterRace ()
	populateRace(
		Halfling,
		name = "Halfling",
		after_a = " Halfling",
		desc = "Stout and extremely resilient. Reasonably wise and charismatic.",
		specials = ["Indomitable", "Select a Skill", "Select a Skill"],
		languages = ["Common"],
		dex = 1,
		agi = 0,
		str = 0,
		con = 1,
		int = 0,
		wis = 1,
		cha = 1,
		res = 3
	)

	Dwarf = CharacterRace ()
	populateRace(
		Dwarf,
		name = "Dwarf",
		after_a = " Dwarf",
		desc = "Strong and capable. Good with metal and stone.",
		specials = ["Rock Lore", "Select a Skill", "Select a Skill"],
		languages = ["Common", "Dwarvish", "Underspeak"],
		dex = 1,
		agi = 0,
		str = 2,
		con = 2,
		int = 0,
		wis = 1,
		cha = 0,
		res = 1
	)

	Elf = CharacterRace ()
	populateRace(
		Elf,
		name = "Elf",
		after_a = "n Elf",
		desc = "Wise and potentially immortal. Also very agile.",
		specials = ["Elvish Blood", "Darkvision"],
		languages = ["Common", "Elvish", "Druidic"],
		dex = 1,
		agi = 2,
		str = 0,
		con = 0,
		int = 1,
		wis = 2,
		cha = 1,
		res = 0
	)

	Half_Elf = CharacterRace ()
	populateRace(
		Half_Elf,
		name = "Half-Elf",
		after_a = " Half-Elf",
		desc = "Generally very touchy about their mixed heritage. Some aspects of humanity, some of elvenkind.",
		specials = ["Elvish Blood"],
		languages = ["Common", "Elvish"],
		dex = 1,
		agi = 2,
		str = 0,
		con = 0,
		int = 2,
		wis = 2,
		cha = 1,
		res = 1
	)

	Urunk = CharacterRace ()
	populateRace(
		Urunk,
		name = "Urunk",
		after_a = "n Urunk",
		desc = "Although not one of the Accursed, often dim-witted and subservient to them. Very capapble warriors.",
		specials = ["Attunement","Tracking"],
		languages = ["Common", "Uruthk"],
		dex = 1,
		agi = 1,
		str = 2,
		con = 3,
		int = 0,
		wis = 0,
		cha = -1,
		res = 1
	)

	Gnome = CharacterRace ()
	populateRace(
		Gnome,
		name = "Gnome",
		after_a = " Gnome",
		desc = "Capable of flight, having a love of both the air and the earth.",
		specials = ["Flight","Rock Lore"],
		languages = ["Common", "Underspeak"],
		dex = 2,
		agi = 2,
		str = 0,
		con = 0,
		int = 1,
		wis = 1,
		cha = 1,
		res = 0
	)

	Goblin = CharacterRace ()
	populateRace(
		Goblin,
		name = "Goblin",
		after_a = " Goblin",
		desc = "Sneaky, and tainted by the Darkness, although not one of the Accursed. They have very nimble fingers.",
		specials = ["Darkvision","Attunement"],
		languages = ["Common", "Underspeak"],
		dex = 3,
		agi = 2,
		str = 0,
		con = 0,
		int = 1,
		wis = 0,
		cha = 0,
		res = 1
	)