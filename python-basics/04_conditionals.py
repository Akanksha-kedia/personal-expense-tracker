# Conditional Statements in Python

print("=== CONDITIONAL STATEMENTS ===")
print()

# Basic if statement
age = 20
if age >= 18:
    print(f"Age {age}: You are an adult!")
print()

# If-else statement
temperature = 25
if temperature > 30:
    print("It's hot outside!")
else:
    print("The weather is pleasant")
print()

# If-elif-else statement
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")
print()

# Multiple conditions with and/or
age = 22
has_license = True

if age >= 18 and has_license:
    print("You can drive!")
elif age >= 18 and not has_license:
    print("You need to get a license first")
else:
    print("You are too young to drive")
print()

# Checking if a number is positive, negative, or zero
number = -5
if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero")
print()

# Checking membership (in/not in)
favorite_colors = ["blue", "green", "red"]
color = "blue"

if color in favorite_colors:
    print(f"{color} is one of my favorite colors!")
else:
    print(f"{color} is not my favorite color")
print()

# String comparison
username = "admin"
password = "secret123"

if username == "admin" and password == "secret123":
    print("Login successful!")
else:
    print("Invalid credentials")
print()

# Nested conditions
weather = "sunny"
temperature = 28

if weather == "sunny":
    if temperature > 25:
        print("Perfect day for swimming!")
    else:
        print("Nice sunny day, but a bit cool")
else:
    if temperature > 25:
        print("Warm but not sunny")
    else:
        print("Cool and cloudy day")
print()

# Ternary operator (short if-else)
age = 17
status = "adult" if age >= 18 else "minor"
print(f"Age {age}: You are a {status}")
