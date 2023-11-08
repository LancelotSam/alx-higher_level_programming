#!/usr/bin/python3
"""Defibition of class Student"""


class Student:
    """Represents attributes of Student"""

    def __init__(self, first_name, last_name, age):
        """Initializes class Student
        Args:
            first_name
            last_name
            age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets a dict represnetation of Student
        Args:
            attrs(list)
        """
        if attrs is not None and (type(attrs) == list):
            return (
                    {attr: getattr(self, attr) for attr in
                        attrs if hasattr(self, attr)}
                    )
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replace all Student attributes
        Args:
            json(dict)
        """
        for key, value in json.items():
            setattr(self, key, value)
