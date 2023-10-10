#!/usr/bin/python3
"""
Module '100-my_int' inherits from int
"""
class MyInt(int):
    """
    MyInt class inherits from int and inverts the == and != operators.
    """
    def __eq__(self, other):
        """
        Invert the equality operator
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Invert the inequality operator
        """
        return super().__eq__(other)
