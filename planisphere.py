class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
         return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)


central_corridor = Room("Central Corridor",
"""
The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew. You are the last surviving member and your last
<F11><F12>mission is to get the neutron destruct bomb from the Weapons Armory, put it in the bridge, and blow the ship up after getting into an escape pod""")
laser_weapon_armory = Room("Laser Weapon Armory",
 """
Lucky for you they made you learn Gothon insults in the academy. You
 tell the one Gothon joke you know: Lbhe zbgure vf fb sng, jura fur fvgf
 nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr. The Gothon stops, tries
 not to laugh, then busts out laughing and can't move. While he's
 laughing you run up and shoot him square in the head putting him down,
 then jump through the Weapon Armory door.""")
the_bridge = Room("The Bridge",
 """
 The container clicks open and the seal breaks, letting gas out. You
 grab the neutron bomb and run as fast as you can to the bridge where you
 must place it in the right spot.""")
escape_pod = Room("Escape Pod",
 """
You point your blaster at the bomb under your arm and the Gothons put
their hands up and start to sweat. You inch backward to the door, open
it, and then carefully place the bomb on the floor, pointing your
blaster at it. You then jump back thro""")
the_end_winner = Room("The End", """
jump into pod 2 and hit the eject button. The pod easily slides out into space heading to the planet below. As it flies to the planet, you
 look back and see your ship implode then explode like a bright star,
 taking out the Gothon ship at the same time. You won!
 """)
the_end_loser = Room("The End",
 """
 You jump into a random pod and hit the eject button. The pod escapes
 out into the void of space, then implodes as the hull ruptures, crushing
your body into jam jelly.""")
escape_pod.add_paths({
    '2': the_end_winner,
     '*': the_end_loser
})

generic_death = Room("death", "You died.")

the_bridge.add_paths({
    'throw the bomb': generic_death,
    'slowly place the bomb': escape_pod
})

laser_weapon_armory.add_paths({
    '0132': the_bridge,
     '*': generic_death })

central_corridor.add_paths({
    'shoot!': generic_death,
    'dodge!': generic_death,
     'tell a joke': laser_weapon_armory
 })

START = 'central_corridor'

def load_room(name):
    """
     There is a potential security problem here.
    Who gets to set name? Can that expose a variable?
    """
    return globals().get(name)

def name_room(room):
     
    """Same possible security problem. Can you trust room?

    What's a better solution than this globals lookup?"""
    for key, value in globals().items():
     if value == room:
         return key



