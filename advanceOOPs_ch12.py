# ============================================
# ADVANCED OOP - DESIGN PATTERNS & BEST PRACTICES
# ============================================

import json
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field
from enum import Enum, auto
import logging
from functools import wraps
import time

# ============================================
# 1. SINGLETON PATTERN
# ============================================

class Singleton:
    """Singleton pattern - only one instance allowed"""
    
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, name="Default"):
        # Only initialize if first time
        if not hasattr(self, 'initialized'):
            self.name = name
            self.initialized = True
            print(f"🔷 Singleton created: {name}")

# ============================================
# 2. FACTORY PATTERN
# ============================================

class PaymentProcessor(ABC):
    """Abstract payment processor"""
    
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass
    
    @abstractmethod
    def get_type(self) -> str:
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"💳 Processing ${amount} via Credit Card")
        return True
    
    def get_type(self) -> str:
        return "Credit Card"

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"💰 Processing ${amount} via PayPal")
        return True
    
    def get_type(self) -> str:
        return "PayPal"

class CryptoProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"₿ Processing ${amount} via Cryptocurrency")
        return True
    
    def get_type(self) -> str:
        return "Cryptocurrency"

class PaymentFactory:
    """Factory for creating payment processors"""
    
    _processors = {
        "credit": CreditCardProcessor,
        "paypal": PayPalProcessor,
        "crypto": CryptoProcessor
    }
    
    @classmethod
    def create_processor(cls, payment_type: str) -> PaymentProcessor:
        """Create a payment processor"""
        processor_class = cls._processors.get(payment_type.lower())
        if processor_class:
            return processor_class()
        raise ValueError(f"Unsupported payment type: {payment_type}")
    
    @classmethod
    def register_processor(cls, name: str, processor_class):
        """Register a new payment processor"""
        cls._processors[name.lower()] = processor_class

# ============================================
# 3. OBSERVER PATTERN
# ============================================

class Observer(ABC):
    """Observer interface"""
    
    @abstractmethod
    def update(self, subject, event_type: str, data: Any):
        pass

class Subject:
    """Subject that can be observed"""
    
    def __init__(self):
        self._observers = []
    
    def attach(self, observer: Observer):
        """Attach an observer"""
        self._observers.append(observer)
    
    def detach(self, observer: Observer):
        """Detach an observer"""
        self._observers.remove(observer)
    
    def notify(self, event_type: str, data: Any):
        """Notify all observers"""
        for observer in self._observers:
            observer.update(self, event_type, data)

class Stock(Subject):
    """Stock that can be observed"""
    
    def __init__(self, symbol: str, price: float):
        super().__init__()
        self.symbol = symbol
        self._price = price
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value: float):
        old_price = self._price
        self._price = value
        self.notify("price_change", {"old": old_price, "new": value})
    
    def update_price(self, new_price: float):
        """Update price with notification"""
        self.price = new_price

class StockAlert(Observer):
    """Alert observer for stocks"""
    
    def __init__(self, name: str, threshold: float):
        self.name = name
        self.threshold = threshold
    
    def update(self, subject, event_type: str, data: Any):
        if event_type == "price_change" and isinstance(subject, Stock):
            if data["new"] > self.threshold:
                print(f"🔔 {self.name}: {subject.symbol} crossed ${self.threshold}!")
                print(f"   New price: ${data['new']:.2f} (was ${data['old']:.2f})")
            elif data["new"] < self.threshold * 0.9:
                print(f"🔔 {self.name}: {subject.symbol} dropped below ${self.threshold * 0.9:.2f}!")

class StockLogger(Observer):
    """Logger observer"""
    
    def __init__(self):
        self.logs = []
    
    def update(self, subject, event_type: str, data: Any):
        log_entry = {
            "timestamp": time.time(),
            "subject": subject.symbol if hasattr(subject, 'symbol') else "Unknown",
            "event": event_type,
            "data": data
        }
        self.logs.append(log_entry)
        print(f"📝 Logged: {log_entry['subject']} - {event_type}")

# ============================================
# 4. STRATEGY PATTERN
# ============================================

