import pickle

from Player import Player


class Game:

    def __init__(self, player=Player()):
        self.player = player

    def run(self):
        self.player.location.look()
        while True:
            command = input("> ")
            match command:
                case "save":
                    self.save()
                case "load":
                    return True
                case "help" | "h" | "?":
                    self.help()
                case "quit" | "q":
                    return False
                case _:
                    self.handle(command)

    def handle(self, command):
        words = command.lower().split()
        if not words:
            print("Type \"help\" for help.")
            okay = True
        elif 0 < len(words) < 5:
            okay = self.player.handle(words)
        else:
            okay = False
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
