import random
from tamagotchi import Tamagotchi

def pet_screen(pet):
    print(f"Choose an action for {pet.name}:") # input in here
    print("1. Feed")    
    print("2. Play")
    print("3. Sleep")
    print("4. Heal")
    print("5. Rename")
    print("6. Exit")
    while True:
        choice = input("Your choice: ")
        if choice == ["1", "2", "3", "4", "5"]:
            if choice == "1":
                pet.feed()
            elif choice == "2":
                pet.play()
            elif choice == "3":         
                pet.sleep()
            elif choice == "4":
                pet.heal()
            elif choice == "5":
                pet.rename()
            # random_action = action()
        elif choice == "6":
            return 0
        else:
            print("Invalid choice. Please select a valid option.")
    return choice