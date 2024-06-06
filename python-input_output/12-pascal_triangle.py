#!/usr/bin/python3
def pascal_triangle(n):
    triangle = []
    a = 1
    for i in range(n):
        j = 0
        sub_tri = []
        while j <= i:
            if j - 1 < i - j and j != 0:
                a += i - j
            elif j - 1 > i - j:
                a = a - j + 1
            sub_tri.append(a)
            j += 1
        triangle.append(sub_tri)
    return triangle
