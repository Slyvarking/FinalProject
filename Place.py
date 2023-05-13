from Inventory import Inventory


class Place:

    def __init__(self):
        self.name = "Nowhere"
        self.description = "There is not much to see here."
        self.inventory = Inventory()
        self.exits = {}

    def look(self):
        print(self.name)
        print(self.description)
        if self.exits:
            print("Obvious exits:")
            ", ".join(self.exits.keys())
        else:
            print("There are no obvious exits.")

    def move(self, direction):
        if direction in self.exits:
            print("Move", direction)
            return True
        else:
            return False
