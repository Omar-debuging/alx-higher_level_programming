#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    l1 = list(tuple_a)
    l2 = list(tuple_b)
    result = []
    if len(l1) >= 1:
        x1 = l1[0]
    else:
        x1 = 0
    if len(l1) >= 2:
        x2 = l1[1]
    else:
        x2 = 0
    if len(l2) >= 1:
        y1 = l2[0]
    else:
        y1 = 0
    if len(l2) >= 2:
        y2 = l2[1]
    else:
        y2 = 0
    result += [x1 + y1, x2 + y2]
    x = tuple(result)
    print(x)
