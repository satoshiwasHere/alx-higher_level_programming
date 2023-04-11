#!/usr/bin/python3
"""
verifies if an object is an instance of a class or a subclass of it
"""


def is_kind_of_class(obj, a_class):
    """
    checks if object is a subclass of given class, not the class itself.
    """
    return issubclass(obj.__class__, a_class)
