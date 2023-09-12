#!/usr/bin/python3
"""task 11"""


class Student():
    """Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__

        ret = {}
        for i in attrs:
            if hasattr(self, i):
                ret[i] = getattr(self, i)
        return ret

    def reload_from_json(self, json):
        for k, v in json.items():
            setattr(self, k, v)
