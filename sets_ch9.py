# ============================================
# CHAPTER 9: SETS - UNIQUE COLLECTIONS
# ============================================
# 🎯 LEARNING OBJECTIVES:
# 1. Understanding sets and their properties
# 2. Set operations (union, intersection, difference)
# 3. Set methods
# 4. Set comprehensions
# 5. Frozen sets
# 6. Practical applications
# ============================================

# 📦 CREATING SETS
empty_set = set()  # Empty set - {} creates empty dict!
numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "orange", "apple"}  # Duplicates removed
mixed = {1, "hello", 3.14, True}

print(f"Empty set: {empty_set}")
print(f"Numbers: {numbers}")
print(f"Fruits (duplicates removed): {fruits}")
print(f"Mixed: {mixed}")

# Creating set from list
list_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_set = set(list_with_duplicates)
print(f"List with duplicates: {list_with_duplicates}")
print(f"Set (unique values): {unique_set}")

# 🎯 SET PROPERTIES
# 1. Sets are unordered
# 2. Sets contain unique elements
# 3. Sets are mutable (add/remove)
# 4. Set elements must be hashable (immutable)

# 🎨 ADDING AND REMOVING
colors = {"red", "green", "blue"}
print(f"\nOriginal: {colors}")

# Add single element
colors.add("yellow")
print(f"After add: {colors}")

# Add multiple elements
colors.update(["purple", "orange"])
print(f"After update: {colors}")

# Remove elements
colors.remove("green")  # Raises KeyError if not found
print(f"After remove: {colors}")

colors.discard("pink")  # No error if not found
print(f"After discard: {colors}")

# Pop random element
popped = colors.pop()
print(f"Popped: {popped}, Remaining: {colors}")

# Clear all
colors.clear()
print(f"After clear: {colors}")

# 🔍 MEMBERSHIP AND LENGTH
fruits = {"apple", "banana", "orange"}
print(f"\nIs 'apple' in set? {'apple' in fruits}")
print(f"Is 'grape' in set? {'grape' in fruits}")
print(f"Set size: {len(fruits)}")

# 🔄 SET OPERATIONS
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"\nSet1: {set1}")
print(f"Set2: {set2}")

# Union - elements in either set
print(f"Union: {set1 | set2}")
print(f"Union method: {set1.union(set2)}")

# Intersection - elements in both sets
print(f"Intersection: {set1 & set2}")
print(f"Intersection method: {set1.intersection(set2)}")

# Difference - elements in set1 but not in set2
print(f"Difference (set1 - set2): {set1 - set2}")
print(f"Difference method: {set1.difference(set2)}")

# Symmetric difference - elements in either set but not both
print(f"Symmetric difference: {set1 ^ set2}")
print(f"Symmetric difference method: {set1.symmetric_difference(set2)}")

# 🔄 SUBSET AND SUPERSET
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

print(f"\nSet1: {set1}")
print(f"Set2: {set2}")
print(f"Is set1 subset of set2? {set1.issubset(set2)}")
print(f"Is set2 superset of set1? {set2.issuperset(set1)}")
print(f"Are they disjoint? {set1.isdisjoint({6, 7, 8})}")

# 🚀 SET COMPREHENSIONS
# Create set of squares
squares = {x**2 for x in range(5)}
print(f"\nSquares: {squares}")

# Filter with condition
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# 🔧 FROZEN SETS - Immutable sets
frozen = frozenset([1, 2, 3, 4, 5])
print(f"\nFrozen set: {frozen}")

# Can use frozen set as dictionary key
my_dict = {frozenset([1, 2]): "value"}
print(f"Using frozen set as key: {my_dict}")

# 🎯 PRACTICAL APPLICATIONS

# 1. Removing duplicates from list
def remove_duplicates(lst):
    return list(set(lst))

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_numbers = remove_duplicates(numbers)
print(f"\nOriginal: {numbers}")
print(f"Unique: {unique_numbers}")

# 2. Finding common elements in multiple lists
def find_common(*lists):
    if not lists:
        return set()
    common = set(lists[0])
    for lst in lists[1:]:
        common &= set(lst)
    return common

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [2, 3, 4, 5, 8]
common = find_common(list1, list2, list3)
print(f"\nCommon elements: {common}")

# 3. Finding unique elements from multiple lists
def find_unique(*lists):
    all_elements = []
    for lst in lists:
        all_elements.extend(lst)
    return set(all_elements)

unique = find_unique(list1, list2, list3)
print(f"All unique elements: {unique}")

