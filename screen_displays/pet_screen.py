from time import sleep

from game import trigger_random_event
from utils import clear_screen


def _pause_before_next_screen():
    sleep(2)


def pet_screen(pet, pets=None):
    """Display the action menu for one pet until the player goes back."""
    pets = pets or [pet]

    while True:
        clear_screen()
        print(f"Choose an action for {pet.name}:")
        print("1. Feed")
        print("2. Play")
        print("3. Sleep")
        print("4. Heal")
        print("5. Rename")
        print("6. Status")
        print("7. Back")

        choice = input("Your choice: ")

        if choice == "1":
            pet.feed()
            trigger_random_event(pets)
            _pause_before_next_screen()
        elif choice == "2":
            pet.play()
            trigger_random_event(pets)
            _pause_before_next_screen()
        elif choice == "3":
            pet.sleep()
            trigger_random_event(pets)
            _pause_before_next_screen()
        elif choice == "4":
            pet.heal()
            trigger_random_event(pets)
            _pause_before_next_screen()
        elif choice == "5":
            new_name = input("Enter the new name: ").strip()
            if new_name:
                pet.rename(new_name)
            else:
                print("The name cannot be empty.")
            trigger_random_event(pets)
            _pause_before_next_screen()
        elif choice == "6":
            pet.status()
            _pause_before_next_screen()
        elif choice == "7":
            return None
        else:
            print("Invalid choice. Please select a valid option.")
            _pause_before_next_screen()
