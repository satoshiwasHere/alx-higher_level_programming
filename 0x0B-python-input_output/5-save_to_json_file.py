#!/usr/bin/python3
"""
A library defining a JSON file-writing function
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Outputs an object to a text file using JSON notation
    """
    with open(filename, "w") as fn:
        json.dump(my_obj, fn)
