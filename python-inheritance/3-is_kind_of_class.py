#!/usr/bin/python3
"""is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """checks if obj is the instance of a_class or not"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
