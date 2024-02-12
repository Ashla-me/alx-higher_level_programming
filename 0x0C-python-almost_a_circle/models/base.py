#!/usr/bin/python3
"""defines base class"""
import json
import turtle
import csv


class Base:
    """A base class for all future classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializing id
        Args:
            id(int): number of instance class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
