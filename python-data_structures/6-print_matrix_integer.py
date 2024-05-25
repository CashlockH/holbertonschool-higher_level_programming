#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i, j in enumerate(matrix):
        for a, b in enumerate(j):
            if a != len(j) - 1:
                print(b, end = " ")
            else:
                print(b)
