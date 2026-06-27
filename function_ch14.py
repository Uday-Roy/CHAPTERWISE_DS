# ============================================
# COMPLETE FUNCTIONS IN PYTHON - ALL CONCEPTS IN ONE FILE
# ============================================
# 🎯 LEARNING OBJECTIVES:
# 1. Function Definition and Calling
# 2. Parameters and Arguments
# 3. Return Values
# 4. Scope and Lifetime
# 5. Default Parameters
# 6. Keyword Arguments
# 7. Variable-Length Arguments (*args, **kwargs)
# 8. Lambda Functions
# 9. Decorators
# 10. Generators
# 11. Recursion
# 12. Function Annotations
# 13. Functional Programming Tools
# 14. Practical Applications
# ============================================

import functools
import time
from typing import List, Dict, Any, Optional, Callable, Union
from functools import wraps, lru_cache, reduce
from collections import Counter

# ============================================
# 1. BASIC FUNCTION DEFINITION
# ============================================

print("=" * 60)
print("🎯 BASIC FUNCTIONS")
print("=" * 60)

# 1.1 Simple function
print("\n🔹 1.1 Simple Function")
print("-" * 40)

def greet():
    """Simple greeting function"""
    print("  Hello, World!")

greet()

# 1.2 Function with parameters
print("\n🔹 1.2 Function with Parameters")
print("-" * 40)

def greet_person(name):
    """Greet a specific person"""
    print(f"  Hello, {name}!")

greet_person("Alice")
greet_person("Bob")

# 1.3 Function with return value
print("\n🔹 1.3 Function with Return Value")
print("-" * 40)

def add(a, b):
    """Add two numbers and return result"""
    return a + b

result = add(5, 3)
print(f"  5 + 3 = {result}")

# 1.4 Multiple return values
print("\n🔹 1.4 Multiple Return Values")
print("-" * 40)

def get_min_max(numbers):
    """Return min and max from a list"""
    return min(numbers), max(numbers)

min_val, max_val = get_min_max([5, 2, 8, 1, 9])
print(f"  Min: {min_val}, Max: {max_val}")

# ============================================
# 2. PARAMETERS AND ARGUMENTS
# ============================================

print("\n" + "=" * 60)
print("📝 PARAMETERS AND ARGUMENTS")
print("=" * 60)

# 2.1 Default parameters
print("\n🔹 2.1 Default Parameters")
print("-" * 40)

def greet_with_title(name, title="Mr."):
    """Greet with optional title"""
    print(f"  Hello, {title} {name}")

greet_with_title("Smith")
greet_with_title("Johnson", "Dr.")

# 2.2 Keyword arguments
print("\n🔹 2.2 Keyword Arguments")
print("-" * 40)

def create_profile(name, age, city, job):
    """Create a profile with keyword arguments"""
    print(f"  Profile: {name}, {age}, from {city}, works as {job}")

create_profile(name="Alice", age=25, city="New York", job="Developer")
create_profile("Bob", 30, "Boston", "Designer")  # Positional works too

# 2.3 Required vs optional parameters
print("\n🔹 2.3 Required vs Optional Parameters")
print("-" * 40)

def describe_person(name, age, city="Unknown", country="USA"):
    """Required and optional parameters"""
    print(f"  {name} is {age} years old from {city}, {country}")

describe_person("Alice", 25)
describe_person("Bob", 30, "London", "UK")

# ============================================
# 3. VARIABLE-LENGTH ARGUMENTS
# ============================================

print("\n" + "=" * 60)
print("🔢 VARIABLE-LENGTH ARGUMENTS")
print("=" * 60)

# 3.1 *args (positional variable arguments)
print("\n🔹 3.1 *args - Positional Variable Arguments")
print("-" * 40)

def sum_all(*args):
    """Sum any number of arguments"""
    total = 0
    for num in args:
        total += num
    return total

print(f"  Sum of 1,2,3: {sum_all(1, 2, 3)}")
print(f"  Sum of 1,2,3,4,5: {sum_all(1, 2, 3, 4, 5)}")
print(f"  Sum of nothing: {sum_all()}")

def print_info(*args):
    """Print any number of arguments"""
    print("  Arguments received:")
    for i, arg in enumerate(args):
        print(f"    {i+1}: {arg}")

