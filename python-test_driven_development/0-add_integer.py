#!/usr/bin/python3
doctest_testfile.py
import doctest
if __name__ == '__main__':
    doctest.testfile('add_integer.txt')
def add_integer(a, b=98):
    if (c := isinstance(a, (float, int))) and (d := isinstance(b, (float, int))):
        if (c:= isinstance(a, float)) or (d:= isinstance(b, float)):
            if c:
                a = int(a)
            elif d:
                b = float(b)
        return a + b
    elif not c:
        raise TypeError("a must be an integer")
    else:
        raise TypeError("b must be an integer")
