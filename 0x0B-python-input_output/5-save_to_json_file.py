#!/usr/bin/python3
"""Write to JSON file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an obj to atext file using JSON format"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
