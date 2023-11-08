#!/usr/bin/python3
"""The funtion retruns the dictionary description of a simple data structure"""


def class_to_json(obj):
    """Returns a serialized(converted) dictionary representation
    of simple data structure"""
    return obj.__dict__
