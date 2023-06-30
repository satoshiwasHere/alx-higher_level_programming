#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status using package requests
"""

import requests


if __name__ == "__main__":
    res = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))
