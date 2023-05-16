class Item:
    def __init__(self, name, ids, description="It's really something!"):
        self.name = name
        self.ids = ids
        self.description = description
        self.hidden = False

    def match_id(self, name):
        return name == self.name.lower() or name in self.ids
