#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = sorted(my_list.copy())
    print(new_list)
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
