#!/usr/bin/python3
""" this is a class Square that represents a square"""


class Square:
    """class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """initializes Square"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """gets the size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """gets the area and returns it"""
        return (self.__size ** 2)

    @property
    def position(self):
        """
        retrieves the position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """sets the position"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of "
                            "two positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of "
                            "two positive integers")
        elif not (isinstance(value[0], int) and isinstance(value[1], int)):
            raise TypeError("position must be a tuple of"
                            "two positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of "
                            "two positive integers")
        else:
            self.__position = value

    def my_print(self):
        """prints a square"""
        if self.size == 0:
            print("")
        else:
            for i in range(self.position[1]):
                print("")
            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
