#!/usr/bin/python3
def comb(L):
    for digit in range(10):
        for digit1 in range(digit+1, 10):
            if (digit != digit1):
                print("{}{}".format(digit, digit1), end=', ')
