def area_of_square(side):
    area_square = side * side
    return area_square

print(f"The area of the square is {area_of_square(5)} square units!")

def area_of_rectangle(length, width):
    area_rectangle = length * width
    return area_rectangle

print (f"The area of the rectangle is {area_of_rectangle(4,2)} square units!")

def print_step(step_num):
    print(f"--- Step {step_num} ---")
    return step_num + 1

def process_data(a, b):
    c = print_step(1)
    d = print_step(2) 
    return a + b + c + d

# Program execution begins here:
print("START (Line A)") 
result = process_data(5, 10)
print("END (Line B)")
print(f"Final Result: {result}")


def meters_to_centimeters(meters):
    centimeters_converted = meters*100
    return centimeters_converted

print(meters_to_centimeters(4.5))