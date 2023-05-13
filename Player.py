from Inventory import Inventory
from Place import Place


class Player:
    def __init__(self, location=Place()):
        self.location = location
        self.inventory = Inventory()

    def handle(self, words):
        match words[0]:
            case "look" | "l":
                self.location.look()
            case _:
                destination = self.location.move(words[0])
                if destination:
                    self.location = destination
                    return True
                return False
        return True
