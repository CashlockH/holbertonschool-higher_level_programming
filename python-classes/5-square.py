#!/usr/bin/python3
""" This module holds Square class"""


class Square:
    """class with an private attribute and area method"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        for i in range(0, self.size):
            print('#' * self.size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        self.__size = value
