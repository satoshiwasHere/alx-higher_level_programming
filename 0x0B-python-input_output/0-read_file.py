#!/usr/bin/python3
"""
function that opens a file and read its content
"""


def read_file(filename=""):
    """
    Prints UTF-8 file contents
    """
    with open(filename, encoding="utf-8") as fn:
        print(fn.read(), end="")
