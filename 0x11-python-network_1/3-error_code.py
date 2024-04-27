#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL and
displays the body of the response
"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        req = Request(url)
        with urlopen(req) as response:
            res = response.read().decode('utf-8')
            print(res)
    except HTTPError as err:
        print(f"Error code: {err}")