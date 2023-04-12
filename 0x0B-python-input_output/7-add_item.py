#!/usr/bin/python3
"""
This library adds arguments to python list and saves them in a file
'"""
import json

if __name__ == "__main__":
    try:
        with open('add_item.json', 'r') as fn:
            items = json.load(f)
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    with open('add_item.json', 'w') as fn:
        json.dump(items, fn)
