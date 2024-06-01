#!/usr/bin/python3
"""inherits_from function"""


def inherits_from(obj, a_class):
    """checks if obj is the instance of a_class or not"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
