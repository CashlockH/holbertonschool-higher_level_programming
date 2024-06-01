#!/usr/bin/python3
"""module for BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """subclass of BaseGeometry"""
    def __init__(self, width, height):
        super().__init__
        if not BaseGeometry.integer_validator(self, width, height):
            self.__width = width
            self.__height = height
