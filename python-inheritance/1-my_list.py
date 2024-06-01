#!/usr/bin/python3
"""Mylist class"""


class MyList(list):
    """inherit from list and sort the list"""
    def print_sorted(self):
        return sorted(self)
