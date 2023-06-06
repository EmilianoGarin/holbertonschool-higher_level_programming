#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    if len(list_a) < len(list_b):
        for i in range(len(list_b) - len(list_a)):
            list_a += [0]
    else:
        for i in range(len(list_a) - len(list_b)):
            list_b += [0]
    ret = tuple(sum(x) for x in zip(list_a, list_b))
    return (ret)
