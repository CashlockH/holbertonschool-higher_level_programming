#!/usr/bin/python3
"""append_write function module"""


def append_write(filename="", text=""):
    """ Opens a file and append a text to it"""
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
