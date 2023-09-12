#!/usr/bin/python3
"""task 1"""


def write_file(filename="", text=""):
    """write or overwrite a file"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        char_w = f.tell()
    return char_w
