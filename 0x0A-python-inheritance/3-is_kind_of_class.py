#!/usr/bin/python3
"""
Module 'is_kind_of_class'

This module contains a function 'is_kind_of_class' that checks if an object
is an instance of a specified class or a subclass thereof.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the given object is an instance of the specified
    class or its subclass.
    """
    return isinstance(obj, a_class)
