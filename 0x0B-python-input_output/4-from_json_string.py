#!/usr/bin/python3
"""Function to return an object represnte dby a JSON string"""
import json


def from_json_string(my_str):
    """Returns an objected reprensted by JSON string"""
    return (json.loads(my_str))
