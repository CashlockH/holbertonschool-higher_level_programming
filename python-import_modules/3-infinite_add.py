#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    a = 0
    length = len(argv)
    if length == 1:
        print(0)
    elif length == 2:
        print(argv[1])
    else:
        for i in range(length - 1):
            a = a + int(argv[i+1])
        print(a)
