from Place import Place


class Player:
    def __init__(self, location=Place()):
        self.location = location
        self.inventory = []

    def handle(self, command):
        return False
