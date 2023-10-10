#!/usr/bin/python3
"""
Module '101-add_attribute' to add a new attribute
to an object if it’s possible
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
