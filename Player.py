from Inventory import Inventory
from Place import Place


class Player:
    def __init__(self):
        self.location = Place()
        self.inventory = Inventory()

    def handle(self, words):
        match words[0]:
            case "look" | "l":
                self.location.look()
            case _:
                if self.location.move(words[0]):
                    return True
                return False
        return True
