#!/usr/bin/python3
"""task 1"""
import json


class Base():
    """model base"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save JSON in a file"""

        list_dictionaries = []
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            for x in list_objs:
                list_dictionaries.append(x.to_dictionary())
            f.write(cls.to_json_string(list_dictionaries))
