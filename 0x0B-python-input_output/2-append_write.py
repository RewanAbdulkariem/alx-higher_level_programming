#!/usr/bin/python3
"""
Module '2-append_write' that appends a string at the end of a text file.
"""


def append_write(filename="", text=""):
    """
    Append the specified text to a text file using UTF-8 encoding.
    If the file does not exist, it will be created.
    """
    with open(filename, mode='a', encoding="utf-8") as f:
        nb_characters_added = f.write(text)
    return nb_characters_added
