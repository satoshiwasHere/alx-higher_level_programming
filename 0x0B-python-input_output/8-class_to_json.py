#!/usr/bin/python3
"""
A library defining a Python class-to-JSON function"""


def class_to_json(obj):
    """
    Generates a dictionary from a straightforward data structure
    """
    return vars(obj)
