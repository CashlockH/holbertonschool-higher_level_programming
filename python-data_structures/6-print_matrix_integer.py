#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i, j in enumerate(matrix):
        if matrix == [[]]:
            print()
        else:
            for a, b in enumerate(j):
                if a != len(j) - 1:
                    print("{:d}".format(b), end = " ")
                else:
                    print("{:d}".format(b))
