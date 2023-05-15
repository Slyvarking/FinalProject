from Place import Place


class Player:
    def __init__(self, location=Place()):
        self.location = location
        self.inventory = []

    def handle(self, command):
        words = command.split(None, 1)
        match words[0]:
            case 'inventory' | 'inv' | 'i':
                self.inv()
            case '_':
                return False
        return True

    def inv(self):
        print("You are carrying")
        [print("    ", x.name) for x in self.inventory]
