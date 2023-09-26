#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            printed_integers += 1
        print()
    except (TypeError, IndexError):
        pass
    return printed_integers
