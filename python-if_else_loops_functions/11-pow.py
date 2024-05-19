#!/usr/bin/python3
def pow(a, b):
    c = 1
    if b < 0:
        b = b * -1
        for i in range(b):
            c = c * 1 / a
    else:
        for i in range(b):
            c = c * a
    return c
