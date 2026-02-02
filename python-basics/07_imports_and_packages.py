# START GENAI@CLINE
"""
Python Imports and Package Management Demo
Learn: Built-in modules, external packages, pip installation, practical calculations
"""

# =============================================================================
# PART 1: BUILT-IN MODULES (No installation needed)
# =============================================================================

# Math module for advanced mathematical operations
import math

# Datetime module for date and time operations
import datetime

# Random module for generating random numbers
import random

# OS module for operating system interface
import os

# Alternative import methods
from math import pi, sqrt, pow  # Import specific functions
import random as rnd           # Import with alias

def demo_builtin_modules():
    """Demonstrate built-in Python modules"""
    print("=" * 60)
    print("📦 BUILT-IN MODULES DEMO")
    print("=" * 60)
    
    # Math module examples
    print("\n🔢 MATH MODULE:")
    print(f"π (pi) = {math.pi:.4f}")
    print(f"e (Euler's number) = {math.e:.4f}")
    print(f"Square root of 16 = {math.sqrt(16)}")
    print(f"Factorial of 5 = {math.factorial(5)}")
    print(f"sin(90°) = {math.sin(math.radians(90)):.4f}")
    print(f"log(100) = {math.log10(100)}")
    
    # Datetime module examples
    print("\n📅 DATETIME MODULE:")
    now = datetime.datetime.now()
    print(f"Current date and time: {now}")
    print(f"Current year: {now.year}")
    print(f"Day of week: {now.strftime('%A')}")
    
    future_date = now + datetime.timedelta(days=30)
    print(f"Date 30 days from now: {future_date.strftime('%Y-%m-%d')}")
    
    # Random module examples
    print("\n🎲 RANDOM MODULE:")
    print(f"Random integer (1-10): {random.randint(1, 10)}")
    print(f"Random float (0-1): {random.random():.4f}")
    
    colors = ['red', 'blue', 'green', 'yellow', 'purple']
    print(f"Random color: {random.choice(colors)}")
    
    numbers = [1, 2, 3, 4, 5]
    random.shuffle(numbers)
    print(f"Shuffled numbers: {numbers}")
    
    # OS module examples
    print("\n💻 OS MODULE:")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Operating system: {os.name}")
    print(f"Environment PATH exists: {'PATH' in os.environ}")

# =============================================================================
# PART 2: SCIENTIFIC CALCULATIONS WITH BUILT-IN MODULES
# =============================================================================

def scientific_calculator():
    """Advanced calculator using math module"""
    print("\n" + "=" * 60)
    print("🧮 SCIENTIFIC CALCULATOR (Built-in Modules)")
    print("=" * 60)
    
    # Trigonometry calculations
    angle = 45
    angle_rad = math.radians(angle)
    print(f"\nTrigonometry for {angle}°:")
    print(f"sin({angle}°) = {math.sin(angle_rad):.4f}")
    print(f"cos({angle}°) = {math.cos(angle_rad):.4f}")
    print(f"tan({angle}°) = {math.tan(angle_rad):.4f}")
    
    # Logarithms and exponentials
    number = 100
    print(f"\nLogarithms for {number}:")
    print(f"Natural log of {number} = {math.log(number):.4f}")
    print(f"Base-10 log of {number} = {math.log10(number):.4f}")
    print(f"e^{math.log(number):.2f} = {math.exp(math.log(number)):.4f}")
    
    # Statistical calculations
    numbers = [10, 20, 30, 40, 50]
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std_dev = math.sqrt(variance)
    
    print(f"\nStatistics for {numbers}:")
    print(f"Mean: {mean}")
    print(f"Variance: {variance:.2f}")
    print(f"Standard deviation: {std_dev:.2f}")

# =============================================================================
# PART 3: EXTERNAL PACKAGES DEMO
# =============================================================================

def demo_external_packages():
    """Demonstrate external packages (requires installation)"""
    print("\n" + "=" * 60)
    print("📦 EXTERNAL PACKAGES DEMO")
    print("=" * 60)
    
    print("\n⚠️  EXTERNAL PACKAGES INSTALLATION REQUIRED:")
    print("Run these commands in your terminal:")
    print("pip install numpy")
    print("pip install requests")
    print("pip install matplotlib")
    print("\nAfter installation, uncomment the code below to try external packages!")
    
    # Uncomment these sections after installing packages
    """
    # NUMPY - Scientific computing
    try:
        import numpy as np
        print("\n🔢 NUMPY CALCULATIONS:")
        
        # Create arrays
        arr1 = np.array([1, 2, 3, 4, 5])
        arr2 = np.array([10, 20, 30, 40, 50])
        
        print(f"Array 1: {arr1}")
        print(f"Array 2: {arr2}")
        print(f"Sum: {arr1 + arr2}")
        print(f"Product: {arr1 * arr2}")
        print(f"Mean of array 1: {np.mean(arr1)}")
        print(f"Standard deviation: {np.std(arr1):.2f}")
        
        # Matrix operations
        matrix = np.array([[1, 2], [3, 4]])
        print(f"Matrix:\n{matrix}")
        print(f"Matrix determinant: {np.linalg.det(matrix)}")
        
    except ImportError:
        print("❌ NumPy not installed. Run: pip install numpy")
    
    # REQUESTS - HTTP library
    try:
        import requests
        print("\n🌐 REQUESTS - HTTP DEMO:")
        
        # Make a simple API call (example with a free API)
        response = requests.get("https://httpbin.org/json")
        if response.status_code == 200:
            print(f"API Response: {response.json()}")
        else:
            print("Failed to fetch data")
            
    except ImportError:
        print("❌ Requests not installed. Run: pip install requests")
    """

