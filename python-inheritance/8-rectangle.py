#!/usr/bin/python3
"""task 8"""


class BaseGeometry():
    """area"""

    def area(self):
        """an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates a 'value' """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle"""

    def __init__(self, width, height):
        """initialize width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
