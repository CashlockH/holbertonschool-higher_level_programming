#!/usr/bin/python3
"""module for Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """subclass of Rectangle class"""
    def __init__(self, size):
        super().__init__(size, size)
