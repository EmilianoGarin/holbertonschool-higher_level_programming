#!/usr/bin/python3
"""task 1"""


class MyList(list):
    """inherits of list, print a sorted list of int in ascending sort"""

    def print_sorted(self):
        print(f"{sorted(self)}")
