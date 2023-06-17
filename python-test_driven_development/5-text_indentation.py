#!/usr/bin/python3
"""task 4"""


def text_indentation(text):
    """Text indentation"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_l = ['.', '?', ':']
    jump = False
    for a in range(len(text)):
        if not jump:
            print(f"{text[a]}", end="")
        jump = False
        if text[a] in new_l:
            print(end="\n\n")
            if a < len(text) - 1 and text[a + 1] == " ":
                jump = True