class CompressionStrategy(ABC):
    """Compression strategy interface"""
    
    @abstractmethod
    def compress(self, data: str) -> str:
        pass

class ZipCompression(CompressionStrategy):
    def compress(self, data: str) -> str:
        # Simulate ZIP compression
        return f"ZIP:{data}"

class GzipCompression(CompressionStrategy):
    def compress(self, data: str) -> str:
        # Simulate GZIP compression
        return f"GZIP:{data}"

class NoCompression(CompressionStrategy):
    def compress(self, data: str) -> str:
        return data

class DataCompressor:
    """Context class for compression"""
    
    def __init__(self, strategy: CompressionStrategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy: CompressionStrategy):
        self._strategy = strategy
    
    def compress_data(self, data: str) -> str:
        return self._strategy.compress(data)

# ============================================
# 5. DECORATOR PATTERN (Structural)
# ============================================

class Coffee(ABC):
    """Base coffee class"""
    
    @abstractmethod
    def get_cost(self) -> float:
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        pass

class BasicCoffee(Coffee):
    """Basic coffee implementation"""
    
    def get_cost(self) -> float:
        return 2.00
    
    def get_description(self) -> str:
        return "Basic Coffee"

class CoffeeDecorator(Coffee):
    """Base decorator for coffee"""
    
    def __init__(self, coffee: Coffee):
        self._coffee = coffee
    
    def get_cost(self) -> float:
        return self._coffee.get_cost()
    
    def get_description(self) -> str:
        return self._coffee.get_description()

class MilkDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.50
    
    def get_description(self) -> str:
        return f"{self._coffee.get_description()} + Milk"

class SugarDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.25
    
    def get_description(self) -> str:
        return f"{self._coffee.get_description()} + Sugar"

class WhippedCreamDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.75
    
    def get_description(self) -> str:
        return f"{self._coffee.get_description()} + Whipped Cream"

# ============================================
# 6. COMMAND PATTERN
# ============================================

class Command(ABC):
    """Command interface"""
    
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass

class Light:
    """Receiver"""
    
    def on(self):
        print("💡 Light turned ON")
    
    def off(self):
        print("💡 Light turned OFF")

class LightOnCommand(Command):
    def __init__(self, light: Light):
        self._light = light
    
    def execute(self):
        self._light.on()
    
    def undo(self):
        self._light.off()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self._light = light
    
    def execute(self):
        self._light.off()
    
    def undo(self):
        self._light.on()

class RemoteControl:
    """Invoker"""
    
    def __init__(self):
        self._commands = []
        self._undo_stack = []
    
    def add_command(self, command: Command):
        self._commands.append(command)
    
    def execute_all(self):
        for command in self._commands:
            command.execute()
            self._undo_stack.append(command)
        self._commands.clear()
    
    def undo_last(self):
        if self._undo_stack:
            command = self._undo_stack.pop()
            command.undo()

# ============================================
# 7. BUILDING A COMPLETE SYSTEM
# ============================================

@dataclass
class Product:
    """Product dataclass with validation"""
    
    id: int
    name: str
    price: float
    category: str = "General"
    in_stock: bool = True
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")
        self.price = round(self.price, 2)

class ProductService:
    """Service class managing products"""
    
    def __init__(self):
        self._products: Dict[int, Product] = {}
        self._observers = []
    
    def add_product(self, product: Product):
        """Add a product to the service"""
        self._products[product.id] = product
        self._notify_observers("product_added", product)
    
    def get_product(self, product_id: int) -> Optional[Product]:
        return self._products.get(product_id)
    
    def update_price(self, product_id: int, new_price: float):
        """Update product price with notification"""
        product = self._products.get(product_id)
        if product:
            old_price = product.price
            product.price = new_price
            self._notify_observers("price_updated", {
                "product": product,
                "old_price": old_price,
                "new_price": new_price
            })
    
    def attach_observer(self, observer):
        self._observers.append(observer)
    
    def detach_observer(self, observer):
        self._observers.remove(observer)
    
    def _notify_observers(self, event: str, data: Any):
        for observer in self._observers:
            observer.update(self, event, data)

