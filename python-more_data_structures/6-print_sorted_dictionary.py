#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = [(keys, values) for keys, values in a_dictionary.items()]
    for i in sorted(new):
        print("{:s}: {}".format(i[0], i[1]))
