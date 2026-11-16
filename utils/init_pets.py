from tamagotchi import Tamagotchi

def init_pets():
    name = ["Fluffy", "Sparky", "Buddy"]
    pets = []
    num_pets = 3
    for i in range(num_pets):
        pet = Tamagotchi(name[i])
        pets.append(pet)
    return pets