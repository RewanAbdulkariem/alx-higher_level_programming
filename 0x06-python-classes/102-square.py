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
    Compares if two squares have equal areas.

    Args:
        other (Square): The other square to compare.

    Returns:
        bool: True if the areas are equal, False otherwise.
    """
    def __eq__(self, other):
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    """
    Compares if two squares have unequal areas.

    Args:
        other (Square): The other square to compare.

    Returns:
        bool: True if the areas are unequal, False otherwise.
    """
    def __ne__(self, other):
        if isinstance(other, Square):
            return self.area() != other.area()
        return True

    """
    Compares if one square has a smaller area than another.

    Args:
        other (Square): The other square to compare.

    Returns:
       bool: True if the first square has a smaller area, False otherwise.
    """
    def __lt__(self, other):
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    """
    Compares if one square has a smaller or equal area than another.

    Args:
        other (Square): The other square to compare.

    Returns:
        bool: True if the first square has a smaller or equal area
        , False otherwise.
"""
    def __le__(self, other):
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    """
    Compares if one square has a larger area than another.

    Args:
        other (Square): The other square to compare.

    Returns:
            bool: True if the first square has a larger area, False otherwise.
    """
    def __gt__(self, other):
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    """
    Compares if one square has a larger or equal area than another.

    Args:
        other (Square): The other square to compare.

    Returns:
        bool: True if the first square has a larger or equal area
        , False otherwise.
    """
    def __ge__(self, other):
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented
