import pickle

# Define classes for the game objects
class Room:
    def __init__(self, name, description, items=None, exits=None):
        self.name = name
        self.description = description
        self.items = items if items is not None else []
        self.exits = exits if exits is not None else {}

class Item:
    def __init__(self, name, description, use_func=None):
        self.name = name
        self.description = description
        self.use_func = use_func

# Define functions for game actions
def print_inventory(inventory):
    if len(inventory) == 0:
        print("You have nothing in your inventory.")
    else:
        print("You have the following items in your inventory:")
        for item in inventory:
            print("- " + item.name)

def take_item(room, item_name, inventory):
    for item in room.items:
        if item.name.lower() == item_name.lower():
            room.items.remove(item)
            inventory.append(item)
            print(f"You have taken the {item.name}.")
            return
    print("That item is not in this room.")

def use_item(item_name, inventory, current_room):
    for item in inventory:
        if item.name.lower() == item_name.lower():
            if item.use_func is None:
                print("You can't use that item here.")
            else:
                item.use_func(current_room, inventory)
            return
    print("You don't have that item in your inventory.")

def save_game(current_room, inventory):
    with open('save_game.pkl', 'wb') as f:
        pickle.dump((current_room, inventory), f)
    print("Game saved.")

def load_game():
    try:
        with open('save_game.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("No saved game found.")
        return None, []

# Define the game world
rooms = {}