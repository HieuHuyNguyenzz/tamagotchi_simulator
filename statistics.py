def _average(values):
    if not values:
        return 0
    return round(sum(values) / len(values), 2)


def calculate_statistics(pets):
    """Calculate the statistics required by the project specification."""
    living_pets = [pet for pet in pets if pet.is_alive]

    return {
        "living_pets": len(living_pets),
        "dead_pets": len(pets) - len(living_pets),
        "average_health_living": _average([pet.health for pet in living_pets]),
        "average_hunger": _average([pet.hunger for pet in pets]),
        "average_boredom": _average([pet.boredom for pet in pets]),
        "average_exhaustion": _average([pet.exhaustion for pet in pets]),
    }
