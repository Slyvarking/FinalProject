from Creator import create
import pickle

if __name__ == '__main__':
    game = create()
    while True:
        if game.run():
            try:
                with open("game.dat", "rb") as file:
                    game = pickle.load(file)
            except FileNotFoundError:
                print("No game is saved")
            else:
                print("Loaded game from \"game.dat\"")
        else:
            break
