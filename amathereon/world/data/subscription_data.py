class Listings:
	"""
	A class storing weighted sets of prototype spawn options.
	"""

	HILLROCKIAN_CURRENCY = [
		"hillrockian_currency",
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

	STANDARD_WEAPONS = [
		"standard_weapons",
		[2,"sword"],
		[2,"axe"],
		[3,"spear"],
		[2,"club"],
		[4,"shield"],
		[2,"longsword"],
		[3,"shortsword"],
		[1,"claymore"],
		[2,"rapier"],
		[4,"dagger"],
		[1,"dagger","dagger"],
		[2,"throwing_knife"],
		[2,"swordbreaker"],
		[2,"sabre"],
		[2,"battleaxe"],
		[1,"greataxe"],
		[2,"warhammer"],
		[1,"bardiche"],
		[3,"halberd"],
		[2,"military_fork"],
		[2,"pike"],
		[2,"partisan"],
		[1,"scythe"],
		[3,"javelin"],
		[2,"quarterstaff"],
		[1,"flail"],
		[2,"mace"],
	]

	All = (HILLROCKIAN_CURRENCY, STANDARD_WEAPONS)
