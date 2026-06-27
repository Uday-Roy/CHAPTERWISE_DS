# ============================================
# COMPLETE OOP IN PYTHON - ALL CONCEPTS IN ONE FILE
# ============================================
# 🎯 LEARNING OBJECTIVES:
# 1. Classes and Objects
# 2. Constructors (__init__) and Destructors
# 3. Instance Methods, Class Methods, Static Methods
# 4. Instance Variables, Class Variables
# 5. Inheritance (Single, Multiple, Multilevel)
# 6. Encapsulation (Private, Protected)
# 7. Polymorphism (Method Overriding, Overloading)
# 8. Magic Methods (Dunder Methods)
# 9. Property Decorators (Getters, Setters, Deleters)
# 10. Abstract Classes and Methods
# 11. Composition and Aggregation
# 12. Method Resolution Order (MRO)
# ============================================

import abc
from abc import ABC, abstractmethod
from datetime import datetime

# ============================================
# 1. BASIC CLASS AND OBJECT
# ============================================

class Car:
    """A simple Car class demonstrating basic OOP concepts"""
    
    # Class Variable - shared across all instances
    vehicle_type = "Automobile"
    total_cars = 0
    
    def __init__(self, brand, model, year, color="White"):
        """Constructor - called when object is created"""
        # Instance Variables - unique to each instance
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0
        self.is_running = False
        
        # Increment class variable
        Car.total_cars += 1
        
        print(f"🚗 Created {self.brand} {self.model} ({self.year})")
    
    def __del__(self):
        """Destructor - called when object is destroyed"""
        Car.total_cars -= 1
        print(f"🗑️ Destroyed {self.brand} {self.model}")
    
    # Instance Method
    def start(self):
        """Start the car"""
        if not self.is_running:
            self.is_running = True
            print(f"🚀 {self.brand} {self.model} started!")
            return True
        print(f"⚠️ {self.brand} {self.model} is already running")
        return False
    
    def stop(self):
        """Stop the car"""
        if self.is_running:
            self.is_running = False
            self.speed = 0
            print(f"🛑 {self.brand} {self.model} stopped!")
            return True
        print(f"⚠️ {self.brand} {self.model} is already stopped")
        return False
    
    def accelerate(self, amount=10):
        """Accelerate the car"""
        if self.is_running:
            self.speed += amount
            print(f"⚡ {self.brand} {self.model} accelerated to {self.speed} km/h")
            return self.speed
        print(f"⚠️ Cannot accelerate - car is not running")
        return 0
    
    def brake(self, amount=5):
        """Apply brakes"""
        if self.is_running and self.speed > 0:
            self.speed = max(0, self.speed - amount)
            print(f"🛑 {self.brand} {self.model} slowed to {self.speed} km/h")
            return self.speed
        return 0
    
    def get_info(self):
        """Get car information"""
        return f"{self.brand} {self.model} ({self.year}) - {self.color} - {self.speed} km/h"
    
    # Class Method - works with class variables
    @classmethod
    def get_total_cars(cls):
        """Get total number of cars created"""
        return f"Total cars: {cls.total_cars}"
    
    @classmethod
    def create_from_string(cls, car_string):
        """Alternative constructor - create car from string"""
        brand, model, year, color = car_string.split(',')
        return cls(brand.strip(), model.strip(), int(year), color.strip())
    
    # Static Method - doesn't depend on class or instance
    @staticmethod
    def is_valid_year(year):
        """Check if year is valid"""
        current_year = datetime.now().year
        return 1900 <= year <= current_year
    
    # Magic Methods
    def __str__(self):
        """String representation for users"""
        return f"{self.brand} {self.model} ({self.year})"
    
    def __repr__(self):
        """String representation for developers"""
        return f"Car('{self.brand}', '{self.model}', {self.year}, '{self.color}')"
    
    def __eq__(self, other):
        """Equality comparison"""
        if not isinstance(other, Car):
            return False
        return self.brand == other.brand and self.model == other.model
    
    def __lt__(self, other):
        """Less than comparison (for sorting)"""
        if not isinstance(other, Car):
            return NotImplemented
        return self.year < other.year
    
    def __len__(self):
        """Length of car name"""
        return len(f"{self.brand} {self.model}")

# ============================================
# 2. ENCAPSULATION - Private and Protected Members
# ============================================

