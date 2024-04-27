#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
"""
import requests
if __name__ == '__main__':
    html = requests.get('https://w3schools.com/python/demopage.htm')
    print("Body response:")
    print("\t- type: {}".format(type(html.text)))
    print("\t- content: {}".format(html.text))
