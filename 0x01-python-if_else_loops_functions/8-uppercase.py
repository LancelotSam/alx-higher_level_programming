#!/usr/bin/python3
def uppercase(str):
    """print a string in uppercase"""
    result = ""
    for c in str:
        if 97 <= ord(c) <= 122:
            c = chr(ord(c) - 32)
        result += c
    print("{}".format(result))
