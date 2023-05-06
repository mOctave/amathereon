# Everything related to currency

import math
from evennia.utils import inherits_from

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
	"""
	A class used to inform a player of the contents of a shop.
	"""
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
				msgtarget.msg(f"({i[1]}) {i[0]} -- {startText}{CalculateWorth.FindPrice('buyer')}")
			else:
				msgtarget.msg(f"({i[1]}) {i[0]} -- {startText}{CalculateWorth.FindPrice('none')}")
		return


class Valuer:
	"""
	A class to provide a rough estimate of the value of an object rather
	than a precise value.
	"""
	def Obscure (value: Gold, roughness):
		a = round(math.log(value.gr, roughness))
		b = round(pow(roughness, a), 1)
		return Gold(b)


class CalculateWorth:
	"""
	A class to handle the calculations involved in shopkeeping.
	"""

	def FindPrice (self, price, merchant: str):
		"""
		Calculates a price based on the default price and whether or not the buyer/seller is a merchant.
		Valid values of merchant are 'buyer', 'vendor', and 'none'
		"""
		validOptions = ("buyer","vendor","none")
		if merchant not in validOptions:
			raise ValueError("Parameter 'merchant' must be one of ('buyer','vendor','none')")
		if merchant == "buyer":
			return round(price * 0.95, 1)
		elif merchant == "vendor":
			return round(price * 1.05, 1)
		else:
			return round(price, 1)
		
	def FindCoinage(self, actor, target, value):
		"""
		Tries to find coinage that the actor can use to pay the target.
		"""

		coinNames = []
		coinValues = []
		coinValue = Gold(0)
		chosenCoins = []

		for item in [a for a in actor.contents if a.isCurrency]:
			coinNames.append(item.name)
			coinValues.append(item.db.value)
			coinValue += item.db.Value

		# Check if it's impossible to pay, and avoid the calculations if so
		if coinValue <= value:
			actor.msg("|RYou have insufficient funds to pay %s!" % target.name)
		else:
			sum = Gold(0)
			values = coinValues.copy()
			values.sort()
			# Try to find the smallest amount of money to pay with - imperfect method
			while sum < value:
				aim = value - sum
				selected = False
				for i in values:
					if i > aim:
						# You can cover the costs now, do it
						chosenCoins.append(coinNames.coinValues.index(i))
						values.remove(i)
						selected = True
				if not selected:
					# Use your most valuable coin, if possible
					chosenCoins.append(coinNames.coinValues.index(values.pop()))
			amountPaid = sum - value
				