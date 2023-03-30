import sys
import inspect

def getVariableName(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]

class Religion:
	key: str # Key used to select the religion
	name: str # Proper name of the religion
	deity: str # Supreme diety worshipped by believers
	form: str # eg. Polytheism, Deism, Atheism
	type: str # eg. Organized, Folk, Cult
	the: bool # Does this religion need to be preceded by the word "the"?

	def __new__ (cls, *args, **kwargs):
		return super().__new__(cls)
	
	def __init__ (self, key: str = "none", name: str = "Unaffiliated", deity: str = "", form: str = "", type: str = "", the: bool = False):
		self.key = key
		self.name = name
		self.deity = deity
		self.form = form
		self.type = type
		self.the = the
	
	def __repr__(self) -> str:
		return f"{type(self).__name__}(key: '{self.key}', name: '{'(the) ' if self.the else ''}{self.name}', deity: '{self.deity}', form: '{self.form}', type: '{self.type}')"

class Religions:
	
	def getFromKey(key:str = "none"):
		for obj in inspect.getmembers(Religions):
			if isinstance(obj[1], Religion):
				if obj[1].key == key:
					return obj[1]
			else:
				try:
					print("Object %s has type %s, not type Religion." % (obj[1].__name__, type(obj[1]).__name__))
					pass
				except:
					print("Object has type %s, not type Religion." % (type(obj[1]).__name__))
		return Religion()

	OldSpirits: Religion = Religion("old-spirits", "Cult of the Old Spirits", "", "Nontheism", "Cult", True)
	ElvishCelestialism: Religion = Religion("elvish-celestialism", "Elvish Celestialism", "Alaforonaist'laiezeron", "Polytheism", "Folk", False)
	Litmeate: Religion = Religion("litmeate", "Faith of Litmeate", "Litmeate", "Monotheism", "Folk", True)
	Ratawanda: Religion = Religion("ratawanda", "Faith of Ratawanda", "Ratawanda", "Polytheism", "Organized", True)
	Grireverchism: Religion = Religion("grireverchism", "Grireverchism", "Grireverch", "Dualism", "Cult", False)
	Kazanzaram: Religion = Religion("kazan'zaram", "Kazan'zaram", "Tuzandunzat", "Deism", "Organized", False)
	Orlorianism: Religion = Religion("orlorianism", "Orlorianism", "Dodble", "Monotheism", "Organized", False)
	ShadowWorship: Religion = Religion("shadow-worship", "Shadow Worship", "Arakh", "Monolatrism", "Organized", False)
	Oracle: Religion = Religion("oracle", "Way of the Oracle", "Alaforonaist'laiezeron", "Henotheism", "Organized", True)

class Language:
	name: str # Name of the language, also used as a key
	writtenForm: bool # Does the language have a corresponding written language?
	isCant: bool # Is this a language associated with and closely guarded by a certain group?

	def __new__ (cls, *args, **kwargs):
		return super().__new__(cls)
	
	def __init__ (self, name: str, writtenForm: bool = False, isCant: bool = False):
		self.name = name
		self.writtenForm = writtenForm
		self.isCant = isCant

	def __repr__ (self) -> str:
		return f"{type(self).__name__}(name: {self.name}, writtenForm: {self.writtenForm}, isCant: {self.isCant})"

class Languages:

	# Get an array of all the languages
	def getAll():
		languages = []
		for obj in inspect.getmembers(Languages):
			if isinstance(obj[1], Language):
				languages.append(obj[1])
		return languages

	# Get a language with a specific name
	def getFromKey(key:str):
		for obj in inspect.getmembers(Languages):
			if isinstance(obj[1], Language):
				if obj[1].name == key:
					return obj[1]
			else:
				try:
					print("Object %s has type %s, not type Language." % (obj[1].__name__, type(obj[1]).__name__))
					pass
				except:
					print("Object has type %s, not type Language." % (type(obj[1]).__name__))
		print("No language found for key")

	Common: Language = Language("Common", True, False)
	Dwarvish: Language = Language("Dwarvish", True, False)
	Elvish: Language = Language("Elvish", True, False)
	Uruthk: Language = Language("Uruthk", True, False)
	Underspeak: Language = Language("Underspeak", False, False)
	Koboldic: Language = Language("Koboldic", True, False)
	Giant: Language = Language("Giant", True, False)
	Draconic: Language = Language("Draconic", False, False)
	Celestial: Language = Language("Celestial", True, False)
	ThievesCant: Language = Language("Thieves' Cant", False, True)
	Druidic: Language = Language("Druidic", False, True)