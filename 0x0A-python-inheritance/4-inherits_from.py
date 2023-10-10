#!/usr/bin/python3
"""
Module 'inherits_from'

This module contains a function 'inherits_from' that checks if an object
is an instance of a class that inherited (directly or indirectly) from the
specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if the given object is an instance of a class that inherited
    (directly or indirectly) from the specified class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
