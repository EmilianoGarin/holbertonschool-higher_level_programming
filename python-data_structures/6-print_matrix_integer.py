#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in enumerate(matrix):
        for x in enumerate(i[1]):
            if x[0] == len(i[1]) - 1:
                print("{}".format(x[1]), end="")
            else:
                print("{} ".format(x[1]), end="")
        print()
