#!/usr/bin/python3
"""
Module '1-write_file' that writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    Write the specified text to a text file using UTF-8 encoding.
    If the file does not exist, it will be created. If it exists,
    its content will be overwritten.
    """
    with open(filename, mode='w', encoding="utf-8") as f:
        nb_characters = f.write(text)
    return nb_characters
