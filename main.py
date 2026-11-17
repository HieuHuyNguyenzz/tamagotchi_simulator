from time import sleep

from screen_displays import main_menu, pet_screen, play_menu, statistic
from utils import clear_screen, init_pets
from storage import DEFAULT_SAVE_PATH, SaveLoadError, load_status, store_status
from game import update_pets_for_elapsed_time, utc_now


def _confirm_new_game():
    print("Starting a new game will replace your current progress and saved game.", flush=True)
    while True:
        choice = input("Start a new game? (y/n): ").strip().lower()
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no", ""):
            return False
        print("Please enter y or n.", flush=True)


def run_game(pets, save_path=DEFAULT_SAVE_PATH, last_updated_at=None):
    """Run the main game loop for the current collection of pets."""
    last_updated_at = last_updated_at or utc_now()

    while True:
        action = main_menu()
        clear_screen()
        last_updated_at = update_pets_for_elapsed_time(pets, last_updated_at)

        if action == "play":
            selected_pet = play_menu(pets)
            if selected_pet is not None:
                last_updated_at = pet_screen(selected_pet, pets, last_updated_at)
        elif action == "statistics":
            statistic(pets)
        elif action == "save":
            try:
                last_updated_at = store_status(pets, save_path, now=last_updated_at)
                print("Game saved successfully.", flush=True)
            except SaveLoadError as error:
                print(f"Could not save the game: {error}", flush=True)
            sleep(2)
        elif action == "new_game":
            if _confirm_new_game():
                try:
                    new_pets = init_pets()
                    restarted_at = store_status(new_pets, save_path, now=utc_now())
                except SaveLoadError as error:
                    print(f"Could not start a new game: {error}", flush=True)
                else:
                    pets = new_pets
                    last_updated_at = restarted_at
                    print("New game started.", flush=True)
            else:
                print("New game cancelled.", flush=True)
            sleep(2)
        elif action == "quit":
            print("Exiting the Tamagotchi Simulator. Goodbye!", flush=True)
            return


def main(save_path=DEFAULT_SAVE_PATH):
    started_at = utc_now()
    try:
        pets = load_status(save_path, now=started_at)
    except SaveLoadError as error:
        pets = init_pets()
        if isinstance(error.__cause__, FileNotFoundError):
            try:
                started_at = store_status(pets, save_path, now=started_at)
            except SaveLoadError as creation_error:
                clear_screen()
                print(f"Could not create the save file: {creation_error}", flush=True)
                return
        else:
            clear_screen()
            print(f"Could not load the saved game: {error}", flush=True)
            print("Starting a fresh session. The existing save file has not been changed.", flush=True)
            sleep(2)
    run_game(pets, save_path, last_updated_at=started_at)


if __name__ == "__main__":
    main()
