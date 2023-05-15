class NonPlayer:
    def __init__(self, name, ids):
        self.name = name
        self.chats = {'_': "They have nothing to say to that."}
        self.ids = ids
        self.description = "What a character!"

    def match_id(self, name):
        return name == self.name.lower() or name in self.ids

    def chat(self, actor, topic):
        if topic in self.chats:
            print(self.chats[topic])
        else:
            print(self.chats['_'])
