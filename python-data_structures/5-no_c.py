#!/usr/bin/python3
def no_c(my_string):
    new_string = bytearray(my_string, 'utf-8')
    j = 0
    for i in new_string:
        if i == 67 or i == 99:
            del new_string[j]
        j = j + 1
    return new_string.decode()
