#!/usr/bin/python3

'''
Adds two integers.
This module contains a function, add_integer(a, b=98),that takes two integers
or floats as arguments and returns their sum as an integer.
'''


def add_integer(a, b=98):
    """
    Adds two integers.
    """
    if isinstance(a, str) and a.isdigit():
        a = int(a)
    if isinstance(b, str) and b.isdigit():
        b = int(b)

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    return int(a) + int(b)
