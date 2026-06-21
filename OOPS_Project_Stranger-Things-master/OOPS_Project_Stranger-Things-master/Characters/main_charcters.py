# Importing ABC (Abstract Base Class) and abstractmethod decorator
from abc import ABC, abstractmethod

# Creating an abstract base class called Character
class Character(ABC):
    def __init__(self, name, health, power , special_move):
        # These attributes are encapsulated using underscore (_) as a convention
        self._name = name      # 🔒 Encapsulated name of the character
        self._health = health  # 🔒 Encapsulated health (HP)
        self._power = power    # 🔒 Encapsulated power (attack strength)
        self._special_move = special_move

    # Abstract method means every child class must implement this method
    @abstractmethod
    def attack(self, opponent):
        pass  # No implementation here, subclasses must define it

    # Method to reduce the character's health when they take damage
    def take_damage(self, amount):
        self._health -= amount  # Reduce health by damage amount
        if self._health < 0:
            self._health = 0  # Health should not be negative

    # Method to check if the character is still alive
    def is_alive(self):
        return self._health > 0  # Returns True if health is greater than 0

    # Getter method to access health (read-only access)
    def get_health(self):
        return self._health

    # Getter method to access name
    def get_name(self):
        return self._name

    # Getter method to access power
    def get_power(self):
        return self._power 
    
    # Getter method to access special move
    def get_special_move(self):
        return self._special_move
    
    
    # Method to check if the character is defeated
    def is_defeated(self):
        return self._health <= 0


