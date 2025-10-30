rainfall_list = []

def average_rainfall(rainfall_list):
    total_rainfall = 0
    average_rainfall = 0
    positive_measurements = 0
    for i in range(len(rainfall_list)):
        if rainfall_list[i] >= 0:
            total_rainfall += rainfall_list[i]
            positive_measurements += 1
    if total_rainfall >= 0 and positive_measurements > 0:
        average_rainfall = total_rainfall / positive_measurements
        return average_rainfall
    elif len(rainfall_list) == 0:
        return "No Valid Rainfall Measurements"
    else:
        return "No Valid Rainfall Measurements"

print(average_rainfall([30, 10, 20]))
print(average_rainfall([10, 20, -30]))
print(average_rainfall([20, 0, 10]))
print(average_rainfall([0, 0, 0]))
print(average_rainfall([]))
print(average_rainfall([-1,-20]))