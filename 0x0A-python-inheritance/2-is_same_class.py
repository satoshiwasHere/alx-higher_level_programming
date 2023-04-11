#!/usr/bin/python3
"""
Determines if object is of a given class type.
"""


def is_same_class(obj, a_class):
    """
    determine if the object is an instance of the specified class
    """
    return obj.__class__.__name__ == a_class.__name__
