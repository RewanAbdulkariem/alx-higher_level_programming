#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
"""
import requests

html = requests.get('https://w3schools.com/python/demopage.htm')
print("Body response:")
print("\t- type: {}".format(type(html)))
print("\t- content: {}".format(html.text))