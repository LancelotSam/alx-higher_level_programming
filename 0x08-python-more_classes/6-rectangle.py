#!/usr/bin/python3
""" Area and Perimeter of class Rectangle"""


class Rectangle:
    """ Representation of a Rectangle
    Attributes:
        number of instances (int): rectangle instances
        """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Initializes the Rectangle

        Args:
            width(int): the width of the rectangle
            height(int): the height of the rectangle
            """
        type(self).number_of_instances += 1
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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
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
        for i in range(sel.__height):
            [my_rect.append('#') for j in range(self.__width)]
            if i !+ self.__height - 1:
                rect.append("\n")
        return ("".joint(my.rect))

    def __repr__(self):
        """ returns str representation of the rectangle"""
        my_rect = (
                'Rectangle(' + str(self.width) + ',' +
                str(self.height) + ')'
                )
        return (my_rect)

    def __del__(self):
        """Prints a message when an instnace of triangle is deleted"""
        type(self).number_os_instances -= 1
        print("Bye rectangle...")
