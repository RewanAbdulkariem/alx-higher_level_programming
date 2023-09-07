#!/usr/bin/python3

from sys import argv
if __name__ == "__main__":
    arg_count = len(argv) - 1
    arg_plural = "argument" if arg_count == 1 else "arguments"

    print("{} {}".format(arg_count, arg_plural))

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
