#!/usr/bin/env python3
"""Abstract classes"""
from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    """Abstract class with area and perimeter methods"""
    @abstractmethod
    def area():
        pass

    @abstractmethod
    def perimeter():
        pass

class Circle(Shape):
    """Circle class inherits from Shape"""
    def __init__(self, radius):
        if radius < 0:
            radius = radius * -1
        self.radius = radius

    def area(self):
        return (self.radius ** 2) * pi

    def perimeter(self):
        return 2 * self.radius * pi

class Rectangle(Shape):
    """Rectangle class inherits from Shape"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(duck):
    print("Area: {}".format(duck.area()))
    print("Perimeter: {}".format(duck.perimeter()))
