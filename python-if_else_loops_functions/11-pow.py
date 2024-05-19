#!/usr/bin/python3
def pow(a, b):
    c = 1
    temp = a
    if a < 0:
        temp = temp * -1
    if b < 0:
        b = b * -1
        temp = 1 / temp
    for i in range(b):
        c = c * temp
    if a < 0:
        c = c * -1
    return c
