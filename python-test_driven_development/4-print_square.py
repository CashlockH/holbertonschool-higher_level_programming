#!/usr/bin/python3
"""Print square module"""


def print_square(size):
    """Prints square that length of the side equals to size"""
    if isinstance(size, int):
        if size < 0:
            raise TypeError("size must be >= 0")
        for i in range(size):
            print("#" * size)
    else:
        raise TypeError("size must be an integer")
