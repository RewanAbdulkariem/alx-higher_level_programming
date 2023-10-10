#!/usr/bin/python3
"""
module 'is_same_class' to check if obj is same as class
"""


def is_same_class(obj, a_class):
    """
    a function that returns True
    if the object is exactly an instance of the specified class ;
    otherwise False
    """
    return isinstance(obj, a_class) and a_class is not object
