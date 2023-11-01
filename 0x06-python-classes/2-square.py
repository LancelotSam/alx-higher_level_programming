#!/usr/bin/python3
"""Defining class Square"""


class Square():
    """class Square"""
    def __init__(self, size=0):
        """ Initialize the class Square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
