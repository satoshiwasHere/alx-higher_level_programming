#!/usr/bin/python3
"""A class definning a rectangle"""


class Rectangle:
    """A class Rectangle definning a recyangle"""

    def __init__(self, width=0, height=0):
        """
        method initializing the class atrributes

        attributes:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """
        retrives height atttribute particulars
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets height attribute for rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        width attribute retriver
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets width attribute for rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value 
