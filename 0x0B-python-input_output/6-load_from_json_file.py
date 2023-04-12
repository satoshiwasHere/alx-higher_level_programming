#!/usr/bin/python3
"""
A library defining a JSON file-reading function
"""
import json


def load_from_json_file(filename):
    """
    Generates a Python object from a JSON file
    """
    with open(filename) as fn:
        return json.load(fn)
