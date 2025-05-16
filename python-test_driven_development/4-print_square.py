#!/usr/bin/python3
"""
4-print_square
Contains a function Prints a square with the character #.
"""


def print_square(size):
    if not isinstance(size, int) or (isinstance(size, float) and size <= 0):
        raise TypeError("size must be an integer")
    elif isinstance(size, bool):
        raise TypeError("size must be an integer")
    elif size <= 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#".format(), end="")
        print()
