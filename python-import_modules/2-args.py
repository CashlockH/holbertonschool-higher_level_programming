#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    length = len(argv)
    if length == 1:
        print("0 arguments.")
    elif length == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(length))
        for i in range(length - 1):
            print("{}: {}".format(i + 1, argv[i + 1]))
