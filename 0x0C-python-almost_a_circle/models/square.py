#!/usr/bin/python3
"""Defines a square inherited from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square inherits from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes class Square
        Args:
            size
            x
            y
            id
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the values of given object"""
        if len(args) != 0:
            i = 1
            for arg in args:
                if i == 1:
                    self.id = arg
                elif i == 2:
                    self.size = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        elif len(kwargs) != 0:
            for arg in kwargs.keys():
                if arg == "id":
                    self.id = kwargs.get(arg)
                if arg == "size":
                    self.size = kwargs.get(arg)
                if arg == "x":
                    self.x = kwargs.get(arg)
                if arg == "y":
                    self.y = kwargs.get(arg)

    def to_dictionary(self):
        """Returns a dictionary representation
        of rectangle"""
        return (
                {
                    "id": self.id,
                    "size": self.width,
                    "x": self.x,
                    "y": self.y
                    }
                )

    def __str__(self):
        """returns a string represnetation of
        square object"""
        string = (
                "[Square] ({}) {}/{}"
                .format(self.id, self.x, self.y, self.width)
                )
        return (string)
