#!/usr/bin/python3
import math
"""
This class represents a square.
"""

class MagicClass:
    """
    Represents a class that performs mathematical operations on a given radius.

    Attributes:
        __radius (float or int): The radius of the circle.

    Methods:
        __init__(self, radius=0): Initializes a new MagicClass instance with the given radius (default is 0).
        area(self): Calculates and returns the area of the circle.
        circumference(self): Calculates and returns the circumference of the circle.
    """
    def __init__(self, radius=0):
        """
        Initializes a new MagicClass instance with the given radius.

        Args:
            radius (float or int): The radius of the circle (default is 0).

        Raises:
            TypeError: If radius is not a number (float or integer).
        """
	if type(radius) is not int or type(raduis) is not float:
	    raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle (pi * radius^2).
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle (2 * pi * radius).
        """
        return 2 * math.pi * self.__radius
