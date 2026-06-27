# ============================================
# CHAPTER 2: VARIABLES - STORING YOUR TREASURES
# ============================================
# 🎯 LEARNING OBJECTIVES:
# 1. Understand what variables are
# 2. Learn variable naming rules
# 3. Assign values to variables
# 4. Understand dynamic typing
# 5. Variable reassignment
# ============================================

# 🎯 WHAT ARE VARIABLES?
# Think of variables as labeled boxes where you store information
# Python is dynamically typed = you don't need to declare type!

# 📦 CREATING YOUR FIRST VARIABLE
name = "Alice"  # A string variable - stores text
age = 25  # An integer variable - stores whole numbers
height = 5.7  # A float variable - stores decimal numbers
is_student = True  # A boolean variable - stores True or False

# 👀 LET'S SEE WHAT'S IN OUR BOXES
print(name)  # Output: Alice
print(age)   # Output: 25
print(height)  # Output: 5.7
print(is_student)  # Output: True

# ✏️ VARIABLE NAMING RULES (IMPORTANT!)
# ✅ Valid variable names:
my_name = "Bob"  # snake_case - recommended!
myName = "Bob"  # camelCase - also valid but less common in Python
_private = "secret"  # Starts with underscore - convention for private
MY_CONSTANT = 3.14  # ALL CAPS - convention for constants

# ❌ Invalid variable names (these will cause errors):
# 123abc = "error"  # Can't start with a number
# my-name = "error"  # No hyphens allowed
# class = "error"  # Can't use Python keywords

# 🔄 VARIABLES CAN CHANGE - Dynamic typing in action!
x = 10  # x is an integer
print(x, "is an integer")

x = "Hello"  # Now x is a string! Python allows this!
print(x, "is now a string!")

x = 3.14  # Now x is a float!
print(x, "is now a float!")

# 🎭 MULTIPLE ASSIGNMENT - Set many variables at once
a, b, c = 1, 2, 3  # a=1, b=2, c=3
print(a, b, c)  # Output: 1 2 3

# Swap values easily!
a, b = b, a  # Now a=2, b=1
print(a, b)  # Output: 2 1

# 📦 ASSIGNING SAME VALUE TO MULTIPLE VARIABLES
x = y = z = 100  # All three variables get value 100
print(x, y, z)  # Output: 100 100 100

# 🔍 CHECKING VARIABLE TYPES
print(type(name))  # <class 'str'>
print(type(age))   # <class 'int'>
print(type(height))  # <class 'float'>
print(type(is_student))  # <class 'bool'>

# 🧮 BASIC OPERATIONS WITH VARIABLES
price = 10
quantity = 3
total = price * quantity  # Multiplication
print("Total cost:", total)  # Output: Total cost: 30

# 📊 VARIABLE REASSIGNMENT WITH MATH
count = 0
count = count + 1  # Increment by 1
print(count)  # Output: 1

count += 1  # Shorthand for count = count + 1
print(count)  # Output: 2

count -= 1  # Decrement by 1
print(count)  # Output: 1

count *= 2  # Multiply by 2
print(count)  # Output: 2

# 🧪 USER INPUT - Making programs interactive!
# name = input("What's your name? ")  # Uncomment to test
# print("Hello,", name, "! Welcome to Python!")

# 💡 CONSTANTS - Values that shouldn't change (convention)
# Using ALL CAPS to indicate constants
PI = 3.14159
GRAVITY = 9.8
MAX_SPEED = 299792458  # Speed of light in m/s

print("PI:", PI)
print("Gravity:", GRAVITY)
print("Speed of Light:", MAX_SPEED, "m/s")

# 🎯 CHALLENGE TIME!
# Create variables for:
# 1. Your favorite movie
# 2. The year it was released
# 3. Your rating out of 10
# 4. Print all this information in a sentence

movie = "Inception"
year = 2010
rating = 9.5

print(f"My favorite movie is {movie} from {year}. I rate it {rating}/10!")

# 📚 WHAT WE LEARNED:
# 1. Variables store data in memory
# 2. Python is dynamically typed
# 3. Variable naming rules and conventions
# 4. Multiple assignment and swapping
# 5. Variable reassignment
# 6. The type() function
# 7. Constants convention (ALL_CAPS)

# 🎮 NEXT CHAPTER: Data Types - Understanding Python's building blocks!