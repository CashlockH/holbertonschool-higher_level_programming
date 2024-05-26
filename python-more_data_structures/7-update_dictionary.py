#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for keyo, vali in a_dictionary.items():
        if keyo == key:
            a_dictionary[key] = value
            return a_dictionary
    a_dictionary[key] = value
    return a_dictionary
