#!/usr/bin/python3
"""write_file function module"""


def write_file(filename="", text=""):
    """Opens a file and write a text into it"""
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(text)
