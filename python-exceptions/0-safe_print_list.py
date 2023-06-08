#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end='')
            j += 1
    except IndexError:
        print()
        return (j)
    else:
        print()
        return (j)
