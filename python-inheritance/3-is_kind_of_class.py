#!/usr/bin/python3
"""task 3"""


def is_kind_of_class(obj, a_class):
    """
    true if the obj is an instans of a_class or a class that
    inherited, otherwise false
    """
    return isinstance(obj, a_class)
