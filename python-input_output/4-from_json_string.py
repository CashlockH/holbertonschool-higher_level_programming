#!/usr/bin/python3
"""from_json_string funciton module"""
import json


def from_json_string(my_str):
    """return object from json"""
    return json.loads(my_str)
