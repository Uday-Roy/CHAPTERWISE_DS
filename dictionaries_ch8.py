# ============================================
# CHAPTER 8: DICTIONARIES - KEY-VALUE PAIRS
# ============================================
# 🎯 LEARNING OBJECTIVES:
# 1. Understanding dictionaries
# 2. Creating and accessing dictionaries
# 3. Dictionary methods
# 4. Dictionary comprehensions
# 5. Nested dictionaries
# 6. Practical applications
# ============================================

# 📦 CREATING DICTIONARIES
empty_dict = {}  # Empty dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "is_student": True
}

print(f"Empty dict: {empty_dict}")
print(f"Person: {person}")

# Alternative creation methods
dict_using_constructor = dict(name="Bob", age=30, city="Boston")
dict_from_pairs = dict([("key1", "value1"), ("key2", "value2")])
print(f"Using constructor: {dict_using_constructor}")
print(f"From pairs: {dict_from_pairs}")

# 🎯 ACCESSING VALUES
person = {"name": "Alice", "age": 25, "city": "New York"}

# Direct access
print(f"\nName: {person['name']}")
print(f"Age: {person['age']}")

# Using get() - safer method
print(f"City: {person.get('city')}")
print(f"Country: {person.get('country', 'Not specified')}")  # Default value

# 🎨 ADDING AND UPDATING
person = {"name": "Alice", "age": 25}
print(f"\nOriginal: {person}")

# Add new key-value pair
person["city"] = "New York"
print(f"After adding city: {person}")

# Update existing key
person["age"] = 26
print(f"After updating age: {person}")

# Update with another dictionary
person.update({"email": "alice@email.com", "phone": "123-456-7890"})
print(f"After update: {person}")

# 🛠️ REMOVING ITEMS
person = {"name": "Alice", "age": 25, "city": "New York", "email": "alice@email.com"}
print(f"\nOriginal: {person}")

# Remove specific key
del person["city"]
print(f"After deleting city: {person}")

# Remove and return value
email = person.pop("email")
print(f"Popped email: {email}")
print(f"After pop: {person}")

# Remove and return last item (Python 3.7+ preserves order)
last_item = person.popitem()
print(f"Last item: {last_item}")
print(f"After popitem: {person}")

# Clear all items
person.clear()
print(f"After clear: {person}")

# 🔍 CHECKING KEYS AND VALUES
person = {"name": "Alice", "age": 25, "city": "New York"}

print(f"\nKeys: {person.keys()}")
print(f"Values: {person.values()}")
print(f"Items: {person.items()}")

# Check if key exists
print(f"Is 'name' in dict? {'name' in person}")
print(f"Is 'country' in dict? {'country' in person}")

# Check if value exists
print(f"Is 'Alice' in values? {'Alice' in person.values()}")
print(f"Is 30 in values? {30 in person.values()}")

# 🔄 ITERATING OVER DICTIONARIES
person = {"name": "Alice", "age": 25, "city": "New York"}

print("\nIterating over keys:")
for key in person:
    print(f"  {key}: {person[key]}")

print("Iterating over items:")
for key, value in person.items():
    print(f"  {key}: {value}")

print("Iterating over values:")
for value in person.values():
    print(f"  {value}")

# 🚀 DICTIONARY COMPREHENSIONS
# Create a dictionary of squares
squares = {x: x**2 for x in range(5)}
print(f"\nSquares: {squares}")

# Filter with condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Invert dictionary
original = {"a": 1, "b": 2, "c": 3}
inverted = {value: key for key, value in original.items()}
print(f"Inverted: {inverted}")

# 📊 NESTED DICTIONARIES
students = {
    "student1": {
        "name": "Alice",
        "grades": [85, 90, 88],
        "age": 20
    },
    "student2": {
        "name": "Bob",
        "grades": [75, 80, 85],
        "age": 22
    }
}

print(f"\nNested dictionary: {students}")
print(f"Alice's grades: {students['student1']['grades']}")
print(f"Bob's average: {sum(students['student2']['grades']) / 3:.2f}")

# 🔧 DICTIONARY METHODS AND OPERATIONS

# Merging dictionaries (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}  # Or dict1 | dict2 in Python 3.9+
print(f"\nMerged: {merged}")

# Default dictionary - auto-create missing keys
from collections import defaultdict

