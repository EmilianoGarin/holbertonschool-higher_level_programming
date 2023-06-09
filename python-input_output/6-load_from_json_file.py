#!/usr/bin/python3
"""task 6"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""

    with open(filename, encoding="utf-8") as f:
        ret = json.loads(f.read())
    return ret
