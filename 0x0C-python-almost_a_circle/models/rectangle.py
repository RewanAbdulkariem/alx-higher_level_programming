#!/usr/bin/python3
"""
module rectangle.py that contains class Rectangle,
inheritance of class Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes instances """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def get_width(self):
        """
        function to get width
        """
        return self.__width

    def set_width(self, width):
        """
        function to set value of width
        """
        self.__width = width

    def get_height(self):
        """
        function to get width
        """
        return self.__height

    def set_height(self, height):
        """
        function to set value of width
        """
        self.__height = height

    def get_x(self):
        """
        function to get width
        """
        return self.__x

    def set_x(self, x):
        """
        function to set value of width
        """
        self.__x = x

    def get_y(self):
        """
        function to get width
        """
        return self.__y

    def set_y(self, y):
        """
        function to set value of width
        """
        self.__y = y