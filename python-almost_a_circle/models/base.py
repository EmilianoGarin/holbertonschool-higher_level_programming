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
        if list_objs is not None:
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

        if cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load a list of form"""

        try:
            with open(f"{cls.__name__}.json", encoding="utf-8") as f:
                ret = cls.from_json_string(f.read())
        except FileNotFoundError:
            ret = []
        finally:
            ret_ins = []
            for x in ret:
                ret_ins.append(cls.create(**x))
            return ret_ins
