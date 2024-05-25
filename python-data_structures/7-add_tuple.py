#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ah = [ 0 for b in range(0,2)]
    bh = [ 0 for b in range(0,2)]
    if len(tuple_a) == 1:
        ah[0] = tuple_a[0]
    elif len(tuple_a) >= 2:
        for i,j in enumerate(tuple_a):
            ah[i] = tuple_a[i]
    if len(tuple_a) == 1:
        bh[0] = tuple_b[0]
    elif len(tuple_b) >= 2:
        for i,j in enumerate(tuple_b):
            bh[i] = tuple_b[i]
    new_list = (ah[0] + bh[0], ah[1] + bh[1])
    return new_list
