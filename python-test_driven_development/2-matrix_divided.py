#!/usr/bin/python3
"""Division of list elementd"""
error = "matrix must be a matrix (list of lists) of integers/floats"


def matrix_divided(a, b):
    """Divide each element of list of list a by b"""

    new_matrix = []
    length = len(a[0])
    if not isinstance(b, (int, float)):
        raise TypeError("div must be a number")
    elif b == 0:
        raise ZeroDivisionError("division by zero")
    for i in a:
        if len(i) != length:
            raise TypeError("Each row of the matrix must have the same size")
        row = []
        for j in i:
            if isinstance(j, (float, int)):
                row.append(round(j / b, 2))
            else:
                raise TypeError(error)
        new_matrix.append(row)
        length = len(i)
    return new_matrix
