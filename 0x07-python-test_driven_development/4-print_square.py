#!/usr/bin/python3
'''
This script defines a function named print_square, which
prints a square with the character #.
'''


def print_square(size):
    '''
    prints a square with "#"'s that has a length of size 
    '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    print(("#" * size + "\n") * size, end="")
