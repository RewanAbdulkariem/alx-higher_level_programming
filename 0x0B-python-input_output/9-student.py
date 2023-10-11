#!/usr/bin/python3
"""
Module "9-student"
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


    def to_json(self):
        """
        Retrieves a dictionary representation of the Student instance.
        """
        json_dict = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
        return json_dict
