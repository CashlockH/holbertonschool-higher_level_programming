#!/usr/bin/env python3
"""Iterators"""


class CountedIterator():
    """Iterator class"""
    def __init__(self, data):
        self.counter = 0
        self.data = data
        self.itr_obj = iter(data)

    def get_count(self):
        return self.counter

    def __next__(self):
        if self.counter == len(self.data):
            raise StopIteration
        self.counter += 1
        return self.data[self.counter - 1]
