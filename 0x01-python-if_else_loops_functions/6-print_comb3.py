#!/usr/bin/python3
def comb(L):
    for digit in range(10):
        for digit1 in range(digit+1,10):
            if (digit!=digit1):
                print(f"{digit}{digit1}", end=', ')
comb(range(10))
print()
