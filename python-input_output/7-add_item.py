#!/usr/bin/python3
"""Writing commandline arguments to json file"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
new = []
try:
    a = load_from_json_file("add_item.json")
    for b in a:
        new.append(b)
except:
    pass
i = 1
while(i < len(sys.argv)):
    new.append(sys.argv[i])
    i += 1
save_to_json_file(new, "add_item.json")
