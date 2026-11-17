from statistics import calculate_statistics


def statistic(pets):
    """Display game statistics until the player chooses Back."""
    stats = calculate_statistics(pets)
    displayed_health = max(1, stats["average_health_living"]) if stats["living_pets"] else 0

    print(f"Living pets: {stats['living_pets']}")
    print(f"Dead pets: {stats['dead_pets']}")
    print(f"Average health of living pets: {displayed_health:.0f}")
    print(f"Average hunger: {stats['average_hunger']:.0f}")
    print(f"Average boredom: {stats['average_boredom']:.0f}")
    print(f"Average exhaustion: {stats['average_exhaustion']:.0f}", flush=True)
    print("\n0. Back", flush=True)

    while True:
        choice = input("Your choice: ").strip()
        if choice == "0":
            break
        print("Invalid choice. Enter 0 to go back.", flush=True)

    return stats
