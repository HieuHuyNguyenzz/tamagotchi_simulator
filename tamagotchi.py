

class Tamagotchi():
    def __init__(self, name):
        self.name = name
        self.hunger = 0 # 0 mean its full
        self.happiness_level = 100 # 100 is very happy
        self.energy = 100 # full energy

    def rename(self, new_name):
        self.name = new_name
        print(f"Tamagotchi has been renamed to {self.name}")

    def feed(self, amount):
        self.hunger = max(0, self.hunger - amount)
        print(f"{self.name} has been fed. Hunger level: {self.hunger}")

    def play(self, amount):
        self.happiness_level = min(100, self.happiness_level + amount)
        print(f"{self.name} played. Happiness level: {self.happiness_level}")

    def sleep(self, amount):
        self.energy += min(100, self.energy + amount)
        print(f"{self.name} slept. Energy level: {self.energy}")

    def status(self):
        print(f"{self.name}'s Status - Hunger: {self.hunger}, Happiness: {self.happiness}, Energy: {self.energy}")