#!/usr/bin/python3

def uppercase(str):
    result = ""
    for c in str:
        if ord(c) < 123 and ord(c) > 96:
            result += "{}".format(chr(ord(c) - 32))
        else:
            result += "{}".format(c)

    print("{}".format(result))