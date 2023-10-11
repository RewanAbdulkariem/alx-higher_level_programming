#!/usr/bin/python3
"""
Module '8-class_to_json'
"""


def class_to_json(obj):
    """
    Convert an instance of a class to a dictionary description
    with simple data structures
    suitable for JSON serialization.
    """
    return obj.__dict__
