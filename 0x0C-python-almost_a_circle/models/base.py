#!/usr/bin/python3
"""
This class will be the base of all other classes
the goal of it is to manage id att in all future classes
and avoid duplicating the same code
"""


import json


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """add id value if not none, otherwise add 1 to nb_obj"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of a list of dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """"""
        file = []
        file_name = cls.__name__ + ".json"
        if list_objs is not None:
            for i in list_objs:
                file.append(cls.to_dictionary(i))
        with open(file_name, "w") as fi:
            fi.write(cls.to_json_string(file))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ is "Square":
            dummy = cls(1)

        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        file = []
        try:
            with open(filename, 'r') as fi:
                file = cls.from_json_string(fi.read())
            for i, e in enumerate(file):
                file[i] = cls.create(**file[i])
        except:
            pass
        return file
