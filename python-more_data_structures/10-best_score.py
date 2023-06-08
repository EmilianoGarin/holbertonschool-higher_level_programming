#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    ret, max_v = next(iter(a_dictionary.items()))
    for old_k, k in zip([''] + list(a_dictionary), a_dictionary):
        if old_k != '':
            if max_v < a_dictionary[k]:
                ret = k
                max_v = a_dictionary[ret]
    return (ret)
