#!/usr/bin/python3
def best_score(a_dictionary):
    a = 0
    if not a_dictionary:
        return None
    for key, value in a_dictionary.items():
        if value >= a:
            a = value
    return a
