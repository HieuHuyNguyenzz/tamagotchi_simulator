import __main__
from tamagotchi import Tamagotchi
from storage import store_status, load_status
from screen_displays import main_menu
from utils import init_pets, clear_screen


def main():
    pets = init_pets()
    main_menu(pets)
    clear_screen()



if __name__ == "__main__":
    main()