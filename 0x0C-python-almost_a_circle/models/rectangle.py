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
