#!/usr/bin/python3
"""Rectangle class"""


class Rectangle():
    """Class that plays rectangle role and has its attribures"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        string = ""
        if self.height == 0 or self.width == 0:
            return string
        for i in range(self.height):
            for j in range(self.width):
                string = string + '#'
            if i < self.height - 1:
                string = string + '\n'
        return string

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
