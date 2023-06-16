#!/usr/bin/python3
"""
task 1
"""


def matrix_divided(matrix, div):
    """
    matrix
    """
    err_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(err_matrix)
    for a in range(len(matrix)):
        if not isinstance(matrix[a], list):
            raise TypeError(err_matrix)
        if len(matrix[0]) != len(matrix[a]):
            raise TypeError("Each row of the matrix must have the same size")
        for b in range(len(matrix[a])):
            if not isinstance(matrix[a][b], (int, float)):
                raise TypeError(err_matrix)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    cp_matrix = matrix.copy()
    for a in range(len(matrix)):
        for b in range(len(matrix[a])):
            cp_matrix[a][b] = round((cp_matrix[a][b] / div), 2)
    return (cp_matrix)
