#!/usr/bin/python3
"""task 8"""
import json


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)"""

    return obj.__dict__