print_info("Alice", 25, "Developer", True)

# 3.2 **kwargs (keyword variable arguments)
print("\n🔹 3.2 **kwargs - Keyword Variable Arguments")
print("-" * 40)

def print_dict(**kwargs):
    """Print any number of keyword arguments"""
    print("  Keyword arguments:")
    for key, value in kwargs.items():
        print(f"    {key}: {value}")

print_dict(name="Alice", age=25, city="New York", job="Developer")

# 3.3 Combining *args and **kwargs
print("\n🔹 3.3 Combining *args and **kwargs")
print("-" * 40)

def versatile_function(required, *args, **kwargs):
    """Function with required, *args, and **kwargs"""
    print(f"  Required: {required}")
    print(f"  Args: {args}")
    print(f"  Kwargs: {kwargs}")

versatile_function("Hello", 1, 2, 3, name="Alice", age=25)

# ============================================
# 4. SCOPE AND LIFETIME
# ============================================

print("\n" + "=" * 60)
print("🔍 SCOPE AND LIFETIME")
print("=" * 60)

# 4.1 Global vs Local variables
print("\n🔹 4.1 Global vs Local Variables")
print("-" * 40)

global_var = "I'm global"

def scope_demo():
    local_var = "I'm local"
    print(f"  Inside function - local: {local_var}")
    print(f"  Inside function - global: {global_var}")

scope_demo()
print(f"  Outside function - global: {global_var}")

# 4.2 Modifying global variables
print("\n🔹 4.2 Modifying Global Variables")
print("-" * 40)

counter = 0

def increment_counter():
    global counter
    counter += 1
    print(f"  Counter: {counter}")

increment_counter()
increment_counter()
increment_counter()

# 4.3 Nonlocal variables (nested functions)
print("\n🔹 4.3 Nonlocal Variables")
print("-" * 40)

def outer_function():
    message = "Hello"
    
    def inner_function():
        nonlocal message
        message += " World!"
        print(f"  Inside inner: {message}")
    
    inner_function()
    print(f"  After inner call: {message}")

outer_function()

# ============================================
# 5. LAMBDA FUNCTIONS
# ============================================

print("\n" + "=" * 60)
print("λ LAMBDA FUNCTIONS")
print("=" * 60)

# 5.1 Basic lambda
print("\n🔹 5.1 Basic Lambda")
print("-" * 40)

square = lambda x: x ** 2
print(f"  Square of 5: {square(5)}")

add = lambda x, y: x + y
print(f"  Add: {add(3, 4)}")

# 5.2 Lambda with map
print("\n🔹 5.2 Lambda with Map")
print("-" * 40)

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"  Original: {numbers}")
print(f"  Squared: {squared}")

# 5.3 Lambda with filter
print("\n🔹 5.3 Lambda with Filter")
print("-" * 40)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(f"  Original: {numbers}")
print(f"  Even numbers: {even}")

# 5.4 Lambda with sort
print("\n🔹 5.4 Lambda with Sort")
print("-" * 40)

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 22}
]

people.sort(key=lambda x: x["age"])
print("  Sorted by age:")
for person in people:
    print(f"    {person['name']}: {person['age']}")

# ============================================
# 6. DECORATORS
# ============================================

print("\n" + "=" * 60)
print("🎨 DECORATORS")
print("=" * 60)

# 6.1 Basic decorator
print("\n🔹 6.1 Basic Decorator")
print("-" * 40)

def timer_decorator(func):
    """Decorator that times function execution"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"  {func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(0.1)
    return "Done"

result = slow_function()
print(f"  Result: {result}")

# 6.2 Logging decorator
print("\n🔹 6.2 Logging Decorator")
print("-" * 40)

def logger_decorator(func):
    """Decorator that logs function calls"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"  {func.__name__} returned {result}")
        return result
    return wrapper

@logger_decorator
def multiply(a, b):
    return a * b

multiply(3, 4)

# 6.3 Decorator with parameters
print("\n🔹 6.3 Decorator with Parameters")
print("-" * 40)

