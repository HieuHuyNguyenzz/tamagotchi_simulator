from datetime import datetime, timezone
import random


def utc_now():
    return datetime.now(timezone.utc)


def update_pets_for_elapsed_time(pets, previous_time, now=None):
    """Apply clock-based changes to every pet and return the current timestamp."""
    current_time = (now or utc_now()).astimezone(timezone.utc)
    previous_time = previous_time.astimezone(timezone.utc)
    if current_time <= previous_time:
        return previous_time

    elapsed_hours = (current_time - previous_time).total_seconds() / 3600

    for pet in pets:
        pet.advance_time(elapsed_hours)

    return current_time


def trigger_random_event(pets, rng=None):
    """Possibly apply one random event to a living pet."""
    rng = rng or random
    living_pets = [pet for pet in pets if pet.is_alive]

    if not living_pets or rng.random() >= 0.25:
        return None

    pet = rng.choice(living_pets)
    event_name = rng.choice(["food", "sickness", "health_bonus"])

    if event_name == "food":
        pet.hunger = pet._clamp(pet.hunger - 15)
        print(f"Random event: {pet.name} found food!")
    elif event_name == "sickness":
        pet.health = pet._clamp(pet.health - 10)
        if pet.health == pet.MIN_VALUE:
            pet.is_alive = False
        print(f"Random event: {pet.name} became sick.")
    else:
        pet.health = pet._clamp(pet.health + 10)
        print(f"Random event: {pet.name} received a health bonus!")

    return event_name
