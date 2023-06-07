#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        mat = []
        for i in matrix:
            ret = []
            for x in i:
                ret += [x**2]
            mat += [ret]
        return (mat)
