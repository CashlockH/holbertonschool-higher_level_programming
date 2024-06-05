#!/usr/bin/python3
"""Holds read_file function"""


def read_file(filename=""):
    """Opens the file and read from that"""
    with open(filename, encoding="utf-8") as file:
        file.read()
