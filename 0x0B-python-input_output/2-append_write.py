#!/usr/bin/python3
"""
A library defining a file-appending function
"""


def append_write(filename="", text=""):
    """
    Adds a string to the end of a UTF8 text file
    """
    with open(filename, "a", encoding="utf-8") as fn:
        return fn.write(text)
