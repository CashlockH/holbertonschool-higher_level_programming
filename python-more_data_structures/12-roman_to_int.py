#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or not roman_string:
        return 0
    reducer = 0
    new = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in roman_string:
        if i == 'X' and reducer == 0:
            reducer = 10
        elif i == 'I':
            reducer = 1
        elif (i == 'V' or i == 'X') and reducer == 1:
            total = total - 2
            reducer = 0
        elif i == "C" and reducer == 10:
            total = total - 20
            reducer = 0
        else:
            reducer = 0
        if i in new:
            total = total + new[i]
    return total
