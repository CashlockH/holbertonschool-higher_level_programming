#!/usr/bin/python3
def roman_to_int(roman_string):
    a = 0
    if type(roman_string) is not str or not roman_string:
        return 0
    for i in roman_string:
        match i:
            case 'X':
                a = a + 10
            case 'I':
                a = a + 1
            case 'V':
                a = a + 5
            case 'L':
                a = a + 50
            case 'C':
                a = a + 100
            case 'D':
                a = a + 500
            case 'M':
                a = a + 1000
            case _:
                a = 0
    return a
