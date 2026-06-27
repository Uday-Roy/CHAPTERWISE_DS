# ============================================
# CHAPTER 4: STRINGS - TEXT MANIPULATION MASTERY
# ============================================
# 🎯 LEARNING OBJECTIVES:
# 1. String creation and formatting
# 2. String methods and operations
# 3. String slicing
# 4. String formatting (f-strings, .format())
# 5. String manipulation techniques
# ============================================

# 📝 STRING CREATION - Different ways to create strings
single_quotes = 'Hello'
double_quotes = "World"
triple_quotes = """This is a
multi-line string
with multiple lines"""
triple_single = '''Also works
with single quotes'''

print("Single quotes:", single_quotes)
print("Double quotes:", double_quotes)
print("Triple quotes:", triple_quotes)
print("Triple single:", triple_single)

# 🎯 STRING CONCATENATION - Combining strings
first = "Python"
second = "Programming"
combined = first + " " + second
print(f"Combined: {combined}")

# 🎨 STRING REPETITION
laugh = "ha" * 3
print(f"Laugh: {laugh}")  # Output: hahaha

# ✨ STRING SLICING - Getting parts of strings
text = "Python Programming"
print(f"Original: {text}")
print(f"First 6 characters: {text[:6]}")  # Python
print(f"From index 7: {text[7:]}")  # Programming
print(f"Characters 0-5: {text[0:6]}")  # Python
print(f"Last 6 characters: {text[-6:]}")  # mming

# 🎭 STRING METHODS - The Swiss Army Knife!
text = "  Hello, Python World!  "

# Case conversion
print(f"Lowercase: {text.lower()}")
print(f"Uppercase: {text.upper()}")
print(f"Title case: {text.title()}")
print(f"Capitalized: {text.capitalize()}")
print(f"Swap case: {text.swapcase()}")

# Stripping whitespace
print(f"Stripped: {text.strip()}")  # Removes leading/trailing spaces
print(f"Left strip: {text.lstrip()}")
print(f"Right strip: {text.rstrip()}")

# Finding and replacing
print(f"Find 'Python': {text.find('Python')}")
print(f"Find 'Java': {text.find('Java')}")  # Returns -1 if not found
print(f"Replace: {text.replace('Python', 'Java')}")

# Splitting and joining
words = text.split()  # Split by whitespace
print(f"Split into words: {words}")
print(f"Join with dashes: {'-'.join(words)}")

# Checking content
print(f"Starts with 'Hello': {text.startswith('Hello')}")
print(f"Ends with '!': {text.endswith('!')}")
print(f"Is alphanumeric: {text.isalnum()}")
print(f"Is alpha: {text.isalpha()}")
print(f"Is digit: {'123'.isdigit()}")
print(f"Is space: {'   '.isspace()}")

# 🚀 ADVANCED STRING MANIPULATION
sentence = "The quick brown fox jumps over the lazy dog"

# Counting occurrences
print(f"Count of 'the': {sentence.lower().count('the')}")

# Finding all positions of a character
def find_all(text, char):
    """Find all positions of a character in string"""
    return [i for i, c in enumerate(text) if c == char]

print(f"Positions of 'o': {find_all(sentence, 'o')}")

# 🎨 STRING FORMATTING - Modern ways to create formatted strings

# Method 1: f-strings (Python 3.6+) - RECOMMENDED!
name = "Alice"
age = 25
height = 1.75
print(f"Name: {name}, Age: {age}, Height: {height:.2f}m")

# Method 2: .format() method
print("Name: {}, Age: {}, Height: {:.2f}m".format(name, age, height))

# Method 3: % formatting (older style)
print("Name: %s, Age: %d, Height: %.2fm" % (name, age, height))

# 🎯 ADVANCED FORMATTING
# Padding and alignment
print(f"|{'left':<10}|")  # Left aligned
print(f"|{'center':^10}|")  # Center aligned
print(f"|{'right':>10}|")  # Right aligned

# Number formatting
pi = 3.14159265
print(f"Pi to 2 decimals: {pi:.2f}")
print(f"Pi with comma: {pi:,.2f}")
print(f"Pi in scientific: {pi:.2e}")
print(f"Pi as percentage: {pi:.2%}")

# 💡 STRING MANIPULATION TECHNIQUES

# 1. Reversing a string
text = "Python"
reversed_text = text[::-1]
print(f"Reversed: {reversed_text}")

# 2. Checking if string is palindrome
def is_palindrome(text):
    """Check if a string is a palindrome"""
    text = text.lower().replace(" ", "")
    return text == text[::-1]

print(f"Is 'radar' palindrome? {is_palindrome('radar')}")
print(f"Is 'Python' palindrome? {is_palindrome('Python')}")

# 3. Counting vowels and consonants
def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    v_count = sum(1 for char in text if char in vowels)
    c_count = sum(1 for char in text if char.isalpha() and char not in vowels)
    return v_count, c_count

v, c = count_vowels_consonants("Hello World")
print(f"Vowels: {v}, Consonants: {c}")

# 4. Removing punctuation
import string
def remove_punctuation(text):
    return ''.join(char for char in text if char not in string.punctuation)

print(f"Without punctuation: {remove_punctuation('Hello, World!')}")

# 5. Word count
def word_count(text):
    return len(text.split())

print(f"Word count: {word_count('The quick brown fox')}")

# 📝 ESCAPE SEQUENCES REFRESHER
print("Line 1\nLine 2")  # New line
print("Tab\tSpace")  # Tab
print("Backslash: \\")  # Backslash
print("Single quote: \'")  # Single quote
print("Double quote: \"")  # Double quote

# 🧪 STRING COMPARISON
str1 = "Hello"
str2 = "Hello"
str3 = "hello"

print(f"str1 == str2: {str1 == str2}")  # True
print(f"str1 == str3: {str1 == str3}")  # False (case sensitive)
print(f"str1.lower() == str3.lower(): {str1.lower() == str3.lower()}")  # True

# 🎯 CHALLENGE: Text Analyzer
def analyze_text(text):
    """Complete text analysis"""
    print(f"Original: {text}")
    print(f"Length: {len(text)}")
    print(f"Words: {len(text.split())}")
    print(f"Characters (without spaces): {len(text.replace(' ', ''))}")
    
    # Count specific characters
    vowels = "aeiouAEIOU"
    vowels_count = sum(1 for char in text if char in vowels)
    consonants_count = sum(1 for char in text if char.isalpha() and char not in vowels)
    digits_count = sum(1 for char in text if char.isdigit())
    spaces_count = sum(1 for char in text if char.isspace())
    
    print(f"Vowels: {vowels_count}")
    print(f"Consonants: {consonants_count}")
    print(f"Digits: {digits_count}")
    print(f"Spaces: {spaces_count}")
    
    # Frequency analysis
    from collections import Counter
    freq = Counter(text.lower())
    print(f"Most common characters: {freq.most_common(3)}")

# Test the analyzer
analyze_text("Hello World 123! Python is awesome.")

# 📚 WHAT WE LEARNED:
# 1. String creation and concatenation
# 2. String slicing and indexing
# 3. String methods (lower, upper, strip, split, join)
# 4. String formatting (f-strings, .format(), %)
# 5. Advanced string manipulation
# 6. Palindrome checking
# 7. Text analysis techniques
# 8. Character counting and frequency

# 🎮 NEXT CHAPTER: Numbers - Mathematical operations!