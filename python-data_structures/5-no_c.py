#!/usr/bin/python3
def no_c(my_string):
    string = "".join(my_string.split("c"))
    string = "".join(string.split("C"))
    return (string)
