#!/usr/bin/python3
"""class Square that defines a square"""


class Square():
    """class Square"""
    def __init__(self, size=0):
        """ initailizate class Square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """get the area of the square"""
        return (self.__size ** 2)
