from Place import Place


class Player:
    def __init__(self, location=Place()):
        self.location = location
        self.inventory = []

    def handle(self, words):
        match words[0]:
            case "look" | "l":
                self.location.look()
            case "talk":
                self.talk(words)
            case "give":
                self.give(words)
            case _:
                destination = self.location.move(words[0])
                if not destination:
                    return False
                self.location = destination
        return True

    def talk(self, words):
        if not self.location.npc:
            print("You mutter to yourself.")
        else:
            if words[:4] != "talk to ghost about".split():
                print("Do you want to \"talk to ghost about\" something?")
            else:
                self.location.npc.chat(" ".join(words[4:]))

    def give(self, words):
        if not self.location.npc:
            print("Give what to whom?")
        else:
            if words[-2:] != "to ghost".split():
                print("Do you want to give something \"to ghost\"?")
            else:
                item = " ".join(words[1:-2])
                if item in self.inventory:
                    if self.location.npc.give(item):
                        self.inventory.remove(item)
                else:
                    print(f"You don't have {item}.")