from screen_displays import main_menu, pet_screen, play_menu
from utils import init_pets


def run_game(pets):
    """Run the main game loop for the current collection of pets."""
    while True:
        action = main_menu()

        if action == "play":
            selected_pet = play_menu(pets)
            if selected_pet is not None:
                pet_screen(selected_pet)
        elif action == "statistics":
            print("Statistics functionality is not implemented yet.")
        elif action == "save":
            print("Save functionality is not implemented yet.")
        elif action == "load":
            print("Load functionality is not implemented yet.")
        elif action == "quit":
            print("Exiting the Tamagotchi Simulator. Goodbye!")
            return


def main():
    run_game(init_pets())


if __name__ == "__main__":
    main()
