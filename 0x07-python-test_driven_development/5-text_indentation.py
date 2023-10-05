#!/usr/bin/python3
'''
This script defines a function named text_indentation, which
prints a text with 2 new lines after each of these characters
'''


def text_indentation(text):
    '''
    prints a text with 2 new lines after each of
    these characters: ., ? and :
    '''
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ['.', '?', ':']
    skip_space = False
    for char in text:
        if skip_space and char == ' ':
            continue
        if char in special_chars:
            print('{}\n\n'.format(char), end="")
            skip_space = True
        else:
            print(char, end="")
            skip_space = False
