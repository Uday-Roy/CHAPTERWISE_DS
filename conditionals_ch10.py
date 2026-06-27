# ============================================
# CHAPTER 10: CONDITIONALS - MAKING DECISIONS
# ============================================
# 🎯 LEARNING OBJECTIVES:
# 1. Understanding if/elif/else statements
# 2. Boolean expressions and comparisons
# 3. Logical operators (and, or, not)
# 4. Ternary conditional operator
# 5. Nested conditionals
# 6. Practical applications
# ============================================

# 🎯 BASIC IF STATEMENT
age = 18
print(f"Age: {age}")

if age >= 18:
    print("You are an adult")
    print("You can vote")
    print("You can drive")

# 🎯 IF-ELSE STATEMENT
temperature = 25
print(f"\nTemperature: {temperature}°C")

if temperature > 30:
    print("It's hot outside")
else:
    print("It's pleasant outside")

# 🎯 IF-ELIF-ELSE STATEMENT
score = 85
print(f"\nScore: {score}")

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")

# 📊 COMPARISON OPERATORS
x = 10
y = 20

print(f"\nx = {x}, y = {y}")
print(f"x == y: {x == y}")  # Equal to
print(f"x != y: {x != y}")  # Not equal to
print(f"x > y: {x > y}")    # Greater than
print(f"x < y: {x < y}")    # Less than
print(f"x >= y: {x >= y}")  # Greater than or equal
print(f"x <= y: {x <= y}")  # Less than or equal

# 🔄 LOGICAL OPERATORS
age = 25
has_license = True

print(f"\nAge: {age}, Has License: {has_license}")

# AND - both must be True
if age >= 18 and has_license:
    print("You can drive")

# OR - at least one must be True
if age < 18 or has_license:
    print("You qualify for some driving privileges")

# NOT - reverses boolean
if not has_license:
    print("You need a license to drive")

# 🎯 TERNARY OPERATOR (Conditional Expression)
# Syntax: value_if_true if condition else value_if_false
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"\nAge: {age}, Status: {status}")

# Nesting ternary operators
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
print(f"Score: {score}, Grade: {grade}")

# 🔍 ADVANCED CONDITIONAL CHECKING
# Multiple conditions
def can_vote(age, citizenship, registration):
    """Check if person can vote"""
    return age >= 18 and citizenship and registration

# Check multiple conditions at once
def analyze_weather(temp, humidity, wind):
    """Analyze weather conditions"""
    print(f"\nWeather Analysis:")
    print(f"Temp: {temp}°C, Humidity: {humidity}%, Wind: {wind}km/h")
    
    if temp > 35 and humidity > 80:
        print("☀️ Extremely hot and humid - stay inside!")
    elif temp > 30:
        print("☀️ Hot day - stay hydrated!")
    elif temp > 20:
        print("🌤️ Pleasant weather")
    elif temp > 10:
        print("🌥️ Cool day")
    else:
        print("❄️ Cold day - dress warmly!")
    
    if wind > 50:
        print("💨 Very windy conditions!")
    elif wind > 30:
        print("💨 Windy")

analyze_weather(32, 85, 40)

# 🎯 SHORT-CIRCUIT EVALUATION
def expensive_check():
    print("Performing expensive check...")
    return True

# Python stops evaluating when result is determined
if False and expensive_check():
    print("This won't execute")
else:
    print("Short-circuited")

# 🎯 NESTED CONDITIONALS
def get_insurance_rate(age, driving_years, accidents):
    """Calculate insurance rate based on multiple conditions"""
    print(f"\nAge: {age}, Driving Years: {driving_years}, Accidents: {accidents}")
    
    if age < 18:
        return "Not eligible"
    else:
        if age < 25:
            if driving_years < 2:
                return "High rate"
            else:
                return "Medium-high rate"
        else:
            if accidents == 0:
                return "Low rate"
            elif accidents == 1:
                return "Medium rate"
            else:
                return "High rate"

print(f"Insurance rate: {get_insurance_rate(22, 1, 0)}")
print(f"Insurance rate: {get_insurance_rate(35, 10, 2)}")

# 📝 PRACTICAL EXAMPLES

