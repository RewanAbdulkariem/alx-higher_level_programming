#!/usr/bin/python3
"""
Module 'base_geometry' contains an empty class for representing
geometrical shapes.
"""


class BaseGeometry:
    """
    BaseGeometry class is an empty class for representing geometrical shapes.
    """
    def area(self):
        """
        Raises an exception indicating that the area calculation
        is not implemented.
        """
        raise Exception("area() is not implemented")
