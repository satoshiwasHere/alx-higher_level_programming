#!/usr/bin/python3
"""
A library defining a string-to-JSON function
"""
import json


def to_json_string(my_obj):
    """
    Convert a string object to its JSON representation
    """
    return json.dumps(my_obj)