def repeat(n):
    """Decorator that repeats function n times"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for i in range(n):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):
    return f"Hello, {name}!"

results = say_hello("Alice")
print(f"  Results: {results}")

# 6.4 Multiple decorators
print("\n🔹 6.4 Multiple Decorators")
print("-" * 40)

@timer_decorator
@logger_decorator
def complex_calculation(x, y):
    time.sleep(0.05)
    return x ** y

result = complex_calculation(2, 8)
print(f"  Result: {result}")

# ============================================
# 7. GENERATORS
# ============================================

print("\n" + "=" * 60)
print("🔧 GENERATORS")
print("=" * 60)

# 7.1 Generator function
print("\n🔹 7.1 Generator Function")
print("-" * 40)

def count_up_to(n):
    """Generator that counts from 1 to n"""
    print("  Starting generator...")
    for i in range(1, n + 1):
        print(f"  Yielding {i}")
        yield i

print("Creating generator:")
gen = count_up_to(3)
print("Getting values:")
for value in gen:
    print(f"  Received: {value}")

# 7.2 Infinite generator
print("\n🔹 7.2 Infinite Generator")
print("-" * 40)

def fibonacci():
    """Infinite Fibonacci generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print("First 10 Fibonacci numbers:")
fib = fibonacci()
for i in range(10):
    print(f"  {i+1}: {next(fib)}")

# 7.3 Generator expression
print("\n🔹 7.3 Generator Expression")
print("-" * 40)

# List comprehension (creates full list)
squares_list = [x**2 for x in range(1000000)]

# Generator expression (memory efficient)
squares_gen = (x**2 for x in range(1000000))

print(f"  List memory: more memory")
print(f"  Generator memory: less memory")
print("  Both produce the same values")

# ============================================
# 8. RECURSION
# ============================================

print("\n" + "=" * 60)
print("🔄 RECURSION")
print("=" * 60)

# 8.1 Factorial (recursive)
print("\n🔹 8.1 Factorial - Recursive")
print("-" * 40)

