# Functions in Python

print("=== FUNCTIONS ===")
print()

# Simple function
def greet():
    return "Hello from a function!"

print(greet())
print()

# Function with parameters
def greet_person(name):
    return f"Hello, {name}!"

print(greet_person("Bob"))
print(greet_person("Sarah"))
print()

# Function with multiple parameters
def add_numbers(a, b):
    result = a + b
    return result

print(f"5 + 3 = {add_numbers(5, 3)}")
print(f"10 + 20 = {add_numbers(10, 20)}")
print()

# Function with default parameter
def introduce(name, age=18):
    return f"My name is {name} and I am {age} years old"

print(introduce("Charlie"))
print(introduce("Diana", 25))
print()

# Function that calculates area
def calculate_rectangle_area(length, width):
    area = length * width
    return area

length = 10
width = 5
area = calculate_rectangle_area(length, width)
print(f"Rectangle area ({length} x {width}) = {area}")
print()

# Function that returns multiple values
def get_name_and_age():
    name = "Emma"
    age = 22
    return name, age

person_name, person_age = get_name_and_age()
print(f"Returned values: Name = {person_name}, Age = {person_age}")
print()

# Function with conditional logic
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"

print(check_even_odd(10))
print(check_even_odd(7))
