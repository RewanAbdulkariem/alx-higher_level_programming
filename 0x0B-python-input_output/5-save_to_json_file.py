#!/usr/bin/python3
"""
Module '5-save_to_json_file'
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write the JSON representation of an object to a text file.
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
