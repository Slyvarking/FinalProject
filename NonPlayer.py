from Item import Item


class NonPlayer(Item):
    def __init__(self, name, ids, description="What a character!"):
        super().__init__(name, ids, description)
        self.chats = {'_': "They have nothing to say to that."}

    def match_id(self, name):
        return name == self.name.lower() or name in self.ids

    def chat(self, actor, topic):
        if topic in self.chats:
            print(self.chats[topic])
        else:
            print(self.chats['_'])
