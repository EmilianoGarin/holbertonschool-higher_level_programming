#!/usr/bin/python3
"""Task 2 - private size"""


class Square:
    """private size"""
    def __init__(self, size=0):
        if isinstance(size, int):
            if (size < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return (self.__size**2)
