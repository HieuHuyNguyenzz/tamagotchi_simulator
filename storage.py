import json
from datetime import datetime, timezone
from pathlib import Path

from tamagotchi import Tamagotchi


DEFAULT_SAVE_PATH = Path("save.json")


class SaveLoadError(Exception):
    """Raised when a save file cannot be read or validated."""


def _utc_now():
    return datetime.now(timezone.utc)


def _validate_pet_state(state):
    """Reject malformed data instead of silently changing it while loading."""
    if not isinstance(state, dict):
        raise ValueError("Each pet must be a JSON object.")

    name = state["name"]
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Pet names must be non-empty strings.")

    for field in ("hunger", "health", "boredom", "exhaustion"):
        value = state[field]
        if type(value) not in (int, float) or not 0 <= value <= 100:
            raise ValueError(f"{field} must be a finite number from 0 to 100.")

    if type(state["is_alive"]) is not bool:
        raise ValueError("is_alive must be a boolean.")
    if state["is_alive"] != (state["health"] > 0):
        raise ValueError("Health and living/dead status are inconsistent.")


def store_status(pets, file_path=DEFAULT_SAVE_PATH, now=None):
    """Save all pets and the timestamp of the save operation as JSON."""
    if len(pets) != 3:
        raise SaveLoadError("A save must contain exactly three pets.")

    try:
        timestamp = now or _utc_now()
        if timestamp.tzinfo is None or timestamp.utcoffset() is None:
            raise ValueError("The save timestamp must include a timezone.")
        timestamp = timestamp.astimezone(timezone.utc)
        states = [pet.to_dict() for pet in pets]
        for state in states:
            _validate_pet_state(state)
        payload = {
            "last_updated_at": timestamp.isoformat(),
            "pets": states,
        }
        serialized = json.dumps(payload, indent=2, allow_nan=False)
    except (KeyError, TypeError, ValueError, OverflowError) as error:
        raise SaveLoadError("Cannot save an invalid game state.") from error

    try:
        Path(file_path).write_text(serialized, encoding="utf-8")
    except OSError as error:
        raise SaveLoadError(f"Could not write save file: {error}") from error

    return timestamp


def load_status(file_path=DEFAULT_SAVE_PATH, now=None):
    """Load pets from JSON and apply the time elapsed since the save."""
    try:
        data = json.loads(Path(file_path).read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise SaveLoadError("Save file does not exist.") from error
    except (OSError, ValueError, RecursionError) as error:
        raise SaveLoadError("Save file is missing, unreadable, or invalid JSON.") from error

    try:
        if not isinstance(data, dict):
            raise ValueError("The save must be a JSON object.")
        saved_at = datetime.fromisoformat(data["last_updated_at"])
        if saved_at.tzinfo is None or saved_at.utcoffset() is None:
            raise ValueError("The save timestamp must include a timezone.")
        saved_at = saved_at.astimezone(timezone.utc)
        saved_pets = data["pets"]
        if not isinstance(saved_pets, list) or len(saved_pets) != 3:
            raise ValueError("save must contain exactly three pets")

        pets = []
        for saved_pet in saved_pets:
            _validate_pet_state(saved_pet)
            pet = Tamagotchi(
                saved_pet["name"],
                hunger=saved_pet["hunger"],
                health=saved_pet["health"],
                boredom=saved_pet["boredom"],
                exhaustion=saved_pet["exhaustion"],
            )
            pets.append(pet)
    except (KeyError, TypeError, ValueError, OverflowError) as error:
        raise SaveLoadError("Save file has an invalid game state.") from error

    current_time = now or _utc_now()
    elapsed_hours = max(
        0, (current_time.astimezone(timezone.utc) - saved_at).total_seconds() / 3600
    )
    for pet in pets:
        pet.advance_time(elapsed_hours)

    return pets
