#!/usr/bin/python3
"""
module base.py
"""


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
