from Place import Place
from Game import Game
from Player import Player


def create():
    start = Place("Welcome", """\
You've bought a great new house! It has everything you need, and one thing you
don't: ghosts. After some research, it seems that the easiest method to get rid
of them is to find out what problem is keeping them here and fix it so they can
peacefully move on. You	may enter what will soon be your home... hopefully!""")
    living_room = Place("Living room", """\
In the living room is some antique-looking decor, and a little ghostly dog
sleeping on	an ornate rug. To your left is the kitchen, and ahead of you is a
hallway with two rooms.""")
    kitchen = Place("Kitchen", """\
You enter the kitchen. Inside, you see a door, some cabinets, a stove, and...
an annoyed looking ghost sitting at the table!""")
    hallway = Place("Hallway", """\
In the hallway, there are two rooms: one to the left and one to the right.""")
    right = Place("Right bedroom", """\
You enter the room on the right. Inside is a young, ghostly-looking girl,
hunched over a desk.""")
    left = Place("Left bedroom", """\
You enter the room on the left; there's a large mess inside and a little boy
ghost. He seems to be searching for something.""")
    start.exits['enter'] = living_room
    living_room.exits['kitchen'] = kitchen
    living_room.exits['hallway'] = hallway
    kitchen.exits['leave'] = living_room
    hallway.exits['left'] = left
    hallway.exits['right'] = right
    hallway.exits['leave'] = living_room
    left.exits['out'] = hallway
    right.exits['out'] = hallway
    return Game(Player(start))
