# START GENAI@CLINE
"""
External Python Packages Demo - WORKING EXAMPLES
Learn: Using external packages like NumPy and Requests with real examples
"""

# =============================================================================
# PART 1: NUMPY - SCIENTIFIC COMPUTING
# =============================================================================

try:
    import numpy as np
    numpy_available = True
    print("✅ NumPy successfully imported!")
except ImportError:
    numpy_available = False
    print("❌ NumPy not available. Run: pip install numpy")

def numpy_examples():
    """Demonstrate NumPy capabilities"""
    if not numpy_available:
        return
    
    print("\n" + "=" * 60)
    print("🔢 NUMPY SCIENTIFIC COMPUTING EXAMPLES")
    print("=" * 60)
    
    # Basic arrays
    print("\n📊 ARRAY OPERATIONS:")
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([10, 20, 30, 40, 50])
    
    print(f"Array 1: {arr1}")
    print(f"Array 2: {arr2}")
    print(f"Addition: {arr1 + arr2}")
    print(f"Multiplication: {arr1 * arr2}")
    print(f"Element-wise division: {arr2 / arr1}")
    
    # Statistical functions
    print(f"\n📈 STATISTICS:")
    print(f"Sum: {np.sum(arr1)}")
    print(f"Mean: {np.mean(arr1):.2f}")
    print(f"Standard deviation: {np.std(arr1):.2f}")
    print(f"Maximum: {np.max(arr1)}")
    print(f"Minimum: {np.min(arr1)}")
    
    # 2D arrays (matrices)
    print(f"\n🔳 MATRIX OPERATIONS:")
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    
    print(f"Matrix 1:\n{matrix1}")
    print(f"Matrix 2:\n{matrix2}")
    print(f"Matrix multiplication:\n{np.dot(matrix1, matrix2)}")
    print(f"Matrix determinant: {np.linalg.det(matrix1):.2f}")
    
    # Advanced functions
    print(f"\n🧮 ADVANCED CALCULATIONS:")
    data = np.array([1.2, 2.7, 3.1, 4.9, 5.8, 6.3])
    print(f"Data: {data}")
    print(f"Square root: {np.sqrt(data)}")
    print(f"Natural log: {np.log(data)}")
    print(f"Exponential: {np.exp([1, 2, 3])}")
    
    # Random number generation
    print(f"\n🎲 RANDOM NUMBERS:")
    random_integers = np.random.randint(1, 100, 5)
    random_floats = np.random.random(5)
    normal_distribution = np.random.normal(0, 1, 5)
    
    print(f"Random integers (1-100): {random_integers}")
    print(f"Random floats (0-1): {random_floats}")
    print(f"Normal distribution: {normal_distribution}")

# =============================================================================
# PART 2: REQUESTS - HTTP LIBRARY
# =============================================================================

try:
    import requests
    requests_available = True
    print("✅ Requests successfully imported!")
except ImportError:
    requests_available = False
    print("❌ Requests not available. Run: pip install requests")

