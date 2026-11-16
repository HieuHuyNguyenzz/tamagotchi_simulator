from utils import clear_screen


def main_menu():
    """Display the main menu and return the selected application action."""
    while True:
        clear_screen()
        print("Welcome to the Tamagotchi Simulator")
        print("___________________________________\n")
        print("1. Play")
        print("2. Save")
        print("3. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            return "play"
        if choice == "2":
            return "save"
        if choice == "3":
            return "quit"

        print("Invalid choice. Please select 1, 2, or 3.")


def play_menu(pets):
    """Display the pet-selection menu and return the selected pet."""
    while True:
        clear_screen()
        print("Please select a Tamagotchi")
        print("__________________________\n")

        for index, pet in enumerate(pets, start=1):
            print(f"{index}. {pet.name}")
        print(f"{len(pets) + 1}. Back")

        choice = input("Enter the number of the Tamagotchi you want to select: ")

        if choice.isdigit() and 1 <= int(choice) <= len(pets):
            selected_pet = pets[int(choice) - 1]
            print(f"You have selected {selected_pet.name}!")
            return selected_pet

        if choice == str(len(pets) + 1):
            return None

        print("Invalid selection. Please try again.")
