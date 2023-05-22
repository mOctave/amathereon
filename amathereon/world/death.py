from evennia.utils.evmenu import EvMenu

def node_main(caller):
	"""Starting page."""
	text = 'You hear Onarezuron\'s voice, and you know it is him, although you have never seen or heard him before: "Mortal, are you ready to die? Your life is still strong within you, and it is not necessarily your time yet."'

	options = (
		{"key": ("Yes"),
		 "desc": "Yes, it is my time to die, and I am ready.",
		 "goto": "node_die"},
		{"key": ("No"),
		 "desc": "No! This can't be happening to me! I'm not dead.",
		 "goto": ("node_live")})

	return text, options

def node_live(caller, raw_string, **kwargs):
	caller.msg('"Very well then, you will live. Go, and walk the world once more, and I will be waiting. Waiting for you to come again."')

	caller.move_to(caller.search("#2", global_search=True))

	return None, None

def node_die(caller, raw_string, **kwargs):
	caller.msg('"Yes, I see that you are ready. Come, Entropy awaits you, and you may yet watch the end of time."')
	caller.execute_cmd("ooc")
	caller.delete()

	return None, None