#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    ret = my_list.copy()
    ret = list(map(lambda x: x * number, my_list))
    return (ret)
