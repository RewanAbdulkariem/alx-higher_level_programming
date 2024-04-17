#!/usr/bin/python3
"""
2-rectangle.py module
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

    def area(self):
        """returns the rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2*(self.__height + self.__width))

    def __str__(self):
        total = ""
        if self.__height == 0 or self.width == 0:
            return total
        for i in range(self.__height):
            total += ("#" * self.__width)
            if i != (self.__height - 1):
                total += "\n"
        return total

    def __repr__(self):
        """repr() should return a string representation of the rectangle
        to be able to recreate a new instance by using eval()"""
        return f"Rectangle({self.width}, {self.height})"
