#!/usr/bin/python3
"""
module base.py
"""
import json


class Base:
    """
        Base class for managing id attribute in future classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of the Base class.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'

        json_str = json.dumps(list_dictionaries)
        return (json_str)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.
        """
        if list_objs is None:
            list_objs = []

        filename = f"{cls.__name__}.json"
        with open(filename, "w") as outfile:
            dict_list = [obj.to_dictionary() for obj in list_objs]
            json_str = cls.to_json_string(dict_list)
            outfile.write(json_str)
