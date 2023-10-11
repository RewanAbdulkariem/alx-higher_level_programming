#!/usr/bin/python3
"""
Module '5-save_to_json_file'
"""
import json
import sys
from os.path import exists


load_from_json = __import__("6-load_from_json_file").load_from_json_file
save_to_json = __import__("5-save_to_json_file").save_to_json_file


def add_items_to_list(filename, args):
    """
    Add items to a list and save it as a JSON representation in a file.
    """
    if exists(filename):
        my_list = load_from_json(filename)
    else:
        my_list = []
    my_list.extend(args)
    save_to_json(my_list, filename)


if __name__ == "__main__":
    filename = "add_item.json"
    args = sys.argv[1:]
    add_items_to_list(filename, args)
    load_from_json(filename)
