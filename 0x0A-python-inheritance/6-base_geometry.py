#!/usr/bin/python3
class BaseGeometry:
    """Class Base Geometry"""
    def __init__(self):
        """Initializes the class"""
        pass

    def area(self):
        """Raises an exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")


class BaseGeometry:
    """Class Base Geometry"""
    def __init__(self):
        """Initializes the class"""
        pass

    def area(self):
        """Raises an exception with the message area() is not implemented"""
        raise RuntimeError("area() is not implemented")
