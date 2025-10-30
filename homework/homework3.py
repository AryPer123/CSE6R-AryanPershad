# You are designing a 2D platformer game where the player can collect a gold coin (2 points), a
# silver coin (1 point), or fall into a trap and lose one point (-1 point). Design a program to
# calculate the total number of points that the player collected!
# Name of the function: calculate_points
# Parameter:
# - events: a list of strings, representing the events that the player encountered.

# "gold": the gold coin, which should earn 2 points
# "silver": the silver coin, which should earn 1 point
# "trap": a trap, which should reduce 1 point
# Any other string: ignore, 0 point.

# Data type of return value: integer (int), representing the total amount of points (the value could
# be negative or positive).
# Example of calling and testing the function:
# events_sample = ["gold", "silver", "trap", "mushroom", "trap"]
# print(calculate_points(events_sample)) # Output should be 1
# Explanation: points = 2 + 1 - 1 + 0 - 1 = 1


events = []

def calculate_points(events):
    points = 0
    for i in events:
        if i == "gold":
            points +=2
        elif i == "silver":
            points += 1
        elif i == "trap":
            points -= 1
        else:
            continue
    return points

events = ["gold", "gold", "silver", "trap", "gold", "flower", "silver", "mushroom"]
print(calculate_points(events))

events = ["gold", "gold", "silver", "trap", "gold", "flower", "silver"]
print(calculate_points(events))

events = ["gold", "trap", "gold", "flower", "silver", "mushroom"]
print(calculate_points(events))

events = ["gold", "silver", "trap", "mushroom", "trap"]
print(calculate_points(events))

events = ["gold", "trap", "gold", "mushroom"]
print(calculate_points(events))


