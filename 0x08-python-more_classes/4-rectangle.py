#!/usr/bin/python3
"""
A class definnig a rectangle
"""


class Rectangle:
    """
    A class Rectangle reping a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Method initializing the class attributes
        attributes:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

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

    @property
    def height(self):
        """
        retrieves height attribute particulars
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

    def area(self):
        """
        evaluates the area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Evaluates the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * (self.__width + self.__height)

    def __str__(self) -> str:
        """
        method to print rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        recta = ""
        for column in range(self.__height):
            for row in range(self.__width):
                recta += "#"
            if column < self.__height - 1:
                recta += "\n"
        return (recta)
    
    def __repr__(self):
        """
        method to represent the class as a string
        """
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) +\
            ")"