class BankAccount:
    """Bank Account with encapsulation"""
    
    def __init__(self, account_number, owner, initial_balance=0):
        self.account_number = account_number
        self.owner = owner
        self.__balance = initial_balance  # Private variable (name mangling)
        self._transaction_history = []  # Protected variable (convention)
        self.__pin = "1234"  # Private
    
    # Getter method
    def get_balance(self):
        """Get balance with authentication"""
        if self.__authenticate():
            return self.__balance
        return None
    
    # Setter method
    def deposit(self, amount):
        """Deposit money"""
        if amount > 0:
            self.__balance += amount
            self._transaction_history.append(f"Deposited: ${amount}")
            print(f"💰 Deposited ${amount}. New balance: ${self.__balance}")
            return True
        print("❌ Invalid deposit amount")
        return False
    
    def withdraw(self, amount):
        """Withdraw money"""
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self._transaction_history.append(f"Withdrew: ${amount}")
            print(f"💵 Withdrew ${amount}. New balance: ${self.__balance}")
            return True
        print("❌ Insufficient balance or invalid amount")
        return False
    
    def get_transaction_history(self):
        """Get transaction history"""
        return self._transaction_history.copy()  # Return copy to prevent modification
    
    def change_pin(self, old_pin, new_pin):
        """Change PIN with verification"""
        if old_pin == self.__pin:
            self.__pin = new_pin
            print("✅ PIN changed successfully")
            return True
        print("❌ Incorrect old PIN")
        return False
    
    def __authenticate(self):
        """Private authentication method"""
        # In real app, this would have proper authentication
        return True
    
    # Property decorator - getter
    @property
    def owner(self):
        """Get owner name"""
        return self._owner
    
    # Property decorator - setter
    @owner.setter
    def owner(self, name):
        """Set owner name with validation"""
        if name and len(name.strip()) > 0:
            self._owner = name.strip()
        else:
            raise ValueError("Owner name cannot be empty")
    
    @property
    def balance(self):
        """Get balance using property"""
        return self.__balance if self.__authenticate() else None
    
    @balance.setter
    def balance(self, amount):
        """Set balance directly (careful!)"""
        raise AttributeError("Use deposit() or withdraw() methods to modify balance")
    
    @balance.deleter
    def balance(self):
        """Delete balance (for security)"""
        del self.__balance

# ============================================
# 3. INHERITANCE - Single, Multilevel, Multiple
# ============================================

# 3.1 SINGLE INHERITANCE
class Vehicle:
    """Base class for all vehicles"""
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_moving = False
    
    def start(self):
        """Start the vehicle"""
        self.is_moving = True
        print(f"🚀 {self.brand} {self.model} started")
    
    def stop(self):
        """Stop the vehicle"""
        self.is_moving = False
        print(f"🛑 {self.brand} {self.model} stopped")
    
    def info(self):
        """Vehicle information"""
        return f"{self.brand} {self.model} ({self.year})"

# 3.2 MULTILEVEL INHERITANCE
class ElectricVehicle(Vehicle):
    """Electric vehicle - extends Vehicle"""
    
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity
        self.battery_level = 100
    
    def charge(self, amount=100):
        """Charge the battery"""
        self.battery_level = min(100, self.battery_level + amount)
        print(f"🔋 Battery charged to {self.battery_level}%")
    
    def start(self):
        """Override start method"""
        if self.battery_level > 10:
            super().start()
            print(f"⚡ {self.brand} {self.model} running on electric power")
        else:
            print(f"❌ Battery too low to start")

class Tesla(ElectricVehicle):
    """Tesla - specific electric vehicle"""
    
    def __init__(self, model, year, battery_capacity, autopilot=True):
        super().__init__("Tesla", model, year, battery_capacity)
        self.autopilot = autopilot
        self.__software_version = "v11.0"
    
    def autopilot_drive(self):
        """Engage autopilot"""
        if self.autopilot and self.is_moving:
            print(f"🤖 Autopilot engaged on {self.brand} {self.model}")
        else:
            print("❌ Autopilot not available or vehicle not moving")
    
    def update_software(self, version):
        """Update software"""
        self.__software_version = version
        print(f"🔄 Software updated to {version}")
    
    def info(self):
        """Override info method"""
        base_info = super().info()
        return f"{base_info} - Tesla {self.__software_version}"

