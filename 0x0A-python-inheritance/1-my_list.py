#!/usr/bin/python3
"""
This module is a subclass of the list class
"""


class MyList(list):
    """
    This is subclass of list
    """
    def print_sorted(self):
        """prints a list in order(ascending sort)"""
        print(sorted(self))
