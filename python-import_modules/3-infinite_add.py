#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    ret = 0
    for arg in enumerate(args):
        ret += int(arg[1])
    print("{}".format(ret))
