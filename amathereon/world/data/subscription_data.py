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

	TAILORED_CLOTHES = [
		"tailored clothes",
		[3,"cotton_shirt"],
		[4,"wool_shirt"],
		[1,"silk_shirt"],
		[2,"leather_coat"],
		[4,"cap"],
		[2,"straw_hat"],
		[2,"cotton_gloves"],
		[2,"wool_gloves"],
		[1,"silk_gloves"],
		[2,"leather_gloves"],
		[3,"cotton_pants"],
		[3,"denim_pants"],
		[1,"silk_leggings"],
		[3,"leather_pants"],
		[3,"wool_socks"],
		[1,"silk_socks"],
		[2,"sandles"],
		[2,"boots"],
	]

	ARMOUR = [
		"armour",
		[3,"chain_shirt"],
		[2,"chestplate"],
		[1,"shell_plate"],
		[1,"laminar_mail_shirt"],
		[2,"chain_hood"],
		[2,"armet"],
		[2,"barbute"],
		[1,"lamellar_helmet"],
		[4,"gauntlets"],
		[2,"chain_leggings"],
		[2,"leg_plate"],
		[2,"sabatons"],
	]

	FINE_CLOTHES = [
		"fine clothes",
		[2,"silk_shirt"],
		[2,"silk_gloves"],
		[2,"silk_leggings"],
		[2,"silk_socks"],
		[1,"mage_jacket"],
		[1,"elvyren"],
	]

	All = (ARMOUR, FINE_CLOTHES, HILLROCKIAN_CURRENCY, STANDARD_WEAPONS, TAILORED_CLOTHES)
