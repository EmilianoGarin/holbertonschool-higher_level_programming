#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (None)
    x = my_list[0]
    for j in my_list:
        if j > x:
            x = j
    return (x)
