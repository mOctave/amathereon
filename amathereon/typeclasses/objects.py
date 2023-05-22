"""
Object

The Object is the "naked" base class for things in the game world.

Note that the default Character, Room and Exit does not inherit from
this Object, but from their respective default implementations in the
evennia library. If you want to use this class as a parent to change
the other types, you can do so by adding this as a multiple
inheritance.

"""
from evennia.objects.objects import DefaultObject
from evennia.utils import inherits_from

from world.currency import Gold, Valuer
from world.lighting import Lighting

from commands.gametime import custom_gametime

class ObjectParent:
	"""
	This is a mixin that can be used to override *all* entities inheriting at
	some distance from DefaultObject (Objects, Exits, Characters and Rooms).

	Just add any method that exists on `DefaultObject` to this class. If one
	of the derived classes has itself defined that same hook already, that will
	take precedence.

	"""
	isCurrency = False
	isClothing = False

	def return_appearance(self, looker, **kwargs):
		if Lighting.CalcLighting(looker) == 2:
			x = ""
			if self.db.value != None:
				if self.db.value == Gold(0):
					x = f"\nWorthless."
				else:
					x = f"\nWorth about {Valuer.Obscure(self.db.value, 2)}."

			return self.format_appearance(
				self.appearance_template.format(
					name=self.get_display_name(looker, **kwargs),
					desc=self.get_display_desc(looker, **kwargs) + x,
					header=self.get_display_header(looker, **kwargs),
					footer=self.get_display_footer(looker, **kwargs),
					exits=self.get_display_exits(looker, **kwargs),
					characters=self.get_display_characters(looker, **kwargs),
					things=self.get_display_things(looker, **kwargs),
				),
				looker,
				**kwargs,
			)
		elif Lighting.CalcLighting(looker) == 1:
			return self.format_appearance(
				self.appearance_template.format(
					name=self.get_display_name(looker, **kwargs),
					desc="The light's dim, so you can't see anything too clearly.",
					header=self.get_display_header(looker, **kwargs),
					footer=self.get_display_footer(looker, **kwargs),
					exits=self.get_display_exits(looker, **kwargs),
					characters=self.get_display_characters(looker, **kwargs),
					things=self.get_display_things(looker, **kwargs),
				),
				looker,
				**kwargs,
			)
		else:
			return self.format_appearance(
				self.appearance_template.format(
					name="Darkness",
					desc="It's pitch black, and you can't see a thing.",
					header="",
					footer="",
					exits="",
					characters="",
					things="",
				),
				looker,
				**kwargs,
			)
	
	def get_extra_info(self, looker, **kwargs):
		"""
		Used when an object is in a list of ambiguous objects as an
		additional information tag.

		For instance, if you had potions which could have varying
		levels of liquid left in them, you might want to display how
		many drinks are left in each when selecting which to drop, but
		not in your normal inventory listing.

		Args:
			looker (TypedObject): The object or account that is looking
				at/getting information for this object.

		Returns:
			info (str): A string with disambiguating information,
				conventionally with a leading space.

		"""
		if self.location == looker:
			for key in list(looker.db.wornItems.keys()):
				if len(looker.db.wornItems[key]) > 0:
					if self == looker.db.wornItems[key][-1]:
						return " (worn, outer layer)"
			if self in looker.wornItemList:
				return " (worn)"
			elif self in looker.db.wieldedItems:
				return " (wielded)"
			else:
				return " (carried)"
		return ""

