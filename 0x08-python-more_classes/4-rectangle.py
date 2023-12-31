#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
    """class Rectangle"""
    def __init__(self, width=0, height=0):
        """ Initializes the Rectangle class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns the width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """returns the height of the rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """ return a printable represnetaion of the rectangle
        using # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        my_rect = []
        for i in range(self.__height):
            [my_rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                my_rect.append("\n")
        return ("".join(my_rect))

    def __repr__(self):
        """ returns str representation of the rectangle"""
        my_rect = (
                'Rectangle(' + str(self.width) + ',' +
                str(self.height) + ')'
                )
        return (my_rect)
