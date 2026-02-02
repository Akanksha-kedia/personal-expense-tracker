# Mini-Project #1: Console Calculator
# Learn: User input, arithmetic operations, functions, program organization

# Welcome message
def welcome():
    print("=" * 50)
    print("🧮 WELCOME TO YOUR PYTHON CALCULATOR! 🧮")
    print("=" * 50)
    print("This calculator can perform basic math operations:")
    print("✓ Addition (+)")
    print("✓ Subtraction (-)")
    print("✓ Multiplication (*)")
    print("✓ Division (/)")
    print("✓ Power (**)")
    print("=" * 50)
    print()

# Function to get a number from user
def get_number(prompt):
    """Get a number from user with error handling"""
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("⚠️  Please enter a valid number!")

# Function to get operation from user
def get_operation():
    """Get operation choice from user"""
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (**)")
    
    while True:
        choice = input("\nEnter your choice (1-5): ")
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            print("⚠️  Please enter a number between 1 and 5!")

# Addition function
def add(a, b):
    """Add two numbers"""
    result = a + b
    print(f"\n✅ {a} + {b} = {result}")
    return result

# Subtraction function
def subtract(a, b):
    """Subtract second number from first"""
    result = a - b
    print(f"\n✅ {a} - {b} = {result}")
    return result

# Multiplication function
def multiply(a, b):
    """Multiply two numbers"""
    result = a * b
    print(f"\n✅ {a} × {b} = {result}")
    return result

# Division function
def divide(a, b):
    """Divide first number by second"""
    if b == 0:
        print("\n❌ Error: Cannot divide by zero!")
        return None
    else:
        result = a / b
        print(f"\n✅ {a} ÷ {b} = {result}")
        return result

# Power function
def power(a, b):
    """Raise first number to the power of second"""
    result = a ** b
    print(f"\n✅ {a} raised to power {b} = {result}")
    return result

# Function to perform calculation
def calculate():
    """Main calculation function"""
    # Get first number
    num1 = get_number("Enter the first number: ")
    
    # Get operation
    operation = get_operation()
    
    # Get second number
    num2 = get_number("Enter the second number: ")
    
    # Perform calculation based on choice
    if operation == '1':
        return add(num1, num2)
    elif operation == '2':
        return subtract(num1, num2)
    elif operation == '3':
        return multiply(num1, num2)
    elif operation == '4':
        return divide(num1, num2)
    elif operation == '5':
        return power(num1, num2)

# Function to ask if user wants to continue
def continue_calculating():
    """Ask user if they want to perform another calculation"""
    while True:
        choice = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print("⚠️  Please enter 'yes' or 'no'!")

# Function to show calculation history
def show_history(history):
    """Display calculation history"""
    if history:
        print("\n" + "=" * 30)
        print("📊 YOUR CALCULATION HISTORY:")
        print("=" * 30)
        for i, calc in enumerate(history, 1):
            print(f"{i}. {calc}")
    else:
        print("\n📝 No calculations performed yet!")

# Main program function
def main():
    """Main program that runs the calculator"""
    
    # Show welcome message
    welcome()
    
    # List to store calculation history
    calculation_history = []
    
    # Keep running until user wants to stop
    while True:
        # Perform calculation
        result = calculate()
        
        # Add to history if calculation was successful
        if result is not None:
            # Store the last calculation (you can enhance this to store the full expression)
            calculation_history.append(f"Result: {result}")
        
        print("\nOptions:")
        print("1. Perform another calculation")
        print("2. Show calculation history")
        print("3. Exit calculator")
        
        choice = input("\nWhat would you like to do? (1-3): ")
        
        if choice == '1':
            print("\n" + "-" * 50)
            continue
        elif choice == '2':
            show_history(calculation_history)
            input("\nPress Enter to continue...")
        elif choice == '3':
            print("\n" + "=" * 50)
            print("🎉 Thank you for using the Python Calculator!")
            print("Keep practicing Python - you're doing great! 🐍")
            print("=" * 50)
            break
        else:
            print("⚠️  Please enter 1, 2, or 3!")

# This is the standard way to run a Python program
# It ensures the main() function runs only when this file is executed directly
if __name__ == "__main__":
    main()
