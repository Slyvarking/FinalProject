class Place:

    def __init__(self, name="Nowhere", description="There is not much to see here.", exits=None):
        self.name = name
        self.description = description
        self.exits = {} if exits is None else exits
        self.npc = None
        self.visited = False

    def look(self, detail=True):
        print(self.name)
        if not self.visited or detail:
            print(self.description)
        if self.exits:
            print("Obvious exits:", ", ".join(self.exits.keys()))
        else:
            print("There are no obvious exits.")
        if self.npc:
            print(self.npc.name, "is here.")
        self.visited = True

    def move(self, direction):
        if direction in self.exits:
            destination = self.exits[direction]
            destination.look(False)
            return destination
        else:
            return None
