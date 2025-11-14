def weekly_income_by_store(weekly_income):
    result = []
    for store in weekly_income:
        total = 0
        for day_income in store:
            if day_income >= 0:
                total += day_income
        result.append(total)
    return result

def best_day_by_store(weekly_income):
    result = []
    for store in weekly_income:
        max_income = None
        for day_income in store:
            if day_income >= 0:
                if max_income is None or day_income > max_income:
                    max_income = day_income
        result.append(max_income)
    return result

# Test data from the lab description
income_this_week = [
    [10, 20, 54, 23, 18, -1, -1],
    [15, -1, 30, 28, 32, -1, 49],
    [20, 30, 43, 21, 3,  -1, 51],
]

# Test the functions with the provided data
print("Weekly income by store:", weekly_income_by_store(income_this_week))
print("Best day by store:", best_day_by_store(income_this_week))

# Additional test cases
test1 = [
    [5, 10, 15],
    [20, 25, 30],
    [0, -1, 5]
]

test2 = [
    [-1, -1, -1],
    [100],
    [1, 2, 3, 4, 5]
]

test3 = [
    [50, 40, 30, 20, 10],
    [10, 20, -1, 40, 50],
    [25, 25, 25, 25]
]

print("\nTest 1:")
print("Weekly income:", weekly_income_by_store(test1))
print("Best days:", best_day_by_store(test1))

print("\nTest 2:")
print("Weekly income:", weekly_income_by_store(test2))
print("Best days:", best_day_by_store(test2))

print("\nTest 3:")
print("Weekly income:", weekly_income_by_store(test3))
print("Best days:", best_day_by_store(test3))