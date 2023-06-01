class Listings:
	"""
	A class storing weighted sets of prototype spawn options. 
	"""

	HILLROCKIAN_CURRENCY = [
		"hillrockian currency",
		[1,"hillrockian gold crown"],
		[1,"hillrockian gold mark"],
		[2,"hillrockian gold penny"],
		[4,"hillrockian silver penny"],
		[4,"hillrockian silver fifthpenny"],
		[1,"hillrockian gold penny","hillrockian gold penny"],
		[2,"hillrockian silver penny","hillrockian silver penny"],
		[2,"hillrockian silver fifthpenny","hillrockian silver fifthpenny"],
		[1,"hillrockian gold mark","hillrockian gold penny","hillrockian silver penny","hillrockian silver fifthpenny"],
	]

	STANDARD_WEAPONS = [
		"standard weapons",
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
		[2,"throwing knife"],
		[2,"swordbreaker"],
		[2,"sabre"],
		[2,"battleaxe"],
		[1,"greataxe"],
		[2,"warhammer"],
		[1,"bardiche"],
		[3,"halberd"],
		[2,"military fork"],
		[2,"pike"],
		[2,"partisan"],
		[1,"scythe"],
		[3,"javelin"],
		[2,"quarterstaff"],
		[1,"flail"],
		[2,"mace"],
	]

	All = (HILLROCKIAN_CURRENCY,STANDARD_WEAPONS)
