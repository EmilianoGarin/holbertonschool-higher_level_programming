#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ret = a_dictionary.copy()
    for k, v in a_dictionary.items():
        ret[k] = v * 2
    return (ret)
