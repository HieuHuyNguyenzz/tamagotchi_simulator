from tamagotchi import Tamagotchi
from time import sleep

def main_menu(pets):
    print("Welcome to the Tamagotchi Simulator")
    print("___________________________________ \n")
    print("Please select a Tamagochi")
    print("__________________________ \n")
    for i, pet in enumerate(pets):
        print(f"{i + 1}. {pet.name}")

    while True:
        selected_pet = input("Enter the number of the Tamagochi you want to select: ")
        if selected_pet.isdigit() and 1 <= int(selected_pet) <= len(pets):
            selected_pet = pets[int(selected_pet) - 1]
            print(f"You have selected {selected_pet.name}!")
            sleep(5)
            return selected_pet
        else:
            print("Invalid selection. Must be a valid pet number. Please try again.")
