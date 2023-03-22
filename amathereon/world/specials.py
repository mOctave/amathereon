from typeclasses.characters import Character

# Defintion of all the different specials a character can have.

class Specials:
	def evaluate(character: Character):
		print(character)
		Specials.getSkillPoints(character)

	def evaluateNew(character: Character):
		print(character)
		Specials.getSkillPoints(character, True)

	def getSkillPoints(character: Character, isNew: bool = False):
		print(character.db.dex)
		print(character.db.specials)
		print(character.specials)
		if isNew:
			print("Character skill point conversion beginning for new character " + character.name)
			specialList:list[str] = character.specials
			skptConversions = -1
			for i in specialList:
				if i == "Select a Skill":
					print("Skill point converted for new character " + character.name)
					print(character.specials)
					character.skillpts += 1
					skptConversions += 1
					print(character.skillpts)
			for i in range(skptConversions):
				character.specials.remove("Select a Skill")

		else:
			print("Character skill point conversion beginning for existing character " + character.name)
			specialList:list[str] = character.db.specials
			skptConversions = -1
			for i in specialList:
				if i == "Select a Skill":
					print("Skill point converted for existing character " + character.name)
					print(character.db.specials)
					character.db.skillpts += 1
					skptConversions += 1
					print(character.db.skillpts)
			for i in range(skptConversions):
				character.db.specials.remove("Select a Skill")