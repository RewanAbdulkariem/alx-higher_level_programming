#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Initializes a new square with the given size."""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """
    Calculates and returns the area of the square.
    Returns:
            int: The area of the square (size * size).
    """
    def area(self):
        return self.__size ** 2
