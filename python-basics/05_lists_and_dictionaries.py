# Lists and Dictionaries in Python

print("=== LISTS ===")
print()

# Creating and using lists
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry", "date"]
mixed = [1, "hello", 3.14, True]

print(f"Numbers list: {numbers}")
print(f"Fruits list: {fruits}")
print(f"Mixed list: {mixed}")
print()

# Accessing list elements
print("Accessing list elements:")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Second fruit: {fruits[1]}")
print()

# List methods
fruits.append("elderberry")  # Add to end
print(f"After adding elderberry: {fruits}")

fruits.insert(1, "blueberry")  # Insert at position
print(f"After inserting blueberry at position 1: {fruits}")

removed_fruit = fruits.pop()  # Remove and return last item
print(f"Removed fruit: {removed_fruit}")
print(f"List after removing: {fruits}")
print()

# List slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original numbers: {numbers}")
print(f"First 5 numbers: {numbers[:5]}")
print(f"Last 3 numbers: {numbers[-3:]}")
print(f"Numbers from index 2 to 7: {numbers[2:8]}")
print()

print("=== DICTIONARIES ===")
print()

# Creating dictionaries
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "job": "Engineer"
}

print(f"Person dictionary: {person}")
print()

# Accessing dictionary values
print("Accessing dictionary values:")
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")
print()

# Adding and modifying dictionary items
person["email"] = "alice@email.com"  # Add new key-value
person["age"] = 31  # Modify existing value

print(f"After updates: {person}")
print()

# Dictionary methods
print("Dictionary keys:", list(person.keys()))
print("Dictionary values:", list(person.values()))
print("Dictionary items:", list(person.items()))
print()

# Working with nested data
students = [
    {"name": "Bob", "grade": 85, "subject": "Math"},
    {"name": "Carol", "grade": 92, "subject": "Science"},
    {"name": "David", "grade": 78, "subject": "History"}
]

print("Student records:")
for student in students:
    print(f"{student['name']}: {student['grade']} in {student['subject']}")
print()

# Dictionary comprehension
numbers = [1, 2, 3, 4, 5]
squared_dict = {num: num**2 for num in numbers}
print(f"Numbers squared dictionary: {squared_dict}")
print()

# Checking if key exists in dictionary
if "email" in person:
    print(f"Email found: {person['email']}")
else:
    print("Email not found")

# Safe way to get dictionary value
phone = person.get("phone", "Not provided")
print(f"Phone: {phone}")
