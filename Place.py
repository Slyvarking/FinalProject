from typing import Dict, Any


class Place:

    def __init__(self, name="Nowhere", description="There is not much to see here."):
        self.name = name
        self.description = description
        self.exits = {}
        self.npc = None
        self.details = {}
        self.visited = False

    def handle(self, actor, command):
        words = command.split(None, 1)
        match words[0]:
            case "look" | "l":
                self.look(actor)
            case "talk":
                self.talk(actor, command)
            case "give":
                self.give(actor, command)
            case "examine" | "exa":
                self.examine(actor, command)
            case _:
                if not self.move(actor, command):
                    return actor.handle(command)
        return True

    def talk(self, actor, command):
        if not self.npc:
            print("You mutter to yourself.")
        else:
            words = command.split()
            if words[:4] != "talk to ghost about".split():
                print("Do you want to \"talk to ghost about\" something?")
            else:
                self.npc.chat(actor, " ".join(words[4:]))

    def give(self, actor, command):
        if not self.npc:
            print("Give what to whom?")
        else:
            words = command.split()
            if words[-2:] != "to ghost".split():
                print("Do you want to give something \"to ghost\"?")
            else:
                item = " ".join(words[1:-2])
                if item in actor.inventory:
                    if self.npc.give(actor, item):
                        actor.inventory.remove(item)
                else:
                    print(f"You don't have {item}.")

    def examine(self, actor, command):
        item = ' '.join(command.split()[1:])
        print(self.details.get(item, f"You don't see {item} here."))

    def look(self, actor, detail=True):
        print(self.name)
        if not self.visited or detail:
            print(self.description)
        if self.exits:
            print("Obvious exits:", ", ".join(self.exits.keys()))
        else:
            print("There are no obvious exits.")
        if self.npc:
            print(self.npc.name, "is here.")
        self.visited = True

    def move(self, actor, direction):
        if direction not in self.exits:
            return False
        destination = self.exits[direction]
        actor.location = destination
        destination.look(False)
        return True
