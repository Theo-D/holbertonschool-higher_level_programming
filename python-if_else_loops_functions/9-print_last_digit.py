#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number *= -1
        number %= 10
        print("{:d}".format(number * -1), end="")
    else:
        number %= 10
        print("{:d}".format(number), end="")
