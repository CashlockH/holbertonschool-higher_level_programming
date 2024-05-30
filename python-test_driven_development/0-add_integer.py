#!/usr/bin/python3
"""Documentation of the modulae"""


def add_integer(a, b=98):
    """ Adds two integer"""

    if (c := isinstance(a, (float, int)))
    and (d := isinstance(b, (float, int))):
        if a + 1 == a or b + 1 == b:
            raise OverflowError
        if (c := isinstance(a, float)) or (d := isinstance(b, float)):
            if c:
                a = int(a)
            elif d:
                b = float(b)
        return a + b
    elif not c:
        raise TypeError("a must be an integer")
    else:
        raise TypeError("b must be an integer")
