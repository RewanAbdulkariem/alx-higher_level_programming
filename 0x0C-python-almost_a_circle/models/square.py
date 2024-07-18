#!/usr/bin/python3
"""
module square.py
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square inherits from Rectangle and represents a square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a square instance with size, position (x, y)
        and optional id.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        returns [Square] (<id>) <x>/<y> - <size>
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}")

    @property
    def size(self):
        """ Getter size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        if args:
            attributes = ["id", "size", "x", "y"]
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        returns the dictionary representation of a Square
        """
        return {
            'id': self.id,
            'x': self.x,
            'size': self.height,
            'y': self.y
        }
