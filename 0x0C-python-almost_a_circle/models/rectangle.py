#!/usr/bin/python3
"""Defines Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherites from Base class
    and performs its rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization function

        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
            x(int): space around the width
            y(int): space around the height
            id(int): id of the rectangle
                        increases when another rectangle is added
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
