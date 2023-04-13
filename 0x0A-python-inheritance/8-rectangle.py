#!/usr/bin/python3
"""
import statement for the BaseGeometry class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class inherits from the BaseGeometry class
    and allows us to create rectangles.
    """

    def __init__(self, width, height):
        """
        creates a new instance of the Rectangle class,`
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width
