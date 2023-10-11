#!/usr/bin/python3
"""
Module '4-from_json_string' that returns an object.
"""
import json


def from_json_string(my_str):
    """
    Return the object represented by a JSON string.
    """
    return json.loads(my_str)
