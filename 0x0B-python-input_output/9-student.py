#!/usr/bin/python3
"""Definition of class Student"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes class
        Args:
            first_name:
            last_name
            age:
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary representation of Student"""
        return self.__dict__
