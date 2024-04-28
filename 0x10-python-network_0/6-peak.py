#!/usr/bin/python3
"""
6-peak.py
Created by Rewan 26 Apr
"""


def find_peak(list_of_integers):
    """
    find a peak in a list of unsorted integers
    """
    low = 0
    high = len(list_of_integers) - 1
    if not list_of_integers:
        return None
    list_of_integers.sort()
    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return list_of_integers[low]
