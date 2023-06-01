"""
Currency Prototypes
"""
from world.currency import Gold

CURRENCY = {
	"prototype_key": "CURRENCY",
	"typeclass": "typeclasses.objects.Currency",
	"key": "currency"
}

HILLROCKIAN_GOLD_CROWN = {
	"prototype_key": "HILLROCKIAN_GOLD_CROWN",
	"prototype_parent": "CURRENCY",
	"key": "hillrockian gold crown",
	"desc": "This Hillrockian gold crown is not-quite pure gold, weighing about forty grains. It has been stamped with the head of some minor prince, which appears to be a tradition of the royal family. Worth: 40 gr gold.",
	"value": lambda: Gold(40),
	"mass": 40/16/120
}

HILLROCKIAN_GOLD_MARK = {
	"prototype_key": "HILLROCKIAN_GOLD_MARK",
	"prototype_parent": "CURRENCY",
	"key": "hillrockian gold mark",
	"desc": "This Hillrockian gold mark is slightly smaller than a gold crown, and worth about half as much. It is decorated with an intricate geometric design. Worth: 20 gr gold.",
	"value": lambda: Gold(20),
	"mass": 20/16/80
}

HILLROCKIAN_GOLD_PENNY = {
	"prototype_key": "HILLROCKIAN_GOLD_PENNY",
	"prototype_parent": "CURRENCY",
	"key": "hillrockian gold penny",
	"desc": "This Hillrockian gold penny is the smallest unit of currency in Hillrockia when it comes to gold. It bears no design, being just a thick, small disk of pure gold. Worth: 5 gr gold.",
	"value": lambda: Gold(5),
	"mass": 5/16/480
}

HILLROCKIAN_SILVER_PENNY = {
	"prototype_key": "HILLROCKIAN_SILVER_PENNY",
	"prototype_parent": "CURRENCY",
	"key": "hillrockian silver penny",
	"desc": "This Hillrockian silver penny is used among Hillrockians for when even their smallest gold coins are too valuable. Worth: 1 gr gold.",
	"value": lambda: Gold(1),
	"mass": 4/16/480
}

HILLROCKIAN_SILVER_FIFTHPENNY = {
	"prototype_key": "HILLROCKIAN_SILVER_FIFTHPENNY",
	"prototype_parent": "CURRENCY",
	"key": "hillrockian silver fifthpenny",
	"desc": "This coin is, quite literally, a fifth of a Hillrockian silver penny. Worth: 0.2 gr gold.",
	"value": lambda: Gold(0.2),
	"mass": 4/5/16/480
}
