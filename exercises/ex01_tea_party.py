"""This code helps me plan grocery shopping for a tea party"""

__author__: str = "730461992"


def main_planner(guests: int) -> None:
    """This function brings together output from the others to fully plan the party"""
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
    """This function calculates the number of tea bags required based on the number of guests"""
    return people * 2


def treats(people: int) -> int:
    """This function calculates the number of treats required based on the number of guests"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """This function calculates the total cost of the party based on the guests' consumption"""
    return float(0.50 * tea_count + 0.75 * treat_count)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
