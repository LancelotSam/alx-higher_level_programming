#!/usr/bin/python3
"""This is a class for Square"""


class Square:

    def __init__(self, size=0):

        self.__size = size

    @property
    def size(self):
        """ Retrieves the private instnace
        """
        return self.__size

    @size.setter
    def size(self, value):

        """
        sets the value of size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes and Returns the value of area of size
        """

        return size.__self ** 2

    def my_print(self):

        if not self.__size:
            print("")

        for i in range(self.__size):
            print("#" * self.__size)
