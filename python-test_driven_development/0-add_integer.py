#!/usr/bin/python3
"""

task 0

"""


def add_integer(a, b=98):
    """
    add a + b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a == float('-inf') or a == float('inf'):
        raise OverflowError("Cannot convert float infinity to integer")
    if b == float('-inf') or b == float('inf'):
        raise OverflowError("Cannot convert float infinity to integer")
    return (int(a) + int(b))