class Object(ObjectParent, DefaultObject):
	"""
	This is the root typeclass object, implementing an in-game Evennia
	game object, such as having a location, being able to be
	manipulated or looked at, etc. If you create a new typeclass, it
	must always inherit from this object (or any of the other objects
	in this file, since they all actually inherit from BaseObject, as
	seen in src.object.objects).

	The BaseObject class implements several hooks tying into the game
	engine. By re-implementing these hooks you can control the
	system. You should never need to re-implement special Python
	methods, such as __init__ and especially never __getattribute__ and
	__setattr__ since these are used heavily by the typeclass system
	of Evennia and messing with them might well break things for you.


	* Base properties defined/available on all Objects

	 key (string) - name of object
	 name (string)- same as key
	 dbref (int, read-only) - unique #id-number. Also "id" can be used.
	 date_created (string) - time stamp of object creation

	 account (Account) - controlling account (if any, only set together with
					   sessid below)
	 sessid (int, read-only) - session id (if any, only set together with
					   account above). Use `sessions` handler to get the
					   Sessions directly.
	 location (Object) - current location. Is None if this is a room
	 home (Object) - safety start-location
	 has_account (bool, read-only)- will only return *connected* accounts
	 contents (list of Objects, read-only) - returns all objects inside this
					   object (including exits)
	 exits (list of Objects, read-only) - returns all exits from this
					   object, if any
	 destination (Object) - only set if this object is an exit.
	 is_superuser (bool, read-only) - True/False if this user is a superuser

	* Handlers available

	 aliases - alias-handler: use aliases.add/remove/get() to use.
	 permissions - permission-handler: use permissions.add/remove() to
				   add/remove new perms.
	 locks - lock-handler: use locks.add() to add new lock strings
	 scripts - script-handler. Add new scripts to object with scripts.add()
	 cmdset - cmdset-handler. Use cmdset.add() to add new cmdsets to object
	 nicks - nick-handler. New nicks with nicks.add().
	 sessions - sessions-handler. Get Sessions connected to this
				object with sessions.get()
	 attributes - attribute-handler. Use attributes.add/remove/get.
	 db - attribute-handler: Shortcut for attribute-handler. Store/retrieve
			database attributes using self.db.myattr=val, val=self.db.myattr
	 ndb - non-persistent attribute handler: same as db but does not create
			a database entry when storing data

	* Helper methods (see src.objects.objects.py for full headers)

	 search(ostring, global_search=False, attribute_name=None,
			 use_nicks=False, location=None, ignore_errors=False, account=False)
	 execute_cmd(raw_string)
	 msg(text=None, **kwargs)
	 msg_contents(message, exclude=None, from_obj=None, **kwargs)
	 move_to(destination, quiet=False, emit_to_obj=None, use_destination=True)
	 copy(new_key=None)
	 delete()
	 is_typeclass(typeclass, exact=False)
	 swap_typeclass(new_typeclass, clean_attributes=False, no_default=True)
	 access(accessing_obj, access_type='read', default=False)
	 check_permstring(permstring)

	* Hooks (these are class methods, so args should start with self):

	 basetype_setup()	 - only called once, used for behind-the-scenes
							setup. Normally not modified.
	 basetype_posthook_setup() - customization in basetype, after the object
							has been created; Normally not modified.

	 at_object_creation() - only called once, when object is first created.
							Object customizations go here.
	 at_object_delete() - called just before deleting an object. If returning
							False, deletion is aborted. Note that all objects
							inside a deleted object are automatically moved
							to their <home>, they don't need to be removed here.

	 at_init()			- called whenever typeclass is cached from memory,
							at least once every server restart/reload
	 at_cmdset_get(**kwargs) - this is called just before the command handler
							requests a cmdset from this object. The kwargs are
							not normally used unless the cmdset is created
							dynamically (see e.g. Exits).
	 at_pre_puppet(account)- (account-controlled objects only) called just
							before puppeting
	 at_post_puppet()	 - (account-controlled objects only) called just
							after completing connection account<->object
	 at_pre_unpuppet()	- (account-controlled objects only) called just
							before un-puppeting
	 at_post_unpuppet(account) - (account-controlled objects only) called just
							after disconnecting account<->object link
	 at_server_reload()   - called before server is reloaded
	 at_server_shutdown() - called just before server is fully shut down

	 at_access(result, accessing_obj, access_type) - called with the result
							of a lock access check on this object. Return value
							does not affect check result.

	 at_pre_move(destination)			 - called just before moving object
						to the destination. If returns False, move is cancelled.
	 announce_move_from(destination)		 - called in old location, just
						before move, if obj.move_to() has quiet=False
	 announce_move_to(source_location)	   - called in new location, just
						after move, if obj.move_to() has quiet=False
	 at_post_move(source_location)		  - always called after a move has
						been successfully performed.
	 at_object_leave(obj, target_location)   - called when an object leaves
						this object in any fashion
	 at_object_receive(obj, source_location) - called when this object receives
						another object

	 at_traverse(traversing_object, source_loc) - (exit-objects only)
							  handles all moving across the exit, including
							  calling the other exit hooks. Use super() to retain
							  the default functionality.
	 at_post_traverse(traversing_object, source_location) - (exit-objects only)
							  called just after a traversal has happened.
	 at_failed_traverse(traversing_object)	  - (exit-objects only) called if
					   traversal fails and property err_traverse is not defined.

	 at_msg_receive(self, msg, from_obj=None, **kwargs) - called when a message
							 (via self.msg()) is sent to this obj.
							 If returns false, aborts send.
	 at_msg_send(self, msg, to_obj=None, **kwargs) - called when this objects
							 sends a message to someone via self.msg().

	 return_appearance(looker) - describes this object. Used by "look"
								 command by default
	 at_desc(looker=None)	  - called by 'look' whenever the
								 appearance is requested.
	 at_get(getter)			- called after object has been picked up.
								 Does not stop pickup.
	 at_drop(dropper)		  - called when this object has been dropped.
	 at_say(speaker, message)  - by default, called if an object inside this
								 object speaks

	"""
	isItem = True

	def at_object_creation(self):
		self.db.value: Gold = Gold(0)
		self.db.mass = 0
		self.db.isLit = False

