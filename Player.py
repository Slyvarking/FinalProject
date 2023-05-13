from Place import Place


class Player:
    def __init__(self, location=Place()):
        self.location = location
        self.inventory = []

    def handle(self, words):
        match words[0]:
            case "look" | "l":
                self.location.look()
            case "talk" | "chat" | "speak" | "say":
                if self.location.npc:
                    self.location.npc.chat(words[-1])
                else:
                    print("You mutter to yourself.")
            case _:
                destination = self.location.move(words[0])
                if not destination:
                    return False
                self.location = destination
        return True
