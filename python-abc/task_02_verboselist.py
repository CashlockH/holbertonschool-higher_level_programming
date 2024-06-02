#!/usr/bin/env python3
"""Abstract classes"""


class VerboseList(list):
    """Extends list class"""
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        super().extend(items)
        print("Extended the list with [{}] items".format(len(items)))

    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, item=-1):
        print("Popped [{}] from the list.".format(self[item]))
        super().pop(item)
