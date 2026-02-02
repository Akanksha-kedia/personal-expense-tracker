# Loops in Python

print("=== LOOPS ===")
print()

# For loop with range
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"Count: {i}")
print()

# For loop with a list
fruits = ["apple", "banana", "orange", "grape"]
print("Fruits in our basket:")
for fruit in fruits:
    print(f"- {fruit}")
print()

# For loop with enumeration (getting index and value)
print("Fruits with their positions:")
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")
print()

# While loop
print("Countdown:")
count = 5
while count > 0:
    print(f"{count}...")
    count = count - 1
print("Blast off! 🚀")
print()

# While loop with user condition
print("Finding even numbers from 2 to 10:")
number = 2
while number <= 10:
    if number % 2 == 0:
        print(f"{number} is even")
    number = number + 1
print()

# For loop with multiplication table
print("Multiplication table for 3:")
for i in range(1, 11):
    result = 3 * i
    print(f"3 x {i} = {result}")
print()

# Nested loops (loop inside a loop)
print("Creating a simple pattern:")
for row in range(3):
    for col in range(4):
        print("*", end=" ")
    print()  # New line after each row
print()

# Loop with break and continue
print("Numbers from 1 to 10, but skip 5 and stop at 8:")
for num in range(1, 11):
    if num == 5:
        continue  # Skip 5
    if num == 9:
        break     # Stop before 9
    print(num)
