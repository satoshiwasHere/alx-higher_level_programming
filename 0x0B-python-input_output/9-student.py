#!/usr/bin/python3
"""
This defines a class Student
"""


class Student:
    """
    the student class
    """

    def __init__(self, first_name, last_name, age):
        """
        Sets up a new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns object as a JSON string"""
        vars(self)
