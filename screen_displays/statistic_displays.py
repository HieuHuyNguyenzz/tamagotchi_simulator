from statistics import calculate_statistics


def statistic(pets):
    """Calculate and display game statistics for the current pets."""
    stats = calculate_statistics(pets)

    print(f"Living pets: {stats['living_pets']}")
    print(f"Dead pets: {stats['dead_pets']}")
    print(f"Average health of living pets: {stats['average_health_living']}")
    print(f"Average hunger: {stats['average_hunger']}")
    print(f"Average boredom: {stats['average_boredom']}")
    print(f"Average exhaustion: {stats['average_exhaustion']}")

    return stats
