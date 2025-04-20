import time

class Pet:
    def __init__(self, name):
        """Initialize a new virtual pet with default stats"""
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
        self.age = 0  # New age tracking feature

    def eat(self):
        """Reduces hunger by 3 and increases happiness by 1"""
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        time.sleep(1)
        print(f"{self.name} eats happily! 🍗")

    def sleep(self):
        """Restores energy by 5 points"""
        self.energy = min(10, self.energy + 5)
        self.age += 0.1  # Age increases when sleeping
        time.sleep(1)
        print(f"{self.name} takes a nap... zzz 😴")

    def play(self):
        """Expends energy but increases happiness and hunger"""
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            time.sleep(1)
            print(f"{self.name} plays joyfully! 🎾")
        else:
            print(f"{self.name} is too tired to play 😔")

    def train(self, trick):
        """Teaches the pet a new trick"""
        if trick in self.tricks:
            print(f"{self.name} already knows '{trick}'")
        else:
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 1)
            time.sleep(1)
            print(f"{self.name} learned '{trick}'! 🎓")

    def show_tricks(self):
        """Displays all learned tricks"""
        if not self.tricks:
            print(f"{self.name} hasn't learned any tricks yet 😅")
        else:
            print(f"{self.name} knows: {', '.join(self.tricks)}")

    def get_status(self):
        """Provides a detailed status report"""
        status = (
            f"\n{self.name}'s Status (Age: {self.age:.1f} days):\n"
            f"🍽️ Hunger: {'★' * self.hunger}{'☆' * (10 - self.hunger)}\n"
            f"⚡ Energy: {'★' * self.energy}{'☆' * (10 - self.energy)}\n"
            f"😊 Happiness: {'★' * self.happiness}{'☆' * (10 - self.happiness)}"
        )
        if self.tricks:
            status += f"\n🎓 Tricks: {', '.join(self.tricks)}"
        print(status)

    def __str__(self):
        """String representation of the pet"""
        return f"🐾 {self.name} (Digital Pet)"