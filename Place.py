class Place:

    def __init__(self, name="Nowhere", description="There is not much to see here.", exits=None):
        self.name = name
        self.description = description
        self.exits = {} if exits is None else exits
        self.visited = False

    def look(self):
        print(self.name)
        if not self.visited:
            print(self.description)
        if self.exits:
            print("Obvious exits:", ", ".join(self.exits.keys()))
        else:
            print("There are no obvious exits.")
        self.visited = True

    def move(self, direction):
        if direction in self.exits:
            destination = self.exits[direction]
            destination.look()
            return destination
        else:
            return None
