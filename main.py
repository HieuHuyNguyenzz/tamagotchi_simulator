import __main__
from tamagotchi import Tamagotchi
from storage import store_status, load_status
from screen_displays import main_menu, pet_screen
from utils import init_pets, clear_screen


def main():
    pets = init_pets()
    selected_pet = main_menu(pets)
    clear_screen()
    if selected_pet == 0:
        return 
    pet_screen(selected_pet)


if __name__ == "__main__":
    main()