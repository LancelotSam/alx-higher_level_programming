#!/usr/bin/python3
"""Defines a class and inherited class-checking ftn"""


def is_kind_of_class(obj, a_class):
    """Checks if it is a class or inherited from

    Returns:
        True if object is an instance
        or is an instnce inherited from
        False Otherwise
        """
    if isinstance(obj, a_class):
        return True
    return False
