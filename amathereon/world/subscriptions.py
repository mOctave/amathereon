from world.data.subscription_data import Listings

import utils

import random

class SubscriptionHandler:
	"""
	A class designed to deal with a character's subscriptions (items that they are given on a timer)
	"""
	def fulfill(self, character, subscription):
		# Figure out which subscription to fulfill
		selectedList = None
		for sub in Listings.All:
			print(sub[0])
			if sub[0] == subscription:
				selectedList = sub.copy()
				break
		if selectedList == None:
			raise Exception("No list matched selection!")
		# Choose a variant
		thresholds = []
		for i in range(1,len(selectedList)):
			print(selectedList[i])
			if len(thresholds) == 0:
				thresholds.append(selectedList[i][0])
			else:
				thresholds.append(thresholds[-1] + selectedList[i][0])
		print(thresholds)
		chosenValue = random.randint(1, thresholds[-1])
		print(chosenValue)
		selection = None
		for entry in thresholds:
			if chosenValue <= entry:
				selection = selectedList[thresholds.index(entry) + 1].copy()
				break
		print(selection)
		selection.pop(0)
		# Spawn prototypes
		for prot in selection:
			utils.spawnFromKey(prot, character)

