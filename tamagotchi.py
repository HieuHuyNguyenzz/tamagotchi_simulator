class Tamagotchi:
    """A virtual pet with bounded needs and health values."""

    MIN_VALUE = 0
    MAX_VALUE = 100

    def __init__(
        self,
        name,
        hunger=20,
        health=100,
        boredom=20,
        exhaustion=0,
    ):
        self.name = name
        self.hunger = self._clamp(hunger)
        self.health = self._clamp(health)
        self.boredom = self._clamp(boredom)
        self.exhaustion = self._clamp(exhaustion)
        self.is_alive = self.health > self.MIN_VALUE

    @classmethod
    def _clamp(cls, value):
        return max(cls.MIN_VALUE, min(cls.MAX_VALUE, value))

    def _can_act(self):
        if not self.is_alive:
            print(f"{self.name} is dead and cannot perform actions.")
            return False
        return True

    def rename(self, new_name):
        if not self._can_act():
            return False
        self.name = new_name
        print(f"Tamagotchi has been renamed to {self.name}")
        return True

    def feed(self, amount=20):
        if not self._can_act():
            return False
        self.hunger = self._clamp(self.hunger - amount)
        self.exhaustion = self._clamp(self.exhaustion + 5)
        print(f"{self.name} has been fed. Hunger level: {self.hunger}")
        return True

    def play(self, amount=20):
        if not self._can_act():
            return False
        self.boredom = self._clamp(self.boredom - amount)
        self.hunger = self._clamp(self.hunger + 10)
        self.exhaustion = self._clamp(self.exhaustion + 10)
        print(f"{self.name} played. Boredom level: {self.boredom}")
        return True

    def sleep(self, amount=25):
        if not self._can_act():
            return False
        self.exhaustion = self._clamp(self.exhaustion - amount)
        self.hunger = self._clamp(self.hunger + 5)
        print(f"{self.name} slept. Exhaustion level: {self.exhaustion}")
        return True

    def heal(self, amount=20):
        if not self._can_act():
            return False
        self.health = self._clamp(self.health + amount)
        print(f"{self.name} has been healed. Health level: {self.health}")
        return True

    def advance_time(self, hours):
        """Advance this pet's needs by the given number of elapsed hours."""
        if not self.is_alive or hours <= 0:
            return False

        # Health decreases only after the first need reaches 80.
        hours_until_critical = min(
            max(0, (80 - self.hunger) / 5),
            max(0, (80 - self.boredom) / 4),
            max(0, (80 - self.exhaustion) / 3),
        )
        hours_until_death = hours_until_critical + self.health / 5
        elapsed_hours = min(hours, hours_until_death)

        self.hunger = self._clamp(self.hunger + 5 * elapsed_hours)
        self.boredom = self._clamp(self.boredom + 4 * elapsed_hours)
        self.exhaustion = self._clamp(self.exhaustion + 3 * elapsed_hours)

        if hours >= hours_until_death:
            self.health = self.MIN_VALUE
            self.is_alive = False
        else:
            critical_hours = max(0, elapsed_hours - hours_until_critical)
            self.health = self._clamp(self.health - 5 * critical_hours)

        return True

    def status(self):
        current_status = self.to_dict()
        print(
            f"{self.name}'s Status - "
            f"Hunger: {self.hunger}, "
            f"Health: {self.health}, "
            f"Boredom: {self.boredom}, "
            f"Exhaustion: {self.exhaustion}, "
            f"Alive: {self.is_alive}"
        )
        return current_status

    def to_dict(self):
        """Return the pet state in a JSON-compatible dictionary."""
        return {
            "name": self.name,
            "hunger": self.hunger,
            "health": self.health,
            "boredom": self.boredom,
            "exhaustion": self.exhaustion,
            "is_alive": self.is_alive,
        }
