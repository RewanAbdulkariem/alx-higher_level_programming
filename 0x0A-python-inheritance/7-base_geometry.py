#!/usr/bin/python3
"""
Module 'base_geometry' contains a class for representing geometrical shapes.
"""


class BaseGeometry:
    """
    BaseGeometry class is an empty class for representing geometrical shapes.
    """
    def area(self):
        """
        Raises:
        Exception: Always raises an exception with the message "area() is not
        implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if the given value is a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
