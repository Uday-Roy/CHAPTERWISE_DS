# ============================================
# COMPLETE LOOPS IN PYTHON - ALL CONCEPTS IN ONE FILE
# ============================================
# 🎯 LEARNING OBJECTIVES:
# 1. For Loops (range, iterables, enumerate)
# 2. While Loops
# 3. Nested Loops
# 4. Loop Control Statements (break, continue, pass)
# 5. Else Clause with Loops
# 6. Loop Optimizations
# 7. Infinite Loops and Safety
# 8. Practical Applications
# ============================================

import time
import random
from itertools import product, permutations, combinations

# ============================================
# 1. BASIC FOR LOOPS
# ============================================

print("=" * 60)
print("🔄 BASIC FOR LOOPS")
print("=" * 60)

# 1.1 Loop over range
print("\n🔹 1.1 Range Loops")
print("-" * 40)

print("Basic range loop:")
for i in range(5):
    print(f"  Iteration {i}")

print("\nRange with start and end:")
for i in range(2, 7):
    print(f"  Number: {i}")

print("\nRange with step:")
for i in range(0, 10, 2):
    print(f"  Even number: {i}")

print("\nRange backwards:")
for i in range(10, 0, -1):
    print(f"  Countdown: {i}")

# 1.2 Loop over lists
print("\n🔹 1.2 List Loops")
print("-" * 40)

fruits = ["apple", "banana", "orange", "grape", "kiwi"]

print("Looping through list:")
for fruit in fruits:
    print(f"  Fruit: {fruit}")

print("\nLooping with index using enumerate:")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

print("\nLooping with index starting from 1:")
for index, fruit in enumerate(fruits, 1):
    print(f"  #{index}: {fruit}")

# 1.3 Loop over strings
print("\n🔹 1.3 String Loops")
print("-" * 40)

text = "Python"
print(f"Characters in '{text}':")
for char in text:
    print(f"  Character: {char}")

# 1.4 Loop over dictionaries
print("\n🔹 1.4 Dictionary Loops")
print("-" * 40)

person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "job": "Developer"
}

print("Looping through keys:")
for key in person:
    print(f"  {key}: {person[key]}")

print("\nLooping through key-value pairs:")
for key, value in person.items():
    print(f"  {key} = {value}")

print("\nLooping through values:")
for value in person.values():
    print(f"  Value: {value}")

# 1.5 Loop over tuples and sets
print("\n🔹 1.5 Tuple and Set Loops")
print("-" * 40)

tuple_data = (1, 2, 3, 4, 5)
print("Looping through tuple:")
for item in tuple_data:
    print(f"  {item}")

set_data = {10, 20, 30, 40, 50}
print("\nLooping through set (order not guaranteed):")
for item in set_data:
    print(f"  {item}")

# ============================================
# 2. NESTED LOOPS
# ============================================

print("\n" + "=" * 60)
print("🔲 NESTED LOOPS")
print("=" * 60)

# 2.1 Multiplication table
print("\n🔹 2.1 Multiplication Table")
print("-" * 40)

print("Multiplication Table (1-5):")
for i in range(1, 6):
    row = []
    for j in range(1, 6):
        row.append(f"{i*j:2}")
    print("  " + " ".join(row))

# 2.2 Pattern printing
print("\n🔹 2.2 Pattern Printing")
print("-" * 40)

print("Right Triangle Pattern:")
for i in range(1, 6):
    print("  " + "*" * i)

print("\nPyramid Pattern:")
n = 5
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(f"  {spaces}{stars}")

