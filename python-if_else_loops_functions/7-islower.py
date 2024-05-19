#!/usr/bin/python3
def islower(c):
    a = ord(c)
    if (a >= 65 and a <= 90):
        return False
    elif (a >= 97 and a <= 122):
        return True
