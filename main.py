class Player:
    def __init__(self):

        self.playername = input("What's your name?:")
        self.playerclass = ""
        self.damage = 0
        self.intelligence = 0
        self.health = 100

        self.crit_damage = 0

    def choose_class(self):
        text = f"What class do you want to play, {self.playername}? Choose from Mage, Berserk, Archer, Tank, Healer: "
        a=""
        a = input(text)
        while not( ) :
        self.playerclass = a
        a = input(text)
        
        print("Invalid class. Please choose a valid class.")

class Entity:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def is_alive(self):
        return self.health > 0

class NPC(Entity):
    def __init__(self, name, health, damage, dialogue):
        super().__init__(name, health, damage)
        self.dialogue = dialogue

class Enemy(Entity):
    def __init__(self, name, health, damage, loot):
        super().__init__(name, health, damage)
        self.loot = loot

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Room:
    def __init__(self, description, biome):
        self.description = description
        self.biome = biome
        self.exits = {}
        self.entities = []
        self.items = []

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def add_entity(self, entity):
        self.entities.append(entity)

    def add_item(self, item):
        self.items.append(item)

class Player(Entity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.location = None

    def move(self, direction):
        if direction in self.location.exits:
            self.location = self.location.exits[direction]
        else:
            print("You can't go that way.")

    def attack(self, target):
        if target in self.location.entities:
            target.health -= self.damage
            if not target.is_alive():
                self.location.entities.remove(target)
                print(f"You have defeated the {target.name}!")
        else:
            print("There is no such enemy here.")

class Game:
    def __init__(self, player):
        self.player = player
        self.rooms = self.generate_rooms()

    def generate_rooms(self):
        # Create a 500x500 grid of rooms
        rooms = [[Room(f"Room {i},{j}", "forest") for j in range(500)] for i in range(500)]
        # Add exits to each room
        for i in range(500):
            for j in range(500):
                if i > 0:
                    rooms[i][j].add_exit("north", rooms[i-1][j])
                if i < 499:
                    rooms[i][j].add_exit("south", rooms[i+1][j])
                if j > 0:
                    rooms[i][j].add_exit("west", rooms[i][j-1])
                if j < 499:
                    rooms[i][j].add_exit("east", rooms[i][j+1])
        return rooms

    def start(self):
        # Start the game
        while True:
            print(self.player.location.description)
            command = input("> ")
            if command in ["north", "south", "east", "west"]:
                self.player.move(command)
            elif command.startswith("attack "):
                target_name = command.split(" ", 1)[1]
                target = next((e for e in self.player.location.entities if e.name == target_name), None)
                if target:
                    self.player.attack(target)
                else:
                    print("There is no such enemy here.")
            else:
                print("Invalid command.")
