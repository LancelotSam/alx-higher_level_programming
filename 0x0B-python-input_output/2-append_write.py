#!/usr/bin/python3
"""A fucntion that appends a string to a file"""


def append_write(filename="", text=""):
    """Function appends astring at the ned of a file
    Args:
        filename(str): name of the file
        text(str): string to be appended
    Returns:
        Appended characters
    """
    with open(filename, "a", encoding="utf-8"):
        return (f.write(text))