# 1. Password validator
def validate_password(password):
    """Validate password strength"""
    print(f"\nValidating password: {password}")
    
    if len(password) < 8:
        return "Too short"
    
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)
    
    if all([has_upper, has_lower, has_digit, has_special]):
        return "Strong password"
    elif all([has_upper, has_lower, has_digit]):
        return "Medium password"
    else:
        return "Weak password"

passwords = ["password", "Password123", "Password123!"]
for pwd in passwords:
    print(f"  {pwd}: {validate_password(pwd)}")

# 2. Grade calculator with weight
def calculate_grade(homework, midterm, final):
    """Calculate weighted grade"""
    print(f"\nHomework: {homework}, Midterm: {midterm}, Final: {final}")
    
    total = (homework * 0.2) + (midterm * 0.3) + (final * 0.5)
    
    # Assign letter grade
    if total >= 90:
        letter = "A"
    elif total >= 80:
        letter = "B"
    elif total >= 70:
        letter = "C"
    elif total >= 60:
        letter = "D"
    else:
        letter = "F"
    
    # Check for grade boost
    if final >= 95 and letter in ["B", "C"]:
        letter = chr(ord(letter) - 1)  # Boost one letter
        print(f"⭐ Final exam bonus! New grade: {letter}")
    
    return f"{letter} ({total:.1f}%)"

print(f"Final grade: {calculate_grade(85, 78, 92)}")
print(f"Final grade: {calculate_grade(90, 85, 96)}")

# 3. Ticket pricing system
def get_ticket_price(age, is_student, is_senior_citizen=False):
    """Calculate ticket price based on multiple factors"""
    print(f"\nAge: {age}, Student: {is_student}, Senior: {is_senior_citizen}")
    
    if age < 5:
        price = 0
        category = "Free (Under 5)"
    elif is_student:
        price = 8
        category = "Student Discount"
    elif is_senior_citizen or age >= 65:
        price = 6
        category = "Senior Discount"
    elif age >= 18:
        price = 12
        category = "Adult"
    else:
        price = 8
        category = "Child (5-17)"
    
    return f"{category}: ${price}"

print(f"Ticket: {get_ticket_price(70, False)}")
print(f"Ticket: {get_ticket_price(20, True)}")
print(f"Ticket: {get_ticket_price(10, False)}")

# 🎯 CHALLENGE: Restaurant Order System
class OrderSystem:
    def __init__(self):
        self.menu = {
            "burger": 10,
            "pizza": 12,
            "pasta": 8,
            "salad": 6,
            "soda": 3,
            "coffee": 4
        }
    
    def place_order(self, items):
        """Process an order with multiple items"""
        print(f"\n📝 Order: {items}")
        
        if not items:
            return "No items ordered"
        
        total = 0
        order_details = []
        
        for item in items:
            if item in self.menu:
                total += self.menu[item]
                order_details.append(f"{item}: ${self.menu[item]}")
            else:
                return f"Invalid item: {item}"
        
        # Check for discounts
        discount = 0
        if "burger" in items and "soda" in items:
            discount = 2  # Combo discount
            order_details.append("Combo discount: -$2")
        
        if len(items) >= 4:
            discount += 1  # Bulk discount
        
        total -= discount
        
        # Delivery fee
        delivery_fee = 5 if total < 30 else 0
        
        return {
            "items": order_details,
            "subtotal": sum(self.menu[item] for item in items if item in self.menu),
            "discount": discount,
            "delivery_fee": delivery_fee,
            "total": total + delivery_fee
        }

order_system = OrderSystem()

# Test orders
print("\nOrder Results:")
orders = [
    ["burger", "soda"],
    ["pizza", "salad", "soda"],
    ["burger", "pizza", "pasta", "soda"]
]

for order in orders:
    result = order_system.place_order(order)
    print(f"\nOrder: {order}")
    for key, value in result.items():
        if key == "items":
            print("  Items:")
            for item in value:
                print(f"    {item}")
        else:
            print(f"  {key}: ${value}" if isinstance(value, (int, float)) else f"  {key}: {value}")

# 📚 WHAT WE LEARNED:
# 1. if/elif/else statements
# 2. Comparison operators
# 3. Logical operators (and, or, not)
# 4. Ternary conditional operator
# 5. Nested conditionals
# 6. Password validation
# 7. Grade calculation
# 8. Ticket pricing system
# 9. Order processing system
# 10. Short-circuit evaluation

# 🎮 NEXT CHAPTER: Loops - Repeating actions!