# 4. Text analysis with sets
def analyze_text(text):
    words = text.lower().split()
    
    # All unique words
    unique_words = set(words)
    
    # Words that appear more than once
    word_set = set()
    duplicates = set()
    for word in words:
        if word in word_set:
            duplicates.add(word)
        else:
            word_set.add(word)
    
    print(f"\nText: {text}")
    print(f"Total words: {len(words)}")
    print(f"Unique words: {len(unique_words)}")
    print(f"Duplicate words: {duplicates}")
    print(f"Unique words sorted: {sorted(unique_words)}")

# Test text analysis
analyze_text("the cat in the hat sat on the mat")

# 5. Set operations for real-world data
def compare_users(users1, users2):
    """Compare two sets of users"""
    set1 = set(users1)
    set2 = set(users2)
    
    print(f"\nUser Set 1: {len(set1)} users")
    print(f"User Set 2: {len(set2)} users")
    
    print(f"Users in both: {set1 & set2} ({len(set1 & set2)} users)")
    print(f"Users only in set1: {set1 - set2} ({len(set1 - set2)} users)")
    print(f"Users only in set2: {set2 - set1} ({len(set2 - set1)} users)")
    print(f"Users in either: {set1 | set2} ({len(set1 | set2)} total users)")

# Test user comparison
users1 = ["Alice", "Bob", "Charlie", "David", "Eve"]
users2 = ["Charlie", "David", "Eve", "Frank", "Grace"]
compare_users(users1, users2)

# 📊 SET OPERATIONS VISUALIZATION
def set_operations_demo():
    """Demonstrate all set operations with examples"""
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}
    
    print(f"\nSet A: {A}")
    print(f"Set B: {B}")
    print("-" * 40)
    
    operations = {
        "Union (A ∪ B)": A | B,
        "Intersection (A ∩ B)": A & B,
        "Difference (A - B)": A - B,
        "Difference (B - A)": B - A,
        "Symmetric Difference (A ⊕ B)": A ^ B
    }
    
    for name, result in operations.items():
        print(f"{name}: {result}")

set_operations_demo()

# 🎯 CHALLENGE: Social Network Analysis
class SocialNetwork:
    def __init__(self):
        self.users = {}  # user -> set of friends
    
    def add_user(self, user):
        if user not in self.users:
            self.users[user] = set()
            print(f"Added user: {user}")
    
    def add_friendship(self, user1, user2):
        if user1 in self.users and user2 in self.users:
            self.users[user1].add(user2)
            self.users[user2].add(user1)
            print(f"Friendship between {user1} and {user2}")
    
    def get_friends(self, user):
        return self.users.get(user, set())
    
    def get_mutual_friends(self, user1, user2):
        return self.users.get(user1, set()) & self.users.get(user2, set())
    
    def get_friend_suggestions(self, user):
        """Suggest friends of friends who are not already friends"""
        if user not in self.users:
            return set()
        
        friends = self.users[user]
        suggestions = set()
        
        for friend in friends:
            suggestions |= self.users[friend]
        
        suggestions -= friends  # Remove current friends
        suggestions.discard(user)  # Remove self
        
        return suggestions
    
    def get_degrees_of_separation(self, user1, user2):
        """BFS to find degrees of separation"""
        if user1 not in self.users or user2 not in self.users:
            return -1
        
        if user1 == user2:
            return 0
        
        visited = {user1}
        queue = [(user1, 0)]
        
        while queue:
            current, distance = queue.pop(0)
            
            for friend in self.users[current]:
                if friend == user2:
                    return distance + 1
                
                if friend not in visited:
                    visited.add(friend)
                    queue.append((friend, distance + 1))
        
        return -1
    
    def display_network(self):
        print("\nSocial Network:")
        for user, friends in self.users.items():
            print(f"  {user}: {friends if friends else 'No friends'}")

# Test the social network
network = SocialNetwork()
network.add_user("Alice")
network.add_user("Bob")
network.add_user("Charlie")
network.add_user("David")

network.add_friendship("Alice", "Bob")
network.add_friendship("Alice", "Charlie")
network.add_friendship("Bob", "Charlie")
network.add_friendship("Charlie", "David")

network.display_network()

print(f"\nAlice's friends: {network.get_friends('Alice')}")
print(f"Mutual friends (Alice, Bob): {network.get_mutual_friends('Alice', 'Bob')}")
print(f"Friend suggestions for Alice: {network.get_friend_suggestions('Alice')}")
print(f"Degrees between Alice and David: {network.get_degrees_of_separation('Alice', 'David')}")

# 📚 WHAT WE LEARNED:
# 1. Creating sets and their properties
# 2. Adding and removing elements
# 3. Set operations (union, intersection, difference)
# 4. Subset and superset checking
# 5. Set comprehensions
# 6. Frozen sets
# 7. Removing duplicates
# 8. Finding common elements
# 9. Text analysis with sets
# 10. Social network analysis

# 🎮 NEXT CHAPTER: Conditionals - Making decisions!