print("\nDiamond Pattern:")
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(f"  {spaces}{stars}")
for i in range(n - 1, 0, -1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(f"  {spaces}{stars}")

# 2.3 Matrix operations
print("\n🔹 2.3 Matrix Operations")
print("-" * 40)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(f"  {row}")

print("\nMatrix with indices:")
for i, row in enumerate(matrix):
    for j, value in enumerate(row):
        print(f"  Matrix[{i}][{j}] = {value}")

print("\nMatrix sum:")
total = 0
for row in matrix:
    for value in row:
        total += value
print(f"  Total sum: {total}")

# ============================================
# 3. WHILE LOOPS
# ============================================

print("\n" + "=" * 60)
print("🔄 WHILE LOOPS")
print("=" * 60)

# 3.1 Basic while loop
print("\n🔹 3.1 Basic While Loop")
print("-" * 40)

count = 0
print("Counting to 5:")
while count < 5:
    print(f"  Count: {count}")
    count += 1

# 3.2 While with user input
print("\n🔹 3.2 While with User Input (Simulated)")
print("-" * 40)

# Simulated user input
def simulate_user_input():
    responses = ["yes", "no", "yes", "quit"]
    for response in responses:
        print(f"  User said: {response}")
        yield response

print("Interactive loop (simulated):")
for user_input in simulate_user_input():
    if user_input == "quit":
        print("  Exiting...")
        break
    print(f"  Processing: {user_input}")

# 3.3 While with conditions
print("\n🔹 3.3 While with Conditions")
print("-" * 40)

# Sum until target reached
target = 100
current_sum = 0
count = 0

while current_sum < target:
    count += 1
    current_sum += count
    print(f"  Added {count}, sum = {current_sum}")

print(f"  Reached {target} after {count} iterations")

# ============================================
# 4. LOOP CONTROL STATEMENTS
# ============================================

print("\n" + "=" * 60)
print("🎮 LOOP CONTROL STATEMENTS")
print("=" * 60)

# 4.1 Break statement
print("\n🔹 4.1 Break Statement")
print("-" * 40)

print("Find first even number greater than 10:")
numbers = [3, 7, 9, 12, 15, 18, 20, 25]
for num in numbers:
    if num > 10 and num % 2 == 0:
        print(f"  Found: {num}")
        break

# 4.2 Continue statement
print("\n🔹 4.2 Continue Statement")
print("-" * 40)

print("Print odd numbers only:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"  {i}")

# 4.3 Pass statement
print("\n🔹 4.3 Pass Statement")
print("-" * 40)

print("Using pass as placeholder:")
for i in range(5):
    if i == 2:
        pass  # Placeholder for future code
    else:
        print(f"  {i}")

# ============================================
# 5. ELSE CLAUSE WITH LOOPS
# ============================================

print("\n" + "=" * 60)
print("📝 ELSE CLAUSE WITH LOOPS")
print("=" * 60)

# 5.1 For-else
print("\n🔹 5.1 For-Else")
print("-" * 40)

# Search example with else
def find_number(numbers, target):
    for num in numbers:
        if num == target:
            print(f"  Found {target} in list")
            break
    else:
        print(f"  {target} not found in list")

print("Searching for 7:")
find_number([1, 2, 3, 4, 5], 7)
print("\nSearching for 3:")
find_number([1, 2, 3, 4, 5], 3)

# 5.2 While-else
print("\n🔹 5.2 While-Else")
print("-" * 40)

count = 0
print("Loop with else (successful completion):")
while count < 3:
    print(f"  Count: {count}")
    count += 1
else:
    print("  Loop completed successfully!")

# ============================================
# 6. ADVANCED LOOP TECHNIQUES
# ============================================

print("\n" + "=" * 60)
print("🚀 ADVANCED LOOP TECHNIQUES")
print("=" * 60)

# 6.1 Parallel iteration with zip
print("\n🔹 6.1 Zip for Parallel Iteration")
print("-" * 40)

names = ["Alice", "Bob", "Charlie", "Diana"]
scores = [85, 92, 78, 95]
grades = ["A", "A-", "B+", "A"]

print("Student data:")
for name, score, grade in zip(names, scores, grades):
    print(f"  {name}: {score}% - {grade}")

# 6.2 Enumerate for index
print("\n🔹 6.2 Enumerate for Index")
print("-" * 40)

words = ["apple", "banana", "cherry", "date"]
for index, word in enumerate(words):
    print(f"  Word {index}: {word} ({len(word)} characters)")

# 6.3 Sorted iteration
print("\n🔹 6.3 Sorted Iteration")
print("-" * 40)

unsorted = [5, 2, 8, 1, 9, 3]
print(f"Original: {unsorted}")
print("Sorted iteration:")
for num in sorted(unsorted):
    print(f"  {num}")

# 6.4 Reversed iteration
print("\n🔹 6.4 Reversed Iteration")
print("-" * 40)

items = [1, 2, 3, 4, 5]
print(f"Original: {items}")
print("Reversed iteration:")
for item in reversed(items):
    print(f"  {item}")

# ============================================
# 7. ITERTOOLS - POWERFUL ITERATION TOOLS
# ============================================

print("\n" + "=" * 60)
print("🔧 ITERTOOLS - ADVANCED ITERATION")
print("=" * 60)

from itertools import product, permutations, combinations, cycle, repeat, chain

# 7.1 Product
print("\n🔹 7.1 Product (Cartesian Product)")
print("-" * 40)

colors = ["red", "blue"]
sizes = ["S", "M", "L"]
print("Product of colors and sizes:")
for color, size in product(colors, sizes):
    print(f"  {color} - {size}")

# 7.2 Permutations
print("\n🔹 7.2 Permutations")
print("-" * 40)

items = ["A", "B", "C"]
print(f"Permutations of {items}:")
for perm in permutations(items, 2):
    print(f"  {perm}")

# 7.3 Combinations
print("\n🔹 7.3 Combinations")
print("-" * 40)

items = ["A", "B", "C", "D"]
print(f"Combinations of {items} (2 at a time):")
for comb in combinations(items, 2):
    print(f"  {comb}")

# 7.4 Cycle
print("\n🔹 7.4 Cycle (Infinite Iterator)")
print("-" * 40)

print("First 10 values of cycling through (1, 2, 3):")
cycle_iter = cycle([1, 2, 3])
for i, value in enumerate(cycle_iter):
    if i >= 10:
        break
    print(f"  {value}")

# ============================================
# 8. COMPREHENSIONS - ELEGANT LOOPS
# ============================================

print("\n" + "=" * 60)
print("🎨 COMPREHENSIONS - ELEGANT LOOPS")
print("=" * 60)

# 8.1 List Comprehensions
print("\n🔹 8.1 List Comprehensions")
print("-" * 40)

# Basic list comprehension
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested comprehensions
matrix = [[j for j in range(3)] for i in range(3)]
print(f"Matrix: {matrix}")

# 8.2 Dictionary Comprehensions
print("\n🔹 8.2 Dictionary Comprehensions")
print("-" * 40)

# Square dictionary
square_dict = {x: x**2 for x in range(5)}
print(f"Square dictionary: {square_dict}")

# Filtered dictionary
filtered_dict = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Filtered dictionary: {filtered_dict}")

# 8.3 Set Comprehensions
print("\n🔹 8.3 Set Comprehensions")
print("-" * 40)

# Set of squares
square_set = {x**2 for x in range(5)}
print(f"Square set: {square_set}")

# 8.4 Generator Expressions
print("\n🔹 8.4 Generator Expressions (Memory Efficient)")
print("-" * 40)

# Generator expression (uses parentheses)
gen = (x**2 for x in range(10))
print(f"Generator: {gen}")
print("Values from generator:")
for value in gen:
    print(f"  {value}")

# ============================================
# 9. PERFORMANCE OPTIMIZATIONS
# ============================================

print("\n" + "=" * 60)
print("⚡ PERFORMANCE OPTIMIZATIONS")
print("=" * 60)

# 9.1 Local variable optimization
print("\n🔹 9.1 Local Variable Optimization")
print("-" * 40)

import time

def slow_loop():
    result = []
    for i in range(100000):
        result.append(i * 2)
    return result

def fast_loop():
    result = []
    append = result.append  # Local variable optimization
    for i in range(100000):
        append(i * 2)
    return result

print("Measuring performance (will run 100,000 iterations):")
start = time.time()
slow_loop()
slow_time = time.time() - start
print(f"  Slow loop: {slow_time:.4f} seconds")

start = time.time()
fast_loop()
fast_time = time.time() - start
print(f"  Fast loop: {fast_time:.4f} seconds")
print(f"  Speedup: {slow_time/fast_time:.2f}x")

# 9.2 Using built-in functions
print("\n🔹 9.2 Using Built-in Functions")
print("-" * 40)

numbers = list(range(1000))

# Manual loop for sum
def manual_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Built-in sum
def builtin_sum(numbers):
    return sum(numbers)

print(f"Manual sum: {manual_sum(numbers)}")
print(f"Built-in sum: {builtin_sum(numbers)}")

# ============================================
# 10. PRACTICAL APPLICATIONS
# ============================================

print("\n" + "=" * 60)
print("🎯 PRACTICAL APPLICATIONS")
print("=" * 60)

# 10.1 Data Processing Pipeline
print("\n🔹 10.1 Data Processing Pipeline")
print("-" * 40)

def process_data(data):
    """Process data through multiple stages"""
    print(f"Raw data: {data}")
    
    # Stage 1: Clean data
    cleaned = []
    for item in data:
        if item:  # Remove empty values
            cleaned.append(item.strip())
    print(f"Cleaned: {cleaned}")
    
    # Stage 2: Transform data
    transformed = []
    for item in cleaned:
        transformed.append(item.upper())
    print(f"Transformed: {transformed}")
    
    # Stage 3: Filter data
    filtered = [item for item in transformed if len(item) > 3]
    print(f"Filtered: {filtered}")
    
    # Stage 4: Aggregate data
    aggregated = {}
    for item in filtered:
        aggregated[item] = aggregated.get(item, 0) + 1
    print(f"Aggregated: {aggregated}")
    
    return aggregated

# Test data processing
data = ["apple", "banana", "", "APPLE", "orange", "banana", "  grape  "]
process_data(data)

# 10.2 Simulation - Weather Data Analysis
print("\n🔹 10.2 Weather Data Analysis")
print("-" * 40)

def generate_weather_data(days):
    """Generate simulated weather data"""
    weather_data = []
    for day in range(days):
        temp = random.randint(-10, 35)
        humidity = random.randint(20, 90)
        wind_speed = random.randint(0, 50)
        weather_data.append({
            'day': day + 1,
            'temperature': temp,
            'humidity': humidity,
            'wind_speed': wind_speed
        })
    return weather_data

def analyze_weather(data):
    """Analyze weather data"""
    print(f"Analyzing {len(data)} days of weather data:")
    
    # Temperature analysis
    temps = [d['temperature'] for d in data]
    print(f"  Temperature - Min: {min(temps)}°C, Max: {max(temps)}°C, Avg: {sum(temps)/len(temps):.1f}°C")
    
    # Hot days
    hot_days = [d for d in data if d['temperature'] > 30]
    print(f"  Hot days (>30°C): {len(hot_days)}")
    
    # Windy days
    windy_days = [d for d in data if d['wind_speed'] > 30]
    print(f"  Windy days (>30 km/h): {len(windy_days)}")
    
    # Find best day
    best_day = max(data, key=lambda d: d['temperature'] - d['humidity']/100)
    print(f"  Best day: Day {best_day['day']} - {best_day['temperature']}°C, {best_day['humidity']}% humidity")

# Generate and analyze weather data
weather_data = generate_weather_data(30)
analyze_weather(weather_data)

# 10.3 Game - Number Guessing with Limited Attempts
print("\n🔹 10.3 Number Guessing Game")
print("-" * 40)

class NumberGuessingGame:
    def __init__(self, max_attempts=7):
        self.max_attempts = max_attempts
        self.secret = random.randint(1, 100)
        self.attempts = 0
        self.guesses = []
    
    def play(self):
        """Play the guessing game"""
        print(f"🎮 Guess the number (1-100) - {self.max_attempts} attempts")
        
        while self.attempts < self.max_attempts:
            # Simulate user input
            guess = random.randint(1, 100) if self.attempts < 3 else random.randint(1, 100)
            self.attempts += 1
            self.guesses.append(guess)
            
            print(f"  Attempt {self.attempts}: {guess}")
            
            if guess == self.secret:
                print(f"  🎉 Correct! The number was {self.secret}")
                print(f"  Found in {self.attempts} attempts!")
                break
            elif guess < self.secret:
                print("  📈 Too low")
            else:
                print("  📉 Too high")
            
            remaining = self.max_attempts - self.attempts
            if remaining > 0:
                print(f"  {remaining} attempts remaining")
        else:
            print(f"  😔 Game over! The number was {self.secret}")
        
        print(f"  Guesses: {self.guesses}")

# Play the game
game = NumberGuessingGame()
game.play()

# 10.4 File Processing - Log Analysis
print("\n🔹 10.4 Log Analysis")
print("-" * 40)

def simulate_log_data():
    """Generate simulated log data"""
    log_levels = ["INFO", "WARNING", "ERROR", "DEBUG"]
    messages = [
        "User logged in",
        "Database connection successful",
        "API request failed",
        "Cache miss detected",
        "File not found",
        "Memory usage high",
        "User logged out",
        "Configuration loaded"
    ]
    
    logs = []
    for i in range(100):
        log = {
            'timestamp': f"2024-01-01 00:{i:02d}:00",
            'level': random.choice(log_levels),
            'message': random.choice(messages)
        }
        logs.append(log)
    return logs

def analyze_logs(logs):
    """Analyze log data"""
    print(f"Analyzing {len(logs)} log entries:")
    
    # Count by level
    level_counts = {}
    for log in logs:
        level = log['level']
        level_counts[level] = level_counts.get(level, 0) + 1
    
    print("  Log level distribution:")
    for level, count in sorted(level_counts.items()):
        print(f"    {level}: {count} ({count/len(logs)*100:.1f}%)")
    
    # Find errors
    errors = [log for log in logs if log['level'] == 'ERROR']
    print(f"  Total errors: {len(errors)}")
    
    # Most common messages
    message_counts = {}
    for log in logs:
        msg = log['message']
        message_counts[msg] = message_counts.get(msg, 0) + 1
    
    print("  Most common messages:")
    for msg, count in sorted(message_counts.items(), key=lambda x: x[1], reverse=True)[:3]:
        print(f"    {msg}: {count} times")

# Generate and analyze logs
log_data = simulate_log_data()
analyze_logs(log_data)

# 10.5 Progress Tracking
print("\n🔹 10.5 Progress Tracking")
print("-" * 40)

def process_with_progress(total=100):
    """Process with progress indicator"""
    print(f"Processing {total} items...")
    
    for i in range(1, total + 1):
        # Simulate work
        time.sleep(0.01)  # Simulate processing
        
        # Show progress every 10%
        if i % (total // 10) == 0 or i == total:
            percentage = (i / total) * 100
            bar_length = 30
            filled = int(bar_length * i // total)
            bar = '█' * filled + '░' * (bar_length - filled)
            print(f"  [{bar}] {percentage:.0f}%", end='\r')
    
    print("\n  ✅ Processing complete!")

process_with_progress(100)

# ============================================
# 11. LOOP BEST PRACTICES AND TIPS
# ============================================

print("\n" + "=" * 60)
print("💡 LOOP BEST PRACTICES")
print("=" * 60)

# 11.1 Avoid modifying list while iterating
print("\n🔹 11.1 Avoid Modifying List While Iterating")
print("-" * 40)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# BAD: Modifying list while iterating
print("BAD Practice (using copy):")
for num in numbers[:]:  # Use copy
    if num % 2 == 0:
        numbers.remove(num)  # Removing from original

# GOOD: Use list comprehension
print("GOOD Practice (list comprehension):")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = [num for num in numbers if num % 2 != 0]
print(f"  Result: {numbers}")

# 11.2 Use enumerate for index
print("\n🔹 11.2 Use Enumerate for Index")
print("-" * 40)

items = ['a', 'b', 'c', 'd']

# BAD
print("Bad way:")
for i in range(len(items)):
    print(f"  {i}: {items[i]}")

# GOOD
print("Good way:")
for i, item in enumerate(items):
    print(f"  {i}: {item}")

# 11.3 Use zip for parallel iteration
print("\n🔹 11.3 Use Zip for Parallel Iteration")
print("-" * 40)

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

# BAD
print("Bad way:")
for i in range(len(names)):
    print(f"  {names[i]} is {ages[i]}")

# GOOD
print("Good way:")
for name, age in zip(names, ages):
    print(f"  {name} is {age}")

# ============================================
# SUMMARY AND CHEAT SHEET
# ============================================

print("\n" + "=" * 60)
print("📚 LOOP CHEAT SHEET")
print("=" * 60)

print("""
🔹 FOR LOOPS:
  for item in iterable:          # Iterate over any iterable
  for i in range(n):             # Iterate n times
  for i in range(start, stop):   # Iterate with start and stop
  for i in range(start, stop, step): # Iterate with step
  for i, item in enumerate(list): # Get index and value
  for key, value in dict.items(): # Iterate over dictionary

🔹 WHILE LOOPS:
  while condition:                # Loop while condition is True
  while True:                     # Infinite loop (use with break)

🔹 CONTROL STATEMENTS:
  break                          # Exit loop immediately
  continue                       # Skip current iteration
  pass                          # Placeholder (do nothing)
  else:                         # Execute after loop (if not broken)

🔹 COMPREHENSIONS:
  [expr for item in iterable]    # List comprehension
  {key: value for item in iterable} # Dictionary comprehension
  {expr for item in iterable}    # Set comprehension
  (expr for item in iterable)    # Generator expression

🔹 ITERTOOLS:
  product(iter1, iter2)          # Cartesian product
  permutations(iter, r)          # All permutations
  combinations(iter, r)          # All combinations
  cycle(iter)                    # Infinite cycle
  chain(iter1, iter2)            # Chain iterators

🔹 BEST PRACTICES:
  ✓ Use enumerate instead of range(len())
  ✓ Use zip for parallel iteration
  ✓ Don't modify list while iterating
  ✓ Use list comprehensions when possible
  ✓ Consider generator expressions for large data
  ✓ Use break to exit early when found
  ✓ Use continue to skip unwanted items
""")

print("=" * 60)
print("🎉 LOOP MASTERY COMPLETE!")
print("=" * 60)