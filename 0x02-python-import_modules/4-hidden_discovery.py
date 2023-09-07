#!/usr/bin/python3

import hidden_4 as hidden
if __name__ == "__main__":
    for obj in dir(hidden):
        if (obj[0] != "_"):
            print(obj)