# Example: Counting words
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = defaultdict(int)
for word in words:
    word_count[word] += 1
print(f"\nWord counts using defaultdict: {dict(word_count)}")

# Counter - even easier for counting
from collections import Counter
word_count = Counter(words)
print(f"Word counts using Counter: {word_count}")

# 🎯 PRACTICAL APPLICATIONS

# 1. Phone book application
def phone_book_app():
    """Simple phone book using dictionary"""
    phone_book = {}
    
    while True:
        print("\n📞 Phone Book")
        print("1. Add contact")
        print("2. Find contact")
        print("3. Delete contact")
        print("4. Show all contacts")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            phone_book[name] = phone
            print(f"Added {name}")
        
        elif choice == "2":
            name = input("Enter name to search: ")
            if name in phone_book:
                print(f"{name}: {phone_book[name]}")
            else:
                print("Contact not found")
        
        elif choice == "3":
            name = input("Enter name to delete: ")
            if name in phone_book:
                del phone_book[name]
                print(f"Deleted {name}")
            else:
                print("Contact not found")
        
        elif choice == "4":
            if phone_book:
                print("\nAll Contacts:")
                for name, phone in sorted(phone_book.items()):
                    print(f"  {name}: {phone}")
            else:
                print("Phone book is empty")
        
        elif choice == "5":
            break
        
        else:
            print("Invalid choice")

# Uncomment to run the phone book
# phone_book_app()

# 2. Character frequency counter
def char_frequency(text):
    """Count frequency of each character"""
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq

text = "hello world"
freq = char_frequency(text)
print(f"\nCharacter frequency: {freq}")

# 3. Group by category
def group_by_category(items):
    """Group items by their category"""
    groups = {}
    for item in items:
        category = item.get("category", "uncategorized")
        groups.setdefault(category, []).append(item)
    return groups

items = [
    {"name": "Apple", "category": "fruit"},
    {"name": "Carrot", "category": "vegetable"},
    {"name": "Banana", "category": "fruit"},
    {"name": "Broccoli", "category": "vegetable"}
]
grouped = group_by_category(items)
print(f"\nGrouped by category: {grouped}")

# 🎯 CHALLENGE: Grade Book System
class GradeBook:
    def __init__(self):
        self.students = {}
    
    def add_student(self, name):
        if name not in self.students:
            self.students[name] = []
            print(f"Added student: {name}")
        else:
            print(f"Student {name} already exists")
    
    def add_grade(self, name, grade):
        if name in self.students:
            self.students[name].append(grade)
            print(f"Added grade {grade} for {name}")
        else:
            print(f"Student {name} not found")
    
    def get_average(self, name):
        if name in self.students and self.students[name]:
            avg = sum(self.students[name]) / len(self.students[name])
            return avg
        return None
    
    def get_class_average(self):
        if not self.students:
            return 0
        total = 0
        count = 0
        for grades in self.students.values():
            if grades:
                total += sum(grades)
                count += len(grades)
        return total / count if count > 0 else 0
    
    def get_student_summary(self):
        summary = {}
        for name, grades in self.students.items():
            if grades:
                avg = sum(grades) / len(grades)
                summary[name] = {
                    "grades": grades,
                    "average": avg,
                    "highest": max(grades),
                    "lowest": min(grades)
                }
            else:
                summary[name] = {"grades": [], "average": 0}
        return summary

# Test the grade book
gradebook = GradeBook()
gradebook.add_student("Alice")
gradebook.add_student("Bob")
gradebook.add_grade("Alice", 85)
gradebook.add_grade("Alice", 90)
gradebook.add_grade("Bob", 75)
gradebook.add_grade("Bob", 80)

print(f"\nAlice's average: {gradebook.get_average('Alice')}")
print(f"Class average: {gradebook.get_class_average():.2f}")
print(f"Student summary: {gradebook.get_student_summary()}")

# 📚 WHAT WE LEARNED:
# 1. Creating and accessing dictionaries
# 2. Adding and updating key-value pairs
# 3. Removing items (del, pop, popitem)
# 4. Dictionary methods (keys, values, items)
# 5. Checking membership
# 6. Dictionary comprehensions
# 7. Nested dictionaries
# 8. defaultdict and Counter
# 9. Practical applications
# 10. Iterating over dictionaries

# 🎮 NEXT CHAPTER: Sets - Unique collections!