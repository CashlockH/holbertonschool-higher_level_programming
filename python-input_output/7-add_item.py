#!/usr/bin/python3
"""Writing commandline arguments to json file"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
i = 1
new = []
while(i < len(sys.argv)):
    new[i - 1] = sys.argv[i]
save_to_json_file(new, "add_item.json")
