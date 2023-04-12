#!/usr/bin/python3
"""
A library defining a JSON-to-object function
"""


import json


def from_json_string(my_str):
    """
    Converts a JSON string into its Python object equivalent
    """
    return json.loads(my_str)
