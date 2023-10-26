#!/usr/bin/python3
"""class Square that defines a square"""


class Square():
    """implementing class Square"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Gets the value of size
            Args:
                None
            Returns:
                __size
                """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of the square
            Args:
                value(int)
                Returns:
                None
                """
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """get the area of the square and return it
        Args:
            None
        Returns
            __size * 4
            """
        return self.__size ** 2
