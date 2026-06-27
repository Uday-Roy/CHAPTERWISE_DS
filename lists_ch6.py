# ============================================
# CHAPTER 6: LISTS - YOUR DATA CONTAINERS
# ============================================
# 🎯 LEARNING OBJECTIVES:
# 1. Creating and accessing lists
# 2. List methods and operations
# 3. List slicing and comprehension
# 4. List manipulation techniques
# 5. Nested lists
# ============================================

# 📦 CREATING LISTS - Your data containers
empty_list = []  # Empty list
numbers = [1, 2, 3, 4, 5]  # List of numbers
fruits = ["apple", "banana", "orange", "grape"]  # List of strings
mixed = [1, "hello", 3.14, True, [1, 2, 3]]  # Mixed types!
print(f"Empty list: {empty_list}")
print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Mixed list: {mixed}")

# 🎯 ACCESSING ELEMENTS - Indexing and slicing
fruits = ["apple", "banana", "orange", "grape", "kiwi"]
print(f"\nAccessing elements:")
print(f"First fruit: {fruits[0]}")  # apple
print(f"Last fruit: {fruits[-1]}")  # kiwi
print(f"Second fruit: {fruits[1]}")  # banana
print(f"Last two: {fruits[-2:]}")  # ['grape', 'kiwi']
print(f"First three: {fruits[:3]}")  # ['apple', 'banana', 'orange']
print(f"Middle three: {fruits[1:4]}")  # ['banana', 'orange', 'grape']

# 🎨 LIST OPERATIONS
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
combined = list1 + list2
print(f"\nConcatenated: {combined}")  # [1, 2, 3, 4, 5, 6]

# Repetition
repeated = list1 * 3
print(f"Repeated: {repeated}")  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Membership
print(f"Is 3 in list? {3 in list1}")  # True
print(f"Is 7 in list? {7 in list1}")  # False

# 🛠️ LIST METHODS - The Swiss Army Knife
numbers = [1, 2, 3, 4, 5]
print(f"\nOriginal list: {numbers}")

# Adding elements
numbers.append(6)  # Add to end
print(f"After append: {numbers}")

numbers.insert(0, 0)  # Insert at index
print(f"After insert: {numbers}")

numbers.extend([7, 8, 9])  # Extend with another list
print(f"After extend: {numbers}")

# Removing elements
numbers.remove(5)  # Remove first occurrence
print(f"After remove: {numbers}")

popped = numbers.pop()  # Remove and return last element
print(f"Popped: {popped}, List: {numbers}")

popped_first = numbers.pop(0)  # Remove and return element at index
print(f"Popped first: {popped_first}, List: {numbers}")

# Sorting
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()  # Sort in place
print(f"Sorted: {numbers}")

numbers.sort(reverse=True)
print(f"Reverse sorted: {numbers}")

# Reversing
numbers.reverse()
print(f"Reversed: {numbers}")

# 🎯 LIST SLICING - Advanced techniques
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"\nOriginal list: {numbers}")

# Step slicing
print(f"Even indices: {numbers[::2]}")  # [0, 2, 4, 6, 8]
print(f"Odd indices: {numbers[1::2]}")  # [1, 3, 5, 7, 9]
print(f"Every third: {numbers[::3]}")  # [0, 3, 6, 9]

# Reverse using slicing
print(f"Reversed: {numbers[::-1]}")  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 🔍 FINDING AND COUNTING
fruits = ["apple", "banana", "orange", "apple", "kiwi", "apple"]
print(f"\nFruits: {fruits}")
print(f"Index of 'orange': {fruits.index('orange')}")
print(f"Count of 'apple': {fruits.count('apple')}")

# 🚀 LIST COMPREHENSIONS - Elegant list creation
# Traditional way
squares = []
for i in range(10):
    squares.append(i ** 2)
print(f"\nSquares (traditional): {squares}")

# List comprehension
squares = [i ** 2 for i in range(10)]
print(f"Squares (comprehension): {squares}")

# With condition
even_squares = [i ** 2 for i in range(10) if i % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested comprehensions
matrix = [[j for j in range(3)] for i in range(3)]
print(f"Matrix: {matrix}")

# 🎮 WORKING WITH LISTS - Practical examples

# 1. Removing duplicates
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))  # Preserves order

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(f"\nOriginal with duplicates: {numbers}")
print(f"After removing duplicates: {remove_duplicates(numbers)}")

# 2. Finding common elements
def find_common(list1, list2):
    return list(set(list1) & set(list2))

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(f"Common elements: {find_common(list1, list2)}")

# 3. Flatten a nested list
def flatten_list(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

nested = [1, [2, 3], [4, [5, 6]], 7]
print(f"Flattened: {flatten_list(nested)}")

# 4. List partitioning
def partition_list(lst, size):
    """Split list into chunks of specified size"""
    return [lst[i:i+size] for i in range(0, len(lst), size)]

numbers = list(range(10))
print(f"Partitioned into groups of 3: {partition_list(numbers, 3)}")

# 📊 LIST STATISTICS
def analyze_list(lst):
    if not lst:
        return "Empty list"
    
    print(f"\nAnalyzing list: {lst}")
    print(f"Length: {len(lst)}")
    print(f"Sum: {sum(lst)}")
    print(f"Average: {sum(lst) / len(lst):.2f}")
    print(f"Maximum: {max(lst)}")
    print(f"Minimum: {min(lst)}")
    print(f"Sorted: {sorted(lst)}")
    
    # Frequency of elements
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    print(f"Frequency: {freq}")

# Test analysis
analyze_list([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

# 🎯 CHALLENGE: Shopping List Manager
class ShoppingList:
    def __init__(self):
        self.items = []
        self.prices = {}
    
    def add_item(self, item, price=0):
        self.items.append(item)
        self.prices[item] = price
        print(f"Added '{item}' to shopping list")
    
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            del self.prices[item]
            print(f"Removed '{item}' from shopping list")
        else:
            print(f"'{item}' not in list")
    
    def show_list(self):
        if not self.items:
            print("Shopping list is empty")
        else:
            print("\n🛒 Shopping List:")
            total = 0
            for i, item in enumerate(self.items, 1):
                price = self.prices.get(item, 0)
                total += price
                print(f"{i}. {item} - ${price:.2f}")
            print(f"Total: ${total:.2f}")
    
    def sort_by_price(self):
        sorted_items = sorted(self.items, key=lambda x: self.prices.get(x, 0))
        print("\nSorted by price:")
        for item in sorted_items:
            print(f"{item}: ${self.prices.get(item, 0):.2f}")

# Test the shopping list
shopping = ShoppingList()
shopping.add_item("Apple", 1.50)
shopping.add_item("Bread", 2.00)
shopping.add_item("Milk", 3.50)
shopping.add_item("Eggs", 2.50)
shopping.show_list()
shopping.sort_by_price()

# 📚 WHAT WE LEARNED:
# 1. Creating and accessing lists
# 2. List methods (append, insert, extend, remove, pop)
# 3. Sorting and reversing
# 4. List slicing with steps
# 5. List comprehensions
# 6. Removing duplicates
# 7. Finding common elements
# 8. Flattening nested lists
# 9. List partitioning
# 10. Practical list applications

# 🎮 NEXT CHAPTER: Tuples - Immutable sequences!