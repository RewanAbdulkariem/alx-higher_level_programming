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

    @property
    def width(self):
        """ property to retrieve it """
        return self.__width

    @width.setter
    def width(self, value):
        """property setter to set it"""
        if isinstance(value, int) and value >= 0:
            self.__width = value
        elif isinstance(value, int) and value < 0:
            raise ValueError('width must be >= 0')
        else:
            raise TypeError('width must be an integer')

    @property
    def height(self):
        """ property to retrieve it """
        return self.__height

    @height.setter
    def height(self, value):
        """property setter to set it"""
        if isinstance(value, int) and value >= 0:
            self.__height = value
        elif isinstance(value, int) and value < 0:
            raise ValueError('height must be >= 0')
        else:
            raise TypeError('height must be an integer')
