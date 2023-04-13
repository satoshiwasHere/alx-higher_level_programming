#!/usr/bin/python3
"""
Represents base geometry the class BaseGeometry
"""


class BaseGeometry:
    """
    class reps base geometry
    """

    def area(self):

        raise Exception("area() is not implemented")
     
    def integer_validator(self, name, value):
        """
        checks if a value as an integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
