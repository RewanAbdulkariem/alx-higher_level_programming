#!/usr/bin/python3
"""
Module '8-rectangle' contains Rectangle class.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes the Rectangle instance.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width
