#!/usr/bin/env python3
"""Abstract classes"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract Animal class"""
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """Dog class that inherits from Animal"""
    def sound(self):
        return "Bark"

class Cat(Animal):
    """Cat class that inherits from Animal"""
    def sound(self):
        return "Meow"
