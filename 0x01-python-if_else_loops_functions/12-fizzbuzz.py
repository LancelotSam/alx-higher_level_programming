#!/usr/bin/python3
def fizzbuzz():
    """ Fizz for multiples of 3
    Buzz for multiples of 5
    FizzBuzz for multiples of both"""
    for number in range(1, 101):
        if (number % 3 == 0 and number % 5 == 0):
            print("FizzBuzz", end=' ')
        elif (number % 3 == 0):
            print("Fizz", end=' ')
        elif (number % 5 == 0):
            print("Buzz", end= ' ')
        else:
            print(number, end=' ')
