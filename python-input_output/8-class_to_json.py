#!/usr/bin/python3
"""class_to_json function module"""
import json


def class_to_json(obj):
    """Class dictionary to Json"""
    return json.dumps(obj.__dict__)
