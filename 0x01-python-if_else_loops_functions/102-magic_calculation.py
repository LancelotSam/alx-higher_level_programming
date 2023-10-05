#!/usr/bin/python3
def magic_calculation(a, b, c):
    """loads a&b, compares <
    if false go to offset 16
    also return val of c
    """
    if a < b:
        return c
    if c > b:
        return (a+b)
    return ((a*b) - c)
