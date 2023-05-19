class Listings:
	"""
	A class storing weighted sets of prototype spawn options. 
	"""

	HILLROCKIAN_CURRENCY = [
		"hillrockian currency",
		[1,"hillrockian_gold_crown"],
		[1,"hillrockian_gold_mark"],
		[2,"hillrockian_gold_penny"],
		[4,"hillrockian_silver_penny"],
		[4,"hillrockian_silver_fifthpenny"],
		[1,"hillrockian_gold_penny","hillrockian_gold_penny"],
		[2,"hillrockian_silver_penny","hillrockian_silver_penny"],
		[2,"hillrockian_silver_fifthpenny","hillrockian_silver_fifthpenny"],
		[1,"hillrockian_gold_mark","hillrockian_gold_penny","hillrockian_silver_penny","hillrockian_silver_fifthpenny"],
	]

	All = (HILLROCKIAN_CURRENCY,)
