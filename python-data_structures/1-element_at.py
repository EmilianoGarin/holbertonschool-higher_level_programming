#!/usr/bin/python3
def element_at(my_list, idx):
    if isinstance(idx, int):
        if idx > len(my_list) or idx < 0:
            return (None)
        return (my_list[idx])
