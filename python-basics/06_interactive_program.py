# Interactive Python Program - Simple Calculator and Quiz

print("=== INTERACTIVE PYTHON PROGRAM ===")
print("Welcome to the Python Learning Demo!")
print()

# Simple Calculator
def calculator():
    print("🔢 SIMPLE CALCULATOR")
    print("Available operations: +, -, *, /")
    
    # Get numbers (using fixed values for demo)
    num1 = 10
    num2 = 5
    operation = "+"
    
    print(f"Computing: {num1} {operation} {num2}")
    
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Cannot divide by zero"
    else:
        result = "Error: Invalid operation"
    
    print(f"Result: {result}")
    print()

# Quiz Game
def quiz_game():
    print("🎯 PYTHON QUIZ GAME")
    
    questions = [
        {
            "question": "What is 2 + 2?",
            "options": ["3", "4", "5", "6"],
            "correct": 1
        },
        {
            "question": "Which of these is a Python data type?",
            "options": ["string", "integer", "list", "all of the above"],
            "correct": 3
        },
        {
            "question": "What does 'len()' function do?",
            "options": ["Adds numbers", "Gets length", "Prints text", "Creates lists"],
            "correct": 1
        }
    ]
    
    score = 0
    
    for i, q in enumerate(questions):
        print(f"Question {i + 1}: {q['question']}")
        for j, option in enumerate(q['options']):
            print(f"  {j + 1}. {option}")
        
        # Auto-answer for demo (normally would use input())
        user_answer = q['correct'] + 1  # Simulate correct answer
        print(f"Your answer: {user_answer}")
        
        if user_answer - 1 == q['correct']:
            print("✅ Correct!")
            score += 1
        else:
            correct_answer = q['options'][q['correct']]
            print(f"❌ Wrong! The correct answer was: {correct_answer}")
        print()
    
    print(f"🎉 Quiz Complete! Your score: {score}/{len(questions)}")
    
    if score == len(questions):
        print("Perfect score! You're a Python star! ⭐")
    elif score >= len(questions) // 2:
        print("Good job! Keep learning! 👍")
    else:
        print("Don't worry, practice makes perfect! 💪")
    print()

# Data Analysis Demo
def data_analysis_demo():
    print("📊 DATA ANALYSIS DEMO")
    
    # Sample student data
    students = [
        {"name": "Alice", "math": 85, "science": 92, "english": 78},
        {"name": "Bob", "math": 76, "science": 88, "english": 82},
        {"name": "Carol", "math": 94, "science": 96, "english": 89},
        {"name": "David", "math": 68, "science": 74, "english": 85}
    ]
    
    print("Student Grades:")
    total_students = len(students)
    
    for student in students:
        avg = (student["math"] + student["science"] + student["english"]) / 3
        print(f"{student['name']}: Math={student['math']}, Science={student['science']}, English={student['english']}, Average={avg:.1f}")
    
    print()
    
    # Calculate class averages
    math_total = sum(student["math"] for student in students)
    science_total = sum(student["science"] for student in students)
    english_total = sum(student["english"] for student in students)
    
    print("Class Averages:")
    print(f"Math: {math_total / total_students:.1f}")
    print(f"Science: {science_total / total_students:.1f}")
    print(f"English: {english_total / total_students:.1f}")
    
    # Find top performer
    top_student = max(students, key=lambda s: (s["math"] + s["science"] + s["english"]) / 3)
    top_avg = (top_student["math"] + top_student["science"] + top_student["english"]) / 3
    print(f"\n🏆 Top Student: {top_student['name']} (Average: {top_avg:.1f})")
    print()

# Word Counter Demo
def word_counter():
    print("📝 WORD COUNTER DEMO")
    
    text = "Python is awesome and Python is fun to learn"
    print(f"Text: '{text}'")
    
    words = text.lower().split()
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    print("\nWord frequencies:")
    for word, count in word_count.items():
        print(f"'{word}': {count}")
    
    most_common = max(word_count, key=word_count.get)
    print(f"\nMost common word: '{most_common}' (appears {word_count[most_common]} times)")
    print()

# Main program
def main():
    print("Running all demos...")
    print("=" * 50)
    
    calculator()
    quiz_game()
    data_analysis_demo()
    word_counter()
    
    print("🎉 All demos completed!")
    print("Try running individual files to see each concept in detail:")
    print("- python3 01_variables_and_types.py")
    print("- python3 02_functions.py")
    print("- python3 03_loops.py")
    print("- python3 04_conditionals.py")
    print("- python3 05_lists_and_dictionaries.py")

if __name__ == "__main__":
    main()
