#!/usr/bin/python3
"""
module to class
"""


class MyList(list):
    """
    Custom list class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
