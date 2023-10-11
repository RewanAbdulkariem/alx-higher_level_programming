#!/usr/bin/python3
"""
Module '0-read_file' to read a text file and print its content.
"""


def read_file(filename=""):
    """
    Read the content of the specified text file
    and print it to the standard output.
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
