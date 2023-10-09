#!/usr/bin/python3
"""
module lookup to find the attributes and methods
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    """
    return dir(obj)
