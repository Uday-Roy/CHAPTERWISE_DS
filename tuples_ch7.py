# ============================================
# CHAPTER 7: TUPLES - IMMUTABLE SEQUENCES
# ============================================
# 🎯 LEARNING OBJECTIVES:
# 1. Understanding tuples and their immutability
# 2. Tuple creation and access
# 3. Tuple methods
# 4. When to use tuples vs lists
# 5. Tuple unpacking
# ============================================

# 📦 CREATING TUPLES
empty_tuple = ()  # Empty tuple
single_tuple = (1,)  # Single element - note the comma!
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True)
nested = (1, (2, 3), [4, 5])  # Can contain lists!

print(f"Empty tuple: {empty_tuple}")
print(f"Single tuple: {single_tuple}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")
print(f"Nested: {nested}")

# 🎯 TUPLE CHARACTERISTICS
# 1. Tuples are immutable - can't change after creation
t = (1, 2, 3)
# t[0] = 10  # This would raise TypeError!

# 2. But if tuple contains mutable elements, those can be changed
t = ([1, 2], 3, 4)
t[0][0] = 99  # This works!
print(f"Tuple with modified list: {t}")

# 3. Tuples preserve order
print(f"Original order: {numbers}")

# 🎯 ACCESSING TUPLE ELEMENTS
coordinates = (10, 20, 30)
print(f"\nCoordinates: {coordinates}")
print(f"X: {coordinates[0]}")
print(f"Y: {coordinates[1]}")
print(f"Z: {coordinates[2]}")

# Slicing works like lists
print(f"First two: {coordinates[:2]}")
print(f"Last two: {coordinates[1:]}")

# 🎨 TUPLE UNPACKING - Elegant assignment
point = (3, 4)
x, y = point
print(f"\nUnpacked: x={x}, y={y}")

# Swapping values using tuple unpacking
a, b = 5, 10
print(f"Before swap: a={a}, b={b}")
a, b = b, a
print(f"After swap: a={a}, b={b}")

# Extended unpacking
first, *middle, last = [1, 2, 3, 4, 5]
print(f"First: {first}, Middle: {middle}, Last: {last}")

# 🛠️ TUPLE METHODS
t = (1, 2, 3, 2, 4, 2, 5)
print(f"\nTuple: {t}")
print(f"Count of 2: {t.count(2)}")
print(f"Index of 4: {t.index(4)}")
print(f"Length: {len(t)}")
print(f"Maximum: {max(t)}")
print(f"Minimum: {min(t)}")
print(f"Sum: {sum(t)}")

# 🔍 TUPLE VS LIST - When to use each
# Use tuples for:
# 1. Data that shouldn't change (constants)
# 2. Dictionary keys (immutable)
# 3. Return multiple values from functions
# 4. Better performance (slightly faster than lists)

# Use lists for:
# 1. Dynamic data that changes
# 2. Need to add/remove elements
# 3. Sorting and modifying

# 📊 TUPLE AS DICTIONARY KEYS
# Tuples can be dictionary keys (lists cannot)
locations = {
    (40.7128, 74.0060): "New York",
    (34.0522, 118.2437): "Los Angeles",
    (41.8781, 87.6298): "Chicago"
}
print(f"\nLocation dictionary: {locations}")

# 🎯 TUPLE CONVERSION
# Convert list to tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(f"List to tuple: {my_tuple}")

# Convert tuple to list
my_list_again = list(my_tuple)
print(f"Tuple to list: {my_list_again}")

# 🚀 NAMED TUPLES - Like tuples with field names
from collections import namedtuple

# Define a point type
Point = namedtuple('Point', ['x', 'y', 'z'])
p = Point(10, 20, 30)

print(f"\nNamed tuple: {p}")
print(f"x: {p.x}, y: {p.y}, z: {p.z}")
print(f"As tuple: {p[0]}, {p[1]}, {p[2]}")

# Create a person type
Person = namedtuple('Person', ['name', 'age', 'city'])
alice = Person('Alice', 25, 'New York')
print(f"Person: {alice.name}, {alice.age}, {alice.city}")

# 📝 PRACTICAL EXAMPLES WITH TUPLES

# 1. Returning multiple values from functions
def get_min_max(numbers):
    """Return both minimum and maximum"""
    return min(numbers), max(numbers)

numbers = [5, 2, 8, 1, 9, 3]
min_val, max_val = get_min_max(numbers)
print(f"\nMin: {min_val}, Max: {max_val}")

# 2. Using tuples for coordinates
def distance(p1, p2):
    """Calculate distance between two points"""
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

p1 = (0, 0)
p2 = (3, 4)
print(f"Distance: {distance(p1, p2):.2f}")

# 3. Tuple as record
def get_user_info():
    """Return user information as tuple"""
    return "Alice", 25, "alice@email.com", True

name, age, email, is_active = get_user_info()
print(f"\nUser: {name}, Age: {age}, Email: {email}, Active: {is_active}")

# 4. Sorting with tuples (good for multiple criteria)
students = [
    ("Alice", 85, "A"),
    ("Bob", 72, "B"),
    ("Charlie", 90, "A"),
    ("Diana", 65, "C")
]

# Sort by grade (index 2)
sorted_students = sorted(students, key=lambda x: x[2])
print(f"\nSorted by grade: {sorted_students}")

# Sort by score descending (index 1)
sorted_by_score = sorted(students, key=lambda x: x[1], reverse=True)
print(f"Sorted by score: {sorted_by_score}")

# 🎯 CHALLENGE: Word Frequency with Tuples
def word_frequency(text):
    """Calculate word frequency and return sorted tuple list"""
    words = text.lower().split()
    freq = {}
    
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    
    # Sort by frequency (descending), then alphabetically
    sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_freq

text = "Python is amazing Python is powerful Python is fun"
frequencies = word_frequency(text)
print(f"\nWord frequencies:")
for word, count in frequencies:
    print(f"  {word}: {count}")

# 📊 TUPLE STATISTICS
def analyze_tuple(t):
    """Analyze a tuple of numbers"""
    print(f"\nAnalyzing tuple: {t}")
    print(f"Length: {len(t)}")
    print(f"Sum: {sum(t)}")
    print(f"Average: {sum(t) / len(t):.2f}")
    print(f"Max: {max(t)}")
    print(f"Min: {min(t)}")
    
    # Check if all elements are the same type
    types = set(type(x) for x in t)
    print(f"All same type: {len(types) == 1}")
    print(f"Types: {types}")

# Test analysis
analyze_tuple((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# 📚 WHAT WE LEARNED:
# 1. Creating tuples and their immutability
# 2. Accessing tuple elements
# 3. Tuple unpacking
# 4. Tuple methods (count, index)
# 5. When to use tuples vs lists
# 6. Named tuples for better code
# 7. Tuples as dictionary keys
# 8. Practical tuple applications

# 🎮 NEXT CHAPTER: Dictionaries - Key-value pairs!