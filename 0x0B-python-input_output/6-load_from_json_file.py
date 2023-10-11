#!/usr/bin/python3
"""
Module '6-load_from_json_file'
"""
import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file.
    """
    with open(filename, "r") as file:
        data = json.load(file)
    return data
