#!/usr/bin/python3
"""
subclass square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """subclass"""

    def __init__(self, size):
        """instantiate the class"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2
