from Item import Item
from NonPlayer import NonPlayer
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
sleeping on an ornate rug. To your left is the kitchen, and ahead of you is a
hallway with two rooms.""")
    kitchen = Place("Kitchen", """\
You enter the kitchen. Inside, you see a door, some cabinets, a stove, and...
an annoyed looking ghost sitting at the table!""")
    kitchen.details['cabinets'] = """\
The cabinets are completely empty except for a box of tea. Guess ghosts don't
eat much."""
    kitchen.details['door'] = """\
You walk up to the door. According to the house's layout, it should lead
outside into the yard. It's locked."""
    hallway = Place("Hallway", """\
In the hallway, there are two rooms: one to the left and one to the right.""")
    right = Place("Right bedroom", """\
You enter the room on the right. Inside is a young, ghostly-looking girl,
hunched over a desk.""")
    left = Place("Left bedroom", """\
You enter the room on the left; there's a large mess inside and a little boy
ghost. He seems to be searching for something.""")
    garden = Place("Garden", """\
You emerge outside. There's a lovely garden filled with plants with a ghost
lady tending to them. To the left, there's a small shed.""")
    shed = Place("Shed", """\
The shed is filled with various gardening tools, a watering can, and a stack of
empty flower pots under a table in the corner.""")
    can = Item("a watering can", ['watering can', 'can'], "A watering can")
    can.hidden = True
    shed.inventory.append(can)
    start.exits['enter'] = living_room
    living_room.exits['kitchen'] = kitchen
    living_room.exits['hallway'] = hallway
    kitchen.exits['leave'] = living_room
    hallway.exits['left'] = left
    hallway.exits['right'] = right
    hallway.exits['leave'] = living_room
    left.exits['out'] = hallway
    right.exits['out'] = hallway
    garden.exits['shed'] = shed
    shed.exits['garden'] = garden
    garden.npc = GhostLady()
    kitchen.npc = Ghost(kitchen, garden)

    player = Player(start)
    player.inventory.append(Item("a teapot", ['teapot'], "A china teapot"))
    return Game(player)


class Ghost(NonPlayer):
    def __init__(self, kitchen, garden):
        super().__init__("A grouchy ghost", ['ghost', 'grouch'])
        self.kitchen = kitchen
        self.garden = garden
        self.description = "An annoyed looking ghost sitting at the table!"
        self.chats = {'_': """\
You approach the ghost sat at the table. "Hello there. I'm not in the mood to
talk to you. Someone's stolen my teapot! I can't even have a simple cup of tea
these days...\"""", 'door': """\
Oh, that's the door out to the yard. I would unlock it for you if I had the
bother to locate the key. Unfortunately for you, I do not.""", 'tea': """\
I'm not in the mood to talk to you. Someone's stolen my teapot!""", 'teapot': """\
Yes, my teapot has been stolen, I tell you!"""}

    def give(self, actor, obj):
        if not obj.match_id('teapot'):
            print("The ghost scowls. \"I don't want that! Where's my teapot?\"")
            return False
        self.name = "A contented ghost"
        self.description = "A content ghost enjoying a cup of tea."
        self.chats = {'door': """\
Oh, that's the door out to the yard. I would unlock it for you if I could.
Unfortunately, someone has stolen the key!""",
                      '_': "I'm so happy my teapot was recovered from the thieves!"}
        self.kitchen.details['door'] = """\
According to the house's layout, this door should lead outside into the yard.
You can open it with the key."""
        self.kitchen.exits['door'] = self.garden
        self.garden.exits['house'] = self.kitchen
        print("""\
"Ah, so you had my teapot! Well I'm glad to have it back." He moves throughout
the kitchen, preparing a cup of tea. "I suppose I could find that key for you
while we wait for the water to boil." He searches through a cluttered drawer,
and takes out a small silver key. "Here ya go.\"""")
        actor.inventory.append(Item("a silver key", ['key', 'silver key'], "A silver key"))
        return True


class GhostLady(NonPlayer):

    def __init__(self):
        super().__init__("A ghost lady", ['ghost', 'ghost lady', 'lady'])
        self.description = """\
You approach the gardening ghost. "Oh, hello there. D'ya think you could grab
the watering can? It's just over there in the shed. Thanks.\""""
        self.chats = {'_': "Healthy plants need plenty of water!"}

    def give(self, actor, obj):
        if not obj.match_id('watering can'):
            print("Thank you, but I'm sure you need that more than I.")
            return False
        self.description = "A ghostly lady tending her garden."
        print("""\
"Thank you. That's just what I needed!"

"Wait a moment...\" The gardener peers into the watering can. "What is this
ball doing in the watering can?\"""")
        actor.inventory.append(Item("a red ball", ['red ball', 'ball'], "A chewed up red rubber ball"))
        return True


class Dog(NonPlayer):
    def __init__(self):
        super().__init__("A ghost dog", ['ghost dog', 'dog', 'puppy', 'pup'])
        self.description = """\
The ghost puppy wakes up and stares at you as you come closer.

"Bark!\""""

    def give(self, actor, obj):
        if not obj.match_id('ball'):
            print("The puppy whimpers and his tail droops sadly.")
            return False
        self.description = "The puppy is happily gnawing on a red rubber ball."
        print("The puppy jumps up excitedly and takes the ball. It seems very happy.")
        return True
