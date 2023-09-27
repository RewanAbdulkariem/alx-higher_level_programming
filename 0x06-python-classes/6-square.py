#!/usr/bin/python3
"""
This class represents a square.

Attributes:
    __size (int): The size of the square.

Methods:
    __init__(self, size=0): Initializes a new square with the
    given size (default is 0).
    area(self): Calculates and returns the area of the square.
"""


class Square:
    """
    Initializes a new square with the given size.
    """
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    """
    Calculates and returns the area of the square.

    Returns:
            int: The area of the square (size * size).
    """
    def area(self):
        return self.__size ** 2

    """
    Getter method for retrieving the size attribute.

    Returns:
            int: The size of the square.
    """
    @property
    def size(self):
        return self.__size

    """
    Setter method for setting the size attribute.

    Args:
         value (int): The new size to set.
    Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
    """
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """
    Getter method for retrieving the position attribute.

    Returns:
        tuple: The position of the square as a tuple of two positive integers.
    """
    @property
    def position(self):
        return self.__position

    """
    Setter method for setting the position attribute.

    Args:
       value (tuple): The new position to set.

    Raises:
        TypeError: If value is not a tuple of two positive integers.
    """
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """
    Prints the square to stdout using '#' characters.

    If the size is equal to 0, it prints an empty line.
    """
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)
