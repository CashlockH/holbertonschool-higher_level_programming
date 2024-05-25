#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = [a for a in my_list]
    for i, j in enumerate(my_list):
        if j % 2 == 0:
            new_list[i] = True
        else:
            new_list[i] = False
    return new_list
