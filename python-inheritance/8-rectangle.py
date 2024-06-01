#!/usr/bin/python3
"""module for BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """subclass of BaseGeometry"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator("Rectangle", self.__width)
        super().integer_validator("Rectangle", self.__height)
