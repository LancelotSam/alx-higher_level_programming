#!/usr/bin/python3
"""a definition of class BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """to be implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a param as an integer

        Args:
            name(str)
            value(int)

        Raises:
        TypeError
        ValueError
        """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
