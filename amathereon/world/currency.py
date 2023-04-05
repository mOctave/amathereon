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

class ShopMessager:
	def ReturnArray (room, msgtarget):
		msgtarget.msg("|w--- Shop Contents ---")
		objectArray = []
		#if room.db.shop == False:
		#	msgtarget.msg("This is not a shop! You cannot buy anything.")
		#	return
		print("Listing Shop Contents in " + room.name + " for " + msgtarget.name)
		for obj in room.contents:
			try:
				isItem = obj.isItem
			except:
				isItem = False
			if isItem:
				matchfound = False
				for i in range(0, len(objectArray)):
					if obj.name in objectArray[i]:
						objectArray[i][1] += 1
						matchfound = True
				if not matchfound:
					if msgtarget.db.charClass == "Merchant":
						objectArray.append([obj.name,1,round(obj.db.value * 0.95, 1)])
					else:
						objectArray.append([obj.name,1,round(obj.db.value, 1)])
		for i in objectArray:
			msgtarget.msg(f"({i[1]}) {i[0]} -- {i[2]}")
		return