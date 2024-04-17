#!/usr/bin/python3
"""
0-rectangle.py module
"""


class Rectangle:
    """
    An empty class Rectangle that defines a rectangle
    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    def width(self):
        """ property to retrieve it """
        return self.__width

    def width(self, value):
        """property setter to set it"""
        if isinstance(value, int) and value >= 0:
            self.__width = value
        elif isinstance(value, int) and value < 0:
            raise ValueError('width must be >= 0')
        else:
            raise TypeError('width must be an integer')

    def height(self):
        """ property to retrieve it """
        return self.__height

    def height(self, value):
        """property setter to set it"""
        if isinstance(value, int) and value >= 0:
            self.__width = value
        elif isinstance(value, int) and value < 0:
            raise ValueError('width must be >= 0')
        else:
            raise TypeError('width must be an integer')
