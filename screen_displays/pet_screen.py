from utils import clear_screen


def pet_screen(pet):
    """Display the action menu for one pet until the player goes back."""
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
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.sleep()
        elif choice == "4":
            pet.heal()
        elif choice == "5":
            new_name = input("Enter the new name: ").strip()
            if new_name:
                pet.rename(new_name)
            else:
                print("The name cannot be empty.")
        elif choice == "6":
            pet.status()
        elif choice == "7":
            return None
        else:
            print("Invalid choice. Please select a valid option.")
