# ============================================
# CHAPTER 5: NUMBERS - MATHEMATICAL MASTERY
# ============================================
# 🎯 LEARNING OBJECTIVES:
# 1. Working with integers and floats
# 2. Mathematical operations
# 3. Number methods and functions
# 4. Random number generation
# 5. Number formatting
# ============================================

import math
import random
from decimal import Decimal
from fractions import Fraction

# 🎯 BASIC NUMBER OPERATIONS
a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"Addition: {a + b}")  # 13
print(f"Subtraction: {a - b}")  # 7
print(f"Multiplication: {a * b}")  # 30
print(f"Division: {a / b}")  # 3.333...
print(f"Floor Division: {a // b}")  # 3 (rounded down)
print(f"Modulus: {a % b}")  # 1 (remainder)
print(f"Exponentiation: {a ** b}")  # 1000

# 🎯 OPERATOR PRECEDENCE
result = 2 + 3 * 4  # 14 (multiplication before addition)
print(f"2 + 3 * 4 = {result}")

result = (2 + 3) * 4  # 20 (parentheses change order)
print(f"(2 + 3) * 4 = {result}")

# 📊 MATH MODULE FUNCTIONS
print("\nMath module functions:")
x = -5
y = 25
z = 3.7

print(f"Absolute of -5: {abs(x)}")
print(f"Power: {pow(2, 3)}")  # 2^3 = 8
print(f"Square root of 25: {math.sqrt(y)}")
print(f"Ceiling of 3.7: {math.ceil(z)}")  # 4
print(f"Floor of 3.7: {math.floor(z)}")  # 3
print(f"Round 3.7: {round(z)}")  # 4
print(f"Pi: {math.pi}")
print(f"Euler's number: {math.e}")

# 📐 TRIGONOMETRIC FUNCTIONS
angle = math.pi / 4  # 45 degrees
print(f"\nTrigonometric functions:")
print(f"Sin(45°): {math.sin(angle):.4f}")
print(f"Cos(45°): {math.cos(angle):.4f}")
print(f"Tan(45°): {math.tan(angle):.4f}")

# 🎲 RANDOM NUMBER GENERATION
print("\nRandom numbers:")
print(f"Random integer (1-10): {random.randint(1, 10)}")
print(f"Random float (0-1): {random.random()}")
print(f"Random float (1-10): {random.uniform(1, 10)}")
print(f"Random choice: {random.choice(['apple', 'banana', 'orange'])}")

# Generate a list of random numbers
random_list = [random.randint(1, 100) for _ in range(10)]
print(f"Random list: {random_list}")
random.shuffle(random_list)
print(f"Shuffled list: {random_list}")

# 🎯 NUMBER TYPE CONVERSIONS
print("\nType conversions:")
num_str = "123"
num_int = int(num_str)
num_float = float(num_str)
print(f"String to int: {num_int}")
print(f"String to float: {num_float}")

# 🎨 DECIMAL AND FRACTION - For precise calculations
print("\nDecimal and Fraction:")
# Decimal for precise decimal arithmetic
from decimal import Decimal
price = Decimal('0.10')
tax = Decimal('0.05')
total = price * (1 + tax)
print(f"Price with tax: {total:.2f}")

# Fraction for exact rational numbers
frac1 = Fraction(1, 3)
frac2 = Fraction(2, 3)
print(f"1/3 + 2/3 = {frac1 + frac2}")  # 1

# 🔢 NUMBER FORMATTING
number = 1234567.89123
print(f"\nNumber formatting:")
print(f"Default: {number}")
print(f"2 decimals: {number:.2f}")
print(f"Comma formatting: {number:,.2f}")
print(f"Scientific notation: {number:.2e}")
print(f"Percentage: {number/100000:.2%}")

# 🎯 INTEGER OPERATIONS
print("\nInteger operations:")
# Bitwise operations
x = 5  # 0101 in binary
y = 3  # 0011 in binary
print(f"Bitwise AND: {x & y}")  # 0001 = 1
print(f"Bitwise OR: {x | y}")   # 0111 = 7
print(f"Bitwise XOR: {x ^ y}")  # 0110 = 6
print(f"Bitwise NOT: {~x}")     # -6
print(f"Left shift: {x << 1}")  # 1010 = 10
print(f"Right shift: {x >> 1}") # 0010 = 2

# 🎯 NUMBER UTILITY FUNCTIONS
def analyze_number(n):
    """Analyze a number and return various properties"""
    print(f"\nAnalyzing {n}:")
    print(f"Type: {type(n)}")
    print(f"Is integer: {n.is_integer() if isinstance(n, float) else True}")
    print(f"Absolute value: {abs(n)}")
    
    # Even/odd check (for integers)
    if isinstance(n, (int, float)) and n.is_integer():
        print(f"Is even: {int(n) % 2 == 0}")
        print(f"Is odd: {int(n) % 2 != 0}")
    
    # Prime check (for positive integers)
    if isinstance(n, int) and n > 1:
        is_prime = all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))
        print(f"Is prime: {is_prime}")

# Test the analyzer
analyze_number(17)
analyze_number(3.14)
analyze_number(-10)

# 🎰 RANDOM GAME - Number Guessing
def number_guessing_game():
    """A simple number guessing game"""
    secret = random.randint(1, 100)
    attempts = 0
    
    print("\n🎮 Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
            
            if guess < secret:
                print("Too low! Try again.")
            elif guess > secret:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! The number was {secret}.")
                print(f"You got it in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid number!")

# Uncomment to play the game!
# number_guessing_game()

# 🧪 MATHEMATICAL STATISTICS
def calculate_statistics(numbers):
    """Calculate various statistics for a list of numbers"""
    if not numbers:
        return "No numbers provided"
    
    print(f"\nStatistics for {numbers}:")
    print(f"Count: {len(numbers)}")
    print(f"Sum: {sum(numbers)}")
    print(f"Average: {sum(numbers) / len(numbers):.2f}")
    print(f"Minimum: {min(numbers)}")
    print(f"Maximum: {max(numbers)}")
    
    # Sort and find median
    sorted_nums = sorted(numbers)
    median = sorted_nums[len(numbers)//2] if len(numbers) % 2 == 1 else \
             (sorted_nums[len(numbers)//2 - 1] + sorted_nums[len(numbers)//2]) / 2
    print(f"Median: {median}")

# Test statistics
test_numbers = [random.randint(1, 100) for _ in range(10)]
calculate_statistics(test_numbers)

# 📚 WHAT WE LEARNED:
# 1. Basic arithmetic operations (+, -, *, /, //, %, **)
# 2. Math module functions (sqrt, ceil, floor, abs)
#