from time import sleep

from screen_displays import main_menu, pet_screen, play_menu, statistic
from utils import init_pets
from storage import DEFAULT_SAVE_PATH, SaveLoadError, load_status, store_status
from game import update_pets_for_elapsed_time, utc_now


def run_game(pets, save_path=DEFAULT_SAVE_PATH):
    """Run the main game loop for the current collection of pets."""
    last_updated_at = utc_now()

    while True:
        action = main_menu()
        last_updated_at = update_pets_for_elapsed_time(pets, last_updated_at)

        if action == "play":
            selected_pet = play_menu(pets)
            if selected_pet is not None:
                pet_screen(selected_pet, pets)
        elif action == "statistics":
            statistic(pets)
            sleep(2)
        elif action == "save":
            try:
                last_updated_at = store_status(pets, save_path, now=last_updated_at)
                print("Game saved successfully.")
            except SaveLoadError as error:
                print(f"Could not save the game: {error}")
            sleep(2)
        elif action == "load":
            try:
                pets = load_status(save_path)
                last_updated_at = utc_now()
                print("Game loaded successfully.")
            except SaveLoadError as error:
                print(f"Could not load the game: {error}")
            sleep(2)
        elif action == "quit":
            print("Exiting the Tamagotchi Simulator. Goodbye!")
            return


def main():
    run_game(init_pets())


if __name__ == "__main__":
    main()
