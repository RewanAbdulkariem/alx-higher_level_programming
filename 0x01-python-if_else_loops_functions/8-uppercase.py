#!/usr/bin/python3

def uppercase(str):
    result = ""
    for c in str:
        if ord(c) < 123 and ord(c) > 96:
            result += chr(ord(c) - 32)
        else:
            result += c

    print("{}".format(result))
