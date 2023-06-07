#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return (None)
    ret = len(my_list) * [False]
    for x, i in enumerate(my_list):
        if i % 2 == 0:
            ret[x] = True
    return (ret)