def factorial(n):
    """Calculate factorial recursively"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"  Factorial of 5: {factorial(5)}")
print(f"  Factorial of 10: {factorial(10)}")

# 8.2 Fibonacci (recursive with memoization)
print("\n🔹 8.2 Fibonacci with Memoization")
print("-" * 40)

@lru_cache(maxsize=None)
def fibonacci_memo(n):
    """Fibonacci with memoization"""
    if n <= 1:
        return n
    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)

print("  Fibonacci with memoization:")
for i in range(10):
    print(f"    Fib({i}) = {fibonacci_memo(i)}")

# 8.3 Binary search (recursive)
print("\n🔹 8.3 Binary Search - Recursive")
print("-" * 40)

def binary_search(arr, target, left=0, right=None):
    """Binary search using recursion"""
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)

sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
print(f"  Array: {sorted_array}")
print(f"  Find 7: position {binary_search(sorted_array, 7)}")
print(f"  Find 12: position {binary_search(sorted_array, 12)}")

# ============================================
# 9. FUNCTION ANNOTATIONS
# ============================================

print("\n" + "=" * 60)
print("📝 FUNCTION ANNOTATIONS")
print("=" * 60)

# 9.1 Type annotations
print("\n🔹 9.1 Type Annotations")
print("-" * 40)

def calculate_average(numbers: List[float]) -> float:
    """Calculate average with type annotations"""
    return sum(numbers) / len(numbers)

result = calculate_average([1.0, 2.0, 3.0, 4.0])
print(f"  Average: {result}")

# 9.2 Complex annotations
print("\n🔹 9.2 Complex Annotations")
print("-" * 40)

def process_data(data: Dict[str, Any]) -> Optional[List[Dict[str, Union[str, int]]]]:
    """Process data with complex annotations"""
    if not data:
        return None
    return [{"key": k, "value": v} for k, v in data.items()]

data = {"name": "Alice", "age": 25}
result = process_data(data)
print(f"  Result: {result}")

# ============================================
# 10. FUNCTIONAL PROGRAMMING TOOLS
# ============================================

print("\n" + "=" * 60)
print("🧰 FUNCTIONAL PROGRAMMING TOOLS")
print("=" * 60)

# 10.1 Map
print("\n🔹 10.1 Map")
print("-" * 40)

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(f"  Original: {numbers}")
print(f"  Doubled: {doubled}")

# 10.2 Filter
print("\n🔹 10.2 Filter")
print("-" * 40)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(f"  Original: {numbers}")
print(f"  Even: {even}")

# 10.3 Reduce
print("\n🔹 10.3 Reduce")
print("-" * 40)

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(f"  Product of {numbers} = {product}")

# 10.4 Partial
print("\n🔹 10.4 Partial - Pre-filling Arguments")
print("-" * 40)

def power(base, exponent):
    return base ** exponent

square = functools.partial(power, exponent=2)
cube = functools.partial(power, exponent=3)

print(f"  Square of 5: {square(5)}")
print(f"  Cube of 3: {cube(3)}")

# ============================================
# 11. DOCUMENTATION AND BEST PRACTICES
# ============================================

print("\n" + "=" * 60)
print("📚 DOCUMENTATION AND BEST PRACTICES")
print("=" * 60)

# 11.1 Docstrings
print("\n🔹 11.1 Docstrings")
print("-" * 40)

def calculate_area(shape: str, *dimensions: float) -> float:
    """
    Calculate area of different shapes.
    
    Args:
        shape: Shape type ('rectangle', 'circle', 'triangle')
        *dimensions: Dimensions needed for the shape
            - Rectangle: length, width
            - Circle: radius
            - Triangle: base, height
    
    Returns:
        float: Area of the shape
    
    Examples:
        >>> calculate_area('rectangle', 5, 3)
        15.0
        >>> calculate_area('circle', 3)
        28.274333882308138
    """
    import math
    
    if shape.lower() == 'rectangle':
        if len(dimensions) != 2:
            raise ValueError("Rectangle needs length and width")
        return dimensions[0] * dimensions[1]
    
    elif shape.lower() == 'circle':
        if len(dimensions) != 1:
            raise ValueError("Circle needs radius")
        return math.pi * dimensions[0] ** 2
    
    elif shape.lower() == 'triangle':
        if len(dimensions) != 2:
            raise ValueError("Triangle needs base and height")
        return 0.5 * dimensions[0] * dimensions[1]
    
    else:
        raise ValueError(f"Unsupported shape: {shape}")

# Print docstring
print("  Function docstring:")
print(f"  {calculate_area.__doc__}")

# 11.2 Function signatures
print("\n🔹 11.2 Function Signatures")
print("-" * 40)

def demonstrate_signature():
    """Demonstrate function signatures"""
    print(f"  Function name: {calculate_area.__name__}")
    print(f"  Defaults: {calculate_area.__defaults__}")
    print(f"  Annotations: {calculate_area.__annotations__}")

demonstrate_signature()

# ============================================
# 12. PRACTICAL APPLICATIONS
# ============================================

print("\n" + "=" * 60)
print("🎯 PRACTICAL APPLICATIONS")
print("=" * 60)

# 12.1 Decorator-based cache
print("\n🔹 12.1 Caching with Decorators")
print("-" * 40)

def cache_result(func):
    """Decorator that caches function results"""
    cache = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in cache:
            print(f"  Computing result for {func.__name__}{args}")
            cache[key] = func(*args, **kwargs)
        else:
            print(f"  Returning cached result for {func.__name__}{args}")
        return cache[key]
    
    return wrapper

@cache_result
def expensive_calculation(n):
    """Simulate expensive calculation"""
    time.sleep(0.1)
    return n ** 2

print("First call:")
result1 = expensive_calculation(5)
print("Second call:")
result2 = expensive_calculation(5)

# 12.2 Factory function
print("\n🔹 12.2 Factory Function")
print("-" * 40)

def create_calculator(operation):
    """Factory function that creates calculator functions"""
    
    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    def multiply(a, b):
        return a * b
    
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    
    return operations.get(operation)

calc = create_calculator('multiply')
print(f"  Multiplication: {calc(4, 5)}")

# 12.3 Data validator
print("\n🔹 12.3 Data Validator")
print("-" * 40)

def create_validator(valid_types, required_fields):
    """Create a data validator function"""
    
    def validate(data):
        """Validate data against requirements"""
        errors = []
        
        # Check required fields
        for field in required_fields:
            if field not in data:
                errors.append(f"Missing required field: {field}")
        
        # Check types
        for field, value in data.items():
            if field in valid_types:
                expected_type = valid_types[field]
                if not isinstance(value, expected_type):
                    errors.append(
                        f"Field '{field}' should be {expected_type.__name__}, "
                        f"got {type(value).__name__}"
                    )
        
        return len(errors) == 0, errors
    
    return validate

# Create a validator
user_validator = create_validator(
    valid_types={'name': str, 'age': int, 'email': str},
    required_fields=['name', 'email']
)

# Test validation
valid_data = {'name': 'Alice', 'age': 25, 'email': 'alice@email.com'}
invalid_data = {'name': 'Bob', 'age': '25', 'city': 'NY'}

print("Valid data:")
is_valid, errors = user_validator(valid_data)
print(f"  Valid: {is_valid}, Errors: {errors}")

print("\nInvalid data:")
is_valid, errors = user_validator(invalid_data)
print(f"  Valid: {is_valid}, Errors: {errors}")

# 12.4 Pipeline processing
print("\n🔹 12.4 Pipeline Processing")
print("-" * 40)

def create_pipeline(*functions):
    """Create a data processing pipeline"""
    
    def process(data):
        """Process data through all functions"""
        result = data
        for func in functions:
            result = func(result)
        return result
    
    return process

# Create pipeline functions
def clean_data(data):
    return [x.strip() for x in data if x.strip()]

def uppercase_data(data):
    return [x.upper() for x in data]

def filter_short_words(data):
    return [x for x in data if len(x) > 3]

# Create pipeline
pipeline = create_pipeline(clean_data, uppercase_data, filter_short_words)

# Test pipeline
input_data = ["apple", "", "banana", "  cherry  ", "cat", "  date  "]
result = pipeline(input_data)
print(f"  Input: {input_data}")
print(f"  Result: {result}")

# 12.5 Timer utility
print("\n🔹 12.5 Timer Utility")
print("-" * 40)

def timer_context(func):
    """Decorator that times function execution"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f"  {func.__name__} executed in {duration:.4f} seconds")
        return result
    return wrapper

