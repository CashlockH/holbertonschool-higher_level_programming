#!/usr/bin/python3
"""module for BaseGeometry class"""


class BaseGeometry:
    """class with not implemented area method"""
    def area(self):
        raise Exception("area() is not implemented")
