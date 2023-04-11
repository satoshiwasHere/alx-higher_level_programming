#!/usr/bin/python3
"""
determines if an object is a member of a class derived from the given class
"""


def inherits_from(obj, a_class):
    """
    checks if the object is an instance of a subclass of the specified class
    """
    return issubclass(type(obj), a_class)
