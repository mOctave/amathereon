# Everything related to currency

import math

class Gold:
	# The number of grains of gold something is worth.
	# One grain of gold on Amathereon is worth about $2 in modern currency.
	gr: float

	def __new__ (cls, *args, **kwargs):
		return super().__new__(cls)

	def __init__ (self, value):
		self.gr = value

	def __repr__ (self) -> str:
		if self.gr > 480:
			return f"{math.floor(self.gr / 480)} t oz, {self.gr % 480} gr gold"
		else:
			return f"{self.gr} gr gold"
		
	def __add__ (self, other):
		return Gold(self.gr + other)
		
	def __sub__ (self, other):
		return Gold(self.gr - other)
		
	def __mul__ (self, other):
		return Gold(self.gr * other)
		
	def __truediv__ (self, other):
		return Gold(self.gr / other)
		
	def __floordiv__ (self, other):
		return Gold(self.gr // other)
		
	def __radd__ (self, other):
		return Gold(other + self.gr)
		
	def __rsub__ (self, other):
		return Gold(other - self.gr)
		
	def __rmul__ (self, other):
		return Gold(other * self.gr)
		
	def __round__ (self, ndigits = 0):
		return Gold(round(self.gr, ndigits))
	
	def __lt__ (self, other):
		return self.gr < other
		
	def __le__ (self, other):
		return self.gr <= other
		
	def __eq__ (self, other):
		return self.gr == other
	
	def __ne__ (self, other):
		return self.gr != other
		
	def __gt__ (self, other):
		return self.gr > other
		
	def __ge__ (self, other):
		return self.gr >= other
	
	def __int__ (self):
		return int(self.gr)
	
	def __float__ (self):
		return float(self.gr)

"""
A class used to inform a player of the contents of a shop.
"""
class ShopMessager:
	def ReturnArray (room, msgtarget):
		msgtarget.msg("|w--- Shop Contents ---")
		objectArray = []
		if not "shop" in room.db.flags:
			msgtarget.msg("This is not a shop! You cannot buy anything.")
			return

		print("Listing Shop Contents in " + room.name + " for " + msgtarget.name)
		for obj in room.contents:
			try:
				isItem = obj.isItem
			except:
				isItem = False
			if isItem:
				matchfound = False
				for i in range(0, len(objectArray)):
					# Handle different prices for similar objects
					if obj.name in objectArray[i]:
						if obj.db.value != objectArray[i][2]:
							objectArray[i][3] = True
							if obj.db.value < objectArray[i][2]:
								objectArray[i][2] = obj.db.value
					# Add similar object to list
						objectArray[i][1] += 1
						matchfound = True
						break
				# No object found, add unique object to list
				if not matchfound:
					objectArray.append([obj.name,1,obj.db.value, False])
		for i in objectArray:
			# Report contents, giving merchants a discount.
			if i[3]:
				startText = "starting at "
			else:
				startText = ""
			if msgtarget.db.charClass == "Merchant":
				msgtarget.msg(f"({i[1]}) {i[0]} -- {startText}{round(i[2] * 0.95, 1)}")
			else:
				msgtarget.msg(f"({i[1]}) {i[0]} -- {startText}{round(i[2], 1)}")
		return

"""
A class to provide a rough estimate of the value of an object rather
than a precise value.
"""
class Valuer:
	def Obscure (value: Gold, roughness):
		a = round(math.log(value.gr, roughness))
		b = round(pow(roughness, a), 1)
		return Gold(b)