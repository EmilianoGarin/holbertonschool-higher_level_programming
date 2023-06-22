#!/usr/bin/python3
"""task 1"""


class MyList(list):
    """inherits of list"""

    def print_sorted(self):
        """print a sorted list of int in ascending sort"""
        print(sorted(self))
