#!/usr/bin/python3
def pow(a, b):
    c = 1
    temp = b
    if b < 0:
        b = b * -1
    for i in range(b):
        c = c * a
    if temp < 0:
        c = 1 / c
    return c