# =============================================================================
# PART 4: PACKAGE INSTALLATION COMMANDS AND TIPS
# =============================================================================

def show_package_commands():
    """Show common pip commands and package management"""
    print("\n" + "=" * 60)
    print("📋 PYTHON PACKAGE MANAGEMENT COMMANDS")
    print("=" * 60)
    
    commands = [
        ("pip install package_name", "Install a package"),
        ("pip install package_name==1.2.3", "Install specific version"),
        ("pip install -r requirements.txt", "Install from requirements file"),
        ("pip list", "Show installed packages"),
        ("pip show package_name", "Show package info"),
        ("pip uninstall package_name", "Uninstall a package"),
        ("pip freeze", "Show all installed packages with versions"),
        ("pip freeze > requirements.txt", "Save current packages to file"),
        ("pip install --upgrade package_name", "Upgrade a package"),
        ("python -m pip install --user package_name", "Install for current user only")
    ]
    
    print("\n💻 COMMON PIP COMMANDS:")
    for command, description in commands:
        print(f"  {command:<35} # {description}")
    
    print("\n📦 RECOMMENDED PACKAGES FOR BEGINNERS:")
    packages = [
        ("numpy", "Scientific computing and arrays"),
        ("pandas", "Data analysis and manipulation"),
        ("matplotlib", "Data visualization and plotting"),
        ("requests", "HTTP requests and API calls"),
        ("beautifulsoup4", "Web scraping and HTML parsing"),
        ("pillow", "Image processing"),
        ("flask", "Web development framework"),
        ("jupyter", "Interactive notebooks")
    ]
    
    for package, description in packages:
        print(f"  {package:<15} # {description}")

# =============================================================================
# PART 5: PRACTICAL EXAMPLES
# =============================================================================

def practical_examples():
    """Practical examples using imports"""
    print("\n" + "=" * 60)
    print("🛠️  PRACTICAL EXAMPLES")
    print("=" * 60)
    
    # Example 1: Password generator
    print("\n🔐 PASSWORD GENERATOR:")
    import string
    
    def generate_password(length=8):
        characters = string.ascii_letters + string.digits + "!@#$%^&*"
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    
    for i in range(3):
        print(f"Password {i+1}: {generate_password(12)}")
    
    # Example 2: File size calculator
    print("\n📁 FILE SIZE CALCULATOR:")
    def convert_bytes(bytes_value):
        for unit in ['B', 'KB', 'MB', 'GB']:
            if bytes_value < 1024:
                return f"{bytes_value:.1f} {unit}"
            bytes_value /= 1024
        return f"{bytes_value:.1f} TB"
    
    file_sizes = [1024, 1048576, 1073741824]
    for size in file_sizes:
        print(f"{size} bytes = {convert_bytes(size)}")
    
    # Example 3: Simple encryption
    print("\n🔒 SIMPLE TEXT ENCRYPTION:")
    def simple_cipher(text, shift=3):
        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            else:
                result += char
        return result
    
    original = "Hello World!"
    encrypted = simple_cipher(original)
    decrypted = simple_cipher(encrypted, -3)
    
    print(f"Original:  {original}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")

# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    """Main program demonstrating imports and packages"""
    print("🐍 PYTHON IMPORTS & PACKAGES TUTORIAL")
    print("Learn how to use built-in modules and install external packages")
    
    # Run all demonstrations
    demo_builtin_modules()
    scientific_calculator()
    show_package_commands()
    practical_examples()
    demo_external_packages()
    
    print("\n" + "=" * 60)
    print("✅ TUTORIAL COMPLETE!")
    print("=" * 60)
    print("\n📝 NEXT STEPS:")
    print("1. Try installing external packages: pip install numpy requests")
    print("2. Uncomment the external packages section in this file")
    print("3. Run the script again to see external packages in action")
    print("4. Explore more packages at: https://pypi.org/")
    print("\n🎯 Happy Python learning!")

if __name__ == "__main__":
    main()
# END GENAI@CLINE
