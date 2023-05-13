import pickle

from Player import Player


class Game:

    def __init__(self):
        self.player = Player()
        self.places = {}

    def run(self):
        while True:
            command = input("> ")
            match command:
                case "save":
                    self.save()
                case "load":
                    return True
                case "help":
                    self.help()
                case "quit" | "q":
                    return False
                case _:
                    self.handle(command)

    def handle(self, command):
        words = command.lower().split()
        okay = False
        if words:
            print("Type \"help\" for help.")
        elif 1 < len(words) < 5:
            okay = self.player.handle(words)
        if not okay:
            print("What?")

    def help(self):
        print("""\
Game command:
    save <file> - save game in <file>
    load <file> - load game from <file>
    help, h, ?  - print this help
    quit, q     - quit the game""")
        return 1, False

    def save(self):
        with open("game.dat", "wb") as file:
            pickle.dump(self, file)
        print("Saved game in \"game.dat\"")
        return 1, False
