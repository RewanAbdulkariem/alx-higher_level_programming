#!/usr/bin/python3
"""
Module "10-student"
"""


class Student:
    """
    Defines a student with first_name, last_name, and age attributes.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with the given first_name,
        last_name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__

        json_dict = {}
        for attribute in attrs:
            if hasattr(self, attribute):
                json_dict[attribute] = getattr(self, attribute)
        return json_dict
