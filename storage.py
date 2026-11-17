
import json
from datetime import datetime, timezone
from pathlib import Path

from tamagotchi import Tamagotchi


DEFAULT_SAVE_PATH = Path("save.json")


class SaveLoadError(Exception):
    """Raised when a save file cannot be read or validated."""


def _utc_now():
    return datetime.now(timezone.utc)


def store_status(pets, file_path=DEFAULT_SAVE_PATH, now=None):
    """Save all pets and the timestamp of the save operation as JSON."""
    if len(pets) != 3:
        raise SaveLoadError("A save must contain exactly three pets.")

    timestamp = now or _utc_now()
    payload = {
        "last_updated_at": timestamp.astimezone(timezone.utc).isoformat(),
        "pets": [pet.to_dict() for pet in pets],
    }

    try:
        Path(file_path).write_text(json.dumps(payload, indent=2), encoding="utf-8")
    except OSError as error:
        raise SaveLoadError(f"Could not write save file: {error}") from error

    return timestamp


def load_status(file_path=DEFAULT_SAVE_PATH, now=None):
    """Load pets from JSON and apply the time elapsed since the save."""
    try:
        data = json.loads(Path(file_path).read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise SaveLoadError("Save file does not exist.") from error
    except (OSError, json.JSONDecodeError) as error:
        raise SaveLoadError("Save file is missing, unreadable, or invalid JSON.") from error

    try:
        saved_at = datetime.fromisoformat(data["last_updated_at"])
        saved_at = saved_at.astimezone(timezone.utc)
        saved_pets = data["pets"]
        if len(saved_pets) != 3:
            raise ValueError("save must contain exactly three pets")

        pets = []
        for saved_pet in saved_pets:
            pet = Tamagotchi(
                saved_pet["name"],
                hunger=saved_pet["hunger"],
                health=saved_pet["health"],
                boredom=saved_pet["boredom"],
                exhaustion=saved_pet["exhaustion"],
            )
            if not saved_pet["is_alive"]:
                pet.is_alive = False
            pets.append(pet)
    except (KeyError, TypeError, ValueError) as error:
        raise SaveLoadError("Save file has an invalid game state.") from error

    current_time = now or _utc_now()
    elapsed_hours = max(
        0, (current_time.astimezone(timezone.utc) - saved_at).total_seconds() / 3600
    )
    for pet in pets:
        pet.advance_time(elapsed_hours)

    return pets
