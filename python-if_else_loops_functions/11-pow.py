#!/usr/bin/python3
def pow(a, b):
    ret = 1
    if b < 0:
        for i in range(0, -b):
            ret = a * ret
        ret = 1 / ret
    else:
        for i in range(0, b):
            ret = a * ret
    return (ret)
