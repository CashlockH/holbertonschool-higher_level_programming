#!/usr/bin/python3
def no_c(my_string):
    new_string = bytearray(char for char in my_string.encode('utf-8') if char not in (67, 99))
    return new_string.decode('utf-8')