# 3.3 MULTIPLE INHERITANCE
class GPS:
    """GPS functionality"""
    
    def __init__(self):
        self.location = "Unknown"
        self.satellites = 0
    
    def get_location(self):
        """Get current location"""
        return self.location
    
    def update_location(self, location):
        """Update location"""
        self.location = location
        print(f"📍 Location updated to {location}")
    
    def set_satellites(self, count):
        """Set number of satellites"""
        self.satellites = count
        print(f"🛰️ Connected to {count} satellites")

class Entertainment:
    """Entertainment system"""
    
    def __init__(self):
        self.is_on = False
        self.current_track = "No music"
    
    def play_music(self, track):
        """Play music"""
        self.current_track = track
        self.is_on = True
        print(f"🎵 Playing: {track}")
    
    def stop_music(self):
        """Stop music"""
        self.is_on = False
        print("🎵 Music stopped")

class SmartCar(Vehicle, GPS, Entertainment):
    """Smart car with multiple inheritance"""
    
    def __init__(self, brand, model, year):
        # Call constructors of parent classes
        Vehicle.__init__(self, brand, model, year)
        GPS.__init__(self)
        Entertainment.__init__(self)
        self._wifi_enabled = False
    
    def enable_wifi(self):
        """Enable Wi-Fi"""
        self._wifi_enabled = True
        print("📶 Wi-Fi enabled")
    
    def disable_wifi(self):
        """Disable Wi-Fi"""
        self._wifi_enabled = False
        print("📶 Wi-Fi disabled")
    
    def info(self):
        """Override info with all functionality"""
        vehicle_info = Vehicle.info(self)
        return f"{vehicle_info} - GPS: {self.location}, Music: {self.current_track}"

# ============================================
# 4. ABSTRACT CLASSES AND METHODS
# ============================================

class Animal(ABC):
    """Abstract base class for animals"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @abstractmethod
    def make_sound(self):
        """Abstract method - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def move(self):
        """Abstract method - must be implemented by subclasses"""
        pass
    
    def info(self):
        """Concrete method - can be used by all subclasses"""
        return f"{self.__class__.__name__}: {self.name}, Age: {self.age}"
    
    @classmethod
    def __subclasshook__(cls, subclass):
        """Custom subclass checking"""
        return (hasattr(subclass, 'make_sound') and 
                hasattr(subclass, 'move') or 
                NotImplemented)

class Dog(Animal):
    """Concrete class implementing abstract methods"""
    
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def make_sound(self):
        """Implement abstract method"""
        return "Woof! Woof!"
    
    def move(self):
        """Implement abstract method"""
        return f"{self.name} runs quickly!"
    
    def info(self):
        """Override info with breed"""
        base_info = super().info()
        return f"{base_info} - Breed: {self.breed}"

class Bird(Animal):
    """Another concrete class"""
    
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span
    
    def make_sound(self):
        return "Chirp! Chirp!"
    
    def move(self):
        return f"{self.name} flies with {self.wing_span}cm wingspan!"

# ============================================
# 5. POLYMORPHISM - Method Overriding and Overloading
# ============================================

# 5.1 METHOD OVERRIDING
class Shape:
    """Base shape class"""
    
    def __init__(self, name="Shape"):
        self.name = name
    
    def area(self):
        """Area - to be overridden"""
        return 0
    
    def perimeter(self):
        """Perimeter - to be overridden"""
        return 0
    
    def __str__(self):
        return f"{self.name}: Area={self.area():.2f}, Perimeter={self.perimeter():.2f}"

class Rectangle(Shape):
    """Rectangle - overrides area and perimeter"""
    
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def is_square(self):
        """Additional method"""
        return self.width == self.height

class Circle(Shape):
    """Circle - overrides area and perimeter"""
    
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

# 5.2 METHOD OVERLOADING (via default arguments)
class Calculator:
    """Calculator with overloaded methods using default arguments"""
    
    def add(self, a, b, c=None):
        """Add two or three numbers"""
        if c is None:
            return a + b
        return a + b + c
    
    def multiply(self, *args):
        """Multiply any number of arguments"""
        if not args:
            return 0
        result = 1
        for num in args:
            result *= num
        return result
    
    def power(self, base, exponent=2):
        """Power with default exponent"""
        return base ** exponent

