#!/usr/bin/python3
def roman_to_int(roman_string):
    a = 0
    if type(roman_string) is not str or not roman_string:
        return 0
    for i in roman_string:
            if i == 'X':
                a = a + 10
            elif i == 'I':
                a = a + 1
            elif i == 'V':
                a = a + 5
            elif i ==  'L':
                a = a + 50
            elif i == 'C':
                a = a + 100
            elif i == 'D':
                a = a + 500
            elif i == 'M':
                a = a + 1000
    return a
