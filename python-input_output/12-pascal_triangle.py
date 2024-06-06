#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """prints n row of pascal triangle"""
    triangle = []
    for i in range(n):
        j = 0
        sub_tri = []
        while j <= i:
            if i != 0 and j != 0 and j != i:
                sub_tri.append(triangle[i - 1][j] + triangle[i - 1][j - 1])
            else:
                sub_tri.append(1)
            j += 1
        triangle.append(sub_tri)
    return triangle
