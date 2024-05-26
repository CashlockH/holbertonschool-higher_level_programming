#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new = []
    for keyo, vali in a_dictionary.items():
        if keyo == key:
            new.append(key)
    for i in new:
        del a_dictionary[i]
    return a_dictionary
