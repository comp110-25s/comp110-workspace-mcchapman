"""Plan a cozy tea party!"""

__author__: str = "730464690"


def main_planner(guests: int) -> None:
    """calls other functions and produces printed outputs"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Calculate the number of tea bags needed for the party"""
    return 2 * people


def treats(people: int) -> int:
    """Calculate the number of treats needed for the party"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the total cost of the party"""
    return float(tea_count * 0.50 + treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
