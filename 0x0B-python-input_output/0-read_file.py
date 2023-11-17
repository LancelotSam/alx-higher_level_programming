#!/usr/bin/python3
"""A function for reaidng a text file"""


def read_file(filename=""):
    """Prints the contents of a utf-8 file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