class Clothing(Object):
	"""
	Objects that can be worn

	* Properties:

	 "minLayers" - minimum thickness of undergarments
	 "maxLayers" - maximum thickness of undergarments
	 "layers" - thickness added by this garment

	 "piercingBlock" - hit chance reductions by damage type
	 "slashingBlock"
	 "traumaBlock"
	 "magicBlock"

	 "piercingProtect" - damage reductions by damage type
	 "slashingProtect"
	 "traumaProtect"
	 "magicProtect"

	 "critProtect" - critical hit chance reduction

	 "weartype" - where the garment can be worn
	"""
	isItem = True
	isClothing = True

	def at_object_creation(self):
		super().at_object_creation()

	def at_pre_move(self, destination, move_type, **kwargs):
		super().at_pre_move(destination, move_type)
		# Don't let worn clothing be moved
		if inherits_from(self.location, "typeclasses.characters.Character"):
			if self in self.location.wornItemList:
				self.location.msg("You'll need to take that off first!")
				return False
		return True

	def at_object_delete(self):
		# Clear worn clothing from all lists upon deletion
		if inherits_from(self.location, "typeclasses.characters.Character"):
			for key in ["head","torso","hands","legs","feet"]:
				self.location.db.wornItems[key].remove(self)
		return True

class Weapon(Object):
	"""
	This is the base class for a weapon. Important database attributes are:
	
	\ndamageType  - One of "Piercing", "Slashing", or "Trauma"
	\nrange       - What the effective range of the weapon is. 0 for melee weapons.
	\nammo        - If range is greater than 0, what object this weapon uses for ammo.
	                If this is not defined, the weapon will be thrown when used.
	\nminDamage   - The base minimum damage dealt by this weapon.
	\nmaxDamage   - The base maximum damage dealt by this weapon.
	\nhitChance   - The base chance (out of 100) that this weapon will connect.
	\ncritChance  - The base chance (out of 100) that this weapon will deal double damage before counting armour.
	\nparryChance - The base chance (out of 100) that a character can successfully parry with this weapon.
	\nhands	      - The number of hands needed to wield this weapon.
	"""

	def at_pre_drop(self, dropper, **kwargs):
		# If currently wielded, unwield before dropping
		self.unwield(dropper)
		return True
	
	def at_post_move(self, source_location, **kwargs):
		try:
			self.unwield(source_location)
		except:
			print("Location of object is likely not a character.")
		return super().at_post_move(source_location, **kwargs)
	
	def at_object_delete(self):
		# Objects should be unwielded before deletion to prevent errors
		try:
			self.unwield(self.location)
		except:
			print("Location of object is likely not a character.")
		return True
	
	def unwield(self, character):
		if self in character.db.wieldedItems:
			character.db.wieldedItems.remove(self)
			character.msg("You stop wielding a " + self.name + ".")

	
class Currency(Object):
	isItem = False
	isCurrency = True