#!/usr/bin/python3
"""
A library defininig a file-writing function.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file encoded in UTF8.
    """
    with open(filename, "w", encoding="utf-8") as fn:
        return fn.write(text)
