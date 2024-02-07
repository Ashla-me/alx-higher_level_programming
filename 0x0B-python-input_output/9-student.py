#!/usr/bin/python3
"""
Defines a student
"""


class Student:
    """this class defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary representation of the class"""
        return self.__dict__
