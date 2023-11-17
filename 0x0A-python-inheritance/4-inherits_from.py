#!/usr/bin/python3
"""Defines an inherited class-checking function"""


def inherits_from(obj, a_class):
    """Checks  if an object is an inherited instnce of a class
    Args:
        obj(any): the object to check
        a_class(type): teh class to be matched
    Returns:
        True if object is an inherited instnce of class
        false otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
