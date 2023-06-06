#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    if len(list_a) < 2:
        for i in range(len(list_a), 2):
            list_a += [0]
    if len(list_b) < 2:
        for i in range(len(list_b), 2):
            list_b += [0]
    ret = tuple(sum(x) for x in zip(list_a, list_b))
    return (ret)
