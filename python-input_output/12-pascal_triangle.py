#!/usr/bin/python3
"""task 12"""


def pascal_triangle(n):
    """pascal triangle"""

    if n <= 0:
        return []

    ret = [[1]]
    for x in range(n - 1):
        level = ret[-1]
        col = [1]
        for j in range(1, len(level)):
            col.append(level[j] + level[j - 1])
        col.append(1)
        ret.append(col)
    return ret
