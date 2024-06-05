#!/usr/bin/python3
"""load_fomt_json_file function module"""
import json


def load_from_json_file(filename):
    """creates obj form json file"""
    with open(filename) as file:
        return json.loads(file.read())
