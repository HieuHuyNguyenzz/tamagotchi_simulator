import sys
from time import sleep

from game import (
    trigger_random_event,
    update_pets_for_elapsed_time,
    utc_now,
)
from utils import clear_screen


def _pause_before_next_screen():
    sys.stdout.flush()
    sleep(2)


def _show_status_until_back(pet):
    pet.status()
    print("\n0. Back", flush=True)

    while True:
        choice = input("Your choice: ").strip()
        if choice == "0":
            return
        print("Invalid choice. Enter 0 to go back.", flush=True)


def pet_screen(pet, pets=None, last_updated_at=None):
    """Display the action menu for one pet until the player goes back."""
    pets = pets or [pet]
    last_updated_at = last_updated_at or utc_now()

    while True:
        last_updated_at = update_pets_for_elapsed_time(pets, last_updated_at)
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
        clear_screen()
        last_updated_at = update_pets_for_elapsed_time(pets, last_updated_at)

        if choice == "1":
            if pet.feed():
                trigger_random_event(pets)
            _pause_before_next_screen()
        elif choice == "2":
            if pet.play():
                trigger_random_event(pets)
            _pause_before_next_screen()
        elif choice == "3":
            if pet.sleep():
                trigger_random_event(pets)
            _pause_before_next_screen()
        elif choice == "4":
            if pet.heal():
                trigger_random_event(pets)
            _pause_before_next_screen()
        elif choice == "5":
            new_name = input("Enter the new name: ").strip()
            last_updated_at = update_pets_for_elapsed_time(pets, last_updated_at)
            if new_name:
                if pet.rename(new_name):
                    trigger_random_event(pets)
            else:
                print("The name cannot be empty.")
            _pause_before_next_screen()
        elif choice == "6":
            _show_status_until_back(pet)
        elif choice == "7":
            return last_updated_at
        else:
            print("Invalid choice. Please select a valid option.")
            _pause_before_next_screen()
