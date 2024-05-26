#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i, a in enumerate(my_list):
        if a == search:
            new_list[i] = replace
    return new_list
