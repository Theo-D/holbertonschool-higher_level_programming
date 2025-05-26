#!/usr/bin/python3

"""
Module containing definition for a class that inherits from "list"
"""


class MyList(list):
    """
    A class that inherits from "list"
    """
    def __init__(self):
        """
        Object constructor for MyList class.

        Args:
            no args.
        """
        super().__init__()

    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort)
        """
        toPrint = self
        toPrint.sort()
        print(toPrint)
