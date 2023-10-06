#!/usr/bin/python3
if __name__ == "__main__":
    """number and list of args"""
    import sys

    args = len(sys.argv) - 1

    if args == 0:
        print("0 arguments")
    else:
        for i in range(1, args + 1):
            if args == 1:
                print("{} argument:".format(i))
            else:
                print("{} arguments:".format(i))
