#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return 0
    new_list = sorted(my_list.copy())
    i = 1
    a = new_list[0]
    b = 0
    while i < len(new_list):
        if new_list[i] == a:
            pass
        else:
            b = b + a
            a = new_list[i]
        i = i + 1
    b = b + a
    return b