# 5.3 DUCK TYPING
def calculate_area(shape):
    """Duck typing - any object with area() method works"""
    try:
        return shape.area()
    except AttributeError:
        return "Object doesn't have area() method"

# ============================================
# 6. COMPOSITION AND AGGREGATION
# ============================================

class Engine:
    """Engine class - used in composition"""
    
    def __init__(self, horsepower, fuel_type="Gasoline"):
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.is_running = False
    
    def start(self):
        self.is_running = True
        print(f"🔧 Engine ({self.horsepower} HP) started")
    
    def stop(self):
        self.is_running = False
        print("🔧 Engine stopped")
    
    def get_power(self):
        return self.horsepower

class Wheel:
    """Wheel class - used in aggregation"""
    
    def __init__(self, size, brand):
        self.size = size
        self.brand = brand
        self.pressure = 32
    
    def inflate(self, pressure):
        self.pressure = pressure
        print(f"💨 Wheel inflated to {pressure} PSI")

class CarWithEngine:
    """Car using composition - engine is created inside car"""
    
    def __init__(self, brand, model, horsepower):
        self.brand = brand
        self.model = model
        self.engine = Engine(horsepower)  # Composition
        self.wheels = []  # Aggregation - will be added later
    
    def add_wheels(self, *wheels):
        """Add wheels (aggregation)"""
        self.wheels.extend(wheels)
    
    def start(self):
        self.engine.start()
    
    def stop(self):
        self.engine.stop()
    
    def __del__(self):
        # Engine destroyed with car (composition)
        if hasattr(self, 'engine'):
            del self.engine

# ============================================
# 7. METHOD RESOLUTION ORDER (MRO)
# ============================================

class A:
    def method(self):
        print("A.method()")

class B(A):
    def method(self):
        print("B.method()")
        super().method()

class C(A):
    def method(self):
        print("C.method()")
        super().method()

class D(B, C):
    def method(self):
        print("D.method()")
        super().method()

# ============================================
# 8. PRACTICAL EXAMPLE: LIBRARY MANAGEMENT SYSTEM
# ============================================

class LibraryItem(ABC):
    """Abstract base class for library items"""
    
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.is_available = True
        self.borrower = None
        self.borrow_date = None
    
    @abstractmethod
    def get_type(self):
        pass
    
    def borrow(self, borrower_name):
        """Borrow item"""
        if self.is_available:
            self.is_available = False
            self.borrower = borrower_name
            self.borrow_date = datetime.now()
            print(f"📚 {self.title} borrowed by {borrower_name}")
            return True
        print(f"❌ {self.title} is not available")
        return False
    
    def return_item(self):
        """Return item"""
        if not self.is_available:
            self.is_available = True
            self.borrower = None
            self.borrow_date = None
            print(f"📚 {self.title} returned")
            return True
        print(f"⚠️ {self.title} is already available")
        return False
    
    def get_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nYear: {self.year}\nType: {self.get_type()}\nAvailable: {self.is_available}"

class Book(LibraryItem):
    """Book class"""
    
    def __init__(self, title, author, isbn, year, pages, genre):
        super().__init__(title, author, isbn, year)
        self.pages = pages
        self.genre = genre
    
    def get_type(self):
        return "Book"
    
    def get_reading_time(self):
        """Estimate reading time (pages per minute)"""
        return f"Approx {self.pages / 2:.0f} minutes reading time"

class DVD(LibraryItem):
    """DVD class"""
    
    def __init__(self, title, author, isbn, year, duration, director):
        super().__init__(title, author, isbn, year)
        self.duration = duration
        self.director = director
    
    def get_type(self):
        return "DVD"
    
    def get_duration_string(self):
        hours = self.duration // 60
        minutes = self.duration % 60
        return f"{hours}h {minutes}m"

class Magazine(LibraryItem):
    """Magazine class"""
    
    def __init__(self, title, author, isbn, year, issue_number, publisher):
        super().__init__(title, author, isbn, year)
        self.issue_number = issue_number
        self.publisher = publisher
    
    def get_type(self):
        return "Magazine"