def requests_examples():
    """Demonstrate Requests library capabilities"""
    if not requests_available:
        return
    
    print("\n" + "=" * 60)
    print("🌐 REQUESTS HTTP LIBRARY EXAMPLES")
    print("=" * 60)
    
    # Example 1: Simple GET request
    print("\n📡 MAKING HTTP REQUESTS:")
    try:
        # Using a free testing API
        response = requests.get("https://httpbin.org/json")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ GET request successful!")
            print(f"Status code: {response.status_code}")
            print(f"Response data: {data}")
        else:
            print(f"❌ Request failed with status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"❌ Request error: {e}")
    
    # Example 2: GET request with parameters
    print(f"\n🔍 REQUEST WITH PARAMETERS:")
    try:
        params = {"key1": "value1", "key2": "value2"}
        response = requests.get("https://httpbin.org/get", params=params)
        if response.status_code == 200:
            print(f"✅ Parameterized request successful!")
            print(f"Final URL: {response.url}")
            data = response.json()
            print(f"Parameters sent: {data['args']}")
    except requests.RequestException as e:
        print(f"❌ Request error: {e}")
    
    # Example 3: Headers and user agent
    print(f"\n📋 CUSTOM HEADERS:")
    try:
        headers = {
            "User-Agent": "Python Learning Bot 1.0",
            "Accept": "application/json"
        }
        response = requests.get("https://httpbin.org/headers", headers=headers)
        if response.status_code == 200:
            print(f"✅ Custom headers request successful!")
            data = response.json()
            sent_headers = data['headers']
            print(f"User-Agent sent: {sent_headers.get('User-Agent')}")
    except requests.RequestException as e:
        print(f"❌ Request error: {e}")

# =============================================================================
# PART 3: COMBINING PACKAGES - PRACTICAL EXAMPLE
# =============================================================================

def practical_data_analysis():
    """Practical example combining multiple packages"""
    if not numpy_available:
        print("\n❌ NumPy required for this example")
        return
    
    print("\n" + "=" * 60)
    print("📊 PRACTICAL DATA ANALYSIS EXAMPLE")
    print("=" * 60)
    
    # Simulate some sales data
    print("\n💼 SALES DATA ANALYSIS:")
    
    # Generate sample data
    np.random.seed(42)  # For reproducible results
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    sales_data = np.random.randint(1000, 5000, 6)  # Random sales between 1000-5000
    expenses_data = np.random.randint(500, 2000, 6)  # Random expenses
    
    print(f"Months: {months}")
    print(f"Sales: {sales_data}")
    print(f"Expenses: {expenses_data}")
    
    # Calculate profits
    profits = sales_data - expenses_data
    print(f"Profits: {profits}")
    
    # Analysis
    print(f"\n📈 ANALYSIS RESULTS:")
    print(f"Total sales: ${np.sum(sales_data):,}")
    print(f"Total expenses: ${np.sum(expenses_data):,}")
    print(f"Total profit: ${np.sum(profits):,}")
    print(f"Average monthly profit: ${np.mean(profits):,.2f}")
    print(f"Best month: {months[np.argmax(profits)]} (${profits[np.argmax(profits)]:,})")
    print(f"Worst month: {months[np.argmin(profits)]} (${profits[np.argmin(profits)]:,})")
    
    # Growth analysis
    if len(profits) > 1:
        growth_rates = np.diff(profits) / profits[:-1] * 100
        print(f"\n📊 MONTH-TO-MONTH GROWTH RATES:")
        for i, rate in enumerate(growth_rates):
            print(f"{months[i]} to {months[i+1]}: {rate:.1f}%")

# =============================================================================
# PART 4: PACKAGE MANAGEMENT DEMONSTRATION
# =============================================================================

def show_installed_packages():
    """Show information about installed packages"""
    print("\n" + "=" * 60)
    print("📦 PACKAGE MANAGEMENT INFORMATION")
    print("=" * 60)
    
    # Check package versions
    packages_to_check = ['numpy', 'requests']
    
    print(f"\n🔍 CHECKING PACKAGE VERSIONS:")
    for package in packages_to_check:
        try:
            if package == 'numpy':
                import numpy
                print(f"✅ {package}: version {numpy.__version__}")
            elif package == 'requests':
                import requests
                print(f"✅ {package}: version {requests.__version__}")
        except ImportError:
            print(f"❌ {package}: not installed")
    
    # Show pip commands for reference
    print(f"\n💻 USEFUL PIP COMMANDS:")
    commands = [
        "pip list                    # Show all installed packages",
        "pip show numpy              # Show details about numpy",
        "pip install --upgrade numpy # Upgrade numpy to latest version",
        "pip uninstall numpy         # Remove numpy",
        "pip freeze > requirements.txt # Save current packages to file"
    ]
    
    for cmd in commands:
        print(f"  {cmd}")

# =============================================================================
# PART 5: CREATING A REQUIREMENTS FILE
# =============================================================================

def create_requirements_example():
    """Show how to create and use requirements.txt"""
    print("\n" + "=" * 60)
    print("📄 REQUIREMENTS.TXT EXAMPLE")
    print("=" * 60)
    
    print(f"\n📝 SAMPLE REQUIREMENTS.TXT CONTENT:")
    requirements_content = """# Data Science and Analysis
numpy>=1.20.0
pandas>=1.3.0
matplotlib>=3.4.0

# Web Development
requests>=2.25.0
flask>=2.0.0

# Development Tools
pytest>=6.0.0
black>=21.0.0"""
    
    print(requirements_content)
    
    print(f"\n🚀 HOW TO USE REQUIREMENTS.TXT:")
    usage_commands = [
        "pip install -r requirements.txt    # Install all packages from file",
        "pip freeze > requirements.txt      # Save current packages to file",
        "pip install -r requirements.txt --upgrade  # Upgrade all packages"
    ]
    
    for cmd in usage_commands:
        print(f"  {cmd}")

# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    """Main program demonstrating external packages"""
    print("🐍 EXTERNAL PACKAGES IN ACTION!")
    print("Real examples with NumPy, Requests, and more")
    
    # Run all demonstrations
    numpy_examples()
    requests_examples()
    practical_data_analysis()
    show_installed_packages()
    create_requirements_example()
    
    print("\n" + "=" * 60)
    print("🎉 EXTERNAL PACKAGES DEMO COMPLETE!")
    print("=" * 60)
    print("\n🎯 WHAT YOU LEARNED:")
    print("✅ How to import and use external packages")
    print("✅ NumPy for scientific computing and arrays")
    print("✅ Requests for making HTTP requests")
    print("✅ Package management with pip")
    print("✅ Creating requirements.txt files")
    print("✅ Practical data analysis example")
    
    print("\n🚀 NEXT STEPS:")
    print("1. Try installing more packages: pip install pandas matplotlib")
    print("2. Explore the Python Package Index: https://pypi.org/")
    print("3. Practice combining packages for real projects")
    print("4. Learn about virtual environments: python -m venv myenv")

if __name__ == "__main__":
    main()
# END GENAI@CLINE
