#!/usr/bin/python3
""" say_my_name module"""


def say_my_name(first_name, last_name=""):
    """Prints first_name and last_name"""
    if (c := isinstance(first_name, str)) and \
            (d := isinstance(last_name, str)):
        print("My name is {} {}".format(first_name, last_name))
    elif not c:
        raise TypeError("first_name must be a string")
    elif not d:
        raise TypeError("last_name must be a string")