class Library:
    """Library management system"""
    
    def __init__(self, name):
        self.name = name
        self.items = []
        self.members = set()
        self.transactions = []
    
    def add_item(self, item):
        """Add item to library"""
        self.items.append(item)
        print(f"✅ Added {item.get_type()}: {item.title}")
    
    def add_member(self, member_name):
        """Add library member"""
        self.members.add(member_name)
        print(f"👤 Added member: {member_name}")
    
    def borrow_item(self, isbn, member_name):
        """Borrow item by ISBN"""
        if member_name not in self.members:
            print(f"❌ {member_name} is not a library member")
            return False
        
        for item in self.items:
            if item.isbn == isbn:
                if item.borrow(member_name):
                    self.transactions.append({
                        'type': 'borrow',
                        'item': item.title,
                        'member': member_name,
                        'date': datetime.now()
                    })
                    return True
                return False
        
        print(f"❌ Item with ISBN {isbn} not found")
        return False
    
    def return_item(self, isbn):
        """Return item by ISBN"""
        for item in self.items:
            if item.isbn == isbn:
                if item.return_item():
                    self.transactions.append({
                        'type': 'return',
                        'item': item.title,
                        'member': item.borrower,
                        'date': datetime.now()
                    })
                    return True
                return False
        
        print(f"❌ Item with ISBN {isbn} not found")
        return False
    
    def search_by_title(self, keyword):
        """Search items by title"""
        results = [item for item in self.items if keyword.lower() in item.title.lower()]
        if results:
            print(f"\n🔍 Search results for '{keyword}':")
            for item in results:
                print(f"  - {item.title} by {item.author} ({item.get_type()})")
        else:
            print(f"No items found containing '{keyword}'")
        return results
    
    def get_available_items(self):
        """Get all available items"""
        return [item for item in self.items if item.is_available]
    
    def get_borrowed_items(self):
        """Get all borrowed items"""
        return [item for item in self.items if not item.is_available]
    
    def display_catalog(self):
        """Display full catalog"""
        print(f"\n📚 {self.name} Catalog:")
        for item in self.items:
            print(f"  {item.title} by {item.author} - {item.get_type()} ({'Available' if item.is_available else 'Borrowed'})")

# ============================================
# 9. DEMONSTRATION OF ALL OOP CONCEPTS
# ============================================

