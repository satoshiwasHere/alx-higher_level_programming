#!/usr/bin/python3
"""
text reading module
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout
    Args:
        filename (str): Name of the file to read
    Returns:
        null
    """
    """
    Open file in read mode
    """
    with open(filename, 'r', encoding="utf8") as file:

        """Read every line and print it"""
        for line in file:
            print(line, end="")

    """Calls the function"""


read_file("textfile.txt")
