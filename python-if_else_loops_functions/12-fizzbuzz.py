#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        fb = True
        if ((i % 3) == 0):
            print("Fizz", end="")
            fb = False
        if ((i % 5) == 0):
            print("Buzz", end="")
            fb = False
        if (fb):
            print("{:d}".format(i), end="")
        print(" ", end="")