def demonstrate_oop():
    """Demonstrate all OOP concepts"""
    
    print("=" * 60)
    print("🐍 PYTHON OOP - COMPLETE DEMONSTRATION")
    print("=" * 60)
    
    # 1. BASIC CLASS AND OBJECTS
    print("\n🔹 1. BASIC CLASS AND OBJECTS")
    print("-" * 40)
    
    car1 = Car("Toyota", "Camry", 2020, "Blue")
    car2 = Car("Honda", "Civic", 2021, "Red")
    
    car1.start()
    car1.accelerate(30)
    car1.brake(10)
    car1.stop()
    
    print(f"Car info: {car1.get_info()}")
    print(f"Total cars: {Car.get_total_cars()}")
    print(f"String representation: {car1}")
    print(f"Representation: {repr(car1)}")
    
    # 2. ENCAPSULATION
    print("\n🔹 2. ENCAPSULATION")
    print("-" * 40)
    
    account = BankAccount("123456789", "John Doe", 1000)
    account.deposit(500)
    account.withdraw(200)
    print(f"Balance via property: ${account.balance}")
    print(f"Transactions: {account.get_transaction_history()}")
    
    # 3. INHERITANCE
    print("\n🔹 3. INHERITANCE")
    print("-" * 40)
    
    # Single inheritance
    tesla = Tesla("Model 3", 2022, 75, True)
    tesla.start()
    tesla.charge()
    tesla.autopilot_drive()
    print(tesla.info())
    
    # Multiple inheritance
    smart_car = SmartCar("Tesla", "Model S", 2023)
    smart_car.start()
    smart_car.update_location("San Francisco")
    smart_car.play_music("Bohemian Rhapsody")
    smart_car.enable_wifi()
    print(smart_car.info())
    
    # 4. ABSTRACT CLASSES
    print("\n🔹 4. ABSTRACT CLASSES")
    print("-" * 40)
    
    dog = Dog("Rex", 3, "German Shepherd")
    bird = Bird("Tweety", 1, 15)
    
    animals = [dog, bird]
    for animal in animals:
        print(f"{animal.info()}")
        print(f"  Sound: {animal.make_sound()}")
        print(f"  Movement: {animal.move()}")
    
    # 5. POLYMORPHISM
    print("\n🔹 5. POLYMORPHISM")
    print("-" * 40)
    
    rectangle = Rectangle(5, 3)
    circle = Circle(4)
    
    shapes = [rectangle, circle]
    for shape in shapes:
        print(f"Shape: {shape}")
        print(f"  Area: {shape.area():.2f}")
        print(f"  Perimeter: {shape.perimeter():.2f}")
    
    # Duck typing
    print(f"Area of rectangle via duck typing: {calculate_area(rectangle)}")
    print(f"Area of circle via duck typing: {calculate_area(circle)}")
    
    # Method overloading
    calc = Calculator()
    print(f"Add 2 numbers: {calc.add(3, 4)}")
    print(f"Add 3 numbers: {calc.add(3, 4, 5)}")
    print(f"Multiply: {calc.multiply(2, 3, 4, 5)}")
    print(f"Power (default): {calc.power(3)}")
    print(f"Power (specific): {calc.power(3, 4)}")
    
    # 6. COMPOSITION AND AGGREGATION
    print("\n🔹 6. COMPOSITION AND AGGREGATION")
    print("-" * 40)
    
    car_with_engine = CarWithEngine("BMW", "M3", 400)
    wheel1 = Wheel(19, "Michelin")
    wheel2 = Wheel(19, "Michelin")
    wheel3 = Wheel(19, "Michelin")
    wheel4 = Wheel(19, "Michelin")
    
    car_with_engine.add_wheels(wheel1, wheel2, wheel3, wheel4)
    car_with_engine.start()
    
    # 7. MRO
    print("\n🔹 7. METHOD RESOLUTION ORDER")
    print("-" * 40)
    
    d = D()
    d.method()
    print(f"MRO for D: {D.__mro__}")
    
    # 8. LIBRARY SYSTEM
    print("\n🔹 8. PRACTICAL EXAMPLE: LIBRARY SYSTEM")
    print("-" * 40)
    
    library = Library("Python City Library")
    
    # Create items
    book = Book("1984", "George Orwell", "978-0-451-52493-5", 1949, 328, "Dystopian")
    dvd = DVD("Inception", "Christopher Nolan", "978-0-452-28423-4", 2010, 148, "Christopher Nolan")
    magazine = Magazine("National Geographic", "Various", "978-0-452-28713-2", 2023, 456, "National Geographic Society")
    
    # Add items
    library.add_item(book)
    library.add_item(dvd)
    library.add_item(magazine)
    
    # Add members
    library.add_member("Alice")
    library.add_member("Bob")
    
    # Borrow and return
    library.borrow_item("978-0-451-52493-5", "Alice")
    library.borrow_item("978-0-452-28423-4", "Bob")
    library.return_item("978-0-451-52493-5")
    
    # Display catalog
    library.display_catalog()
    
    # Search
    library.search_by_title("Inception")
    
    # Available items
    print(f"\nAvailable items: {len(library.get_available_items())}")
    print(f"Borrowed items: {len(library.get_borrowed_items())}")
    
    # 9. MAGIC METHODS DEMONSTRATION
    print("\n🔹 9. MAGIC METHODS")
    print("-" * 40)
    
    car3 = Car("Honda", "Civic", 2020, "Blue")
    car4 = Car("Honda", "Civic", 2020, "Red")
    
    print(f"car1 == car2: {car1 == car2}")
    print(f"car1 == car3: {car1 == car3}")
    print(f"car1 < car2: {car1 < car2}")
    print(f"Length of car1: {len(car1)}")
    
    print("\n" + "=" * 60)
    print("🎉 OOP CONCEPTS DEMONSTRATED SUCCESSFULLY!")
    print("=" * 60)

# ============================================
# EXECUTING THE DEMONSTRATION
# ============================================

if __name__ == "__main__":
    demonstrate_oop()
    
    # Additional challenge: Create your own class system
    print("\n📝 YOUR TURN!")
    print("Create a class that represents a digital product with:")
    print("- Name, price, stock, category")
    print("- Methods to: buy, restock, apply discount")
    print("- Properties and encapsulation")
    print("- Inheritance from a base Product class")
    print("- Magic methods (__str__, __repr__, __eq__)")