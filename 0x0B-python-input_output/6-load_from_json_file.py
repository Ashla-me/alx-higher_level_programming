#!/usr/bin/python3
"""
json module
"""
import json


def load_from_json_file(filename):
    """creates an Object from JSON FILE"""
    with open(filename) as f:
        return json.load(f)
