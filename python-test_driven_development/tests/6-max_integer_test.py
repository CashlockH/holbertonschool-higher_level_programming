#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer

import unittest

class TestMethods(unittest.TestCase):
    def regulartest(self):
        self.AssertEqual(max_integer([1, 2, 3, 4]), 4)
if __name__ == '__main__':
    unittest.main()
