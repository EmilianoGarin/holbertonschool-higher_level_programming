#!/usr/bin/python3
"""task 7"""


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
