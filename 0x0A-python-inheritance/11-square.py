#!/usr/bin/python3
"""
subclass of a square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """subclass"""

    def __init__(self, size):
        """instantiate a subclass"""

        super().__init__(size, size)
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
