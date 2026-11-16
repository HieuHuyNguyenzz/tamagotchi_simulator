from tamagotchi import Tamagotchi
from time import sleep

def main_menu(pets):
    print("Welcome to the Tamagotchi Simulator")
    print("___________________________________ \n")
    print("Please select a Tamagochi")
    print("__________________________ \n")
    for i, pet in enumerate(pets):
        print(f"{i + 1}. {pet.name}")
    print(f"{len(pets) + 1}. Exit")
    while True:
        selected_pet = input("Enter the number of the Tamagochi you want to select: ")
        if selected_pet.isdigit() and 1 <= int(selected_pet) <= len(pets):
            selected_pet = pets[int(selected_pet) - 1]
            print(f"You have selected {selected_pet.name}!")
            sleep(2)
            return selected_pet
        elif selected_pet == str(len(pets) + 1):
            print("Exiting the Tamagotchi Simulator. Goodbye!")
            sleep(2)
            return 0
        else:
            print("Invalid selection. Must be a valid pet number. Please try again.")
