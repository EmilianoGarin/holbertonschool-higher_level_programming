#!/usr/bin/python3
"""Task 6 - set size"""


class Square:
    """set size"""
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
        if not p_val(position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if not p_val(value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.__size**2)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for a in range(0, self.__position[1]):
                print()
            for s in range(0, self.__size):
                for a in range(0, self.__position[0]):
                    print(" ", end="")
                for a in range(0, self.__size):
                    print("#", end="")
                print()


def p_val(position):
    if isinstance(position, tuple) and len(position) == 2:
        if isinstance(position[0], int) and isinstance(position[1], int):
            if position[1] >= 0 and position[0] >= 0:
                return (True)
    return (False)
