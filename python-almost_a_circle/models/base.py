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

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save JSON in a file"""

        list_dictionaries = []
        for x in list_objs:
            list_dictionaries.append(x.to_dictionary())
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """JSON to list"""

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create a Reactangle or Square"""

        dummy = cls(1, 1, 1)
        if not dictionary or len(dictionary) == 0:
            return dummy
        dummy.update(**dictionary)
        return dummy
