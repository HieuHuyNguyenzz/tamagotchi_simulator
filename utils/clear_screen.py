import os
import sys

def clear_screen():
    sys.stdout.flush()
    os.system("cls" if os.name == "nt" else "clear")
