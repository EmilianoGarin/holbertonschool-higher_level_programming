#!/usr/bin/python3
"""task 2"""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file """

    with open(filename, "a", encoding="utf-8") as f:
        char_w = f.tell()
        f.write(text)
        char_w = f.tell() - char_w
    return char_w
