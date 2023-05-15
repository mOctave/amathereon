# Everything related to currency

import math
from evennia.utils import inherits_from
from utils import Completion

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
		try:
			otherval = other.gr
			return Gold(self.gr + otherval)
		except:
			return Gold(self.gr + other)
		
	def __sub__ (self, other):
		try:
			otherval = other.gr
			return Gold(self.gr - otherval)
		except:
			return Gold(self.gr - other)
		
	def __mul__ (self, other):
		return Gold(self.gr * other)
		
	def __truediv__ (self, other):
		return Gold(self.gr / other)
		
	def __floordiv__ (self, other):
		return Gold(self.gr // other)
		
	def __radd__ (self, other):
		try:
			otherval = other.gr
			return Gold(otherval + self.gr)
		except:
			return Gold(other + self.gr)
		
	def __rsub__ (self, other):
		try:
			otherval = other.gr
			return Gold(otherval - self.gr)
		except:
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
		for obj in room.db.owner.contents:
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
			if "Merchant" in msgtarget.db.specials:
				msgtarget.msg(f"({i[1]}) {i[0]} -- {startText}{Shopkeeping.FindPrice(Shopkeeping, i[2] * room.db.markup, 'buyer')}")
			else:
				msgtarget.msg(f"({i[1]}) {i[0]} -- {startText}{Shopkeeping.FindPrice(Shopkeeping, i[2] * room.db.markup, 'none')}")
		if len(objectArray) == 0:
			msgtarget.msg("There is nothing for sale.")
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


class Shopkeeping:
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
		
	def FindCoinage(self, actor, target, value) -> bool:
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
			coinValue += item.db.value

		# Check if it's impossible to pay, and avoid the calculations if so
		if coinValue <= value:
			actor.msg("|RYou have insufficient funds to pay %s!" % target.name)
			return False
		
		sum = Gold(0)
		values = sorted(coinValues)
		actor.msg(coinValues)
		actor.msg(values)
		# Try to find the smallest amount of money to pay with - imperfect method
		try:
			while sum < value:
				aim = value - sum
				actor.msg("Aim: %s (%s-%s)" % (aim, value, sum))
				selected = False
				for i in values:
					if i >= aim:
						#actor.msg("Covering Costs of %s with %s" % (aim, i))
						# You can cover the costs now, do it
						chosenCoins.append(coinNames[coinValues.index(i)])
						values.remove(i)
						selected = True
						actor.msg([coinNames[coinValues.index(i)],i])
						sum += i
						raise Completion
				if not selected:
					#actor.msg("Using Maximum Value")
					# Use your most valuable coin, if possible
					val = values.pop()
					chosenCoins.append(coinNames[coinValues.index(val)])
					sum += val
		except Completion:
			pass

		# Actually hand over the coins
		self.TransferCoins(self, actor, target, chosenCoins)

		# Now give change
		changeOwed = sum - value
		#actor.msg("Change owed: %s (%s-%s)" % (changeOwed, sum, value))
		if changeOwed == Gold(0):
			#actor.msg("No Change Needed")
			return True
		change = Gold(0)
		changeCoins = []

		# Start by paying out of the target's cash.
		for item in [a for a in target.contents if a.isCurrency]:
			changeCoins.append(item)

		changeCoins.sort(key = lambda x: x.db.value, reverse=True)
		# Pay the most possible without going over - imperfect method
		try:
			while change < changeOwed:
				aim = changeOwed - change
				selected = False
				for coin in changeCoins:
					if coin.db.value <= aim:
						#actor.msg("Valid Change")
						# A valid coin has been found for change
						self.TransferCoins(self, target, actor, [coin.name])
						changeCoins.remove(coin)
						change += coin.db.value
						selected = True
						# Exact change is possible! Go on!
						if coin.db.value == aim:
							#actor.msg("Exact Change")
							raise Completion
				# It is impossible to make exact change, so move on.
				if not selected:
					#actor.msg("Exact Change Impossible")
					raise Completion
		except Completion:
			pass

		#actor.msg("Change paid out of change owed: %s / %s" % (change, changeOwed))
		actor.msg("You overpaid by %s, because %s could not make exact change." % (changeOwed - change, target))

		# Spawn and give new coins to make change with, depending on the target's nationality.

		return True

	def TransferCoins(self, actor, target, coinList: list[str]):
		for coin in coinList:
			self.FindCoinFromKey(self, coin, actor).move_to(target, quiet=True)
			actor.msg("Paid to %s: %s." % (target.name, coin))
			target.msg("Received from %s: %s." % (actor.name, coin))

	def FindCoinFromKey(self, key, location):
		for obj in location.contents:
			if obj.name == key:
				return obj