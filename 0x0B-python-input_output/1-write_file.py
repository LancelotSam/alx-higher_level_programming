#!usr/bin/python3
"""A function to wrute to a file"""


def write_file(filename="", text=""):
    """Write a string to a utf-8 function

    Args:
        filename(str)
        text(str)
    Returns:
         Number of written characters
    """
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
