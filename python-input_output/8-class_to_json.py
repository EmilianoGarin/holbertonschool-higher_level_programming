#!/usr/bin/python3
"""task 8"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)"""

    return obj.__dict__
