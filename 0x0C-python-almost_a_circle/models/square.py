#!/usr/bin/python3
"""
module square.py
"""
from models.rectangle import Rectangle



class Square(Rectangle):
    """
    
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        returns [Square] (<id>) <x>/<y> - <size>
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}")
