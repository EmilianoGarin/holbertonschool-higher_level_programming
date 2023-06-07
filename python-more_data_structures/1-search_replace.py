#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        ret = my_list.copy()
        for x, i in enumerate(my_list):
            if search == i:
                ret[x] = replace
        return (ret)
