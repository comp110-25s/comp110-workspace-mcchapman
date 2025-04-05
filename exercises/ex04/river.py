"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        # Create new lists to store survivors
        surviving_fish = []
        surviving_bears = []
        # Check each fish's age and keep fish aged <= 3 years
        for Fish in self.fish:
            if Fish.age <= 3:
                surviving_fish.append(Fish)
        # Check each bear's age and keep bears aged <= 5 years
        for Bear in self.bears:
            if Bear.age <= 5:
                surviving_bears.append(Bear)
        # Update both lists so they only contain survivors
        self.fish = surviving_fish
        self.bears = surviving_bears

    def remove_fish(self, amount: int):
        """Remove a specified amount of Fish from the river, starting from index 0"""
        for _ in range(amount):
            if self.fish:  # Check to make sure fish isn't an empty list
                self.fish.pop(0)  # Remove the zeroth entry

    def bears_eating(self):
        """For each bear, if ≥ 5 fish in river, bear will eat 3"""
        for Bear in self.bears:
            if len(self.fish) >= 5:
                Bear.eat(3)
                self.remove_fish(3)

    def check_hunger(self):
        """Check each bear's hunger score and remove any bear with score < 0"""
        fed_bears = []
        # Create new list to store bears that have eaten
        for Bear in self.bears:
            if Bear.hunger_score >= 0:
                fed_bears.append(Bear)
        self.bears = fed_bears  # Update original list of surviving bears

    def repopulate_fish(self):
        """Each pair of fish will produce 4 offspring fish"""
        num_pairs = len(self.fish) // 2
        for _ in range(num_pairs):
            self.fish.extend([Fish() for _ in range(4)])

    def repopulate_bears(self):
        """Each pair of bears will produce 1 offspring bear"""
        new_bears = len(self.bears) // 2
        self.bears.extend([Bear() for _ in range(new_bears)])

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week, a.k.a. 7 days, in the river"""
        for _ in range(7):
            self.one_river_day()
