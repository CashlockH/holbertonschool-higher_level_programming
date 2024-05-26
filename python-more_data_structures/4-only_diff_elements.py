#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set(x for s in (set_1, set_2) for x in s)
    return new_set
