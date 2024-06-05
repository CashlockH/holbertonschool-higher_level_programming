#!/usr/bin/python3
"""save_to_json_file function module"""
import json


def save_to_json_file(my_obj, filename):
    """Save obj to json_file"""
    with open(filename, 'w') as file:
        file.write(json.loads(my_obj))
