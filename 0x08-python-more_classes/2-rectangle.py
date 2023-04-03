#!/usr/bin/python3
"""
A class defining a rectangle
"""


class Rectangle:
    """A class representing a rectangle(s)"""

    def __init__(self, width=0, height=0):
        """"Initilization of the class attribute

        Attributes:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        retrieves particulars for width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets particular rectangle width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        retrieves particular height attriute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets height attribute of rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0"
        self.__height = value

    def area(self):
        """returns/calculates areaa of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns/evaluates the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
