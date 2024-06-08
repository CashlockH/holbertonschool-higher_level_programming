"""Serialization and Deserialization module for JSON"""
import json


def serialize_and_save_to_file(data, filename):
    """Serialze object to json format and save to file"""
    with open(filename, 'w') as file:
        json.dump(data, file)
        

def load_and_deserialize(filename):
    """Deserialize from json format from file"""
    with open(filename, 'r') as file:
        return json.load(file)
