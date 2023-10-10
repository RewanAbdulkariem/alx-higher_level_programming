#!/usr/bin/python3
"""
Module '8-rectangle' contains Rectangle class.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle.
    """
    def __init__(self, size):
        """
        Initializes the Rectangle instance.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

   def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
        str: String representation of the Square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
