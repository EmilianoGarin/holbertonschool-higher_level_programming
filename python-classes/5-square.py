#!/usr/bin/python3
"""Task 5 - set size"""


class Square:
    """set size"""
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

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if (value < 0):
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for s in range(0, self.size):
                for a in range(0, self.size):
                    print("#", end="")
                print()
