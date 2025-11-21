def average_rainfall(rainfall_data):
    averages = []

    for month in rainfall_data:
        if len(month) == 0:
            averages.append(0)
        else:
            total = 0
            count = 0

            for rainfall in month:
                total = total + rainfall
                count = count + 1

            average = total / count
            averages.append(average)

    return averages

rainfall_sample = [
    [],
    [3.2, 3.6, 2.2],
    [4.1, 4.6],
]

test1 = [
    [1.0, 2.0, 3.0, 4.0],
    [],
    [5.5],
]

test2 = [
    [2.1, 2.9],
    [1.0, 1.0, 1.0],
    [10.0, 20.0, 30.0],
    []
]

test3 = [
    [],
    [],
    [],
]

print(average_rainfall(rainfall_sample))
print(average_rainfall(test1))
print(average_rainfall(test2))
print(average_rainfall(test3))