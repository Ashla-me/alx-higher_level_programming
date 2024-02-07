#!/usr/bin/python3
"""
JSON string module
"""
import json


def from_json_string(my_str):
    """returns an object represented by JSON string"""
    return json.loads(my_str)
