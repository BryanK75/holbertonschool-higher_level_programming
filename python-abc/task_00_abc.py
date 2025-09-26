from abc import ABC, abstractmethod

# Abstract Base Class
class Animal(ABC):
    """Abstract class representing an animal"""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses"""
        pass


# Subclass Dog
class Dog(Animal):
    """Dog class inheriting from Animal"""

    def sound(self):
        return "Bark"


# Subclass Cat
class Cat(Animal):
    """Cat class inheriting from Animal"""

    def sound(self):
        return "Meow"
