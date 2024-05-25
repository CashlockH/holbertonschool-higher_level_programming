#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_value = my_list[0]
    for i,j in enumerate(my_list):
        if j > max_value:
            max_value = j
    return max_value