@timer_context
def process_data(data):
    """Process some data"""
    result = []
    for item in data:
        result.append(item ** 2)
    time.sleep(0.01)  # Simulate processing
    return result

numbers = list(range(1000))
result = process_data(numbers)
print(f"  Processed {len(result)} items")

# ============================================
# 13. SUMMARY AND CHEAT SHEET
# ============================================

print("\n" + "=" * 60)
print("📚 FUNCTION CHEAT SHEET")
print("=" * 60)

print("""
🔹 BASIC FUNCTIONS:
  def function_name():              # Define function
  def function_name(param1, param2): # With parameters
  def function_name() -> return_type: # With return type
  return value                      # Return value

🔹 PARAMETERS:
  def func(a, b):                    # Required parameters
  def func(a, b=default):            # Default parameters
  func(a=1, b=2)                     # Keyword arguments
  
🔹 VARIABLE ARGUMENTS:
  def func(*args):                   # Variable positional
  def func(**kwargs):                # Variable keyword
  def func(a, *args, **kwargs):      # Combined

🔹 SCOPES:
  global variable                     # Use global variable
  nonlocal variable                   # Use enclosing scope variable

🔹 LAMBDA:
  lambda x: x**2                      # Simple lambda
  lambda x, y: x + y                  # Multiple parameters

🔹 DECORATORS:
  @decorator                          # Apply decorator
  def func():...
  def decorator(func):                # Define decorator
      def wrapper(*args, **kwargs):...
      return wrapper

🔹 GENERATORS:
  def generator():                    # Generator function
      yield value                     # Yield value
  gen = (x**2 for x in range(10))     # Generator expression

🔹 FUNCTIONAL TOOLS:
  map(func, iterable)                 # Apply function
  filter(func, iterable)              # Filter items
  reduce(func, iterable)              # Reduce items
  functools.partial(func, arg)        # Partial application

🔹 BEST PRACTICES:
  ✓ Use descriptive function names
  ✓ Write docstrings
  ✓ Use type annotations
  ✓ Keep functions small and focused
  ✓ Don't use mutable default arguments
  ✓ Return early when possible
  ✓ Use error handling
  ✓ Test functions thoroughly
""")

print("=" * 60)
print("🎉 FUNCTION MASTERY COMPLETE!")
print("=" * 60)