#!/usr/bin/python3
"""This is a class for Square"""


class Square:
    """class Square"""
    def __init__(self, size=0):
        """initialize the class Square"""
        self.__size = size

    @property
    def size(self):
        """ Retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Computes and Returns the area"""
        return size.__self ** 2

    def my_print(self):
        """prints # as a square"""
        if not self.__size:
            print("")

        for i in range(self.__size):
            print("#" * self.__size)
