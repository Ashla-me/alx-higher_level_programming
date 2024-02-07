#!/usr/bin/python3
"""
json module
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using JSON representation"""
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
