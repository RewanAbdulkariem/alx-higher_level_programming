#!/usr/bin/python3
'''
This script defines a function named say_my_name, which prints
a formatted string containing the provided first name and last name.
'''


def say_my_name(first_name, last_name=""):
    '''
    Print a formatted string with the provided first name and last name.

    Parameters:
    first_name (str): The first name to be included in the output.
    last_name (str, optional): The last name to be included in the output.
    Default is an empty string.

    Raises:
    TypeError: If first_name or last_name is not a string.
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