class ProductObserver(ABC):
    @abstractmethod
    def update(self, subject, event: str, data: Any):
        pass

class EmailNotifier(ProductObserver):
    def update(self, subject, event: str, data: Any):
        if event == "price_updated":
            product = data["product"]
            print(f"📧 Email sent: Price of {product.name} changed from ${data['old_price']:.2f} to ${data['new_price']:.2f}")

class InventoryManager(ProductObserver):
    def update(self, subject, event: str, data: Any):
        if event == "product_added":
            product = data
            print(f"📦 Inventory updated: {product.name} added to warehouse")

# ============================================
# 8. DEMONSTRATION
# ============================================

def demonstrate_advanced_oop():
    """Demonstrate all advanced OOP concepts"""
    
    print("=" * 60)
    print("🚀 ADVANCED OOP PATTERNS")
    print("=" * 60)
    
    # 1. Singleton
    print("\n🔹 1. Singleton Pattern")
    print("-" * 40)
    
    s1 = Singleton("First")
    s2 = Singleton("Second")
    print(f"s1 is s2: {s1 is s2}")
    print(f"s1.name: {s1.name}")
    
    # 2. Factory Pattern
    print("\n🔹 2. Factory Pattern")
    print("-" * 40)
    
    factory = PaymentFactory()
    for payment_type in ["credit", "paypal", "crypto"]:
        processor = factory.create_processor(payment_type)
        print(f"Created {processor.get_type()} processor")
        processor.process_payment(99.99)
    
    # 3. Observer Pattern
    print("\n🔹 3. Observer Pattern")
    print("-" * 40)
    
    stock = Stock("AAPL", 150.00)
    stock.attach(StockAlert("Alert1", 160.00))
    stock.attach(StockLogger())
    
    stock.update_price(155.00)
    stock.update_price(162.50)
    stock.update_price(140.00)
    
    # 4. Strategy Pattern
    print("\n🔹 4. Strategy Pattern")
    print("-" * 40)
    
    data = "Hello, World! This is some data to compress."
    compressor = DataCompressor(NoCompression())
    print(f"Original: {compressor.compress_data(data)}")
    
    compressor.set_strategy(ZipCompression())
    print(f"ZIP: {compressor.compress_data(data)}")
    
    compressor.set_strategy(GzipCompression())
    print(f"GZIP: {compressor.compress_data(data)}")
    
    # 5. Decorator Pattern
    print("\n🔹 5. Decorator Pattern")
    print("-" * 40)
    
    coffee = BasicCoffee()
    print(f"{coffee.get_description()}: ${coffee.get_cost():.2f}")
    
    coffee_with_milk = MilkDecorator(coffee)
    print(f"{coffee_with_milk.get_description()}: ${coffee_with_milk.get_cost():.2f}")
    
    coffee_with_everything = WhippedCreamDecorator(SugarDecorator(MilkDecorator(coffee)))
    print(f"{coffee_with_everything.get_description()}: ${coffee_with_everything.get_cost():.2f}")
    
    # 6. Command Pattern
    print("\n🔹 6. Command Pattern")
    print("-" * 40)
    
    light = Light()
    remote = RemoteControl()
    
    remote.add_command(LightOnCommand(light))
    remote.add_command(LightOffCommand(light))
    remote.execute_all()
    remote.undo_last()
    
    # 7. Complete System
    print("\n🔹 7. Complete System")
    print("-" * 40)
    
    product_service = ProductService()
    product_service.attach_observer(EmailNotifier())
    product_service.attach_observer(InventoryManager())
    
    # Add product
    product = Product(1, "iPhone 15 Pro", 999.99, "Electronics")
    product_service.add_product(product)
    
    # Update price
    product_service.update_price(1, 899.99)
    
    # Get product
    retrieved = product_service.get_product(1)
    print(f"Retrieved: {retrieved.name} - ${retrieved.price:.2f}")
    
    print("\n" + "=" * 60)
    print("🎉 ADVANCED OOP DEMONSTRATED SUCCESSFULLY!")
    print("=" * 60)

# ============================================
# EXECUTE DEMONSTRATION
# ============================================

if __name__ == "__main__":
    demonstrate_advanced_oop()