#!/usr/bin/python3
"""is_same_class function"""


def is_same_class(obj, a_class):
    """checks if obj is the instance of a_class or not"""
    if type(obj) is a_class:
        return True
    else:
        return False
