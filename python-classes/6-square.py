#!/usr/bin/python3
"""Task 6 - set size"""


class Square:
    """set size"""
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        if not isinstance(position, tuple) or :
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position      
        self.__size = size



    def area(self):
        return (self.__size**2)

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
        return (__position)

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for s in range(0, self.size):
                for a in range(0, self.size):
                    print("#", end="")
                print()

def p_int(tup):
    if len(tup) == 2 and [tup[1], tup[0]] >= 0:
        return (False)
    return (True)

