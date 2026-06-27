# ============================================
# CHAPTER 3: DATA TYPES - THE BUILDING BLOCKS
# ============================================
# 🎯 LEARNING OBJECTIVES:
# 1. Learn all Python data types
# 2. Understand type conversion
# 3. Work with None type
# 4. Learn about type checking
# ============================================

# 🌟 PYTHON'S BUILT-IN DATA TYPES
# Let's explore each type with examples!

# 1️⃣ TEXT TYPE - String (str)
# Strings are sequences of characters
greeting = "Hello, Python!"  # Double quotes
name = 'Alice'  # Single quotes
multi_line = """This is a
multi-line string"""  # Triple quotes

print("String examples:")
print(greeting)
print(multi_line)

# 2️⃣ NUMERIC TYPES - Integer (int), Float (float), Complex (complex)
print("\nNumeric types:")
age = 25  # Integer
temperature = 98.6  # Float
complex_num = 3 + 4j  # Complex number

print(f"Integer: {age}, Type: {type(age)}")
print(f"Float: {temperature}, Type: {type(temperature)}")
print(f"Complex: {complex_num}, Type: {type(complex_num)}")

# 3️⃣ SEQUENCE TYPES - List, Tuple, Range
print("\nSequence types:")
my_list = [1, 2, 3, "four", 5.0]  # List - mutable, can change
my_tuple = (1, 2, 3, "four", 5.0)  # Tuple - immutable, can't change
my_range = range(5)  # Range - sequence of numbers

print(f"List: {my_list}")
print(f"Tuple: {my_tuple}")
print(f"Range: {list(my_range)}")  # Convert range to list to display

# 4️⃣ MAPPING TYPE - Dictionary (dict)
print("\nMapping type:")
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "is_student": True
}
print(f"Dictionary: {person}")
print(f"Name: {person['name']}")

# 5️⃣ SET TYPES - Set, Frozenset
print("\nSet types:")
my_set = {1, 2, 3, 4, 4, 5}  # Set - unique elements, unordered
print(f"Set: {my_set}")  # Duplicates removed!

my_frozenset = frozenset([1, 2, 3, 4, 5])  # Immutable set
print(f"Frozenset: {my_frozenset}")

# 6️⃣ BOOLEAN TYPE - bool
print("\nBoolean type:")
is_python_fun = True
is_difficult = False
print(f"Is Python fun? {is_python_fun}")
print(f"Is it difficult? {is_difficult}")

# 7️⃣ NONE TYPE - NoneType
print("\nNone type:")
nothing = None  # Represents absence of value
print(f"Nothing: {nothing}")
print(f"Type: {type(nothing)}")

# 🎭 TYPE CONVERSION - Changing between types
print("\nType Conversion:")

# String to Integer
num_str = "123"
num_int = int(num_str)
print(f'"{num_str}" converted to integer: {num_int}')

# Integer to String
num = 456
num_str2 = str(num)
print(f"{num} converted to string: {num_str2}")

# Float to Integer (truncates decimal)
float_num = 3.99
int_num = int(float_num)
print(f"{float_num} converted to integer: {int_num}")  # 3 (not rounded!)

# String to Float
float_str = "3.14"
float_num2 = float(float_str)
print(f'"{float_str}" converted to float: {float_num2}')

# 🧪 TYPE CHECKING AND VALIDATION
print("\nType checking:")

def check_type(value):
    """Function to check and describe the type of a value"""
    if isinstance(value, int):
        return f"{value} is an integer"
    elif isinstance(value, str):
        return f"{value} is a string"
    elif isinstance(value, list):
        return f"{value} is a list"
    elif isinstance(value, dict):
        return f"{value} is a dictionary"
    elif isinstance(value, float):
        return f"{value} is a float"
    elif isinstance(value, bool):
        return f"{value} is a boolean"
    elif value is None:
        return "Value is None"
    else:
        return f"{value} is of type {type(value)}"

# Test the function
test_values = [42, "Hello", [1, 2, 3], {"key": "value"}, 3.14, True, None]
for val in test_values:
    print(check_type(val))

# 🎯 TRUTHINESS - What's True and False?
print("\nTruthiness:")
# These values are considered False in Python:
false_values = [False, None, 0, "", [], {}, set(), ()]

for val in false_values:
    print(f"{val} is {bool(val)}")

# Everything else is True!
truthy_values = [True, 1, "Hello", [1, 2], {"a": 1}, 3.14]
print("\nTruthy values:")
for val in truthy_values:
    print(f"{val} is {bool(val)}")

# 🚀 CHALLENGE TIME!
# Create a program that:
# 1. Asks for user's name (string)
# 2. Asks for user's age (convert to int)
# 3. Asks for user's height in meters (convert to float)
# 4. Asks if they're a Python beginner (boolean)
# 5. Store everything in a dictionary and display it

print("\n📝 User Information Program:")
# Uncomment below to test with user input:
"""
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
user_height = float(input("Enter your height in meters: "))
is_beginner = input("Are you a Python beginner? (yes/no): ").lower() == "yes"

user_info = {
    "name": user_name,
    "age": user_age,
    "height": user_height,
    "is_beginner": is_beginner
}

print("\nUser Information:")
for key, value in user_info.items():
    print(f"{key.title()}: {value}")
"""

# 📚 WHAT WE LEARNED:
# 1. Python has many built-in data types
# 2. Strings (str), Numbers (int, float, complex)
# 3. Lists (mutable sequences), Tuples (immutable sequences)
# 4. Dictionaries (key-value pairs)
# 5. Sets (unique elements), Frozensets (immutable sets)
# 6. Booleans (True/False)
# 7. NoneType (None)
# 8. Type conversion with int(), float(), str()
# 9. Type checking with type() and isinstance()
# 10. Truthiness of values

# 🎮 NEXT CHAPTER: Strings - Mastering text manipulation!