#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = set()
    for item in my_list:
        if item not in unique_integers:
            unique_integers.add(item)
    result = sum(unique_integers)
    return result
