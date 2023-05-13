from Inventory import Inventory
from Place import Place


class Player:
    def __init__(self):
        self.location = Place()
        self.inventory = Inventory()

    def handle(self, words):
        pass
